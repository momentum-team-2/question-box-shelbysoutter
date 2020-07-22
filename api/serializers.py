from rest_framework import serializers
from core.models import Question, QuestionQuerySet, Answer
from django.contrib.auth.models import User


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Question
        fields = ['url', 'id', 'title', 'body', 'author']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', ]
