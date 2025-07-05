pipeline {
    agent {
        label 'agent-python'
    }

    environment {
        PATH = "/home/jenkins/.pyenv/versions/3.12.6/bin:${env.PATH}"
        APP = "my-crud-project"
    }

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'coverage run -m pytest && coverage xml'
            }
        }

        stage('Analyse code') {
            environment {
                scannerHome = tool 'sonarqube'
            }
            steps {
                withSonarQubeEnv(credentialsId: 'SONARQUBE_TOKEN', installationName: 'sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }

        stage('Build Docker') {
            when {
                branch 'main'
            }

            steps {
                script {
                    withCredentials([string(credentialsId: 'HARBOR_EXTERNAL_URL', variable: 'HARBOR_EXTERNAL_URL'), string(credentialsId: 'HARBOR_REGISTRY', variable: 'HARBOR_REGISTRY')]) {
                        sh "docker buildx build -f ./Dockerfile -t ${APP}:${BUILD_NUMBER} ."
                        sh "docker tag ${APP}:${BUILD_NUMBER} ${HARBOR_REGISTRY}/${APP}:${BUILD_NUMBER}"
                        docker.withRegistry("${HARBOR_EXTERNAL_URL}", "HARBOR") { sh "docker push ${HARBOR_REGISTRY}/${APP}:${BUILD_NUMBER}"}
                        sh "docker rmi ${APP}:${BUILD_NUMBER} || true"
                        sh "docker rmi ${HARBOR_REGISTRY}/${APP}:${BUILD_NUMBER} || true"
                    }
                }
            }
        }

        stage("Deploy") {
            when {
                branch 'main'
            }

            steps {
                build job: 'deploy-to-environment', parameters: [
                    string(name: 'VERSION', value: "${BUILD_NUMBER}"),
                    string(name: 'ENVIRONMENT', value: 'dev'),
                    string(name: 'APP', value: "${APP}")
                ]
            }
        }
    }
}
