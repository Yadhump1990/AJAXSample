from django.http import JsonResponse
from django.shortcuts import render, redirect
from ajapp.models import *

def searchcrs(request):
    dep = request.GET['dep']
    sob = course.objects.filter(did=dep)
    data = []
    for r in sob:
        row = {"id": r.id, "course": r.course}
        data.append(row)
    res = {"res": data}
    print(res)
    print(res)
    return JsonResponse(res)

def searchsub(request):
    crs = request.GET['crs']
    sem=request.GET['sem']
    sob = subject.objects.filter(cid=crs,sem=sem)
    data = []
    for r in sob:
        row = {"id": r.id, "sub": r.sub}
        data.append(row)
    res = {"res": data}
    print(res)
    print(res)
    return JsonResponse(res)

def likepost(request):
    username = request.GET['username']
    print(username)
    data = {
        'is_taken': login.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."
        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)
    # Create your views here.
