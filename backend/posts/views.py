from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def post_list(request):
    # For testing, return a simple response
    return Response({'message': 'It works!', 'posts': []})