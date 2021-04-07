#!/bin/bash
source variables.txt
# Build lambda:
if [ ! -d "./package" ] 
then
    mkdir ./package
fi
# PATH=$PATH\:/c/Users/alec.horn/Anaconda3/Scripts ; export PATH
pip install --target ./package -r requirements.txt
cd package 
zip -r ../jwt_auth.zip .
cd ..
zip -g jwt_auth.zip jwt_authorizer.py login.py test_method.py
aws s3 cp ./jwt_apigw_cfn.yaml s3://${S3_BUCKET}/jwt_apigw_cfn.yaml
aws s3 cp ./jwt_auth.zip s3://${S3_BUCKET}/jwt_auth.zip