import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import *



@api_view()
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title', 'price'])
    return  JsonResponse(data)