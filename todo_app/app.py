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

# Would like to use PUT, but PUT doesn't work with the HTML method attribute
@app.route('/start/<id>', methods=['POST'])
def start_item(id: str):
    trello_items.start_item(id)
    return redirect('/')

@app.route('/complete/<id>', methods=['POST'])
def complete_item(id: str):
    trello_items.complete_item(id)
    return redirect('/')

@app.route('/undo/<id>', methods=['POST'])
def undo_item(id: str):
    trello_items.undo_item(id)
    return redirect('/')