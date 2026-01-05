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
                sh 'echo Build started'
        }
        }

        /* 🔴 Force failure for testing (remove later) */
        stage('Force Failure') {
            steps {
                sh 'exit 1'
            }
        }

        /* 🤖 AI Failure Analysis using Phi */
        stage('AI Failure Analysis') {
            when {
                failure()
            }
            steps {
                sh '''
                  echo "Collecting Jenkins logs..."
                  cp $WORKSPACE/console.log build.log || true

                  echo "Running AI analysis..."
                  python3 ai_log_analyzer.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
