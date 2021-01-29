from django.contrib import admin

from car_wash.models import *


admin.site.register([Washer],admin.ModelAdmin)
admin.site.register([Car],admin.ModelAdmin)
admin.site.register([Order],admin.ModelAdmin)

