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

        /* 🔴 Force failure (demo kosam) */
        stage('Force Failure') {
            steps {
                sh 'exit 1'
            }
        }
    }

    /* 🤖 FAILURE ayyaka AI analysis */
    post {
        failure {
            echo 'Build failed. Running AI failure analysis...'

            sh '''
              cp $WORKSPACE/console.log build.log || true
              python3 ai_log_analyzer.py
            '''
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
