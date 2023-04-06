from django.urls import path
from DashboardApp import views 
from django.contrib.auth.decorators import login_required 
from DashboardApp.view.Question.views import *
from DashboardApp.view.ChooseQuestion.views import *
from DashboardApp.view.Category.views import *
from DashboardApp.view.Course.views import *

app_name = 'Dash'
urlpatterns = [
    path('Dashboard/',views.InicioView.as_view(),name='Dashboard'),   
    
    path('ListQuestion/',ListQuestion.as_view(),name='ListQuestion'),
    path('CreateQuestion/',CreateQuestion.as_view(),name='CreateQuestion'),
    path('UpdateQuestion/<int:pk>/',UpdateQuestion.as_view(),name='UpdateQuestion'),
    path('DeleteQuestion/<int:pk>/',DeleteQuestion.as_view(),name='DeleteQuestion'), 

    path('ListChooseQuestion/',ListChooseQuestion.as_view(),name='ListChooseQuestion'),
    path('CreateChooseQuestion/',CreateChooseQuestion.as_view(),name='CreateChooseQuestion'),
    path('UpdateChooseQuestion/<int:pk>/',UpdateChooseQuestion.as_view(),name='UpdateChooseQuestion'),
    path('DeleteChooseQuestion/<int:pk>/',DeleteChooseQuestion.as_view(),name='DeleteChooseQuestion'), 

    path('ListCategory/',ListCategory.as_view(),name='ListCategory'),
    path('CreateCategory/',CreateCategory.as_view(),name='CreateCategory'),
    path('UpdateCategory/<int:pk>/',UpdateCategory.as_view(),name='UpdateCategory'),
    path('DeleteCategory/<int:pk>/',DeleteCategory.as_view(),name='DeleteCategory'), 

    path('ListCourse/',ListCourse.as_view(),name='ListCourse'),
    path('CreateCourse/',CreateCourse.as_view(),name='CreateCourse'),
    path('UpdateCourse/<int:pk>/',UpdateCourse.as_view(),name='UpdateCourse'),
    path('DeleteCourse/<int:pk>/',DeleteCourse.as_view(),name='DeleteCourse'), 

]