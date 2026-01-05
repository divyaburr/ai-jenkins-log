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
        echo Jenkins build failed at %DATE% %TIME% > build.log
        echo Stage: Force Failure >> build.log
        echo Reason: Non-zero exit code >> build.log

        python ai_log_analyzer.py
        '''
    }

    always {
        echo 'Pipeline execution completed.'
    }
}

}
