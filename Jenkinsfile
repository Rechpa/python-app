pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/Rechpa/python-app.git'
        GIT_BRANCH = 'link'
        IMAGE_NAME = 'python-app'
        IMAGE_TAG = 'latest'
        KIND_CLUSTER = 'kind-3nodes'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Build Python App') {
            steps {
                sh '''
                python3 --version
                python3 -m compileall .
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Load Image into kind') {
            steps {
                sh '''
                kind load docker-image ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Deploy to kind') {
            steps {
                sh '''
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
