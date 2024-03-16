from django.contrib import admin

# Register your models here.
from .models import Finch, Feeding, Toy, Photo

admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)

# add Photo import

# add Photo registration
admin.site.register(Photo)
