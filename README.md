## Deploy English sentence Recognition platform

This is a nlp project I did when I study serverless and apply machine learning in AWS. \n
You can check my other serverless project about [regression model](https://github.com/dukesky/Tutorial_of_Deploy_Serverless_ML_Model) and [Image recognition model]() 

### Step1: use Jupyter notebook to create project 
Just like your normal data science project with jupyter notebook, coding with what you used, processing data, build model and analysis result.

### Step2: create serverless framework
go to project folder in command line and type: \n
`sls create --template aws-python3 --name project_name`  \n
`sls plugin install -n serverless-python-requirements`  \n
Make sure you have already install `npm` and `serverless` before. If not, you can click here to install [node.js](https://nodejs.org/en/) and [serverless](https://www.serverless.com/framework/docs/getting-started/)

### Step3: edit handler.py
Add functions we want to used as APIs in AWS server

### Step4: config serverless.yml file
Edit serverless.yml, define functions we used in AWS server


### Step5: add requirements.txt file


### Step6: Deploy

I learned this project from [udemy](https://www.udemy.com/) course [Deploy Serverless Machine Learning Models to AWS Lambda](https://www.udemy.com/course/deploy-serverless-machine-learning-models-to-aws-lambda/)