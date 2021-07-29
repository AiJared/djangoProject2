from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow World. You're at the polls index.")