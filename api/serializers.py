from rest_framework import serializers
from core.models import Question, QuestionQuerySet, Answer
from users.models import User


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    question_id = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ['url', 'id', 'author', 'question_id', 'answer']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    answers = AnswerSerializer(many=True, read_only=True)

    
    class Meta:
        model = Question
        fields = ['url', 'id', 'title', 'body', 'author', 'answers']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only = True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'questions']
