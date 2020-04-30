from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',UserAPIView.as_view()),
    path('api/vendor/',VendorAPIView.as_view()),
    path('basictable/',basictable),
    path('blank/',blank),
    path('buttons/',buttons),
    path('calendar/',calendar),
    path('chartjs/',chartjs),
    path('formcomponent/',formcomponent),
    path('gallery/',gallery),
    path('general/',general),
    path('lockscreen/',lockscreen),
    path('login/',login),
    path('morris/',morris),
    path('panels/',panels),
    path('responsivetable/',responsivetable),
    path('todolist/',todolist),
    path('adminlogin/',adminlogin),
    path('error/',error),
    path('addvendor/',addvendor),
    path('addproduct/',addproduct),
    path('addproductcategory/',addproductcategory),
    path('displayvendor/',displayvendor),
    path('addvendorcategory/',addvendorcategory),
    path('savevendorcategory/',savevendorcategory),
    path('savevendor/',savevendor),
    path('addvendorimages/',addvendorimages),
    path('deletevendor/',deletevendor),
    path('addvendorproduct/',addvendorproduct),
    path('deleteproduct/',deleteproduct),
    path('addproductimages/',addproductimages),
    path('addvendorcategory/',addvendorcategory),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)