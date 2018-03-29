from django.contrib import admin

# Register your models here.
from .models import Budget, Budget_Pos, Budget_Base

admin.site.register(Budget)
admin.site.register(Budget_Pos)
admin.site.register(Budget_Base)
