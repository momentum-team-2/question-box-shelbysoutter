from rest_framework import views, viewsets
from core.models import QuestionQuerySet, Question, Answer
from api.serializers import QuestionSerializer, UserSerializer, AnswerSerializer
from rest_framework import generics
from users.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers 
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
        'answers': reverse('answer-list', request=request, format=format),
    })

