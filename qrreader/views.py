from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View
from django.core.files.storage import FileSystemStorage

import os
import cv2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import qrcode

class HomeView(View):
    def get(self, request):
        path = os.path.normpath(os.getcwd())
        list = os.listdir(path + '/media')
        list_media = [file for file in list]
        context = {
            'list_files': list_media,
        }
        return render(request, 'qrreader/index.html', context)


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
            if data == '':
                data = "Haven't any data"
        except Exception:
            data = 'Wrong format'
        return render(request, 'qrreader/list-images.html', {
            'data': data,
            'file_url': file_url
        })
    return HttpResponse('')

def delete_file(request, name_file):
    path = os.getcwd()
    if os.path.isfile(path + '/media/' + name_file):
        os.remove(path + '/media/' + name_file)
    else:
        print("The file does not exist")

    path = os.path.normpath(os.getcwd())
    list = os.listdir(path + '/media')
    list_media = [file for file in list]
    context = {
        'list_files': list_media,
    }
    return render(request, 'qrreader/list-of-all-images.html', context)

def create_image(request):
    text = request.POST.get('text')
    if text != '' and not None:
        qr = qrcode.QRCode(version=1,
                          error_correction=qrcode.constants.ERROR_CORRECT_L,
                          box_size=20,
                          border=2)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')
        path = os.path.normpath(os.getcwd())
        len_all_files = len(os.listdir(path + '/media'))
        file_name = f'/media/newqr{len_all_files+2}.png'
        img.save(path + file_name)
        return render(request, 'qrreader/created-image.html', {
            'data': text,
            'file_url': file_name
        })
    return HttpResponse('')

from django.http import FileResponse

def download_image(request):
    url_img = request.GET.get('url_image')
    path = os.path.normpath(os.getcwd())
    img = open(path + url_img, 'rb')
    response = FileResponse(img, as_attachment=True)
    os.remove(path + url_img)
    return response




