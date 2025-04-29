# Python deployment to AWS Lambda using GitHub Actions (No Jenkins)

This project demonstrates how to automate the deployment of an AWS Lambda function using GitHub Actions and Python. It showcases CI/CD in action completely serverless, without using Jenkins or any external deployment tools. This project helped me practice real world DevOps automation and troubleshoot AWS deployments handson.

---

## 📝 Project Description

The goal of this project is to:

- Automate Lambda function deployment using GitHub Actions
- Write simple Python code to be deployed in AWS Lambda
- Use GitHub Secrets to securely manage AWS credentials
- Use `aws cli` inside GitHub Actions for deployment
- Eliminate manual deployment or reliance on Jenkins
- Learn by resolving real errors during deployment

---

## 🔧 Built With

- 🐍 Python
- ☁️ AWS Lambda
- ⚙️ AWS CLI
- 💡 GitHub Actions (CI/CD)
- 💻 Visual Studio Code

---

## 📂 Folder Structure

📂Deployment-to-AWS-Lambda/

├──📂 lambda_function.py

├──📂 hello.py

├──📂 .github/

│   └──📂 workflows/

│         └──📂 deploy.yaml

└──📂 README.md

├──📂Output Screenshots


---
## Git commands used in VS code
  - git add
  - git commit
  - git push
  - git clone
  - git pull
  - git merge
  - git log

## ⚙️ GitHub Actions CI/CD Workflow

- The workflow:
  - Installs AWS CLI
  - Configures AWS credentials via GitHub Secrets
  - Zips the code
  - Deploys it to Lambda
  - Confirms successful deployment
 

## GitHub Secrets Configuration process

  | Secret Name             | Description                        |
|-------------------------|------------------------------------|
| AWS_ACCESS_KEY_ID       | Your AWS access key                |
| AWS_SECRET_ACCESS_KEY   | Your AWS secret key                |
| AWS_REGION              | e.g., us-east-1                    |
| FUNCTION_NAME           | Your Lambda function name          |



![1_THAg1_WwiSFdWtMRAMYK4w](https://github.com/user-attachments/assets/c61eceba-b8f9-4818-9a7d-981dbeca5697)



---
## Lambda Function Code
def lambda_handler(event, context):
    return "This function came from GitHub Actions"
## Output i got from Lambda function 
"This function came from GitHub Actions"
##  Problems i Faced & How i solved them 
**Problem**                             **Solution**
AWS CLI failed to install------Corrected YAML indentation and added unzip and curl in setup
Zip file not found-------------Added zip command to GitHub Actions before deployment
Bad indentation in YAML file--Fixed spacing and aligned run: blocks properly
No response from Lambda----- 	Updated Lambda function code and tested with sample payload
AWS credentials error------- 	Created GitHub secrets and used aws configure inside Actions properly

**Tip for Beginners**
Don't worry if you see errors in the beginning solving them gives you real knowledge. Every error I faced helped me understand how GitHub Actions and AWS Lambda really work together.

---

## ⚙️ GitHub Actions CI/CD Workflow

- The workflow:
  - Installs AWS CLI
  - Configures AWS credentials via GitHub Secrets
  - Zips the code
  - Deploys it to Lambda
  - Confirms successful deployment

📄 `.github/workflows/deploy.yml`:

```yaml
name: Deploy Lambda to AWS

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install AWS CLI v2
        run: |
          sudo apt-get update
          sudo apt-get install -y unzip curl
          curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          unzip awscliv2.zip
          sudo ./aws/install
          aws --version

      - name: Configure AWS credentials
        run: |
          aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws configure set aws_secret_access_key ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws configure set region ${{ secrets.AWS_REGION }}

      - name: Zip Lambda Function
        run: |
          zip function.zip lambda_function.py

      - name: Deploy Lambda Function
        run: |
          aws lambda update-function-code \
            --function-name ${{ secrets.FUNCTION_NAME }} \
            --zip-file fileb://function.zip




---




