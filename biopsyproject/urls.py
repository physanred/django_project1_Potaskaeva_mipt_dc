from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from biopsyclassification.views import predict

urlpatterns = [
    path('', include('biopsyclassification.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('predict/', predict, name='predict'),
    path('', predict),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/upload/', permanent=True)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)