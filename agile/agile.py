import json
from flask import Blueprint, render_template
from tools.connect_db import dishes


agile_bp = Blueprint("agile", __name__)


@agile_bp.route('/', methods=['GET', 'POST'])
def agile_food():
    docs = list(dishes.find())
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return render_template("agile_food.html", docs=json.dumps(docs))