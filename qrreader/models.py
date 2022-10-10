from django.db import models


class ImageQR(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date = models.DateTimeField(auto_now_add=True)
