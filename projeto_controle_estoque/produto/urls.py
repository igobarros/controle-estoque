from django.urls import path
from projeto_controle_estoque.produto import views

app_name = 'produto'


urlpatterns = [
	path('', views.ProdutoList.as_view(), name='produto_list'),
	path('<int:pk>', views.produto_detail, name='produto_detail'),
	path('add/', views.ProdutoCreate.as_view(), name='produto_add'),
	path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='produto_edit'),
	path('<int:pk>/json/', views.produto_json, name='produto_json'),
	path('import/csv/', views.import_csv, name='import_csv'),
	path('export/csv/', views.export_csv, name='export_csv'),
	path('import/xlsx/', views.import_xlsx, name='import_xlsx'),
	path('export/xlsx', views.export_xlsx, name='export_xlsx'),
]