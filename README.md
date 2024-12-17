Microservice Project
Overview
This project is a microservice-based architecture that includes two primary services:

AI Backend Service
UI Backend Service
Both services are containerized using Docker and communicate within a shared network.

Key Features
AI Backend: Runs a Flask application that serves prediction endpoints.
UI Backend: Runs a Flask application to handle the user interface.
Dockerized: The entire project is containerized for easy deployment.
Microservices: Independent services for modular design and scalability.
Technologies Used
Python (Flask Framework)
Docker (for containerization)
Git (for version control)
Setup Instructions
Follow these steps to set up and run the project locally:

1. Clone the Repository
bash
Kodu kopyala
git clone <repository-url>
cd microservice_project
2. Build and Run the Docker Containers
Make sure Docker is installed and running on your machine.

Run the following command to build and start the containers:

bash
Kodu kopyala
docker-compose up --build
This will:

Create a network for the microservices.
Build and launch ai_backend and ui_backend containers.
3. Access the Services
AI Backend: http://127.0.0.1:5000
UI Backend: http://127.0.0.1:5001
Testing the Services
1. AI Backend
Test the prediction endpoint using cURL or Postman:

bash
Kodu kopyala
curl http://127.0.0.1:5000/predict
2. UI Backend
Visit the UI in your browser:

bash
Kodu kopyala
http://127.0.0.1:5001
Stop the Services
To stop the running containers:

bash
Kodu kopyala
docker-compose down
Folder Structure
plaintext
Kodu kopyala
microservice_project/
├── ai_backend/
│   ├── app.py       # Flask app for AI service
│   ├── requirements.txt
│
├── ui_backend/
│   ├── app.py       # Flask app for UI service
│   ├── requirements.txt
│
├── Dockerfile       # Dockerfile for both services
├── docker-compose.yml
└── README.md
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
