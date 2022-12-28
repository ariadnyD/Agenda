from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name="url_index"),
    path('layout/', layout, name="url_layout"),


    path('login/', login_user, name="url_login"),
    path('sair/', sair, name="url_sair"),
    path('cadastro/', cadastro, name="url_cadastro"),
    
    path('inicio/', inicio, name="url_inicio"),

    path('formTarefa/', formTarefa, name="url_formTarefa"),
    path('updateTarefa/<int:id>/', updateTarefa, name="url_updateTarefa"),
    path('deleteTarefa/<int:id>/', deleteTarefa, name="url_deleteTarefa"),
    path('detTarefa/<int:id>/', detTarefa, name="url_detTarefa"),

    path('showMateria/', showMateria, name="url_showMateria"),
    path('formMateria/', formMateria, name="url_formMateria"),
    path('deleteMateria/<int:id>/', deleteMateria, name="url_deleteMateria"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)