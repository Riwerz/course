from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse


HOST_EMAIL = 'Riwerz2@yandex.ru'


def load_mainpage(request):
    return render(request, 'mainpage.html')


def load_profile(request):
    return render(request, 'profile.html')


def load_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'wrapper.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def load_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, HOST_EMAIL, [to_email])
            return render(request, 'email_confirm.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        message = 'Адрес электронной почти подтверждён'
    else:
        message = 'Недействительная ссылка'
    return HttpResponse(message)


def log_out(request):
    logout(request)
    return render(request, 'mainpage.html')
