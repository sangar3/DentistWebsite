from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST": #IF STATEMENT IS CALLED ONCE USER FILLS OUT FORM
        message_name = request.POST['message-name'] # NAME TAG
        message_email = request.POST['message-email']# EMAIL TAG
        message = request.POST['message']# MESSGAE TAG

        #SENDING EMAIL
        send_mail(
           'Message from'+ message_name,#subject
            message, #message
            message_email,#from email
            ['sgarcia@mail.bradley.edu'], #to Email
        )

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html', {})





