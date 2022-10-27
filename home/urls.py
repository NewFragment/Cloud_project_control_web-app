from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('communications', views.communications, name='communications'),
    path('faq', views.faq, name='faq'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path("<int:u_id>", include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
