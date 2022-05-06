from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('predictHF',views.predictHF, name='predictHF'),
    path('updateDataBase',views.updateDataBase, name='updateDataBase'),
    #path('viewDataBase/',views.viewDataBase, name='viewDataBase'),
    path('dashboard_with_pivot/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]