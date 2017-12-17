import random

QUESTIONS = [
    {
        "question": "What male tennis player has won the most major titles in his career?",
        "answers": ["Roger Federer", "Rafael Nadal", "Pete Sampras", "Rod Laver"],
        "correct_index": 0
    }
]

def lambda_handler(event, context):
    print(event)

    if event["session"]["application"]["applicationId"] != "amzn1.ask.skill.bd1dff94-195d-4e65-b69f-234ee4325c4d":
        raise Exception("Invalid Application ID")

    return response(random.choice(QUESTIONS)["question"], False)

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