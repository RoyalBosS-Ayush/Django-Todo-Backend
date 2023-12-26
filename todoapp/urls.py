from django.urls import path
from . import views

urlpatterns = [
    path('api/todo/', views.TodoItemListView.as_view(), name='todo-list'),
    path('api/todo/create/', views.TodoItemCreateView.as_view(), name='todo-create'),
    path('api/todo/<int:pk>/', views.TodoItemReadView.as_view(), name='todo-detail'),
    path('api/todo/<int:pk>/update/', views.TodoItemUpdateView.as_view(), name='todo-update'),
    path('api/todo/<int:pk>/delete/', views.TodoItemDeleteView.as_view(), name='todo-delete'),
]
