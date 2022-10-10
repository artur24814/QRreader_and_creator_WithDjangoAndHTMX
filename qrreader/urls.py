from django.urls import path
from .views import (
    QRmainPage,
    #HTMX
    save_image,
)

app_name = 'qrreader'

urlpatterns = [
    path('main/', QRmainPage.as_view(), name='qr-main-page'),
    path('save-image/', save_image, name='save-image'),
]