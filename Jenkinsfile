pipeline {

    agent any

    stages {

        stage('Checkout code') {
            steps {
                git 'https://github.com/yourname/your-repo.git'
            }
        }

        stage('Build containers') {
            steps {
                bat 'docker compose down -v'
                bat 'docker compose build'
            }
        }

        stage('Run tests') {
            steps {
                bat 'docker compose up --abort-on-container-exit'
            }
        }

        stage('Collect results') {
            steps {
                archiveArtifacts artifacts: 'allure-results/**'
            }
        }

    }

    post {

        always {

            emailext(
                subject: "Test Result: ${currentBuild.currentResult}",
                body: "Pipeline finished",
                to: "InsertYour@Mail.Here"
            )

        }

    }

}