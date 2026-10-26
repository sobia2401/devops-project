
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
                bat 'set DOCKER_HOST=npipe:////./pipe/dockerDesktopLinuxEngine && docker run -d --name scholarship-app -p 5000:5000 --restart unless-stopped scholarship-eligibility-finder'
            }
        }
    }
}
