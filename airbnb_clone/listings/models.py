from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Property(models.Model):
    # host = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    listing = models.ForeignKey(
        Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/uploaded_images/')

    def __str__(self):
        return f"Image for {self.listing.title}"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
