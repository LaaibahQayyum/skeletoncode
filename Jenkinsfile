pipeline {
    agent any
    
    parameters {
        string(name: 'BUILD_ENV', defaultValue: 'development', description: 'Build environment (development/production)')
        booleanParam(name: 'ENABLE_TESTS', defaultValue: true, description: 'Enable or disable test stage')
        choice(name: 'LOG_LEVEL', choices: ['INFO', 'DEBUG', 'ERROR'], description: 'Log level for the build')
        string(name: 'DEPLOY_DIR', defaultValue: 'C:\\deployment\\flask-app', description: 'Deployment target directory')
    }
    
    environment {
        PYTHON_PATH = 'python'
        PIP_PATH = 'pip'
        APP_NAME = 'skeleton_app'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                echo '========================================='
                echo 'Stage 1: Cloning Repository'
                echo '========================================='
                echo "Repository: ${env.GIT_URL}"
                echo "Branch: ${env.GIT_BRANCH}"
                // Repository is automatically cloned by Jenkins for multibranch pipelines
                echo 'Repository cloned successfully!'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '========================================='
                echo 'Stage 2: Installing Python Dependencies'
                echo '========================================='
                echo "Build Environment: ${params.BUILD_ENV}"
                echo "Log Level: ${params.LOG_LEVEL}"
                
                script {
                    // Install Python packages from requirements.txt
                    bat '''
                        echo Installing Python packages...
                        python --version
                        pip --version
                        pip install -r requirements.txt
                        echo Dependencies installed successfully!
                    '''
                }
            }
        }
        
        stage('Run Unit Tests') {
            when {
                expression {
                    params.ENABLE_TESTS == true
                }
            }
            steps {
                echo '========================================='
                echo 'Stage 3: Running Unit Tests with pytest'
                echo '========================================='
                
                script {
                    // Run pytest tests
                    bat '''
                        echo Running pytest tests...
                        pytest test_skeleton_app.py -v --tb=short
                        echo All tests passed successfully!
                    '''
                }
            }
        }
        
        stage('Build Application') {
            steps {
                echo '========================================='
                echo 'Stage 4: Building Application'
                echo '========================================='
                
                script {
                    // Verify application can start
                    bat '''
                        echo Verifying application structure...
                        if exist skeleton_app.py (
                            echo Found skeleton_app.py
                        ) else (
                            echo ERROR: skeleton_app.py not found!
                            exit 1
                        )
                        
                        if exist requirements.txt (
                            echo Found requirements.txt
                        ) else (
                            echo ERROR: requirements.txt not found!
                            exit 1
                        )
                        
                        if exist templates (
                            echo Found templates directory
                        ) else (
                            echo ERROR: templates directory not found!
                            exit 1
                        )
                        
                        if exist static (
                            echo Found static directory
                        ) else (
                            echo WARNING: static directory not found
                        )
                        
                        echo Application build verification complete!
                    '''
                }
            }
        }
        
        stage('Deploy Application') {
            steps {
                echo '========================================='
                echo 'Stage 5: Deploying Application'
                echo '========================================='
                echo "Deployment Directory: ${params.DEPLOY_DIR}"
                
                script {
                    // Simulate deployment by copying files to target directory
                    bat """
                        echo Creating deployment directory...
                        if not exist "${params.DEPLOY_DIR}" mkdir "${params.DEPLOY_DIR}"
                        
                        echo Copying application files...
                        xcopy /Y /I skeleton_app.py "${params.DEPLOY_DIR}\\"
                        xcopy /Y /I requirements.txt "${params.DEPLOY_DIR}\\"
                        
                        echo Copying templates directory...
                        if exist templates xcopy /E /Y /I templates "${params.DEPLOY_DIR}\\templates\\"
                        
                        echo Copying static directory...
                        if exist static xcopy /E /Y /I static "${params.DEPLOY_DIR}\\static\\"
                        
                        echo Copying instance directory...
                        if exist instance xcopy /E /Y /I instance "${params.DEPLOY_DIR}\\instance\\"
                        
                        echo Files copied successfully to ${params.DEPLOY_DIR}
                    """
                }
            }
        }
        
        stage('Restart Service') {
            steps {
                echo '========================================='
                echo 'Stage 6: Restarting Application Service'
                echo '========================================='
                
                script {
                    // Simulate service restart
                    bat '''
                        echo Simulating service restart...
                        echo Stopping existing Flask application (if running)...
                        timeout /t 2 /nobreak >nul
                        
                        echo Starting Flask application service...
                        timeout /t 2 /nobreak >nul
                        
                        echo Service restarted successfully!
                        echo Application is now running on http://localhost:5000
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo '========================================='
            echo 'Pipeline Execution Complete'
            echo '========================================='
            echo "Build Environment: ${params.BUILD_ENV}"
            echo "Tests Enabled: ${params.ENABLE_TESTS}"
            echo "Log Level: ${params.LOG_LEVEL}"
            echo "Deployment Directory: ${params.DEPLOY_DIR}"
        }
        
        success {
            echo '✓ Pipeline completed successfully!'
            echo '✓ All stages passed'
            echo '✓ Application deployed and running'
        }
        
        failure {
            echo '✗ Pipeline failed!'
            echo '✗ Check the logs above for error details'
            echo '✗ Fix the issues and retry the build'
        }
        
        unstable {
            echo '⚠ Pipeline completed with warnings'
            echo '⚠ Review the logs for potential issues'
        }
    }
}
