
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
                bat 'set DOCKER_HOST=npipe:////./pipe/dockerDesktopLinuxEngine && docker build -t scholarship-eligibility-finder .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'set DOCKER_HOST=npipe:////./pipe/dockerDesktopLinuxEngine && docker compose down --remove-orphans'
                bat 'set DOCKER_HOST=npipe:////./pipe/dockerDesktopLinuxEngine && docker compose up -d --build'
            }
        }
    }
}

