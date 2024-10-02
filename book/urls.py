


from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.home , name='home' ),
   
    path('edit_book_id/<int:id>/', views.edit_book_id , name='edit_book_id'),
   
    path('store_book/', views.store_book , name='store_book'),
    path('show_book/', views.show_book, name='show_book' ),
    path('delete_book_id/<int:id>/', views.delete_book_id , name='delete_book_id'),
    
    
    
]
