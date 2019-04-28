from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib import messages
from noslqdjango import settings
import boto3

from galery.models import Photos

def read(request):
    pass

def upload(request):
    if request.method == 'GET':
        return render(
            request,
            template_name='gallery/upload.html'
        )
    
    if request.method == 'POST':

        request_success = 'Thank you for contributing to our wedding album ! Your photos will show up as soon as grooms aprove.'
        request_error = 'Opss ! Something went wrong: '
        request_empty = 'Please choose an image to send.'
        
        author = request.POST.get('friend_name') 
        images = request.FILES.getlist('images[]')

        if len(images) == 0: 
            messages.error(request, request_empty)
            return HttpResponseRedirect(reverse('upload_image'))

        try:        
            for image in images:
                
                new_photo = Photos()
                new_photo.upload_photo(request, file=image, authors_name=author)
                
            messages.success(request, request_success)
            return HttpResponseRedirect(reverse('index'))
            
        except Exception as ex:
            messages.error(request, request_error+str(ex))
            return HttpResponseRedirect(reverse('upload_image'))
