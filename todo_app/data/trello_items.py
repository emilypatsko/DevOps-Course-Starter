import os;
import requests;
from todo_app.data.classes import Item, List 

base_url = 'https://api.trello.com/1'

def get_items():
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    board_id = os.getenv('BOARD_ID')

    response = requests.get(f'{base_url}/boards/{board_id}/cards', params=auth_params).json()
    items = list(map(Item.from_trello_card, response))
    return items

def get_item(id: str):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item.id == id), None)
    
def get_lists():
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    board_id = os.getenv('BOARD_ID')

    response = requests.get(f'{base_url}/boards/{board_id}/lists', params=auth_params).json()
    lists = list(map(List.from_trello_list, response))
    return lists

def get_list_by_name(list_name: str):
    lists = get_lists()
    return next((list for list in lists if list.name == list_name), None)

def add_item(title: str):
    """
    Adds a new item with the specified title to the 'To Do' column

    Args:
        title: The title of the item.
        list_name: The name of the list you want to add the item to.

    Returns:
        The request response.
    """
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    
    list = get_list_by_name('To Do')
    query_params = {
        "name": title,
        "idList": list.id
    }

    response = requests.post(f'{base_url}/cards', params=auth_params | query_params)
    return response.json()

def start_item(item_id: str):
    """
    Moves an item with the specified ID to the 'Doing' column

    Args:
        id: The ID of the item.

    Returns:
        The request response.
    """
    list = get_list_by_name('Doing')
    return move_item(item_id, list.id)

def complete_item(item_id: str):
    """
    Moves an item with the specified ID to the 'Done' column
    """
    list = get_list_by_name('Done')
    return move_item(item_id, list.id)

def undo_item(item_id: str):
    """
    Moves an item with the specified ID back to the 'To Do' column
    """
    list = get_list_by_name('To Do')
    return move_item(item_id, list.id)

def move_item(item_id: str, list_id: str):
    auth_params = {
        "key": os.getenv('APP_KEY'),
        "token": os.getenv('APP_TOKEN')
    }
    
    query_params = {
        "idList": list_id
    }

    response = requests.put(f'{base_url}/cards/{item_id}', params=auth_params | query_params)
    return response.json()
