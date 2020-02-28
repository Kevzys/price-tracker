
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('create_list/', views.create_list, name='createlist'),
    path('view_list/', views.view_list, name='viewlist'),
    path('create_item/<int:id>', views.create_item, name='createitem'),
    path('remove_list/<int:id>', views.remove_list, name='removelist'),
    path('remove_item/<int:id>/<str:name>', views.remove_item, name='removeitem'),
]