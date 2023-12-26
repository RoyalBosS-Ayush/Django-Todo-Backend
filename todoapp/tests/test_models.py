from django.test import TestCase
from todoapp.models import TodoItem, Tag

class TodoItemModelTestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='Tag1')
        self.tag2 = Tag.objects.create(name='Tag2')

        self.todo_item = TodoItem.objects.create(
            title='Test Todo',
            description='This is a test todo',
            status='OPEN'
        )
        self.todo_item.tags.add(self.tag1, self.tag2)

    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.get(title='Test Todo')
        self.assertEqual(todo_item.description, 'This is a test todo')
        self.assertEqual(todo_item.status, 'OPEN')
        self.assertEqual(todo_item.tags.count(), 2)
