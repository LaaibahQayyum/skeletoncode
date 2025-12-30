pipeline {
    agent any
    
    parameters {
        string(name: 'BUILD_ENV', defaultValue: 'development', description: 'Build environment (development/production)')
        booleanParam(name: 'ENABLE_TESTS', defaultValue: true, description: 'Enable or disable test stage')
        choice(name: 'LOG_LEVEL', choices: ['INFO', 'DEBUG', 'ERROR'], description: 'Log level for the build')
    }
    
    stages {
        // Stage 1: Repository is auto-cloned by Jenkins
        stage('Clone & Setup') {
            steps {
                echo '✓ Repository cloned automatically by Jenkins'
                echo "Build Environment: ${params.BUILD_ENV}"
                echo "Log Level: ${params.LOG_LEVEL}"
                bat 'dir'  // For Windows - shows directory structure
            }
        }
        
        // Stage 2: Install Python packages
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python packages...'
                bat '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        // Stage 3: Run unit tests with pytest
        stage('Run Tests') {
            when {
                expression { 
                    params.ENABLE_TESTS == true  // FIXED: Was 'params.exceuteTests'
                }
            }
            steps {
                echo 'Running unit tests with pytest...'
                bat 'python -m pytest --junitxml=test-results.xml -v'
            }
            post {
                always {
                    junit 'test-results.xml'  // Collect test reports for Jenkins
                }
            }
        }
        
        // Stage 4: Build the application
        stage('Build Application') {
            steps {
                echo 'Building Flask application...'
                // Add any build steps here (e.g., collect static files)
                bat 'echo "Build completed for ${params.BUILD_ENV} environment"'
            }
        }
        
        // Stage 5: Simulate deployment
        stage('Deploy Simulation') {
            steps {
                echo 'Simulating deployment...'
                script {
                    // Create deployment directory if it doesn't exist
                    bat 'if not exist "C:\\deploy_target" mkdir C:\\deploy_target'
                    
                    // Copy files to target directory (simulating deployment)
                    bat 'copy /Y skeleton_app.py C:\\deploy_target\\'
                    bat 'copy /Y requirements.txt C:\\deploy_target\\'
                    if (fileExists('templates')) {
                        bat 'xcopy /E /I /Y templates C:\\deploy_target\\templates\\'
                    }
                    
                    echo '✓ Files copied to C:\\deploy_target'
                    echo 'Simulating service restart...'
                    bat 'echo "Service would restart here"'
                    
                    // Optional: Actually run the Flask app in background
                    // bat 'start /B python C:\\deploy_target\\skeleton_app.py'
                }
            }
        }
    }
    
    post {
        always {
            echo "Pipeline completed with environment: ${params.BUILD_ENV}"
            // Clean up if needed
            // bat 'taskkill /F /IM python.exe 2>nul || echo "No Python process to kill"'
        }
        failure {
            echo 'Pipeline failed! Check stages above.'
        }
        success {
            echo '✓ All stages completed successfully!'
            echo 'Application is ready in C:\\deploy_target'
        }
    }
}
