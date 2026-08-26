# 🚀 DevOps Cloud Deployment

A beginner-level DevOps project that demonstrates how to build, containerize, and deploy a Python Flask web application using Docker, GitHub, and Render.

## 🌐 Live Application

https://devops-cloud-deployment-1.onrender.com/

## 🛠️ Technologies Used

- Python
- Flask
- Docker
- Gunicorn
- Git
- GitHub
- Render

## 📁 Project Structure

```text
devops-cloud-deployment/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Environment Variables

The application uses environment variables for configuration.

### Local Environment

```text
APP_NAME=DevOps Cloud App
APP_ENV=development
PORT=5000
```

### Production Environment

For cloud deployment:

```text
APP_NAME=DevOps Cloud App
APP_ENV=production
```

Render provides the production environment variables.

## 💻 Run Locally

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Run the application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## 🐳 Docker

### Build the Docker image

```bash
docker build -t devops-cloud-app .
```

### Run the Docker container

```bash
docker run -p 5000:5000 --env-file .env devops-cloud-app
```

Open:

```text
http://localhost:5000
```

## ❤️ Health Check

The application provides a health-check endpoint:

```text
/health
```

Example response:

```json
{
  "status": "healthy",
  "application": "DevOps Cloud App",
  "environment": "production"
}
```

## ☁️ Cloud Deployment

The application is deployed using Render.

Deployment flow:

```text
GitHub
   ↓
Docker
   ↓
Render
   ↓
Live Web Application
```

## 🎯 DevOps Concepts Demonstrated

- Git version control
- GitHub repository management
- Environment variables
- Docker containerization
- Docker image creation
- Docker container execution
- Gunicorn production server
- Cloud deployment
- Health-check endpoint

## 👩‍💻 Author

Kandriga Vijaya Mahalakshmi