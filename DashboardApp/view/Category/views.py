from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms.models import inlineformset_factory


class ListCategory(ListView):
    template_name = 'Dashboard/Category/List.html'
    model = CategoryModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateCategory'
        context['update'] = 'Dash:UpdateCategory' 
        context['delete'] = 'Dash:DeleteCategory' 
        return context  
  

class CreateCategory(CreateView):
    template_name = 'Dashboard/Category/Create.html'
    model = CategoryModel
    form_class = CategoryForm
    success_url = reverse_lazy('Dash:ListCategory')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Category'
        context['list'] = 'Dash:ListCategory' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response
    
class UpdateCategory(UpdateView):
    template_name = 'Dashboard/Category/Update.html'    
    model = CategoryModel
    form_class = CategoryForm
    success_url = reverse_lazy('Dash:ListCategory')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditCategory'
        context['list'] = 'Dash:ListCategory' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteCategory(DeleteView):
    template_name = 'Dashboard/Category/Delete.html'
    model = CategoryModel
    success_url = reverse_lazy('Dash:ListCategory') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Category'
        context['delete'] = 'Dash:DeleteCategory' 
        return context
