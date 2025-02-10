from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from core.models import Booking
import paypalrestsdk
import datetime

paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox or live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def index(request):
    return render(request, 'index.html')

def book_session(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        date_str = request.POST.get('date')
        time = request.POST.get('time')
        session_type = request.POST.get('session_type')

        # Convert date format
        date = datetime.datetime.strptime(date_str, '%B %d, %Y').date()

        # Set price based on session type
        if session_type == '2-station':
            price = "200.00"
        elif session_type == '4-station':
            price = "400.00"

        # Create PayPal payment
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payment/execute/'),
                "cancel_url": request.build_absolute_uri('/payment/cancel/')
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": f"{session_type} mock session",
                        "sku": "001",
                        "price": price,
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": price,
                    "currency": "USD"
                },
                "description": f"Booking for {session_type} mock session on {date} at {time}."
            }]
        })

        if payment.create():
            print(payment)
            
            # Create a new booking
            booking = Booking(email=email, date=date, time=time, session_type=session_type, payment_id=payment.id)
            booking.save()
            
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    return redirect(approval_url)
        else:
            print(payment.error)

    return render(request, 'book_session.html')

def payment_execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    try:
        # Check if booking already exists and is paid
        existing_booking = Booking.objects.filter(payment_id=payment_id).first()
        if existing_booking and existing_booking.payment_status:
            return redirect('booking_success')

        print(f"Finding payment with ID: {payment_id}")
        payment = paypalrestsdk.Payment.find(payment_id)
        
        if payment.execute({"payer_id": payer_id}):
            # Update or create booking payment status
            booking = Booking.objects.get(payment_id=payment_id)
            booking.payment_status = True
            booking.save()

            # Send confirmation email
            send_mail(
                'Mock Session Booking Confirmation',
                f'Thank you for booking a {booking.session_type} mock session on {booking.date} at {booking.time}.',
                settings.DEFAULT_FROM_EMAIL,
                [booking.email],
                fail_silently=False,
            )

            return redirect('booking_success')
        else:
            print(f"Payment execution failed: {payment.error}")
            return redirect('booking_failed')
            
    except Exception as e:
        print(f"Payment processing error: {str(e)}")
        return redirect('booking_failed')
    
def booking_success(request):
    return render(request, 'booking_success.html')

def booking_failed(request):
    return render(request, 'booking_failed.html')

