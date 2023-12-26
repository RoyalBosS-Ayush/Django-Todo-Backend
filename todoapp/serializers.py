from rest_framework import serializers
from .models import TodoItem, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

    def to_internal_value(self, data):
        return data


class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = TodoItem
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        todo_item = TodoItem.objects.create(**validated_data)

        for tag_data in tags_data:
            tag_name = tag_data["name"]
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            todo_item.tags.add(tag)

        return todo_item

    def update(self, instance, validated_data):
        tags_data = validated_data.pop(
            "tags", []
        )  # Extract tags data from validated_data

        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.due_date = validated_data.get("due_date", instance.due_date)
        instance.status = validated_data.get("status", instance.status)
        instance.save()  # Update TodoItem fields

        existing_tags = list(instance.tags.all())
        existing_tag_names = {tag.name for tag in existing_tags}

        # Handle removal of tags
        for tag in existing_tags:
            tag_name = tag.name
            if tag_name not in [tag_data["name"] for tag_data in tags_data]:
                instance.tags.remove(tag)
                existing_tag_names.remove(tag_name)

        # Handle addition of new tags and update existing tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(
                name=tag_data["name"]
            )  # Get or create Tag object
            if tag_data["name"] not in existing_tag_names:
                instance.tags.add(tag)  # Associate the Tag with the TodoItem
                existing_tag_names.add(tag_data["name"])

        return instance
