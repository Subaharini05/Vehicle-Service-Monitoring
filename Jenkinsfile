pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting Vehicle Service Monitoring project from GitHub'
            }
        }

        stage('Run Vehicle Monitoring') {
            steps {
                bat  '"C:\\Users\\ELCOT\\AppData\\Local\\Python\\bin\\python.exe" vehicle_service.py'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'vehicle_metrics.json', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Vehicle Service Monitoring completed successfully!'
        }

        failure {
            echo 'Vehicle Service Monitoring failed!'
        }
    }
}
