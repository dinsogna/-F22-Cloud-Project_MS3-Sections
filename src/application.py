from flask import Flask, Response, request
from datetime import datetime
import json
from contacts_resource import ContactsResource
from flask_cors import CORS

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

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result

'''
TO DO: Routes
students/<uni>/addresses
students/<uni>/phones
'''

'''
ROUTE: students/<uni>/emails
'''
@app.route("/students/<uni>/emails", methods=["GET"])
def get_email_by_uni(uni):
    print("UNI:", uni)
    result = ContactsResource.get_email_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

'''
ROUTE: students/<uni>/addresses
'''
@app.route("/students/<uni>/addresses", methods=["GET"])
def get_address_by_uni(uni):
    print("UNI:", uni)
    result = ContactsResource.get_address_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

'''
ROUTE: students/<uni>/phones
'''
@app.route("/students/<uni>/phones", methods=["GET"])
def get_phone_by_uni(uni):
    print("UNI:", uni)
    result = ContactsResource.get_phone_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/students/<uni>/emailaddress", methods=["GET"])
def get_email_address_by_uni(uni):
    print("UNI:", uni)
    result = ContactsResource.get_email_address_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/students/<uni>/emailtype", methods=["GET"])
def get_email_type_by_uni(uni):
    print("UNI:", uni)
    result = ContactsResource.get_email_type_by_uni(uni)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
    # app.run(host="0.0.0.0", port=3306)

