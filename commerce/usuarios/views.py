from typing import Pattern
from django.contrib.sites import requests
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .models import User
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import json
from .serializers import UserSerializer
from django.template.loader import render_to_string





@api_view(['POST'])    

def signup(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        form = SignupForm(data)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Ative sua conta do site Máquinas Fereira.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, 'Não responda <do_not_reply@domain.com>', to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return HttpResponse(request.errors)
    else:
        return HttpResponse(request.method)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.uid = uid
        user.token = token
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('http://localhost:8080/login')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def changePassword(request, uidb64, token):
    
    return redirect('http://localhost:8080/activate/'+str(uidb64)+'/'+str(token)+'/') 
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

