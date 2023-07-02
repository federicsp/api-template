from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import boto3
import logging
from config import app_config as config


router = APIRouter()
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key,
    region_name=config.region_name
)

table_name = config.table_name

class User(BaseModel):
    userId: int
    name: str
    email: str

class ErrorResponse(BaseModel):
    detail: str
    code: int
    message: str

class CustomErrorResponse(JSONResponse):
    def render(self, content):
        return super().render({"error": content.detail})

def create_custom_response(error: ErrorResponse, status_code: int):
    return JSONResponse(content=error.dict(), status_code=status_code)


@router.post("/users", responses={409: {"model": ErrorResponse}, 500: {"model": ErrorResponse, "response_class": CustomErrorResponse}})
async def create_user(user: User):
    try:
        table = dynamodb.Table(table_name)

        # Check if user already exists
        existing_user = table.get_item(Key={'userId': user.userId})
        if existing_user.get('Item'):
            error = ErrorResponse(detail="CONFLICT", code=409, message="User already exists")
            return create_custom_response(error, status.HTTP_409_CONFLICT)

        # Create the user
        table.put_item(Item=user.dict())
        return {"message": "User created successfully"}
    except Exception as e:
        if "prod" == config.ENV:  # Assuming app.config contains the environment configuration
            # Log the detailed error for debugging
            logging.exception("Exception occurred while creating user")
            # Return a generic error message without exposing details
            error = ErrorResponse(detail="INTERNAL SERVER ERROR", code=500, message="An error occurred while processing the request.")
            return create_custom_response(error, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return the detailed error message for non-production environment
            return {"error": str(e)}


@router.get("/users/{userId}", responses={404: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def get_user_by_id(userId: int):
    try:
        table = dynamodb.Table(table_name)
        response = table.get_item(Key={'userId': userId})
        item = response.get('Item')
        if item:
            return item
        else:
            error = ErrorResponse(detail="USER NOT FOUND", code=404, message="User not found")
            return create_custom_response(error, status.HTTP_404_NOT_FOUND)
    except Exception as e:
        if "prod" == config.ENV:
            error = ErrorResponse(detail="INTERNAL SERVER ERROR", code=500, message="An error occurred while processing the request.")
            return create_custom_response(error, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return {"error": str(e)}