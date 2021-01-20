"""poll_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from poll import views as poll_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('radio_vote/<radio_id>/', poll_views.radio_vote, name='radio_vote'),
    path('checkbox_vote/<checkbox_id>/', poll_views.checkbox_vote, name='checkbox_vote'),
    path('radio_results/<radio_id>/', poll_views.radio_results, name='radio_results'),
    path('checkbox_results/<checkbox_id>/', poll_views.checkbox_result, name='checkbox_results'),
    path('login/', poll_views.login_user, name="login"),
    path('logout/', poll_views.logout_user, name='logout'),
    path('register/', poll_views.user_registration, name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

