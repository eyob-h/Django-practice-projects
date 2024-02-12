from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='home'),
        path('mark_as_done/<task_id>', views.mark_as_done, name='mark_as_done'),
        path('deleteTask/<task_id>', views.deleteTask, name='deleteTask' ),
]

