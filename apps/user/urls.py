"""application admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    # Admin
    path('admin/user/add', CreateUserView.as_view(), name='admin-user-add'),
    path('admin/user/', ListUserView.as_view(), name='admin-user-list'),
    path('admin/user/list/ajax', ListUserViewJson.as_view(), name='admin-user-list-ajax'),
    path('admin/user/detail/<int:pk>', DetailUserView.as_view(), name='admin-user-detail'),
    path('admin/user/edit/<int:pk>', UpdateUserView.as_view(), name='admin-user-edit'),
    path('admin/user/delete/<int:pk>', DeleteUserView.as_view(), name='admin-user-delete'),
    path('admin/subscription/', SubscriptionTemplate.as_view(), name='admin-subscription-list'),
    path('admin/subscription/list/ajax', SubscriptionJsonView.as_view(), name='admin-subscription-list-ajax'),

    # Frontend User
    path('', LandingView.as_view(), name="landing"),
    path('login/', LoginView.as_view(), name="user-login"),
    # path('register/', RegisterView.as_view(), name="user-register"),
    path('logout/', LogoutView.as_view(), name="user-logout"),
    path('profile/', UpdateUserProfileView.as_view(), name="user-profile"),
    path('change-password/', ChangeUserSelfPasswordView.as_view(), name="user-change-password"),
    path('home/', HomePageView.as_view(), name="user-home"),

    # Service related Paths for user
    path('user/service/list/', UserServiceListViewJson.as_view(), name="user-service-list"),

    # buy url

    path('service/detail/<int:pk>', DetailServiceView.as_view(), name='service-detail'),
  # subscriptions path
    path('subscription/<int:pk>/', SubscribeView.as_view(), name='subscription_page'),
    path('subscribe/<int:service_id>/', views.subscribe_service, name='subscribe-page'),
    path('razorpay/callback/', views.razorpay_callback, name='razorpay_callback'),

    path('subscription/success/', views.subscription_success, name='subscription_success'),

    # email validation path
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('otp-confirmation/', OTPConfirmationView.as_view(), name='otp-confirmation'),

]

