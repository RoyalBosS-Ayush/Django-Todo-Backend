from django.test import TestCase, Client
from rest_framework import status
import base64
from django.contrib.auth.models import User
from todoapp.models import TodoItem
from todoapp.serializers import TodoItemSerializer


class TodoItemAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

        credentials = f"{self.username}:{self.password}"
        credentials_base64 = base64.b64encode(credentials.encode()).decode()
        self.auth_header = f"Basic {credentials_base64}"

        self.todo_item = TodoItem.objects.create(
            title="Test Todo API", description="Testing API for Todo", status="OPEN"
        )
        self.todo_item_data = TodoItemSerializer(self.todo_item).data
        self.valid_todo_item_payload = {
            "title": "New Todo",
            "description": "A new task",
            "due_date": "2023-12-31",
            "status": "OPEN",
            "tags": []
        }

    def test_get_all_todo_items(self):
        auth_headers = {"HTTP_AUTHORIZATION": self.auth_header}
        response = self.client.get("/todos/api/todo/", **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_todo_item(self):
        auth_headers = {"HTTP_AUTHORIZATION": self.auth_header}
        response = self.client.get(
            f"/todos/api/todo/{self.todo_item.id}/", **auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.todo_item_data)

    def test_create_todo_item(self):
        auth_headers = {"HTTP_AUTHORIZATION": self.auth_header}
        response = self.client.post(
            "/todos/api/todo/create/",
            self.valid_todo_item_payload,
            content_type="application/json",
            **auth_headers,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_todo_item(self):
        auth_headers = {"HTTP_AUTHORIZATION": self.auth_header}
        updated_title = "Updated Todo"
        updated_data = self.valid_todo_item_payload
        updated_data["title"] = updated_title
        response = self.client.put(
            f"/todos/api/todo/{self.todo_item.id}/update/",
            data=updated_data,
            content_type="application/json",
            **auth_headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_title)

    def test_delete_todo_item(self):
        auth_headers = {"HTTP_AUTHORIZATION": self.auth_header}
        response = self.client.delete(
            f"/todos/api/todo/{self.todo_item.id}/delete/", **auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
