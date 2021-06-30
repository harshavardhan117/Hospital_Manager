from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from .forms import CustomRegistrationForm


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# Create your views here.

def send(tomail):
    from_add='harshavardhansuram@gmail.com'
    to_add=tomail
    subject="Registration Successful!!"

    msg=MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject

    body="<b>Dear user, You have successfully registered on Hospital Manager.Now Login and access your account</b>"
    msg.attach(MIMEText(body,'html'))

    # my_file=open(filename,'rb')
    #
    # part=MIMEBase('application','octet-stream')
    # part.set_payload((my_file).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition','attachment; filename= '+ filename)
    # msg.attach(part)
    message=msg.as_string()

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'juwbxqkmiwugxiri')
    server.sendmail(from_add,to_add,message)
    server.quit()

def register(request):
    if request.method=="POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            str=request.POST["email"]
            send(str)
            messages.success(request,("New User Account Created Login to get Started!"))
            return redirect('register')
    else:
         register_form = CustomRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})