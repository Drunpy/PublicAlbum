from django import template
from galery.models import Likes

register = template.Library()

# Check if a photo is liked by the user
@register.simple_tag
def is_liked(request, photo):

    user = request.META.get('REMOTE_ADDR')
    photo = int(photo)

    is_liked = Likes.objects.filter(author_ip=user, reference_photo=photo).exists()

    if is_liked == True:
        return False
    else: 
        return True
    