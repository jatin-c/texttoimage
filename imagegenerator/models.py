from django.db import models
import os
from django.conf import settings

def upload_to(instance, filename):
    return f'YourImages/{filename}'

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image generated for prompt: {self.prompt}"

    @property
    def filename(self):
        return os.path.basename(self.image.name)
