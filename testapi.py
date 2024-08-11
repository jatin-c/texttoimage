import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "texttoimage.settings")
django.setup()

from django.utils import timezone
import requests
import base64
from django.conf import settings

prompt = "A piano ninja"

response = requests.post(
    "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
    headers={
        "authorization": f"Bearer sk-YmurDZasA4EWuI3IM3sxAEhoz8D3lF3Z073wvljqxrN7uAMW",
        "Content-type": "application/json",
        "accept": "application/json",
    },
    json={
        "text_prompts": [
            {
                "text": prompt
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
