from re import template
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio.as_view(template_name="inicio.html"), name='inicio'),
    path('crear/', views.CrearPost.as_view(), name='crear'),
    path('post/<int:pk>/',views.BlogDetail.as_view(template_name = 'details.html'),name= 'details'),
    path('post/edit/<int:pk>',views.PostUpdate.as_view(template_name = 'edit.html'),name='editar'),
    path('post/delete/<int:pk>',views.PostDelete.as_view(template_name = 'post_confirm_delete.html'),name='borrar'),
    
 ]
