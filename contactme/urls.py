from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.contactform, name="contactme"),
    path('thankyou/', views.thankyou, name="thankyou"),
]