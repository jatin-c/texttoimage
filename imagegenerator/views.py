from imagegenerator.tasks import generate_images
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def imagine(request):
    prompt = request.GET.get('prompt')
    if not prompt:
        return Response({'error': 'Prompt is required'}, status=400)

    generate_images.delay(prompt)
    return Response({'message': 'Your image is being generated'}, status=202)