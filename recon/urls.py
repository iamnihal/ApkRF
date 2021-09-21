from django.urls import path
from .views import analyze_apk, download_result, index, result_view, download_result

urlpatterns = [
    path('', index, name='index-page'),
    path('scan/', analyze_apk, name='scan-apk'),
    path('result/', result_view, name="result-view"),
    path('download-result/', download_result, name="download-result"),
]