from django.urls import path

from . import views

app_name = 'cmsapp'

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
path('details/', views.details, name='details'),
    path('details_form/', views.details_form, name='details_form'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
]
