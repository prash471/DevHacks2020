
from flask import Flask, request, make_response
from slack import WebClient
from slack.errors import SlackApiError
app = Flask(__name__)
slack_token = 'xoxb-1106306265124-1085398447143-UgJEqF6V1XrnrcF4XQtVtSRQ'
signing_secret = '76676c1dbc22e3138b45d8fa87d0c2db'
search_token = 'xoxp-1106306265124-1100127660274-1100922555715-fc6154e3e2db6a491dcb4dd9bbf3bf70'
client = WebClient(token=slack_token)
searchResult = []

@app.route("/question/", methods=["POST"])
def slack_app():
  if "command" in request.form and request.form["command"] == "/question":
    try:
      # Search for text
      res = client.search_messages(token=search_token,query=request.form["text"])
      # Restructure the search result
      link = res['messages']['matches'][0]['permalink']
      for x in res['messages']['matches'] :
          searchResult.append(x['blocks'][0])
      filteredList = []
      for x in searchResult :
        filteredList.append({
            'type':x.get('type'),
            'text':{
                'text':str(x.get('text',{}).get('text',None))+'<'+link+'| Jump to thread>',
                'type':x.get('text',{}).get('type',None)
            }
        }
        )
      filteredList2 = [x for x in filteredList if x['type'] != None and x['text']['type'] != None]

      # Send to channel
      response = client.chat_postEphemeral(
        user=request.form["user_id"],
        channel=request.form["channel_id"],
        blocks=filteredList2
      )
      return make_response("", 200)
    # Exception Handling
    except SlackApiError as e:
      code = e.response["error"]
      return make_response(f"Failed to open a modal due to {code}", 200)

  # Exception Handling
  elif "payload" in request.form:
    payload = json.loads(request.form["payload"])
    if payload["type"] == "view_submission" \
      and payload["view"]["callback_id"] == "modal-id":
      submitted_data = payload["view"]["state"]["values"]
      return make_response("", 200)

  return make_response("", 404)
  
if __name__ == '__main__':
  app.run()