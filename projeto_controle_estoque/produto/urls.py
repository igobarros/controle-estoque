from django.urls import path
from projeto_controle_estoque.produto import views


app_name = 'produto'


urlpatterns = [
	path('', views.produto_list, name='produto_list'),
	path('<int:pk>', views.produto_detail, name='produto_detail'),
	path('add/', views.produto_add, name='produto_add'),
]