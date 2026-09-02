pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Persitent-python-PCCE/Isha-Harmalkar.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('p1_0') {
                    bat 'docker build -t midblue12/flask-lms:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-12',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        docker logout

                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin

                        if errorlevel 1 (
                            echo Docker login failed
                            exit /b 1
                        )

                        echo Docker login successful
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker push midblue12/flask-lms:latest'
            }
        }

    }
}