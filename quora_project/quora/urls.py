from django.urls import path
from . import views
app_name='quora'

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post-question/', views.post_question, name='post_question'),
    path('view-question/', views.view_question, name='view_question'),
    path('answer-question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like-answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]
