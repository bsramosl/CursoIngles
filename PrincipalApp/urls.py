from django.urls import path
from PrincipalApp import views 
from django.contrib.auth.decorators import login_required  
from .forms import *
 
 


app_name = 'Long'
urlpatterns = [
    
    
    path('',views.Index.as_view(),name='Inicio'),       

	path('Login/', views.Login.as_view(), name='Login'),
	path('Logout/', views.Logout.as_view(), name='Logout'),
	path('Register/', views.RegisterUser.as_view(), name='Register'), 
 
	path('Resultado/', views.Resultado.as_view(), name='Resultado'),
        
	path('Play/<int:id>/', views.Quiz,name='Play'),
    
	
    
	 

]