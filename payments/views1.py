from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Payment

# Create your views here.
def payments(request):
    if request.method == 'POST':
        roomType = request.POST["roomType"]
        if roomType == 'singleRoom':
            numberOfRooms = request.POST["singleRoomCount"]
        elif roomType == 'doubleRoom': 
            numberOfRooms = request.POST["doubleRoomCount"]
        elif roomType == 'twinRoom': 
            numberOfRooms = request.POST["twinRoomCount"]
        elif roomType == 'kingRoom': 
            numberOfRooms = request.POST["kingRoomCount"]
        fullName = request.POST["fullName"]
        phoneNo = request.POST["phoneNo"]
        creditCardType = request.POST["creditCardType"]
        creditCard = request.POST["creditCard"]
        validThru = request.POST["validThru"]
        CVC = request.POST["cvc"]
        checkInDate = request.POST["checkIn"]
        checkOutDate = request.POST["checkOut"]
        totalPrice = request.POST["totalPrice"]
        has_paid = Payment.objects.all().filter(fullName=fullName,roomType=roomType)
        if has_paid:
            messages.error(request,"You have already made a payment")
#           return redirect('payments')
            return render(request, 'payments/payments.html')
        payment = Payment(roomType=roomType, numberOfRooms=numberOfRooms,fullName=fullName,phoneNo=phoneNo,creditCardType=creditCardType,creditCard=creditCard,validThru=validThru,CVC=CVC,checkInDate=checkInDate,checkOutDate=checkOutDate,totalPrice=totalPrice)
        payment.save()
        messages.success(request,"Your request has been submitted a payment successfully")
#    return redirect('roomtypes')
        return render(request, 'index.html')
    else:
        return render(request, 'payments/payments.html')