from django.db import models

# Create your models here.
class LostItem(models.Model):
    item_name = models.CharField(max_length=150)
    item_img = models.ImageField(upload_to='media')
    item_desc = models.TextField()
    place = models.TextField()
    claim = models.BooleanField(default=False)
    claimed = models.BooleanField(default=False)
    