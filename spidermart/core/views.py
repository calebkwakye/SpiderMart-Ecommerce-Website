from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):
    items = Item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()


    return render(request, "core/index.html", {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Send the email to the user
            subject = 'Sign Up Confirmation'
            html_message = render_to_string('email/signup.html', {'user': user})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

            messages.success(request, 'Account created successfully. An email has been sent to your registered email address.')
            return redirect('login')  # Redirect to the login page after successful sign-up
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})