# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
https://trello.com/invite/b/4EFtOKS1/ATTIde9f7a97ccbc88358f17fa37a940c352CB752D2D/project-6-ci-cd

* A link to a spreadsheet that includes the original and final project plan>
https://docs.google.com/spreadsheets/d/1MuTdgJHaKLMtBAChJjcO1XEwVGcNuIiiuUzVuBr77VE/edit?usp=sharing

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>
![image](https://github.com/msabbaghian/udacityproject6/raw/main/Screenshots/Architecture.jpg)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell
![image](https://github.com/msabbaghian/udacityproject6/raw/main/Screenshots/Clone_repo.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![image](https://github.com/msabbaghian/udacityproject6/raw/main/Screenshots/Pass_test_CI.png)

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

![image](https://github.com/msabbaghian/udacityproject6/raw/main/Screenshots/Successfull_deploy.png)

* Running Azure App Service from Azure Pipelines automatic deployment

![image](https://github.com/msabbaghian/udacityproject6/raw/main/Screenshots/Running_webapp.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements
The models can be improved with better data and alternative prediction models should be tested to increate the accuracy of the model
  

## Demo 




