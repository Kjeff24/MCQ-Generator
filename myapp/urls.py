from django.urls import path
from .views import *

urlpatterns = [
    path('', genQuizHome, name='generate-quiz-home'),
    path('quizGenPage/', quizGenPage, name='quizGenPage'),
]