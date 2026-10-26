pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/sobia2401/devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker --context desktop-linux build -t scholarship-eligibility-finder .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker --context desktop-linux compose down --remove-orphans'
                bat 'docker --context desktop-linux compose up -d --build'
            }
        }
    }
}
