import os
import pytest
from dao.todo import TodoDAO

@pytest.fixture
def todo_instance():
    return TodoDAO()

class TestTodoClass:

    # def test_1(todo_instance):
    #     obj = todo_instance.create({'task': 'Build an API'})
    #     id = obj.id
    #     test_a = todo_instance.get(id)
    #     actual_task = test_a.task
    #     assert 'Build an API' == actual_task

    def test_create(self, todo_instance):
        # instance = TodoDAO()
        obj = todo_instance.create({'task': 'Build an API'})
        # a = 1
        # b = 2
        # assert a != b
        assert 'Build an API' == obj['task']
        assert len(todo_instance.todos) == 1

    # def test_get(self):
    #     instance = TodoDAO()
    #     assert len(instance.todos) == 3

# def test_2(todo_instance):
#     # todo_instance = TodoDAO()
#     obj = todo_instance.create({'task': 'Build an API'})
#     a = 1
#     b = 2
#     # assert a != b
#     assert 'Build an API' == obj['task']