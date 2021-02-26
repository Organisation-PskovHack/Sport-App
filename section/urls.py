from django.urls import path
from .views import *

app_name = "section"

urlpatterns = [
    path("", homePage.as_view(), name="home"),
    path("scan/", ScanQR.as_view(), name="scan"),
    path("sections/", SectionList.as_view(), name="section_list"),
    # path("section/<int:pk>/", SectionDetail.as_view(), name="section_list"),TestSectionDetail
    path("section/", TestSectionDetail.as_view(), name="section_list"),
    path("profile/", Profile.as_view(), name="Profile"),
]
