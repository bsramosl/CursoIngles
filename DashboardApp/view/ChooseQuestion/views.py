from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


class ListChooseQuestion(ListView):
    template_name = 'Dashboard/ChooseQuestion/List.html'
    model = ChooseQuestionModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateChooseQuestion'
        context['update'] = 'Dash:UpdateChooseQuestion' 
        context['delete'] = 'Dash:DeleteChooseQuestion' 
        return context 

class CreateChooseQuestion(CreateView):
    template_name = 'Dashboard/ChooseQuestion/Create.html'
    model = ChooseQuestionModel
    form_class = ChooseQuestionForm
    success_url = reverse_lazy('Dash:ListChooseQuestion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'ChooseQuestion'
        context['list'] = 'Dash:ListChooseQuestion' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

class UpdateChooseQuestion(UpdateView):
    template_name = 'Dashboard/ChooseQuestion/Update.html'    
    model = ChooseQuestionModel
    form_class = ChooseQuestionForm
    success_url = reverse_lazy('Dash:ListChooseQuestion')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditChooseQuestion'
        context['list'] = 'Dash:ListChooseQuestion' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteChooseQuestion(DeleteView):
    template_name = 'Dashboard/ChooseQuestion/Delete.html'
    model = ChooseQuestionModel
    success_url = reverse_lazy('Dash:ListChooseQuestion') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'ChooseQuestion'
        context['delete'] = 'Dash:DeleteChooseQuestion' 
        return context
