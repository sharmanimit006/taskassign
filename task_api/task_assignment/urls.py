from django.urls import path,include
from django.conf import settings
from . import views
urlpatterns = [
    
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/',views.taskDetail,name="task-detail"),
    path('task-update/',views.taskUpdate,name="task-update"),
    path('task-create/',views.taskCreate,name="task-create"),
    path("task-delete/",views.taskDelete,name="task-delete"),
  ]