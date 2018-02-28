from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from tools.scrapers import yelp_scraper
from tools.connect_db import dishes
from os.path import expanduser
import json


def get_googlemap_key():
    key_f = expanduser("~/.credentials/googlemapapi")
    with open(key_f) as f:
        key = f.read()
    return key


key = get_googlemap_key().strip()

add_bp = Blueprint('add_items', __name__)


@add_bp.route('/', methods=['GET', 'POST'])
def add_items(key=key):
    return render_template('add_items.html', key=key)


@add_bp.route('/load', methods=['GET','POST'])
def get_food_info():
    if request.method == "POST":
        tmp = request.args.to_dict()
        tmp["restaurant"]=tmp["restaurant"].replace("%and%", "&")
        tmp["location"] = json.loads(tmp["location"])
        tmp["restaurant_categories"] = tmp["restaurant_categories"].split(",")

        dishes.insert(tmp)
        return redirect(url_for(".add_items"))
    else:
        if "restaurant" in request.args and "img_id" in request.args:
            restaurant = request.args["restaurant"]
            img_id = request.args["img_id"]
            return jsonify(yelp_scraper(restaurant, img_id))
        else:
            return redirect(url_for(".add_items"))