pipeline {
    agent any

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
    }
}