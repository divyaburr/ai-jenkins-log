pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Running build...'
                bat 'echo Build started'
            }
        }

        /* 🔴 Intentional failure for demo */
        stage('Force Failure') {
            steps {
                bat 'exit /b 1'
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Running AI failure analysis...'

            bat '''
            copy console.log build.log || echo "No console.log found"
            python ai_log_analyzer.py
            '''
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
