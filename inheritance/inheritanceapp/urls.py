from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# sets the urls for pages on the site
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('ourstory', views.ourstory, name='ourstory'),
    path('gallery/',views.imagedisplay, name='gallery'), 
    path('addartifact/', views.image_upload_view, name='addartifact'),
    path('editartifact/<int:artifact_id>', views.editartifact, name="editartifact"), 
]

urlpatterns += staticfiles_urlpatterns()
