from django.contrib import admin
from main_app.models import SiteUser,Fleet,Ship,Section,Item,Order,Ship_Type

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(Fleet)
admin.site.register(Ship)
admin.site.register(Section)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Ship_Type)