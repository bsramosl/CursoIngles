from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms.models import inlineformset_factory


class ListQuestion(ListView):
    template_name = 'Dashboard/Question/List.html'
    model = QuestionModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateQuestion'
        context['update'] = 'Dash:UpdateQuestion' 
        context['delete'] = 'Dash:DeleteQuestion' 
        return context  

QuestionFormset = inlineformset_factory(
    QuestionModel, ChooseQuestionModel,form=ChooseQuestionForm, fields=('text','correct'),can_delete= False,max_num = ChooseQuestionModel.MAXIMUN_RESPONSE,
    min_num = ChooseQuestionModel.MAXIMUN_RESPONSE
)

class CreateQuestion(CreateView):
    template_name = 'Dashboard/Question/Create.html'
    model = QuestionModel
    form_class = QuestionForm
    success_url = reverse_lazy('Dash:ListQuestion')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Question'
        context['list'] = 'Dash:ListQuestion'  
        if self.request.POST:
            context["question"] = QuestionFormset(self.request.POST)
        else:
            context["question"] = QuestionFormset() 
        return context
    
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        context = self.get_context_data()
        question = context["question"]
        self.object = form.save()
        if question.is_valid():
            question.instance = self.object
            question.save()
        return super().form_valid(form)

class UpdateQuestion(UpdateView):
    template_name = 'Dashboard/Question/Update.html'    
    model = QuestionModel
    form_class = QuestionForm
    success_url = reverse_lazy('Dash:ListQuestion')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditQuestion'
        context['list'] = 'Dash:ListQuestion' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteQuestion(DeleteView):
    template_name = 'Dashboard/Question/Delete.html'
    model = QuestionModel
    success_url = reverse_lazy('Dash:ListQuestion') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Question'
        context['delete'] = 'Dash:DeleteQuestion' 
        return context
