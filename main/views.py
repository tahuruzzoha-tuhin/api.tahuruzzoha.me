from django.http import JsonResponse
from django.core.serializers import serialize
from main.models import BaseBlogModel

def index(request):
    queryset = BaseBlogModel.objects.all()

    serialized_data = serialize('json', queryset)

    data = {
        'blog_entries': serialized_data,
    }

    return JsonResponse(data, safe=False)
