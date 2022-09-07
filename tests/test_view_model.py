from todo_app.data.classes import ViewModel, Item, List

def test_view_model_doing_items_returns_doing_items():
    # Arrange
    item_1 = Item(1, "Item 1", 1)
    item_2 = Item(2, "Item 2", 2)
    item_3 = Item(3, "Item 3", 3)
    items = [ item_1, item_2, item_3 ]

    lists = [
        List(1, 'To Do'),
        List(2, 'Doing'),
        List(3, 'Done')
    ]

    view_model = ViewModel(items, lists)

    # Act
    filtered_items = view_model.doing_items

    # Assert
    assert filtered_items == [ item_2 ]
