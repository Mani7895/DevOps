@Library('qa-sharedlibraries')

pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        import src.blueocean.lib
        obj = new Utilities(this)
        echo 'This is Setup'
        Utilities.print 'test'
      }
    }
  }
}