from hello import message

def lambda_handler(event, context):
    print(message())
    return {
        'statusCode': 200,
        'body': message()
    }
name: Deploy Lambda

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install AWS CLI
        run: |
          curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          unzip awscliv2.zip
          sudo ./aws/install

      - name: Configure AWS credentials
        run: |
          aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws configure set aws_secret_access_key ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws configure set default.region ${{ secrets.AWS_REGION }}

      - name: Create zip
        run: zip lambda_function.zip lambda_function.py hello.py

      - name: Deploy to Lambda
        run: |
          aws lambda update-function-code \
            --function-name myGithubLambda \
            --zip-file fileb://lambda_function.zip
