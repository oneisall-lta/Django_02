
from django.urls import path

from templateapp import views

urlpatterns = [
    path('dict/',views.dict_info),
    path('obj/',views.obj_info),
    path('list/',views.list_info),
    path('iftags/',views.iftag),
    path('book/',views.books_info),

]
