from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('categoria/api/', views.CategoriaListApiView.as_view()),
]