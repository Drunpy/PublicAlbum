from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from galery.models import Photos

class LikeManager(APIView):

    """ Likes or dislike photos."""

    def get(self, request, format=None):
        image_id = request.GET.get('image_id', '')

        photo = Photos.objects.filter(pk=image_id)
        
        if photo.exists() == True:
            photo = photo.first()
            like = photo.like_manager(request)
            
            if like == True:
                return Response(status.HTTP_200_OK)
            else:
                return Response(status.HTTP_401_UNAUTHORIZED)
        
        else:
            return Response(status.HTTP_400_BAD_REQUEST)