from django.shortcuts import render, get_object_or_404

from home.models import RF433Switch


def index(request):
    context = {'gadgets': RF433Switch.objects.all()}
    return render(request, 'index.html', context)


def gadget_details(request, gadget_id):
    gadget = get_object_or_404(RF433Switch, pk=gadget_id)
    context = {'gadget': gadget}
    return render(request, 'gadget.html', context)


def gadget_do(request, gadget_id):
    action = request.POST.get('action')
    gadget = get_object_or_404(RF433Switch, pk=gadget_id)
    assert action in ('on', 'off')
    gadget.turn(action)
    context = {'gadget': gadget}
    return render(request, 'gadget.html', context)
