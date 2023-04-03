from django.urls import path
from PrincipalApp import views 
from django.contrib.auth.decorators import login_required 


app_name = 'Long'
urlpatterns = [
    
      path('',views.Index.as_view(),name='Inicio'),       

	path('Login/', views.Login.as_view(), name='Login'),
	path('Logout/', views.Logout.as_view(), name='Logout'),
	path('Register/', views.RegisterUser.as_view(), name='Register'),
	path('tablero/', views.tablero, name='tablero'),
 
	path('Resultado/', views.Resultado.as_view(), name='Resultado'),
        
	path('Play/', views.Quiz,name='Play'),
	path('Resultado/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='Resultado'),

]