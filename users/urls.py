from atexit import register
from django.urls import path,include
from users.views import Register, mtavari_viwe, fulluser_view, delete_view, commentview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registracia/',Register.as_view(), name='registracia'),
    path('mtvari/',mtavari_viwe, name='mtavari'),
    path('fulluser/',fulluser_view, name='fulluser'),
    path('delete',delete_view, name='delete'),
    path('comment/',commentview.as_view, name='comment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)