pipeline {

    agent any

    stages {

        stage('Install dependencies') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'python -m pip install pytest'
                bat 'python -m pytest test_calculator.py -v --junitxml=report.xml'
            }
        }

        stage('Collect results') {
            steps {
                junit allowEmptyResults: true, testResults: 'report.xml'
            }
        }
    }

    post {
        always {
            emailext(
                subject: "Jenkins Test Result: ${currentBuild.currentResult}",
                body: "Pipeline finished. Check Jenkins for details.",
                to: "oleg.cherniai@gmail.com"
            )
        }
    }
}