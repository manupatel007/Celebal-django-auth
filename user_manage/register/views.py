from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'users/dashboard.html', {})

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(
            request, "users/register.html",
            {"form": form}
        )