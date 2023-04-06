from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms.models import inlineformset_factory


class ListCourse(ListView):
    template_name = 'Dashboard/Course/List.html'
    model = CourseModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateCourse'
        context['update'] = 'Dash:UpdateCourse' 
        context['delete'] = 'Dash:DeleteCourse' 
        return context  
  

class CreateCourse(CreateView):
    template_name = 'Dashboard/Course/Create.html'
    model = CourseModel
    form_class = CourseForm
    success_url = reverse_lazy('Dash:ListCourse')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Course'
        context['list'] = 'Dash:ListCourse' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response
    
class UpdateCourse(UpdateView):
    template_name = 'Dashboard/Course/Update.html'    
    model = CourseModel
    form_class = CourseForm
    success_url = reverse_lazy('Dash:ListCourse')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditCourse'
        context['list'] = 'Dash:ListCourse' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteCourse(DeleteView):
    template_name = 'Dashboard/Course/Delete.html'
    model = CourseModel
    success_url = reverse_lazy('Dash:ListCourse') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Course'
        context['delete'] = 'Dash:DeleteCourse' 
        return context
