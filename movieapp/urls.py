from django.urls import path,include
from . import views
app_name = 'movieapp'
urlpatterns = [
    path('',views.fun,name='fun'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/', views.add_movie, name='add_movie'),
   path('update/<int:id>/', views.update, name='update'),
   path('delet/<int:id>/', views.delet, name='delet'),

]