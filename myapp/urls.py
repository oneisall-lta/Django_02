
from django.urls import path, re_path

from myapp import views

urlpatterns = [
    path('fruit/',views.show_fruit),
    path('register/',views.register),
    path('welcome/',views.welcome),
    path('transDate/',views.trans_date),
    # re_path('sports/$',views.show_sports)
    path('<tag>/',views.show_sports)
]