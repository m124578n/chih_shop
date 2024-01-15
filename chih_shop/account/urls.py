from django.urls import path
from account import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.AccountsView)

urlpatterns = [
    path('test', views.test_check),
    path('register/', views.CreateAccount.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('update_password/', views.ChangePasswordView.as_view()),
    # path('', views.AccountsView.as_view()),
]


urlpatterns += router.urls
