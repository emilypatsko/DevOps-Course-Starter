import os;
import requests;

board_id = os.getenv('BOARD_ID')

def get_lists_on_board():
    return requests.get(f'/1/boards/{board_id}/lists')

def get_items_in_list(listId):
    """
    Fetches all saved items from the Trello board.

    Returns:
        list: The list of saved items.
    """
    return requests.get('https://api.trello.com/1')