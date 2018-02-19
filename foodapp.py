import json
from tools.scrapers import yelp_scraper
from tools.connect_db import dishes
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)


@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('add.html')


@app.route('/add/load', methods=['GET', 'POST'])
def get_food_info():
    if request.method == "POST":
        tmp = dict(request.args)

        # By default xmlhttp send lists as values
        for k in tmp:
            tmp[k] = tmp[k][0]
        tmp["restaurant"]=tmp["restaurant"].replace("%and%", "&")
        dishes.insert(tmp)
        return redirect(url_for("add"))
    else:
        if "restaurant" in request.args and "img_id" in request.args:
            restaurant = request.args["restaurant"]
            img_id = request.args["img_id"]
            return jsonify(yelp_scraper(restaurant, img_id))
        else:
            return redirect(url_for("add"))


@app.route('/agile', methods=['GET', 'POST'])
def agile_food():
    docs = list(dishes.find())
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return render_template("agile_food.html", docs=json.dumps(docs))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
