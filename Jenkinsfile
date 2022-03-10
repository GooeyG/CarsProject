pipeline {
    agent any
    environment {
        SECRET_KEY = credentials('SECRET_KEY')
        DATABASE_URI = credentials('DATABASE_URI')
        DOCKER_LOGIN = credentials('DOCKER_LOGIN')
        APP_RUN = 'True'
    }
// create virtual environment for the python container
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
// run unit tests
        stage('Test') {
            steps {
                sh """ . ./venv/bin/activate
                python3 -m pytest --cov --cov-report term-missing""" 
            }
        }
// build image and push to docker hub
        stage('build and push') {
            steps {
                sh """echo $DOCKER_LOGIN_PSW | docker login -u $DOCKER_LOGIN_USR --password-stdin
                docker build --build-arg DATABASE_URI=$DATABASE_URI --build-arg SECRET_KEY=$SECRET_KEY -t 1gooey1/webapp .
                docker push 1gooey1/webapp
                """
            }
    }
// This stage copies a compose file into the manager node sshs into manager node of swarm and sets up the docker stack
        stage('deploy') {
            steps {
                sh """docker stack deploy --compose-file docker-compose.yml webapp
                """
            }
        }   
    }
}