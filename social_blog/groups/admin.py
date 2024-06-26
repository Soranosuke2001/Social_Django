from django.contrib import admin
from .models import Group, GroupMember


class GroupMemberInline(admin.TabularInline):
  model = GroupMember


# Register your models here.
admin.site.register(Group)
