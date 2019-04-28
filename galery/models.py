from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from noslqdjango import settings
import boto3


# Extra user Data
class Extra(models.Model):
    user = models.ForeignKey(User, verbose_name='Extended user data.', null=False, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=150, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now_add=False, null=True)

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        super().save()

    def save(self):
        if self.full_name == None or self.full_name == '':
            self.full_name = '{0} {1}'.format(str(self.user.first_name).title(), str(self.user.last_name).title())
        
        super().save()

    def __str__(self):
        return '{0}'.format(self.full_name)

# Documentation doesn't specify if the user must be registered or not.
class Likes(models.Model):
    author_ip = models.CharField(max_length=50)
    reference_photo = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{0}'.format(self.author.extra_set.full_name)


class Photos(models.Model):

    author = models.CharField(verbose_name="Author's name if provided.", max_length=150, null=True)
    author_ip = models.CharField(verbose_name="Author's IP.", max_length=50)
    reference_url = models.URLField(verbose_name='URL to the picture in AWSS3', max_length=200)
    alt_description = models.CharField(max_length=50)
    is_aproved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    like_count = models.PositiveIntegerField(default=0)
    deleted_at = models.DateTimeField(auto_now_add=False, null=True)
    deleted_by = models.ForeignKey(User, related_name='delete_photo', null=True, on_delete=models.CASCADE)
    aproved_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # AWS base prefix which photos will be uploaded
    @property
    def aws_prefix(self):
        return 'https://s3.amazonaws.com/galeryapp/'

    # AWS Client
    @property
    def client(self):
        client = boto3.client(
            service_name='s3',
            region_name="us-east-1",
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
        )
        return client
    
    # Upload a picture to AWS S3
    def upload_photo(self, request, file=None, authors_name=''):

        self.author = authors_name

        if request:
            self.author_ip = request.META.get('REMOTE_ADDR')

        if file != None or file != '':
            filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + file.name
            self.client.upload_fileobj(
                Fileobj=file,
                Bucket='galeryapp',
                Key=filename,
                ExtraArgs={'ACL':'public-read'},
            )
            self.reference_url = self.aws_prefix + filename
            super().save()
        else: 
            raise ValueError("File can't be empty.")

    # Likes or dislike a photo
    def like_manager(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        like_obj = Likes.objects.filter(reference_photo=self.id, author_ip=user_ip)

        self.like_count = Likes.objects.only('reference_photo').filter(reference_photo=self.id).count()
        self.save()

        if like_obj.exists() == False:
            Likes.objects.create(
                author_ip=user_ip,
                reference_photo=self.id,
            )
            return True
        else: 
            like_obj.first().delete()

    # Number of likes of a Photos instance
    def number_of_likes(self):
        return Likes.objects.filter(reference_photo=self.id).count()

    # Method to aprove a photo
    # Only avaliable to staff
    def aprove(self, request):
        # Check if user has permission to aprove the photo
        if request.user.is_staff == True:
            self.is_aproved = True
            self.aproved_by = request.user
            super().save()
        else:
            return False

    def delete(self, request): 
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.deleted_by = request.user
        super().save()
    
    def __str__(self):
        return '{0}'.format(self.reference_url)
