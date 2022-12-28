from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create_course),
    path('destroy/<int:number>', views.delete_page, name='delete'),
    path('confirm_destroy', views.delete_course),
    path('<int:number>/comment', views.comment, name='add_comment'),
    path('add_comment', views.add_comment),
]	