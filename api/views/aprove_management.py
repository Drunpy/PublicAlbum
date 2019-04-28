from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from galery.models import Photos

class aproveManagement(APIView):

    def get(self, request, format=None):

        if request.user.is_authenticated == True:
            image_id = request.GET.get('image', '')

            image = Photos.objects.filter(id=int(image_id))

            if image.exists() == True:
                image = image.first()
                was_aproved = image.aprove(request)
                
                if was_aproved != False:
                    return Response(status.HTTP_200_OK)
                
                else:
                    return Response(status.HTTP_401_UNAUTHORIZED)
            
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
    
        else:
            return Response(status.HTTP_403_FORBIDDEN)