from django.urls import path, include
from .views import login, registr
from users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registr, name='register'),
    path('info/<int:user_id>/', views.get_personal_account, name='detail_user')
]
