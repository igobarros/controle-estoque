from django.urls import path
from projeto_controle_estoque.core import views


app_name = 'core'

urlpatterns = [
	path('', views.index, name='index'),
]