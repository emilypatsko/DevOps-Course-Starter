class Item:
    def __init__(self, id, name, list_id):
            self.id = id
            self.name = name
            self.list_id = list_id

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], card['idList'])

class List:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_trello_list(cls, list):
        return cls(list['id'], list['name'])