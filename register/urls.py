from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('employee/', views.employee_view, name='employee'),
    path('list/',views.employee_list,name='employee_list'),
    path('',views.employee_form,name='employee_insert'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
]