pipeline {

    agent {
        label 'deploy'
    }

    environment {
        TOMCAT_HOME = '/opt/apache-tomcat-9.0.122'
        APP_NAME = 'tomcat-practice'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Mohamedthoufiq31/jenkins-pra2.git'
            }
        }

        stage('Build WAR') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Find WAR') {
            steps {
                sh 'find target -name "*.war" -type f'
            }
        }

        stage('Deploy to Tomcat') {
            steps {
                sh '''
                    sudo cp target/*.war $TOMCAT_HOME/webapps/$APP_NAME.war
                '''
            }
        }
    }

    post {

        success {
            echo 'Application deployed successfully!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}