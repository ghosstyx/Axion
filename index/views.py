from django.shortcuts import render
from index.models import *
from django.http import JsonResponse
import json

def index(request , *args, **kwargs):
    user_pk = kwargs['pk']
    user = User.objects.filter(id=user_pk).first()
    count = request.GET.get('count', 0)
    # try:
    #     count = int(count)
    # except ValueError:
    #     return HttpResponse("Invalid count value")
    #
    # user.tap_count += 1
    # user.save()
    if request.method == 'POST':
        data = json.loads(request.body)
        count = data.get('count', 0)
        try:
            count = int(count)
        except ValueError:
            return JsonResponse({'error':'Invalid count value'}, status=400)
        user.tap_count += count
        user.save()
        return JsonResponse({'message':'Count updated', 'tap_count':user.tap_count})
    context = {'user': user}
    return render(request, 'index.html', context=context)

def leaderboard(request, *args, **kwargs):
    user_pk = kwargs['pk']
    user = User.objects.filter(id=user_pk).first()
    leaderboard = User.objects.all().order_by('-tap_count')
    context = {'leaderboard': leaderboard, 'user': user}
    return render(request, 'leaderboard.html', context=context)
