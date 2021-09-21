from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from ApkSF.settings import MEDIA_URL
import os
import re
import random
import string
import subprocess

# Setting Up Variables
tools_dir = os.path.join(settings.BASE_DIR, 'tools')
output_dir = os.path.join(settings.BASE_DIR, 'output')
file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


# To store and rename uploaded file
def handle_uploaded_file(f):
    with open(os.path.join(settings.BASE_DIR, f'media/{f.name}'), "ab+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return os.rename(f'media/{f.name}', f'media/{file_name}.apk')


# To validate and check request
def index(request):
    if request.method == "POST":
        if "apkfile" in request.FILES:
            uploaded_file = request.FILES.get("apkfile", False)
            file_content_type = uploaded_file.content_type
            file_extension = uploaded_file.name.rsplit('.',1)[1]
            if file_content_type == "application/octet-stream" or file_content_type == "application/vnd.android.package-archive":
                if file_extension == "apk" or file_extension == "xapk":
                    handle_uploaded_file(uploaded_file)
    return render(request, "recon/index.html")


# Analyze APK
def analyze_apk(request):
    if os.path.isfile(MEDIA_URL + file_name + '.apk'): 
        apkleaks = subprocess.run(["python", tools_dir + "/apkleaks/apkleaks.py", "-f", MEDIA_URL + file_name + ".apk", "-o", f'{output_dir}/{file_name}.txt'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        global context
        context = parse_result(request)
    else:
        return HttpResponse("Ooops!! File Doesn't Exist.")

    finalContext = {
        'context':context
    }
    return render(request, "recon/overview.html", finalContext)


section_list = []
content_list = []
content_amount = []

# To parse result
def parse_result(request):
    global section_list
    global content_list
    global content_amount
    #Open file
    with open(f'{output_dir}/{file_name}.txt', 'r') as read_result_file:
        data = read_result_file.readlines()

    element_list = []
    list_of_list = []
    for item in data:
        if item != '\n':
            element_list.append(item.strip())
        elif item == '\n':
            list_of_list.append(element_list)
            element_list = []
    return list_of_list

# Parsing result
def result_view(request):
    if request.method == "GET":
        section = request.GET.get("section", None)
        for itemList in context:
            for item in itemList:
                if item == section:
                    return render(request, "recon/result.html", {'resultContext':itemList, 'title':section})
    return render(request, "recon/result.html", {'resultContext':"Something is Wrong!!"})

# To download result
def download_result(request):
    if request.method == "GET":
        result_file = output_dir + '/' + file_name + '.txt'
        with open(result_file, "r") as fh:
                response = HttpResponse(
                    fh.read(), content_type="text/plain charset=utf-8"
                )
                response["Content-Disposition"] = "attachment; filename=%s" % file_name
                return response