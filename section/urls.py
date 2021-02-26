from django.urls import path
from .views import *

app_name = "section"

urlpatterns = [
    path("", homePage.as_view(), name="home"),
    path("section/<int:pk>/scan/<str:work>/", ScanQR.as_view(), name="scan"),
    path("sections/", SectionList.as_view(), name="section_list"),
    path("section/<int:pk>/", SectionDetail.as_view(), name="section_list"),
]
