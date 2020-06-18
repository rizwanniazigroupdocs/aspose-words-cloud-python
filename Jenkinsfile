properties([
	gitLabConnection('gitlab'),
	[$class: 'ParametersDefinitionProperty', 
		parameterDefinitions: [
			[$class: 'StringParameterDefinition', name: 'branch', defaultValue: 'master', description: 'the branch to build'],
			[$class: 'StringParameterDefinition', name: 'apiUrl', defaultValue: 'https://api-qa.aspose.cloud', description: 'api url'],
            [$class: 'BooleanParameterDefinition', name: 'ignoreCiSkip', defaultValue: false, description: 'ignore CI Skip'],
		]
	]
])

def runtests(dockerImageVersion)
{
    def needToBuild = false

    dir(dockerImageVersion){
        try {
            stage('checkout'){
				checkout([$class: 'GitSCM', branches: [[name: params.branch]], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'LocalBranch', localBranch: "**"]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '361885ba-9425-4230-950e-0af201d90547', url: 'https://git.auckland.dynabic.com/words-cloud/words-cloud-python.git']]])
                
                sh 'git show -s HEAD > gitMessage'
                def commitMessage = readFile('gitMessage').trim()
                echo commitMessage
                needToBuild = params.ignoreCiSkip || !commitMessage.contains('[ci skip]')               
                sh 'git clean -fdx'
                
                if (needToBuild) {
                    withCredentials([usernamePassword(credentialsId: '6839cbe8-39fa-40c0-86ce-90706f0bae5d', passwordVariable: 'AppKey', usernameVariable: 'AppSid')]) {
                        sh 'mkdir -p Settings'
                        sh 'echo "{\\"AppSid\\": \\"$AppSid\\",\\"AppKey\\": \\"$AppKey\\", \\"BaseUrl\\": \\"$apiUrl\\"}" > Settings/servercreds.json'
                    }
                }
            }
            
            if (needToBuild) {
                docker.image('python:' + dockerImageVersion).inside('-u root'){
                    stage('build'){
                        sh "python -m pip install -r requirements.txt && python -m pip install -r test-requirements.txt"
                    }
                
                    stage('tests'){
                        try {
                            sh "python -m xmlrunner discover -v -s --output-file testReport.xml ."
                        } 
                        finally {
                            junit '**\\testReport.xml'
                        }
                    }
                
                    stage('bdd-tests'){
                        
                    }
                    
                    stage('clean-compiled'){
                        sh "rm -rf %s"
                    }
                } 
            }
        } finally {
			 cleanWs()
        }
    }
}

node('words-linux') {
	stage('newpy'){
		try {
			runtests("3.7") 
		} finally {
			cleanWs()
		}
	}
}
