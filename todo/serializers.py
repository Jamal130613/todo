from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, attrs):
        title = attrs.get('title')
        print(title)
        title = title.upper()
        attrs['title'] = title
        return attrs

    def validate_description(self, desc):
        if len(desc) < 20:
            raise serializers.ValidationError('Описание слишком короткое!')
        return desc

