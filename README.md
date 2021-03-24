# AWS API Gateway JWT Example Project

The following is a sample Amazon API Gateway project with lambda backing using Python 3.8. It uses a custom authorizer with PyJWT to secure a generic endpoint. The authorizer is using the default template from AWS.

## Deployment:
- Clone the project into a local repository
- Create and/or set an S3 bucket you have access to in the variables.txt
- Run setup.sh (this was developed using cygwin on Windows)
- Navigate to the CloudFormation console, and create a stack updating the parameters to match your settings:
    
    - **APIGatewayName**: The name of your API Gateway
    - **APIGatewayStageName**: The name of the stage deployment for your API Gateway (default is fine)
    - **S3BucketName**: Name of the S3 bucket that contains the deployement packages
    

## Testing
Find your API Gateway URL and replace api-gw-id in the below url's with yours
- Post a login: 
    > curl -i -d '{"username":"user", "password":"asdf"}' -X POST https://api-gw-id.execute-api.us-east-1.amazonaws.com/generic/login
- Copy the jwt_token header and replace {auth_token} below with the value:
    > curl -i -H "Auth: {auth_token}" https://api-gw-id.execute-api.us-east-1.amazonaws.com/generic