from django.http import JsonResponse
from django.core.serializers import serialize
from .models import BaseBlogModel
import json

def index(request):
    queryset = BaseBlogModel.objects.all()

    # Serialize queryset to JSON
    serialized_data = serialize('json', queryset)

    # Convert serialized data to Python list/dictionary
    data = json.loads(serialized_data)

    # Extract only required fields from each entry
    processed_data = [
        {
            'title': entry['fields']['title'],
            'subtitle': entry['fields']['subtitle'],
            'description': entry['fields']['description'],
            'created_at': entry['fields']['created_at'],
        }
        for entry in data
    ]

    return JsonResponse({'blog_entries': processed_data}, safe=False)
