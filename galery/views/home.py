from django.core.paginator import Paginator
from django.shortcuts import render
from galery.models import Photos

def index(request):
    date = request.GET.get('date', '')
    likes = request.GET.get('like', '')
    base_host = 'https://album42.herokuapp.com/'
    
    photos = Photos.objects.filter(is_aproved=True, is_deleted=False)

    # Filter by date 
    if date == '1':
        photos = Photos.objects.filter(is_aproved=True, is_deleted=False).order_by('-created_at')
    
    # Filter by like
    if likes == '1':
        photos = Photos.objects.filter(is_aproved=True, is_deleted=False).order_by('-like_count')

    paginator = Paginator(photos, 10)

    page = request.GET.get('page')
    pag_photos = paginator.get_page(page)
   
    return render(
        request,
        template_name='gallery/index.html',
        context={
            'photos':pag_photos,
            'base_host':base_host
        }
    )
    