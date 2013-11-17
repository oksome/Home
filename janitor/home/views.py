from django.shortcuts import render

from home.models import RF433Switch


def index(request):
    context = {'gadgets': RF433Switch.objects.all()}
    return render(request, 'index.html', context)
