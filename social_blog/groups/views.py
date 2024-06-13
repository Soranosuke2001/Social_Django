from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin 
from django.views.generic import CreateView, DetailView, ListView

from .models import *


# Create your views here.
class CreateGroup(LoginRequiredMixin, CreateView):
  fields = ('name', 'description')
  model = Group


class SingleGroup(DetailView):
  model = Group


class ListGroups(ListView):
  model = Group

