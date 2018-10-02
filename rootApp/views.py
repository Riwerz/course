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
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import ConspectForm
from .models import Conspect


HOST_EMAIL = 'Riwerz2@yandex.ru'


def load_conspect(request):
    return render(request, 'conspect_create.html')


def load_mainpage(request):
    return render(request, 'mainpage.html')


def conspect_browse(request):
    return render(request, 'conspect_browse.html', {'conspect': Conspect.objects.get(pk=request.GET['pk'])})


def load_profile(request):
    return render(request, 'profile.html', {'conspects': Conspect.objects.filter(author=request.user)})


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
            user.first_name = request.POST['name']
            user.last_name = request.POST['surname']
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
            send_mail(mail_subject, message, HOST_EMAIL, [to_email], fail_silently=False)
            return render(request, 'email_confirm.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def publish_conspect(request):
    if request.method == 'POST':
        form = ConspectForm(request.POST)
        if form.is_valid():
            conspect = form.save(commit=False)
            conspect.author = request.user
            conspect.publish()
            conspect.save()
            return HttpResponseRedirect('profile')
    else:
        form = ConspectForm()
    return render(request, 'conspect_create.html', {'form': form})


def conspect_entries(request):
    return render(request, 'conspect_table.html', {'conspects': Conspect.objects.filter(author=request.user)})


def conspect_delete(request):
    id = request.POST['id']
    Conspect.objects.filter(pk=id).delete()
    return JsonResponse({})


def conspect_edit(request, id):
    post = Conspect.objects.get(pk=id)
    if request.method == 'POST':
        form = ConspectForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
    else:
        form = ConspectForm(instance=post)
    return render(request, 'conspect_create.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        message = 'Адрес электронной почти подтверждён'
    else:
        message = 'Недействительная ссылка'
    return HttpResponse(message)


def log_out(request):
    logout(request)
    return render(request, 'mainpage.html')
