from django.shortcuts import render
from index.models import *
from django.http import HttpResponse


def index(request , *args, **kwargs):
    print(request.GET)
    user_pk = kwargs['pk']
    user = User.objects.filter(id=user_pk).first()
    count = request.GET.get('count', 0)
    try:
        count = int(count)
    except ValueError:
        return HttpResponse("Invalid count value")

    user.tap_count += 1
    user.save()
    context = {'user': user}
    return render(request, 'index.html', context=context)

def leaderboard(request, *args, **kwargs):
    user_pk = kwargs['pk']
    user = User.objects.filter(id=user_pk).first()
    leaderboard = User.objects.all().order_by('-tap_count')
    context = {'leaderboard': leaderboard, 'user': user}
    return render(request, 'leaderboard.html', context=context)
