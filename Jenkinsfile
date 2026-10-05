pipeline {

    agent {
        label 'tomcat'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checkout completed'
            }
        }

        stage('Check Files') {
            steps {
                sh '''
                    echo "Running on:"
                    hostname

                    echo "Jenkins node:"
                    echo "$NODE_NAME"

                    echo "Workspace:"
                    pwd

                    echo "Files:"
                    ls -la

                    echo "POM files:"
                    find . -name "pom.xml"
                '''
            }
        }

        stage('Build WAR') {
            steps {
                dir('tomcat-pratice1') {
                    sh 'mvn clean package'
                }
            }
        }

        stage('Find WAR') {
            steps {
                dir('tomcat-pratice1') {
                    sh 'find target -name "*.war"'
                }
            }
        }

        stage('Deploy to Tomcat') {
            steps {
                sh '''
                    cp tomcat-pratice1/target/*.war /opt/apache-tomcat-9.0.122/webapps/
                '''
            }
        }

        stage('Application URL') {
            steps {
                echo 'Application deployed!'
                echo 'http://54.221.60.120:9090/tomcat-practice-1.0/hello'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}