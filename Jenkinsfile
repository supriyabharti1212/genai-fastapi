pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t genai-fastapi .'
            }
        }

        stage('Test') {
            steps {
                sh '/usr/local/bin/docker run --rm genai-fastapi python -m pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'cp /Users/supriya/Documents/genai-fastapi/.env .env'
                sh '/usr/local/bin/docker rm -f genai-fastapi-container || true'
                sh '/usr/local/bin/docker compose up -d --build'
            }
        }

    }
}