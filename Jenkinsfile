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
                    if (isUnix()) {
                        sh 'docker build -t sentiment-analysis .'
                    } else {
                        bat 'docker build -t sentiment-analysis .'
                    }
                }
            }
        }
        stage('Run Model Training') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm sentiment-analysis'
                    } else {
                        bat 'docker run --rm sentiment-analysis'
                    }
                }
            }
        }
    }
}