from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('srdsitemap/',sitemap),
    path('index/',index),
    path('about/',aboutus),
    path('service/',service),
    path('portfolio/',portfolio),
    path('blog/',blog),
    path('contact/',contact),
    path('blog-item/',blogitem),
    path('sendmail/',contactmail),
    path('subscribe/',newsletter)
]
