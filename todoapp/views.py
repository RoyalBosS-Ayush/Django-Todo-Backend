from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import TodoItem
from .serializers import TodoItemSerializer


class TodoItemCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemReadView(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemListView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemUpdateView(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoItemDeleteView(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
