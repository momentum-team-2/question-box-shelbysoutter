from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    def is_favorite_question(self, question):
        return self.favorite_question.filter(pk=question.pk).count() == 1
