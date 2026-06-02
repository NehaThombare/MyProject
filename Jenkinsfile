pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from the GitHub repository we link later
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running python automated unit tests...'
                // Jenkins tells your local Docker engine to spin up a quick python environment to run pytest
                sh 'docker run --rm -v "$(pwd)":/app -w /app python:3.7-slim sh -c "pip install -r requirements.txt && pytest"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Tests passed! Building production Docker image...'
                // Builds your final local project image automatically
                sh 'docker build -t local-flask-app:latest .'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed perfectly! New image is ready.'
        }
        failure {
            echo 'Something failed during the tests or build stage.'
        }
    }
}