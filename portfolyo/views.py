from django.shortcuts import render
from .models import Portfolyo

def portfolyo(request):

    portfolyo_1 = Portfolyo.objects.first()

    return render(request , 'portfolyo_base.html' , {'portfolyo':portfolyo_1})