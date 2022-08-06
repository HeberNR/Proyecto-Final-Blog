from re import template
from django.urls import path
from . import views


urlpatterns = [
    # path('inicio/', views.inicio, name='inicio'),
    path('crear/', views.CrearPost.as_view(), name='crear'),
    # path('comentario/', views.CrearComentario.as_view(), name='crear'),
    # path('<slug:slug>/', views.blog_detail(),name='details'),
    path('inicio/', views.Inicio.as_view(template_name="inicio.html"), name='inicio'),
    path('post/<int:pk>/',views.post_detail,name= 'details'),
    path('edit/post/<int:pk>',views.PostUpdate.as_view(template_name = 'edit.html'),name='editar'),
    path('edit/delete/<int:pk>',views.PostDelete.as_view(),name='borrar'),
]
