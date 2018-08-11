from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # reqeust: HttpRequest
    # numbers = 123/54324/234/234/324
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)