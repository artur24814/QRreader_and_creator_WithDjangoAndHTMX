from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
import os

import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import qrcode

class HomeView(View):
    def get(self, request):
        return render(request, 'qrreader/index.html', {})


class QRmainPage(View):
    def get(self, request):
        return render(request, 'qrreader/qrmain.html', {})


#HTMX
def save_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        #read content

        path = os.getcwd()
        path_last = '../' + os.path.basename(path) + file_url
        try:
            img = cv2.imread(str(path_last))
            detector = cv2.QRCodeDetector()
            data, _ , _ = detector.detectAndDecode(img)
            print(data)
        except Exception:
            data = ''
        return render(request, 'qrreader/list-images.html', {
            'data': data,
            'file_url': file_url
        })
    return HttpResponse('')


