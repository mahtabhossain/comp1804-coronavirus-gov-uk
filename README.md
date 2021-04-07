Prediction of newCases in England using data obtained through GOV.UK's coronavirus developer API:

Part 1 (Data Preparation and Modelling):
----------------------------------------
Files:
model_training.ipynb
helper_functions.py

Data Preparation - uses GOV.UK's coronavirus developer API to retrieve the daily newCases upto today. Depending on the time of the request, the most recent data (today's newCases) may not be updated through the API (e.g., generally udpated information can be obtained in the evening of that day). But you can definitely obtain all the data until the previous day irrespective of the time of the request. Refer to the link for the API information: 
https://coronavirus.data.gov.uk/details/developers-guide


Modelling - Jupyter notebook environment. Exploratory data analysis motivated the choice of the ML algorithm (Support Vector Regression). Refer to the notebook for the modelling and evaluation steps: model_training.ipynb. The model is then saved as a pickle file (model.pkl) for deployment.

Part 2 (Prediction as a Web Service - Flask Application):
---------------------------------------------------------
Files:
model_inference.py
model.pkl

A Flask Web service application is created for deployment which can be run via the following command:
python model_inference.py

This should run as a Web service on port 5000. Two different routes are created: one for the landing page (http://127.0.0.1:5000/) and the other one as the Web service model prediction (http://127.0.0.1:5000/predict?newCases=20000). Refer to the model_inference.py file for details. The variable newCases as a GET parameter to receive the feature (e.g., previous day's newCases) to predict the next newCases. Open these links in your Web browser (e.g., Firefox, Google Chrome) to test these two page contents, provided your Flask application ran successfully with no errors.

Remember, this is a development server and also from localhost (127.0.0.1), only http may work (not https). 

Part 3 (Docker Containerisation):
---------------------------------
Files:
Dockerfile
requirements.txt

Please refer to the instaliation guide as suggested in Docker website (https://www.docker.com/) which depends on the Operating System (OS) you plan to use. I could even use the legacy Docker-Tools on Windows 7 [apart from Linux machines] which are not supported anymore by the Docker community. From Windows 10 onwards, you should install Docker-Desktop (recommended).

If you are using Linux-based machines, the installation is quite straightforward (search for DigitalOcean Docker Installation for 'Linux distribution that you are using' in Google) to find the exact steps of adding repository, dependencies, etc.

After the successful installation on the OS of your choice, follow the tutorial below upto "Docker on AWS" section for the creation of the Docker containerised Web service:
https://docker-curriculum.com/

Related files of GitHub repository for Docker containerisation:
Dockerfile - contains information for the docker daemon for the container creation (e.g., which port the Web service will be running).
requirements.txt - contains the dependencies, e.g., the sklearn version used to create the model.pkl and also the Flask version used for the Web service.

If you want to achieve Part 4 below, publish the containerised Web service through a public repository (e.g., Docker Hub - https://hub.docker.com/). The Docker tutorial (https://docker-curriculum.com/) mentions the steps of this publishing as well.

Part 4 (Deployment through Amazon Cloud - AWS):
-----------------------------------------------
Files:
Dockerrun.aws.json

There are multiple options to achieve this part. We will be utilising an option that makes use of the Docker container registry (mahtabhossain/comp1804-coronavirus-gov-uk) created in Part 3. Follow the instructions inside "Docker on AWS" section of the tutorial (https://docker-curriculum.com/).

Amazon Management Console link: https://aws.amazon.com/console/

CAUTION: make sure you clean up all the resources (including orphan ones) to avoid cost incurred for continually using AWS PaaS.
