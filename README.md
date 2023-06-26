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

Create an SQLite database file:

```bash
    cd api_template && python -m init_db
```

## Usage
Start the application:

cd api_template && python -m uvicorn main:app --host 0.0.0.0 --port $(PORT)

Open your browser and go to http://localhost:8000/docs to access the Swagger UI documentation. The API endpoints and their descriptions will be available there.

## API Endpoints
##### Create User

Endpoint: POST /users
Description: Creates a new user with the provided information.

Request Body:

```bash
{
  "userId": "string",
  "name": "string",
  "email": "string"
}
```

Response (200 OK):

```bash
{
  "message": "User created successfully"
}
```

##### Get User by ID
Endpoint: GET /users/{userId}
Description: Retrieves user information by their ID.

Path Parameters:
userId (string): The ID of the user to retrieve.


Response (200 OK):

```bash
{
  "userId": "string",
  "name": "string",
  "email": "string"
}
```

Response (404 Not Found):

```bash
{
  "error": "User not found"
}
```

## Database
The application uses an SQLite database to store user data.

## Contributing
Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.
