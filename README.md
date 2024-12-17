Microservice Project
This project implements a microservice-based architecture featuring two services:

AI Backend - Handles model predictions and logic.
UI Backend - Manages the user interface and interacts with the AI backend.
Table of Contents
Project Overview
Technologies Used
Architecture
Setup Instructions
Endpoints
Testing
Troubleshooting
License
Project Overview
This project is built to demonstrate a simple Flask-based microservice architecture.

The AI Backend serves model predictions through a REST API.
The UI Backend interacts with the AI backend to display results on a simple user interface.
Technologies Used
Backend: Flask
Containerization: Docker
Orchestration: Docker Compose
Communication: REST APIs
Language: Python 3.8+
Architecture
lua
Kodu kopyala
+---------------------+       +---------------------+
|    UI Backend       | <-->  |     AI Backend      |
| (Frontend & Client) |       |   (Model API)       |
+---------------------+       +---------------------+
          |                          |
          |      Docker Network      |
          +--------------------------+
Setup Instructions
Follow the steps below to set up and run the project:

Prerequisites
Ensure the following are installed:

Docker & Docker Compose
Python 3.8+
cURL (for testing)
Steps to Run
Clone the Repository

bash
Kodu kopyala
git clone <repo-link>  
cd microservice_project  
Build and Start Containers
Use Docker Compose to build and start the services:

bash
Kodu kopyala
docker-compose up --build  
Verify Services

AI Backend: http://127.0.0.1:5000/predict
UI Backend: http://127.0.0.1:5000
Endpoints
1. AI Backend
Method	Endpoint	Description
GET	/predict	Returns model predictions.
Sample cURL request:

bash
Kodu kopyala
curl http://127.0.0.1:5000/predict  
2. UI Backend
Serves the user interface at http://127.0.0.1:5000.

Testing
Check Running Containers

bash
Kodu kopyala
docker ps  
Test AI Backend

bash
Kodu kopyala
curl http://127.0.0.1:5000/predict  
Access UI Backend
Open your browser and navigate to:

arduino
Kodu kopyala
http://127.0.0.1:5000  
Troubleshooting
Issue	Solution
Unable to connect to endpoints	Ensure Docker containers are running.
Error port already in use	Stop conflicting processes or change ports.
404 error for /predict	Ensure the AI backend container is running.
