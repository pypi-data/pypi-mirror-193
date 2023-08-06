from django.urls import path, re_path

from . import views

urlpatterns = [
    path("regiones/", views.RegionListView.as_view(), name="list_region"),
    path("provincias/", views.ProvinciaListView.as_view(), name="list_provincia"),
    path("distritos/", views.DistritoListView.as_view(), name="list_distrito"),
    re_path(
        r"regiones/(?P<coddpto>[0-9]{2})/$",
        views.RegionDetailView.as_view(),
        name="detail_region",
    ),
    re_path(
        r"provincias/(?P<idprov>[0-9]{4})/$",
        views.ProvinciaDetailView.as_view(),
        name="detail_provincia",
    ),
    re_path(
        r"distritos/(?P<iddist>[0-9]{6})/$",
        views.DistritoDetailView.as_view(),
        name="detail_distrito",
    ),
    re_path(
        r"regiones/(?P<coddpto>[0-9]{2})/provincias/$",
        views.RegionDetailView.as_view(),
        name="detail_region",
    ),
    re_path(
        r"regiones/(?P<coddpto>[0-9]{2})/provincias/(?P<idprov>[0-9]{4})/$",
        views.ProvinciaDetailView.as_view(),
        name="detail_region_provincias",
    ),
    re_path(
        r"regiones/(?P<coddpto>[0-9]{2})/provincias/(?P<idprov>[0-9]{4})/distritos/$",
        views.ProvinciaDetailView.as_view(),
        name="detail_provincia_distritos",
    ),
    re_path(
        r"regiones/(?P<coddpto>[0-9]{2})/provincias/(?P<idprov>[0-9]{4})/distritos/(?P<iddist>[0-9]{6})/$",
        views.DistritoDetailView.as_view(),
        name="detail_provincia_distrito",
    ),
]
