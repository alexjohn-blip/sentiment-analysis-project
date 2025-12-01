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
                script {
                    docker.build('sentiment-analysis')
                }
            }
        }
        stage('Run Model Training') {
            steps {
                script {
                    docker.image('sentiment-analysis').inside {
                        sh 'python src/model_training.py'
                    }
                }
            }
        }
    }
}