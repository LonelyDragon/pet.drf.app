from django.urls import path
from .views import *


'''
POST /api/createPoll/ создать голосование c вариантами ответов
POST /api/poll/ проголосовать за конкретный вариант: <poll_id, choice_id>
POST /api/getResult/ получить результат по конкретному голосованию: <poll_id>
'''
urlpatterns = [
    path('api/createPoll/', CreatePool.as_view(), name='create_poll'),
#    path('api/poll/'),
    path('api/getResult', GetPoolInfo.as_view(), name='get_result'),
]