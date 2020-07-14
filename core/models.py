from django.db import models
from users.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    favorited_by = models.ManyToManyField(User, related_name='favorite_question', blank=True)

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
