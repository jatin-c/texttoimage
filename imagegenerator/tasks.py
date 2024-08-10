from celery import shared_task
import requests
import os
from django.conf import settings
from .models import GeneratedImage
from django.utils import timezone

@shared_task
def generate_images(prompt):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "authorization": f"Bearer {settings.STABILITY_API_KEY}",
        "accept": "image/*"
    }
    data = {
        "prompt": prompt,
        "output_format": "webp",
    }
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        image_name = f"{prompt.replace(' ', '_')}_{timestamp}.webp"
        image_path = os.path.join(settings.MEDIA_ROOT, 'YourImages', image_name)
        
        with open(image_path, 'wb') as file:
            file.write(response.content)

        GeneratedImage.objects.create(prompt=prompt, image=f'YourImages/{image_name}')
    else:
        # Handle the error (log it, retry, etc.)
        raise Exception(f"Error generating image: {response.status_code} {response.json()}")
