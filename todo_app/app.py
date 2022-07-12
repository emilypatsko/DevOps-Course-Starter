from flask import Flask, render_template
import todo_app.data.session_items as session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template('index.html', items=items)
