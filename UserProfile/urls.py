from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from UserProfile import views

router = DefaultRouter()
router.register(r'business', views.BusinessViewSet, base_name='business')
router.register(r'register', views.UserRegistrationViewSet, base_name='register')
router.register(r'login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^', include(router.urls)),
]
