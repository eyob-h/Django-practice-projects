from django.db import models
from accounts.models import User, UserProfile
# Create your models here.
from accounts.utils import send_notification

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_licence = models.ImageField(upload_to='vendors/licence')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
    
    def save(self, *args, **kwargs):

        if self.pk is not None:
            original = Vendor.objects.get(pk=self.pk)
            if original.is_approved != self.is_approved:
                context = {
                    "user":self.user,
                    "is_approved":self.is_approved
                }
                mail_template = "accounts/emails/admin_approval_email.html"
                if self.is_approved == True:
                    mail_subject = "Congrats! Your business is approved"
                    send_notification(mail_subject, mail_template, context)
                else:
                    mail_subject = "Sorry! Your business is not approved"
                    send_notification(mail_subject, mail_template, context)


        return super(Vendor, self).save(*args, **kwargs)
