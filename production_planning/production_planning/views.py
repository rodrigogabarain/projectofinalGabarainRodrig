from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(requets):
    return render (requets, 'index.html', context={})