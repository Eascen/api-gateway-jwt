# api-gateway-jwt

# To test:
Find your API Gateway URL
Post a login: 
curl -i -d '{"username":"user", "password":"asdf"}' -X POST https://api-gw-id.execute-api.us-east-1.amazonaws.com/generic/login
Copy the jwt_token header and replace {auth_token} below with the value:
curl -i -H "Auth: {auth_token}" https://api-gw-id.execute-api.us-east-1.amazonaws.com/generic
