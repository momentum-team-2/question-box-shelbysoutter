from django.forms import ModelForm, Textarea
from .models import Question, Answer

class QuestionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs['class']='db border-box hover-black w-100 measure ba b--black-20 pa2 br2 mv2'
    
    class Meta:
        model = Question
        fields = [
            'question',
        ]


class AnswerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs['class']='db border-box hover-black w-100 measure ba b--black-20 pa2 br2 mv2'
        
    class Meta:
        model = Answer
        fields = [
            'answer',
        ]