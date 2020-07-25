from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid
from uuid import UUID


# Create your models here.

class Category(models.Model):
    category_id = models.CharField(max_length = 1000)
    category =  models.TextField()

    def __str__(self):
        return self.category

def upload_location(instance, filename):
    return "profiles/{track_id}".format(filename=track_id)


class Complaint(models.Model):
    track_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 255, default=None)
    phonenumber = models.CharField(max_length = 15, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.TextField()
    description = models.TextField()
    category = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField(max_length = 3)
    image = models.ImageField(upload_to = upload_location, blank = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.category


    def get_api_url(self):
        return reverse('complaint-api:detail', kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={"slug": self.slug})
