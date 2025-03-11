

from django.urls import path
from pos import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("category",views.CategoryViewSet,basename="category")



urlpatterns=[

]+router.urls