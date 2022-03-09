pipeline {
    agent any
    environment {
        SECRET_KEY = "my-secret"
        DATABASE_URI = "sqlite:///data.db"
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        APP_RUN = 'True'
    }
// This stage creates virtual environment for the python container
    stages {
        stage('Setup') {
            steps {
                sh """sudo apt install python3-venv -y 
                python3 -m venv venv
                . ./venv/bin/activate
                pip3 install -r requirements.txt
                """
            }
        }
// This stage runs unit tests and saves them to files to be picked up post build 
        stage('Test') {
            steps {
                sh """ . ./venv/bin/activate
                python3 -m pytest --cov --cov-report term-missing""" 
            }
        }
// This stage builds the two containers and pushes to docker hub
        stage('build and push') {
            steps {
                sh """echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin
                docker build --build-arg DATABASE_URI=$DATABASE_URI --build-arg SECRET_KEY=$SECRET_KEY -t 1gooey1/webapp .
                docker push 1gooey1/webapp
                /"""
            }
    }   
  }
}