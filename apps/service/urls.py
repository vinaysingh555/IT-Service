from django.urls import path

from apps.service.views import ServiceView, ServiceUpdateView, ServiceDeleteView, ServiceTemplate, ServiceListViewJson

urlpatterns=[
    path("create/Service",ServiceView.as_view(),name="create-service"),
    path("service/list",ServiceTemplate.as_view(),name="service-list"),
    path("service/edit/<int:pk>/",ServiceUpdateView.as_view(),name="service-edit"),
    path("service/delete/<int:pk>/",ServiceDeleteView.as_view(),name="service-delete"),
    path("service/list/ajax",ServiceListViewJson.as_view(),name="service-list-ajax")

]