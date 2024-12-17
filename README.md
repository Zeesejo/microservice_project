**Microservice Project**

Overview

This is a microservice architecture with two main services:

AI Backend Service

UI Backend Service

Both services are containerized using Docker and share a network.

Features

AI Backend: Runs a Flask app that serves prediction endpoints.

UI Backend: Runs a Flask app for the UI.

Dockerized: Entire project is containerized for deployment.

Microservices: Separate services for modularity and scalability.

Tech

Python (Flask)

Docker

Git (for version control)

Setup

Follow these steps to set up and run locally:

1. Clone the Repository

git clone <repository-url>

cd microservice_project

2. Build and Run the Docker Containers

Make sure Docker is installed and running on your machine.

Run the following command to build and start the containers:

docker-compose up --build

This will:

Create a network for the microservices.

Build and start ai_backend and ui_backend containers.

3. Access the Services

AI Backend: http://127.0.0.1:5000

UI Backend: http://127.0.0.1:5001

Testing the Services

1. AI Backend

Use cURL or Postman to test the prediction endpoint:

curl http://127.0.0.1:5000/predict

2. UI Backend

Visit the UI in your browser:

http://127.0.0.1:5001

Stop the Services

docker-compose down

Folder Structure

microservice_project/

├── ai_backend/

│ ├── app.py # Flask app for AI service

│ ├── requirements.txt

│

├── ui_backend/

│ ├── app.py # Flask app for UI service

│ ├── requirements.txt

│

├── Dockerfile # Dockerfile for both services

├── docker-compose.yml

└── README.md

Contributing

Open an issue or submit a pull request.
