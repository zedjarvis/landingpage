from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Contact
# Create your views here.


def index(request):
    return render(request, 'MyProfile/index.html')


# Contact Form ajax call
class ContactForm(View):
    def post(self, request):
        full_name = request.POST.get('name', None)
        subject = request.POST.get('subject', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)

        contact = Contact(full_name=full_name,
                          email=email,
                          subject=subject,
                          message=message)
        contact.save()

        # Send email to user who contacted the company
        template = render_to_string('MyProfile/email_template.html',
                                    {'name': full_name})
        email = EmailMessage(
            'This is an Automated reply, Let me get back to you shortly.',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        try:
            email.send()
        except (Exception) as e:
            print(str(e))

        return JsonResponse({'msg': 'successful'})
