from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import SignUpForm


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = '/rent/rentals/'