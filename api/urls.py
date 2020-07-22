from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import QuestionViewSet, UserViewSet, api_root
from rest_framework import renderers


question_list = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('questions/', question_list, name='question-list'),
    path('questions/<int:pk>/', question_detail, name='question-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)