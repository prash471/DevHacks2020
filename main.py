from deta.lib import app
import requests
import json
mytoken = 'xoxb-553244196757-1092574336726-ZwUbL0gfbiEjVOCnzLLYbO8K'
webhook_url = 'https://hooks.slack.com/services/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'
slack_data = {'text': "Random Text"}

@app.lib.http("/", methods=["GET"])
def get_handler(event):
    name = event.params.get("name")
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    print(response)

