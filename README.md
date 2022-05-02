1) First step of creating the CI/CD pipeline is to setup the tests for the code in order to make sure what’s being deployed least buggy as possible and suitable for costumer consumption 

2) Now we create the fundamentals in order to have a smooth creation of the pipeline for example we will create our digital ocean account in order to get a runner for us to be able to deploy it online.As well as while installing gunicorn to your desktop as well as the postgresql driver and django-enviro, and installing docker with the nessescary configurations with this updating your requirements list.

3) Creating a duplicate of settings.py where you will change the name of the copy and edit it heavily.

4) Creating a env file similar to the original settings.py where we use variables mostly so we can use this with the variable settings in CI/CD pipeline in gitlab 

5) Now we connect our runner to our gitlab project using our terminal allowing this to be deployed. Furthermore we now create a gitlab-ci.yml file where the pipeline will be actually created initially setting up our image which is “python:latest” ( no compile stage required as we are using python). Making migrations every time we want to deploy putting this in the before script before we run our tests in the “script” section which we made in the first step that are in the test folder which contains tests for the view , url , form parts of our code.

6) Now we create our artifact where we turn our project into a downloadable zip file  
                                   
7) Now we set up our deploy stage (this where our website will actually deploy online ) we initially Setup ssh on the python image, open the ports on the firewall then  setup postgresql and create a production database for Django that use our variables that we’ve already set up 

8) Transfer the project over scp and install pip , requirements.txt and Setup the gunicorn application server on UBUNTU_SERVER

9) Setup the nginx web server to get “https://“ certificates then restart the server with the Django app and https.
