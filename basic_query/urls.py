from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('create', views.createPage, name='create'),
    path('createPage1', views.createPage1, name='createPage1'),
    path('createPage2', views.createPage2, name='createPage2'),
    path('createPage3', views.createPage3, name='createPage3'),
    path('createForm1', views.createForm1, name='createForm1'),
    path('createForm2', views.createForm2, name='createForm2'),
    path('createForm3', views.createForm3, name='createForm3'),
    path('deleteEntry', views.deleteEntry, name='deleteEntry'),
    path('rerouteUpdate', views.rerouteUpdate, name='rerouteUpdate'),
    path('updateForm1', views.updateForm1, name='updateForm1'),
    path('updateForm2', views.updateForm2, name='updateForm2'),
    path('updateForm3', views.updateForm3, name='updateForm3'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
