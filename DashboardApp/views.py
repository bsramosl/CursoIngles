from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import * 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
import json
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
 



class InicioView(TemplateView):
    template_name = 'Dashboard/Index.html'

     