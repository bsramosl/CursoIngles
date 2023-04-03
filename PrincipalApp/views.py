from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from PrincipalApp.forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
import json , random
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash,authenticate
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.core.exceptions import *
from django.http import Http404


class Index(TemplateView):
    template_name = 'Major/Index.html'
 
   
def tablero(request):
    total_usaurios_quiz = QuizUser.objects.order_by('-puntaje_total')[:10]
    contador = total_usaurios_quiz.count()

    context = {
        'usuario_quiz':total_usaurios_quiz,
        'contar_user':contador
    }

    return render(request, 'Major/Tablero.html', context)
 
def jugar(request):

    Quiz, created = QuizUser.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        print(request.POST)
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = Quiz.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_selecionada = pregunta_respondida.pregunta.questions.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404 
        return redirect('Long:Resultado')

    else:
        pregunta = Quiz.obtener_nuevas_preguntas()    
        if pregunta is not None:
            Quiz.crear_intentos(pregunta)  
        context = {
            'pregunta':pregunta
        } 
    return render(request, 'Major/Jugar.html', context)


def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    context = {
        'respondida':respondida
    }
    return render(request, 'Major/Resultados.html', context)

class Login(FormView):
    template_name = 'User/Login.html'
    form_class = UsuarioLoginFormulario
    success_url = reverse_lazy('Long:Inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))  
    

class RegisterUser(CreateView):
    template_name = 'User/Register.html'
    form_class = RegistroFormulario    
    success_url = reverse_lazy('Long:Inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Usuario'
        return context

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response
 

class Logout(RedirectView):
    pattern_name = 'Long:Inicio'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
 

def Quiz(request):
    data = []            
    qs = QuestionModel.objects.all()
    for i in qs:
        item = i.toJSON() 
        cq = ChooseQuestionModel.objects.filter(question=i.id)
        dat = []
        for j in cq:
            res = j.toJSON()
            res['correct'] = str(j.correct)
            dat.append(res)
            item['respuestas'] = dat
        data.append(item)

    return render(request,"Major/Jugar.html", 
                  context={'question': random.SystemRandom().sample(data, 10)})

class Resultado(TemplateView):
    template_name = "Major/Resultado.html"