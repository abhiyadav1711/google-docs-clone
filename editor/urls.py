from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('new/', views.document_create, name='document_create'),
    path('document/<int:pk>/', views.document_edit, name='document_edit'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]