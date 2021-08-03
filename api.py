import flask
from flask import request, jsonify
from main import bs,links

app=flask.Flask(__name__)
app.config["DEBUG"]=True
@app.route("/",methods=["GET"])
def home():
    if "name" in request.args:
        result = bs(request.args['name'])
    elif "link" in request.args:
        result=links(request.args["link"])
    return jsonify(result)

app.run()