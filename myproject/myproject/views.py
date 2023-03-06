"""
This module provides utility functions for rendering templates and returning HTTP responses.
"""

from django.shortcuts import render
from django.http import HttpResponse



def hello_world() -> HttpResponse:
    """
    Returns a HttpResponse object that displays a "Hello, World!" message.

    Returns:
        HttpResponse: A HTTP response object with "Hello, World!" message.
    """
    return HttpResponse("Hello, World!")




def greet(request) -> HttpResponse:
    """
    Greet the user with their name if request is received, else render the 'hello.html' template.

    Args:
        request (HttpRequest): The request object passed by Django.

    Returns:
        HttpResponse: A HTTP response object with a greeting message or a rendered template.
    """
    if request.method == 'POST':
        name = request.POST['name']
        return HttpResponse(f'Hello {name}!')

    return render(request, 'templates/hello.html')
