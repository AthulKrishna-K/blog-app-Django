from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('recent/',views.recent,name='recent'),
    path('add-post/',views.addPost,name='add-post'),
    path('add/',views.add,name='add'),
    path('details/<int:post_id>/', views.details, name='details'),
    path('delete/<int:del_id>/', views.delete, name='delete'),
    path('edit/<int:edit_id>/', views.edit, name='edit')
]