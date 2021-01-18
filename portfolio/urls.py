from django.contrib import admin
from django.urls import path

import jobs.views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),
    url(r'^resume', jobs.views.resume, name='resume'),
] 

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
