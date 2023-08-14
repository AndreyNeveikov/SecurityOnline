# SecurityOnline Application

This is the README for the SecurityOnline application. It consists of a backend built with Django.

## Prerequisites

- Docker and Docker Compose are installed on your system.

## Getting Started

1. Clone the repository:

   git clone https://github.com/AndreyNeveikov/SecurityOnline.git
   cd SecurityOnline

2. Create a .env file in the project root directory based on .env.example and configure your environment variables.

3. Build and start the services using Docker Compose:

   docker-compose up --build
   
4. Access the backend at http://0.0.0.0:8000/api/v1/server-chart/

5. There is no frontend part implemented

##Features
Backend: Django REST framework for API endpoints.
Frontend: Vue.js for interactive user interfaces.
Celery and Redis for asynchronous task processing.
PostgreSQL database for data storage.

##Project Structure
backend/: Django backend code.
docker-compose.yml: Docker Compose configuration for services.
.env.example: Example environment variables file.

##License
This project is licensed under the MIT License.

