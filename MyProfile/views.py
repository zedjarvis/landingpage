from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
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

        # Send email to user who contacted the company
        template = render_to_string('MyProfile/email_template.html',
                                    {'name': name})
        email = EmailMessage(
            'Thank You For Contacting Me.',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        try:
            email.send()
        except (Exception):
            pass

    return render(request, 'MyProfile/index.html')
