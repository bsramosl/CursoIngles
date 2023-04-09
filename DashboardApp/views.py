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
from django.db.models import Count
 



class InicioView(TemplateView):
    template_name = 'Dashboard/Index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []            
        ct = CategoryModel.objects.all()
        for i in ct:
            res = i.toJSON()
            res["count"] = QuestionModel.objects.filter(category=i.id).count()
            data.append(res)
        context["category"] = data
        return context
    

     