from rest_framework import status
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

    
