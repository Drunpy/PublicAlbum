from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from galery.models import Photos

def aprove(request):
    if request.method == 'GET':

        photos = Photos.objects.filter(is_aproved=False).order_by('-created_at')

        return render(request,
            template_name="gallery/administration/aprove.html",
            context={
                'photos':photos
            }
        )

def adm_login(request):
    
    if request.method == 'GET':
        return render(request, template_name="gallery/administration/login.html")
    
    if request.method == 'POST':

        request_deny = "You can't access this area."
    
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username != '' and password != '':
            auth = authenticate(request, username=username, password=password)

            if auth != None:
                if auth.is_staff == True:
                    login(request, auth)
                    return HttpResponseRedirect(reverse('aprove_photos'))
                else:
                    messages.error(request, request_deny)
                    return HttpResponseRedirect(reverse('adm_login'))
                
            else:
                messages.error(request, request_deny)
                return HttpResponseRedirect(reverse('adm_login'))
