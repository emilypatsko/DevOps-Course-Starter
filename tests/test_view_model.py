from todo_app.data.classes import ViewModel, Item, List
import pytest

@pytest.fixture
def view_model():
    items = [ 
        Item(1, "Item 1", 1),
        Item(2, "Item 2", 2),
        Item(3, "Item 3", 3)
    ]

    lists = [
        List(1, 'To Do'),
        List(2, 'Doing'),
        List(3, 'Done')
    ]

    yield ViewModel(items, lists)

def test_view_model_to_do_items_returns_to_do_items(view_model: ViewModel):
    # Act
    filtered_items = view_model.to_do_items

    # Assert
    assert filtered_items == [ view_model._items[0] ]

def test_view_model_doing_items_returns_doing_items(view_model: ViewModel):
    # Act
    filtered_items = view_model.doing_items

    # Assert
    assert filtered_items == [ view_model._items[1] ]

def test_view_model_done_items_returns_done_items(view_model: ViewModel):
    # Act
    filtered_items = view_model.done_items

    # Assert
    assert filtered_items == [ view_model._items[2] ]
