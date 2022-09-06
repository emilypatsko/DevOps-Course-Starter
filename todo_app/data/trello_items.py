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
    
# def get_lists_on_board():
#     return requests.get(f'/1/boards/{board_id}/lists')

# def get_items_in_list(listId):
#     """
#     Fetches all saved items from the Trello board.

#     Returns:
#         list: The list of saved items.
#     """
#     return requests.get('https://api.trello.com/1')