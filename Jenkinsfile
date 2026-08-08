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
                sh 'docker build -t genai-fastapi .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm genai-fastapi python -m pytest'
            }
        }
    }
}