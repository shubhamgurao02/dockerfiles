# PPM Migration

##Architecture of PPM


##PPM applaction overview
The application comprises two main components:

Frontend: Developed using React
Backend: Developed using Java

###Containerization with Podman
####Frontend Containerization (React):

Utilize a Dockerfile to define the React application's containerization specifics.
Include necessary dependencies and build commands within the Dockerfile.
Use Podman commands or scripts to build and manage the React frontend container.

####Backend Containerization (Java):

Create a Dockerfile to package the Java backend as a container image.
Include the required JDK, dependencies, and application build steps within the Dockerfile.
Leverage Podman to build and handle the Java backend container.

###GitLab CI Deployment Workflow
####Setup GitLab CI Pipeline:

Define a CI/CD pipeline in GitLab CI/CD configuration.
Configure stages and jobs for building, testing, containerizing, and deploying the microservices.
Build and Deploy Stages:

Set up build stages for both frontend and backend services.
Include unit tests, linting, and any necessary validations for each service.

####Containerization Stage:

Implement a stage to containerize the React frontend and Java backend separately using Podman within the CI pipeline.
Use Dockerfiles to build the respective container images.

####Deployment Stage:

Deploy the containerized microservices to the target environment (e.g., production, staging) using Podman commands.
Define deployment scripts or commands within the CI pipeline for seamless deployment.

####Continuous Integration and Continuous Deployment (CI/CD)
#####Continuous Integration:

Automate the build and integration of new code changes.
Ensure that tests pass and the application builds successfully.

#####Continuous Deployment:

Automate the deployment process after successful CI stages.
Push container images to a container registry.
Deploy updated containers to the target environment using Podman.

####Monitoring and Iteration
Implement monitoring tools to track application performance and health.
Iterate on the deployment pipeline based on feedback, enhancing automation and optimizing the deployment process.

##Pre-requisite
1) Podman
2) Gitlab Runner

#### Podman Installation

To install Podman on your system, follow these steps:

##### For Linux:

1. **Ubuntu/Debian**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y podman

#### Gitlab Runner

1. Add the official GitLab repository:
    curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash

Note: Url can vary as per version

2. Install the GitLab Runner package:

    sudo apt install -y gitlab-runner

3. Register the Runner:
   Obtain the registration token from your GitLab project's settings.
   Run the following command and follow the interactive prompts:

   sudo gitlab-runner register

   Note: To register you need the token that you will get from settings > CICD > runner > add runner
   copy the token and register the runner
4. Configure and Start the Runner:
   Once registered, start the runner with:
    
    sudo gitlab-runner start
