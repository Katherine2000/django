from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
	path('', views.feed, name='feed'),
	path('profile/', views.profile, name='profile'),
	path( 'login/', LoginView.as_view(template_name = 'social/login.html'), name='login'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)