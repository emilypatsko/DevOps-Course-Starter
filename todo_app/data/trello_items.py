import os;
import requests;

params = {
    "key": os.getenv('APP_KEY'),
    "token": os.getenv('APP_TOKEN')
}

base_url = 'https://api.trello.com/1'
board_id = os.getenv('BOARD_ID')

def get_items():
    return requests.get(f'{base_url}/boards/{board_id}/cards', params=params).json()

def get_item(id: str):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == id), None)
    
def get_lists():
    lists = requests.get(f'{base_url}/boards/{board_id}/lists', params=params).json()
    return dict((list["name"], list["id"]) for list in lists)

def get_list_id(list_name: str):
    lists = get_lists()
    return lists[list_name]

def add_item(title: str, list_name: str):
    """
    Adds a new item with the specified title to the 'To Do' column

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    list_id = get_list_id(list_name)
    post_params = {
        "name": title,
        "idList": list_id
    }

    response = requests.post(f'{base_url}/cards', params=params | post_params)
    return response.json()
