from django.views.generic import TemplateView

class Otp(TemplateView):
    template_name = 'otp.html'
