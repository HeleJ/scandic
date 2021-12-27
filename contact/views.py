from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            message = form.cleaned_data['message']

    else:
        form = ContactForm()


def send_success(request):
    return HttpResponse('thanks you for you email ^_^')
