from django.forms import ModelForm, Textarea
from .models import Question, Answer

class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = [
            'title',
            'body',
            'author',
        ]


class AnswerForm(ModelForm):
   
    class Meta:
        model = Answer
        fields = [
            'answer',
            'author',
            'question',
        ]