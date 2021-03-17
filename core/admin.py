from django.contrib import admin
from .models import Faculty, Building, MemberInfo, Conference, MemberApplication, ConferenceSections, Member
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



class ConferenceSectionsInline(admin.StackedInline):
    model = ConferenceSections


class ConferenceAdmin(admin.ModelAdmin):
    model = Conference
    inlines = [ConferenceSectionsInline,]



class FacultyInline(admin.StackedInline):
    model = Faculty

class BuildingAdmin(admin.ModelAdmin):
    model = Building
    inlines = [FacultyInline,]

admin.site.register(Faculty)
admin.site.register(Conference,ConferenceAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(MemberInfo)
admin.site.register(MemberApplication)
admin.site.register(ConferenceSections)
admin.site.register(Member)
