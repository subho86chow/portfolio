from django.contrib import admin
from django.http import HttpResponse
from .models import *
from captcha.models import *
import csv
import xlsxwriter


def download_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'  # Fixed quote
    writer = csv.writer(response)
    headers = [field.verbose_name for field in modeladmin.model._meta.fields]
    writer.writerow(headers)
    for obj in queryset:
        data_row = [getattr(obj, field.name) for field in modeladmin.model._meta.fields]
        writer.writerow(data_row)
    return response


# Register your models here.
admin.site.register(Projects)
admin.site.register(Testimonials)
admin.site.register(Technology)
admin.site.register(Customer_emails)
admin.site.register(CaptchaStore)
admin.site.register(social_links)


download_csv.short_description = "Download CSV Data"

@admin.register(Contact_message)
class MessageAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'email',
        'message',
    )

    actions = [download_csv]
