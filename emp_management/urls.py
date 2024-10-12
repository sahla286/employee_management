from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router=DefaultRouter()

router.register('users',views.UserView,basename='users')
router.register('emp',views.EmpView,basename='emp')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tokenpair', TokenObtainPairView.as_view(), name='tokenpair'),
    path('tokenrefresh', TokenRefreshView.as_view(), name='tokenrefresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + router.urls
