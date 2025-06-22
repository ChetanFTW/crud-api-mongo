<!-- # Flask MongoDB CRUD Application

Check if MongoDB is running locally on your machine and stop it
On Linux/macOS:

sudo systemctl stop mongod

or

ps aux | grep mongod

## Setup

```bash
git clone https://github.com/yourusername/flask-mongo-crud.git
cd flask-mongo-crud
docker-compose down
docker-compose up --build

 -->


# Flask Application for CRUD operations on MongoDB


A simple Flask REST API with MongoDB for basic CRUD operations on users.

---

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
- If you have a local MongoDB instance running, stop it to avoid port conflicts.

### Stop local MongoDB (Linux/macOS)

```bash
sudo systemctl stop mongod
# or alternatively
ps aux | grep mongod
```


## Setup & Run
Clone the repository:
```bash
git clone https://github.com/yourusername/flask-mongo-crud.git
cd flask-mongo-crud
```

Bring down any running containers (if any) => Build and start the Flask app with MongoDB:

```bash
docker-compose down
docker-compose up --build
```

Your API will be accessible at:
http://localhost:5000
(or http://172.21.0.3:5000 if using a specific Docker network)
## API Endpoints

```bash
| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/users`      | List all users          |
| GET    | `/users/<id>` | Get a user by ID        |
| POST   | `/users`      | Create a new user       |
| PUT    | `/users/<id>` | Update an existing user |
| DELETE | `/users/<id>` | Delete a user by ID     |

```
Example Usage (with curl or Postman) =>
Create a user:

```bash
curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "password": "secret123"}'
```
Get all users:
```bash
curl -X GET http://localhost:5000/users
```
Update a User (PUT)
Replace <id> with the actual user ID:

```bash
curl -X PUT http://localhost:5000/users/<id> \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Name", "email": "updated@example.com", "password": "newpassword123"}'
```
Delete a User (DELETE)
Replace <id> with the actual user ID:
```bash
curl -X DELETE http://localhost:5000/users/<id>
```


If you'd like, I can also generate a downloadable `README.md` file for you. Would you want that?
