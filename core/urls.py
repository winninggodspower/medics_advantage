from django.urls import path
from .views import index, book_session, payment_execute, booking_success, booking_failed, contact_us

urlpatterns = [
    path('', index, name='index'),
    path('contact_us/', contact_us, name='contact_us'),
    path('book_session/', book_session, name='book_session'),
    path('payment/execute/', payment_execute, name='payment_execute'),
    path('booking_success/', booking_success, name='booking_success'),
    path('booking_failed/', booking_failed, name='booking_failed'),
]
