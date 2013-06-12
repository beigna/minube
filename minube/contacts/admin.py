from django.contrib import admin
from .models import Group, Contact, ContactData


class GroupAdmin(admin.ModelAdmin): pass


class ContactAdmin(admin.ModelAdmin): pass


class ContactDataAdmin(admin.ModelAdmin): pass


admin.site.register(Group, GroupAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactData, ContactDataAdmin)
