
from django.contrib import admin
from django.urls import path,include
from operation_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_table, name='all_table'),
    path('complaint/', views.complaint, name='complaint'),
    path('profile/', views.create_profile, name='create_profile'),
    path('list/', views.profile_list, name='profile_list'),
    path('delete/<int:pk>/',views.delete_profile, name='delete_profile'),
    #path('update/<int:pk>/', views.update_profile, name='update_profile'),
   
]
