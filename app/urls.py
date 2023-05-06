from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home),
    path('book/',views.book),
    path('menu/',views.menu),
    path('about/',views.about),
    path('page/<name>/',views.page),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)