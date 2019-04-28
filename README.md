### Deployed application: https://album42.herokuapp.com/

## Project composition
    - Main app
    - API
    - MongoDB stored at Atlas
    - AWS S3 for image files
    - Static files provided via CDN
    - Bootstrap4 and AJAX for frontend 

## Setting up localy
    - Clone repo at https://github.com/Drunpy/PublicAlbum.git
    - Configure your AWS keys at nosqldjango/settings.py
    - Configure your database at DATABASES also in nosqldjango/settings.py
    - Install both requirements
    - Whit open ./manage.py shell 
        - from django.contrib.auth.models import User
        - User.objects.create_user(username="jonh@wedding.com", first_name='Jonh', last_name="Doe", password='424242', is_staff=True)
        - User.objects.create_user(username="jana@wedding.com", first_name='Jana', last_name="Doe", password="424242", is_staff=True)
    - At project root run ./manage.py test
    - To run application do ./manage.py runserver

## Requested features 
    - Users must be able to upload photos
        - Open the https://album42.herokuapp.com/
        - Click the "Upload button"
        - Choose one or more photos and confirm
        - Check the preview and hit upload
        - Your upload will be at administration area waiting bride and groom aprovement.
    
    - Users must be able to filter photos by date and likes
        - At https://album42.herokuapp.com/
        - Above the photos there you will see the filter option
        - "Filter by: Likes | Date"
        - There are three example pictures to test filter
        - Clear button should clean the filters

    - Users must be able to like photos
        - Above the photos you have a like button 
        - When clicked it changes it's color and makes an AJAX
        - to the "likes_management" API
        - Somehow AJAX calls got messed when deployed at heroku.
        - Thus invalidating the like feature as well as aprove photo feature
        - Which uses AJAX calls as well.
        - You can see the broken request being called at "Network" in the developer painel

    - Bride and groom should aprove the photos
        - Administration area can be accessed at https://album42.herokuapp.com/administration/login
        - You can choose between "jana@wedding.com" or "john@wedding.com" to login.
        - Password is 424242 for both of them.
        - after login you will be able to see the pictures which were not aproved.
        - As said before, features that include AJAX calls, which includes "Aprove" photos got messed after deploy.
        - You can see the broken request being called at "Network" in the developer painel.
    
## Main Technologies && Libs 
    - Python3.7
    - Django2.1
    - Djongo (MongoDB related)
    - Django Rest Framework (APIs) 
    - boto3 (AWS related)
    - Heroku for deploy
    - AWS S3 (for image storage)
    - MongoDB (at Atlas server)

## Additional inforamation
    - Author: Lorran Rosa (rosalorran@gmai.com)
    - Project repo: https://github.com/Drunpy/PublicAlbum.git
    - Project site: https://album42.herokuapp.com/
    - Models for the app can be found at galery/models.py