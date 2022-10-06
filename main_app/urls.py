from django.urls import path
from . import views

urlpatterns = [
    # <- here we have added the new path
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('peppers/', views.PepperList.as_view(), name="pepper_list"),
    path('peppers/new/', views.PepperCreate.as_view(), name="pepper_create"),
    path('peppers/<int:pk>', views.PepperDetail.as_view(), name="pepper_detail"),
    path('peppers/<int:pk>/update',
         views.PepperUpdate.as_view(), name="pepper_update"),
    path('peppers/<int:pk>/delete',
         views.PepperDelete.as_view(), name="pepper_delete")
]
