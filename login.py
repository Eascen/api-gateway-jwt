import boto3
import os
import logging
import base64
import jwt
import json
from datetime import datetime, timedelta

logger = logging.getLogger("login")
logger.setLevel(os.environ["LOG_LEVEL"])
KMS_KEY_ID=os.environ["KMS_KEY"]

kms_client = boto3.client("kms")

def checkCreds(username, password):
    # TODO: Implement
    return True


def lambda_handler(event, context):
    body = json.loads(event["body"])
    username = body["username"]
    password = body["password"]
    # check the password
    if checkCreds(username, password):
        # If we're here, assume we have a successful auth
        # Next step is to generate the JWT
        kmsDataKey = kms_client.generate_data_key(KeyId=KMS_KEY_ID, NumberOfBytes=32)
        ciphertextBlob = kmsDataKey["CiphertextBlob"] # Encrypted data key
        ciphertextKey = base64.b64encode(ciphertextBlob).decode("utf-8") # To store with JWT
        plaintextKey = base64.b64encode(kmsDataKey["Plaintext"])
        # JWT Expiration
        expiresDatetime = datetime.utcnow() + timedelta(hours=1)

        encodedJwt = jwt.encode({"Username": username, "exp": expiresDatetime},
        plaintextKey,
        algorithm="HS256",
        headers={"KID": ciphertextKey})
        return {
            "statusCode": 200,
            "JWT_Token": encodedJwt.decode('utf-8')
        }

    return {
        "statusCode": "403", "Message": "Unable to login"
    }