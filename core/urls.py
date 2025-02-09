from django.urls import path
from .views import index, book_session, payment_execute, booking_success, booking_failed

urlpatterns = [
    path('', index, name='index'),
    path('book_session/', book_session, name='book_session'),
    path('payment/execute/', payment_execute, name='payment_execute'),
    path('booking_success/', booking_success, name='booking_success'),
    path('booking_failed/', booking_failed, name='booking_failed'),
]
