"""mysmallecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from django.urls import include, path
from django.contrib import admin
from shopapp import views
from django.conf import settings

#use below comnneted lines only if you do not have django.contrib.staticfiles as installed apps in settings.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('shopapp/',include('shopapp.urls')),
    path('search_app/',include('search_app.urls')),
    path('Cart/',include('Cart.urls')),
    path('order/', include('order.urls')),
    path('account/create/', views.signupView, name='signup'),
    path('account/login/', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
