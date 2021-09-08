from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("index.html", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('location_crash_pad', hello.views.location_crash),
    path('tarifs/', hello.views.tarifs, name="tarifs"),
    path('contact/', hello.views.tarif_grid, name="tarifs_grid"),
    path('menu_photo', hello.views.menu_photo, name="menu_photo"),
    path('photo', hello.views.photo, name="photo"),

]
