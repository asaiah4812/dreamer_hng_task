from django.http import JsonResponse
from .models import Dreamer
from .serializer import DreamerSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def dreamer_list(request):
    if request.method == 'GET':
        dreamer = Dreamer.objects.first()
        data = {
                "email": dreamer.email,
                "current_datetime": dreamer.current_datetime,
                "github_url": dreamer.github_url,
            }
        return JsonResponse(data, status=200, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)
