from django.shortcuts import render


# pages/views.py


def home(request):
    return render(request, "blog/index.html", {})