from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")


def greet(request):
    if request.method == 'POST':
        name = request.POST['name']
        return HttpResponse(f'Hello {name}!')
    else:
        return render(request, 'templates/hello.html')
