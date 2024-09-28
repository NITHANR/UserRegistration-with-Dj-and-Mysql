from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name="index"),
    path('userreg/',views.userreg,name="userreg"),
    path('insertuser/',views.insertuser,name="insertuser"),
]