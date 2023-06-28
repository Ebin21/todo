from django.urls import path,include
from .  import views
app_name='todo'

urlpatterns = [
    path('',views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('cvhome/', views.Taskview.as_view(), name='cvhome'),
    path('cvdetail/<int:pk>/', views.TaskDetailview.as_view(),name='cvdetail'),
    path('cvupdate/<int:pk>/', views.TaskUpdate.as_view(), name='cvupdate'),
    path('cvdelete/<int:pk>/', views.TaskDelete.as_view(), name='cvdelete'),

]