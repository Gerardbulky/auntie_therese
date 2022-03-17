import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    data = []
    with open("data/aunt-img.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", images=data)



@app.route("/about")
def about():
    data = []
    with open("data/data.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Tribute To Auntie Therese", collection=data)



@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/data.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", item=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", page_title="Condolense Message")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
