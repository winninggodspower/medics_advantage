from django.urls import path
from .views import index, book_session

urlpatterns = [
    path('', index, name='index'),
    path('book_session', book_session, name='book_session')
]
