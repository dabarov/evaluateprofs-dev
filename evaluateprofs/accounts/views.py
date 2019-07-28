import requests
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import UserLoginForm, UserRegistrationForm
from .tokens import account_activation_token


def login_view(request):
    form = UserLoginForm(request.POST or None)
    page_title = 'Login'
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    context = {'form': form, 'page_title': page_title}
    return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    page_title = 'Registeration'
    recaptcha_result = 0
    if form.is_valid():
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''
        if result['success']:
            recaptcha_result = 1
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('email_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            print("Success")
            return HttpResponse('Please confirm your email address to\
                                 complete the registration')
        else:
            recaptcha_result = 2
    context = {'form': form, 'page_title': page_title, 'recaptcha_result': recaptcha_result}
    return render(request, 'signup.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')