pipeline {

    agent any

    environment {
        TOMCAT_HOME = '/opt/apache-tomcat-9.0.122'
        APP_NAME = 'tomcat-practice'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checkout completed'
            }
        }

        stage('Build WAR') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Find WAR') {
            steps {
                sh 'find target -name "*.war"'
            }
        }

        stage('Deploy to Tomcat') {
            steps {
                sh '''
                    sudo cp target/*.war $TOMCAT_HOME/webapps/
                '''
            }
        }
    }

    post {

        success {
            echo 'Application deployed successfully!'
        }

        failure {
            echo 'Deploymentsss failed!'
        }
    }
}