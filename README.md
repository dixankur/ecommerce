# E-commerce Microservices

This project is a simple e-commerce application built with microservices architecture using Flask and PostgreSQL. It includes services for user authentication, product management, and order processing.

## Services

1. **Auth Service**: Handles user registration and login.
2. **Product Service**: Manages product CRUD operations.
3. **Order Service**: Manages order creation and updates.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Postgres shouls also installed on your machine.
- Python 3.8 and pip installed if running locally.

## Setup

### Running with Docker Compose

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/e-commerce-microservices.git
   cd e-commerce-microservices

2. Create a .env file in the root of the project with the following content:
DATABASE_HOST=postgres
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
JWT_SECRET=your_jwt_secret

3. Run Docker Compose:
docker-compose up --build

4. Tables Creation:
After the containers are up, verify that the tables have been created by connecting to the PostgreSQL container and listing the tables:

   1. Connect to the PostgreSQL container:
   docker exec -it <postgres_container_id> psql -U postgres -d ecommerce
   2. Once inside the PostgreSQL prompt, list the tables:
   \dt

   ecommerce=# \dt
          List of relations
   Schema |   Name   | Type  |  Owner
   --------+----------+-------+----------
   public | orders   | table | postgres
   public | products | table | postgres
   public | users    | table | postgres
   You should see the products, users, and orders tables listed.

   If tables not created then follow these steps
   1. Access the PostgreSQL container:
   docker exec -it <postgres_container_id> bash
   2. Run the psql command:
   psql -U postgres -d ecommerce
   3. run create sql query

4. The services will be available at:
Auth Service: http://localhost:5000
Product Service: http://localhost:5001
Order Service: http://localhost:5002

## Endpoints
### Auth Service
POST /auth/register: Register a new user
POST /auth/login: Login and obtain a JWT

### Product Service
POST /products: Create a new product
GET /products/:id: Get a product by ID
PUT /products/:id: Update a product
DELETE /products/:id: Delete a product

### Order Service
POST /orders: Create a new order
GET /orders/:id: Get an order by ID
PUT /orders/:id: Update an order
DELETE /orders/:id: Delete an order


## Running the Tests
To run the tests, simply execute the following command in your terminal:
pytest