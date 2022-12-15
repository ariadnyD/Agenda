from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name="url_index"),

    path('login/', login_user, name="url_login"),
    path('sair/', sair, name="url_sair"),
    path('cadastro/', cadastro, name="url_cadastro"),
    
    path('inicio/', inicio, name="url_inicio"),
    path('formTarefa/', formTarefa, name="url_formTarefa"),
]
