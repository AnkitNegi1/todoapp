from django.contrib import admin
from Todo.models import TodoData

class TodoAdmin(admin.ModelAdmin):

    list_display = ('todotitle','todotimestamp','tododescription','tododate','todostatus')

# Register your models here.

admin.site.register(TodoData,TodoAdmin)


