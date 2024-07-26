from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView

from application.custom_classes import AjayDatatableView, AdminRequiredMixin
from apps.service.forms import ServiceForm
from apps.service.models import Service


# Create your views here.


class ServiceView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "service/form.html"
    success_message=""
    success_url = reverse_lazy('service-list')


class ServiceTemplate(TemplateView):
    template_name = "service/list.html"

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "service/form.html"
    success_url = reverse_lazy('service-list')

class ServiceDeleteView(DeleteView):
    model = Service

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)

class ServiceListViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Service
    columns = ["id","service_name","payment_terms","service_price","service_package","service_tax","service_image","active","actions"]
    exclude_from_search_columns = ["actions"]
    # extra_search_columns = ['']

    def get_initial_queryset(self):
        return self.model.objects.all()

    def render_column(self, row, column):
        if column == 'active':
            if row.active:
                return '<span class="badge badge-success">Active</span>'
            else:
                return '<span class="badge badge-danger">Inactive</span>'

        if column == 'service_image':
            return f'<img src="{row.service_image.url}" height=50px alt="SampleImage">'

        if column == 'actions':
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('service-edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('service-delete', kwargs={'pk': row.pk}))
            return edit_action+delete_action
        else:
            return super(ServiceListViewJson, self).render_column(row,column)

