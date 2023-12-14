
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota -> view -> nome
    path('',views.home, name='home'),
]
