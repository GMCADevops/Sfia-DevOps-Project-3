pipeline {
    agent any 
    enviroment {
        rootpass = credentials("rootpass")
        SECRET_KEY = credentials("SECRET_KEY")
    }
    stages{
        stage('testing'){
                steps{
                    sh './jenkins/testing.sh'
                }
            }
        stage("Build Images"){
            steps{
                sh './jenkins/build.sh'
            }
        }
         stage('Push'){
                steps{
                    script{
                            docker.withRegistry('', 'docker-hub-credentials'){
                                sh "docker-compose push"
                                sh "docker system prune -af"
                            
                        }
                    }
                }
            }
        stage("Deployment"){
            steps{
                sh './jenkins/deployment.sh'
            }
        }
    }
}