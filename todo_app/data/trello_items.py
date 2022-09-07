import os;
import requests;

class Item:
    def __init__(self, id, name, list_id):
            self.id = id
            self.name = name
            self.list_id = list_id

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], card['idList'])

auth_params = {
    "key": os.getenv('APP_KEY'),
    "token": os.getenv('APP_TOKEN')
}

base_url = 'https://api.trello.com/1'
board_id = os.getenv('BOARD_ID')

def get_items():
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
    return next((item for item in items if item['id'] == id), None)
    
def get_lists():
    lists = requests.get(f'{base_url}/boards/{board_id}/lists', params=auth_params).json()
    return dict((list["name"], list["id"]) for list in lists)

def get_list_id(list_name: str):
    lists = get_lists()
    return lists[list_name]

def add_item(title: str):
    """
    Adds a new item with the specified title to the 'To Do' column

    Args:
        title: The title of the item.
        list_name: The name of the list you want to add the item to.

    Returns:
        The request response.
    """
    list_id = get_list_id('To Do')
    query_params = {
        "name": title,
        "idList": list_id
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
    list_id = get_list_id('Doing')
    return move_item(item_id, list_id)

def complete_item(item_id: str):
    """
    Moves an item with the specified ID to the 'Done' column
    """
    list_id = get_list_id('Done')
    return move_item(item_id, list_id)

def undo_item(item_id: str):
    """
    Moves an item with the specified ID back to the 'To Do' column
    """
    list_id = get_list_id('To Do')
    return move_item(item_id, list_id)

def move_item(item_id: str, list_id: str):
    query_params = {
        "idList": list_id
    }

    response = requests.put(f'{base_url}/cards/{item_id}', params=auth_params | query_params)
    return response.json()
