import json
import random

def lambda_handler(event, context):
    print(event)

    if event["session"]["application"]["applicationId"] != "amzn1.ask.skill.bd1dff94-195d-4e65-b69f-234ee4325c4d":
        raise Exception("Invalid Application ID")

    with open("questions.json") as f:
        questions = json.load(f)

    return response(random.choice(questions)["question"], False)

def response(output_text, finish_session = False):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": output_text
            },
            "shouldEndSession": finish_session
        }
    }