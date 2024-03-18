from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

def detectUser(user):
    # print(f"00000000002222222222222000000000000 {user.get_role()}")

    if user.get_role() == 'Vendor':
        redirectURL = 'venDashboard'
        return redirectURL
    elif user.get_role() == 'Customer':
        redirectURL = 'custDashboard'
        return redirectURL
    


#Email sending helper function
def send_verification_email(request, user, mail_subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    message = render_to_string(email_template, {
        'user' : user,
        'domain' : current_site,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : default_token_generator.make_token(user),
    })
    destination_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[destination_email])
    mail.send()


