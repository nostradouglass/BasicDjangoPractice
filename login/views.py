from django.shortcuts import render, redirect
from .forms import TestForm

# Create your views here.


def login(request):
    return render(request, 'login/login.html')


def new_post(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'login/login.html')
    else:
        form = TestForm()
    return render(request, 'login/new_post.html', {'form': form})