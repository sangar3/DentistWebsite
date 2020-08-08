from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST": #IF STATEMENT IS CALLED ONCE USER FILLS OUT FORM
        message_name = request.POST['message-name'] # NAME TAG
        message_email = request.POST['message-email']# EMAIL TAG
        message = request.POST['message']# MESSGAE TAG
        subject = request.POST['subject']# MESSGAE TAG
        #SENDING EMAIL
        send_mail(
            subject,#subject
            message, #message
            message_email,#from email
            ['sgarcia@mail.bradley.edu'], #to Email
        )

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request,'about.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def service(request):
    return render(request,'service.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blog_details(request):
    return render(request,'blog-details.html',{})


def appointment(request):
    if request.method == "POST": #IF STATEMENT IS CALLED ONCE USER FILLS OUT FORM
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        # SENDING EMAIL
        appointment = "Name: " + your_name + "Phone:" + your_phone + "Email" + your_email + "Address: " + your_address + "Schedule: " + your_schedule + "Day: " + your_date + "Message: " + your_message
        send_mail(
            'Appointment Request',#subject
            appointment, #message
            your_email,#from email
            ['sgarcia@mail.bradley.edu'], #to Email
        )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule': your_schedule,
            'your_date':your_date,
            'your_message':your_message,

        })

    else:
        return render(request, 'home.html', {})
