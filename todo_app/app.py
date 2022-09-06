from flask import Flask, render_template, request, redirect
import todo_app.data.trello_items as trello_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = trello_items.get_items()
    lists = trello_items.get_lists()
    return render_template('index.html', items=items, lists=lists)

@app.route('/', methods=['POST'])
def create_todo():
    trello_items.add_item(request.form.get('todo'), 'To Do')
    return redirect('/')