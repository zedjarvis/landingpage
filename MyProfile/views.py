from django.shortcuts import render
from .models import Contact
# Create your views here.


def index(request):
    if request.method == "POST":
        # instance of model.contacts
        contact = Contact()

        # Getting values from contact form
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")

        # committing form values to the database
        contact.full_name = name
        contact.email = email
        contact.phone = phone
        contact.message = subject
        contact.save()

    return render(request, 'MyProfile/index.html')
