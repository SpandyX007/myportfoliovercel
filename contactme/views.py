from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from contactme.models import contactmemodel
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contactform(request):
    param={'title':'contactme'}
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        name=fname+" "+lname
        email=request.POST.get("email")
        contactnumber=request.POST.get("contactnumber")
        designation=request.POST.get("designation")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contactdata=contactmemodel(email_model=email, name_model=name, subject_model=subject, message_model=message, contactnumber_model=contactnumber, designation_model=designation)
        contactdata.save()
        #email to client
        # send_mail(
        #     subject='Thank You for Connecting to Me',
        #     message='Dear '+name+"!\nThank you for reaching out! I truly appreciate the opportunity to collaborate and explore creative ideas together. I'm excited to discuss how we can work on something amazing. Looking forward to connecting, sharing insights, and making this collaboration a success. Let’s schedule a time to chat soon!\nFeel free to contact me anytime as per your requirements.\nContact Number: +91 9679291101\nEmail-ID: spandanar1234@gmail.com\nThank You\n",
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[email],
        #     fail_silently=False,
        # )
        # #email to me
        # send_mail(
        #     subject='Connection Request by '+name,
        #     message='Mr/Mrs. '+name+" is trying to reach you out for a collaboration for a project\n Please check your portfolio\n",
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=['spandanar1234@gmail.com'],
        #     fail_silently=False,
        # )
        return redirect(thankyou)
    return render(request, "contactme.html",param)

def thankyou(request):
    param={'title':'Thank You'}
    return render(request, "thankyou.html",param)
