from django.conf import settings as django_settings
from django.views.generic.base import ContextMixin
from djoser import email


class UpdateContext(ContextMixin):
    """
    Custom context mixin for adding extra context data to DJOSER email templates.
    """
    def get_context_data(self):
        context = super().get_context_data()
        context['frontend_site_name'] = django_settings.ALLOWED_HOSTS[0]

        return context


class ActivationEmail(UpdateContext, email.ActivationEmail):
    """
    Class for sending an account activation email based on the DJOSER class
    """
    # Override activation email template
    template_name = 'email/account_email_activation.html'


class PasswordResetEmail(UpdateContext, email.PasswordResetEmail):
    """
    Class for sending a password reset email based on the DJOSER class
    """
    # Override password reset email template
    template_name = 'email/account_password_reset.html'
