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

class ViewModel:
    def __init__(self, items, lists):
        self._items = items
        self._lists = lists

    @property
    def items(self):
        return self._items

    @property
    def lists(self):
        return self._lists

    @property
    def to_do_items(self):
        return []

    @property
    def doing_items(self):
        return []

    @property
    def done_items(self):
        return []
