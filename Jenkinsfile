     pipeline {

    agent any

    stages {

        stage('Install dependencies') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python -m pip install pytest'
                sh 'pytest -v --junitxml=report.xml'
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