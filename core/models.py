from django.db import models
from users.models import User
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class QuestionQuerySet(models.QuerySet):
    def for_user(self, user):
        if user.is_authenticated:
            questions = self.filter(Q(public=True) | Q(author=user))
        else:
            questions = self.filter(public=True)
        return questions

    def search(self, search_term):
        questions = self.annotate(search=SearchVector(
            'title', 'body'
        ))
        questions = questions.filter(search=search_term).distinct('pk')
        return questions
    
    def public(self):
        return self.filter(public=True)


class Question(models.Model):
    objects = QuestionQuerySet.as_manager()
    title = models.CharField(max_length=225)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    favorited_by = models.ManyToManyField(User, related_name='favorite_question', blank=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author}: {self.title}"


class Answer(models.Model):
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    favorited_by = models.ManyToManyField(User, related_name='favorite_answer', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to: {self.author}: {self.question}"


def get_question_for_user(queryset, user):
    if user.is_authenticated:
        questions = queryset.filter(Q(public=True) | Q(author=user))
    else:
        questions = queryset.filter(public=True)
    return questions


def search_questions_for_user(user, search_term):
    questions = get_question_for_user(Question.objects, user)
    questions = questions.annotate(search=SearchVector(
        'title', 'body'
    ))
    questions = questions.filter(search=search_term).distinct('pk')
    return questions