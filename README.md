## api_template

The project is a simple API for managing user information. It provides functionality to create users and retrieve user details based on their ID.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/federicsp/api-template.git
```

2. Navigate to the project directory:

```bash
cd api-template
```

3. Create a virtual environment (optional but recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Update the file `api_template/config/prod_config.py` declaring the AWS configuration parameters: `aws_access_key_id`, `aws_secret_access_key`, `region_name`, and `table_name`.

## Usage

To deploy the API, firstly, run the following command:

```bash
    sls deploy
```

This command will create a DynamoDB table using the AWS DynamoDB service and also create an S3 bucket. You can load your zipped application into the S3 bucket. To zip your application, execute the following commands:

```bash
	cp -r ./api_template ./api_template/lambda_function
	pip3 install -t api_template/lambda_function -r requirements.txt
	cd api_template && (cd lambda_function; zip ../lambda_artifact.zip -r .) && rm -rf lambda_function
```

Upload the generated zip file to the previously created S3 bucket.

Next, go to the AWS Management Console and open the Lambda service. Click on "Create function" and provide a name for your function. Choose the desired runtime, in this case, "Python". In the "Function code" section, specify the path to the zip file created in the S3 bucket. Specify the handler name as `<module_name>.<handler_function>`.

## Test
After creating the users table, you can test your application locally. Run the following command:

cd api_template && python -m uvicorn main:app --host 0.0.0.0 --port $(PORT)

Open your browser and go to http://localhost:8000/docs to access the Swagger UI documentation. The API endpoints and their descriptions will be available there.

## API Endpoints
##### Create User

Endpoint: POST /users
Description: Creates a new user with the provided information.

Request Body:

```bash
{
  "userId": "int",
  "name": "string",
  "email": "string"
}
```

##### Get User by ID
Endpoint: GET /users/{userId}
Description: Retrieves user information by their ID.

Path Parameters:
userId (string): The ID of the user to retrieve.

## Database
The application uses AWS DynamoDB to store user data.

## Contributing
Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.
