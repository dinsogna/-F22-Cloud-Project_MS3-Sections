from flask import Flask, Response, request
from datetime import datetime
import json
from contacts_resource import ContactsResource
from flask_cors import CORS
import os
import requests

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)

@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Microservice-3-Contacts",
        "health": "Good",
        "at time": t
    }

    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result

@app.route("/api/contacts/<id>/contact", methods=["GET"])
def get_contact_by_id(id):
    result = ContactsResource.get_contact_by_id(id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/contacts/<id>/addresses", methods=["GET"])
def get_address_by_id(id):
    print("id:", id)
    result = ContactsResource.get_address_by_id(id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/contacts/<id>/phones", methods=["GET"])
def get_phone_by_id(id):
    print("id:", id)
    result = ContactsResource.get_phone_by_id(id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/contacts/<id>/emailaddress", methods=["GET"])
def get_email_address_by_id(id):
    print("id:", id)
    result = ContactsResource.get_email_address_by_id(id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/contacts/<id>/emailtype", methods=["GET"])
def get_email_type_by_id(id):
    print("id:", id)
    result = ContactsResource.get_email_type_by_id(id)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

# POST API to add new candidate contact information; use Smarty Address Verification API to verify address
#Source: https://www.youtube.com/watch?v=SuLBFOHiS5g&ab_channel=THESHOW
@app.route("/api/contacts/<id>/newaddress/", methods=["GET", "POST"])
def post_address(id):
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    
    street_raw = request.form["address"]
    street = street_raw.replace(" ", '+')
    smarty_url = f"https://us-street.api.smartystreets.com/street-address?street={street}&auth-id={auth_id}&auth-token={auth_token}&license=us-core-cloud"
    response = requests.get(url=smarty_url).json()[0]

    if response:
        res = response['delivery_line_1'] + " " + response['last_line']
        rsp = Response(json.dumps(res), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011, debug=True)
    # app.run(host="0.0.0.0", port=3306)

