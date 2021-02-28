from django.shortcuts import render
from quiz.settings import EMAIL_HOST_USER

from .forms import Subscribe
from django.core.mail import send_mail

# Create your views here.
# Send your email
def subscribe(request):
    
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = str(sub['subject'].value())#'Welcome to Polls'
        message = str(sub['Email_body'].value())#'Thank you for your registration'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'useremail/success.html', {'recepient': recepient})
    else:
        sub = Subscribe()
    return render(request, 'useremail/index.html', {'form':sub})