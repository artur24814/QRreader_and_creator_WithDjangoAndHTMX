from django.urls import path
from .views import (
    QRmainPage,
    #HTMX
    save_image,
    create_image,
    delete_file,
    download_image,
)

app_name = 'qrreader'

urlpatterns = [
    path('main/', QRmainPage.as_view(), name='qr-main-page'),
    path('save-image/', save_image, name='save-image'),
    path('create-image/', create_image, name='create-image'),
    path('download-image/', download_image, name='download-image'),
    path('delete-file/<str:name_file>/', delete_file, name='delete-file'),
]