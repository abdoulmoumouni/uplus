from django.contrib import admin
from .models import Livre
from .models import Infos

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Infos


admin.site.register(Livre)
admin.site.register(Infos,ProductAdmin)
