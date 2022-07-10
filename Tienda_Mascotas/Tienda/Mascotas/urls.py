from django.urls import path, include
from . import views

 
urlpatterns = [
     # llamando a la clases 
    path('add_mascotas/', views.MascotaCreate.as_view(), name="add_mascotas"),
 
    path('list_mascotas/', views.MascotaList.as_view(), name='list_mascotas'),
    path('list_mascotasadopcion/', views.MascotaAdoList.as_view(), name='list_mascotasadopcion'),
    path('edit_mascotas/<int:pk>', views.MascotaUpdate.as_view(), name='edit_mascotas'),
 
    path('del_mascotas/<int:pk>', views.MascotaDelete.as_view(), name='del_mascotas'),
 
    # api
    path('mascotas/',  views.mascotas_collection , name='mascotas_collection'),
    path('mascotas/<int:pk>/', views.mascotas_element ,name='mascotas_element'),
    
    path('info/', views.MascotaView.as_view()),
]
