from django.urls import path, include
from . import views
 
urlpatterns = [
     # llamando a la clases 
    path('add_productos', views.ProductoCreate.as_view(), name="add_productos"),
 
    path('list_productos/', views.ProductoList.as_view(), name='list_productos'),
 
    path('edit_producto/<int:pk>', views.ProductoUpdate.as_view(), name='edit_producto'),
 
    path('del_producto/<int:pk>', views.ProductoDelete.as_view(), name='del_producto'),
 
    # api
    path('productos/',  views.productos_collection , name='productos_collection'),
    path('productos/<int:pk>/', views.productos_element ,name='productos_element')

]
