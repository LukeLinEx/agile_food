from flask import Flask
from add_items.add_items import add_bp
from agile.agile import agile_bp


app = Flask(__name__)


app.register_blueprint(add_bp, url_prefix='/add_items')
app.register_blueprint(agile_bp, url_prefix='/agile')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
