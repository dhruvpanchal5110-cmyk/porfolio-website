from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
import requests


def home(request):
    return render(request, "home.html")


def submit_contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Database me save
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Formspree ko send
        requests.post(
            "https://formspree.io/f/xlgvvvnb",
            data={
                "name": name,
                "email": email,
                "subject": subject,
                "message": message
            }
        )

        messages.success(request, "Message sent successfully!")

    return redirect("home")