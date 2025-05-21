from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from listings.signals import listing_added


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
            listing_added.send(sender=self)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title
