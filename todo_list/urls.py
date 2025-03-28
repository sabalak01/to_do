from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from tasks.views import task_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('', task_list, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)