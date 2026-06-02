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
                echo 'Building temporary test image...'
                // Create a temporary container blueprint that copies your current workspace inside it
                sh 'docker build -t temporary-test-env -f - . <<EOF\nFROM python:3.7-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ["pytest"]\nEOF'
                
                echo 'Running python automated unit tests...'
                // Run the isolated test container
                sh 'docker run --rm temporary-test-env'
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
