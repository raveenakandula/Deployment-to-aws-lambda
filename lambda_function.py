from hello import message

def lambda_handler(event, context):
    print(message())
    return {
        'statusCode': 200,
        'body': message()
    }
