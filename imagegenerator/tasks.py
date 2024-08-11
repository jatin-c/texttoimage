from celery import shared_task
import requests
import os
from django.conf import settings
from .models import GeneratedImage
from django.utils import timezone
import base64
#"authorization": f"Bearer {settings.STABILITY_API_KEY}",


@shared_task
def generate_images(prompt):
    response = requests.post(
        "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
        headers={
            "authorization": f"Bearer {settings.STABILITY_API_KEY}",
            "Content-type" : "application/json",
            "accept": "application/json",
                },
    
        json={
            "text_prompts" : [
                {
                    "text" : prompt
                }
            ]
        },
    )

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.json()}")
    data = response.json()
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    image_name = f"{prompt.replace(' ', '_')}_{timestamp}.png"
    image_path = os.path.join(settings.MEDIA_ROOT, 'YourImages', image_name)

    for i, image in enumerate(data["artifacts"]):
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))
    GeneratedImage.objects.create(prompt=prompt, image=f'YourImages/{image_name}')
    # if response.status_code == 200:
    #     timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    #     image_name = f"{prompt.replace(' ', '_')}_{timestamp}.webp"
    #     image_path = os.path.join(settings.MEDIA_ROOT, 'YourImages', image_name)
        
    #     with open(image_path, 'wb') as file:
    #         file.write(response.content)

    #     GeneratedImage.objects.create(prompt=prompt, image=f'YourImages/{image_name}')
    # else:
    #     # Handle the error (log it, retry, etc.)
    #     raise Exception(f"Error generating image: {response.status_code} {response.json()}")
