from django.contrib import admin
from .models import Facility, Review

admin.site.register(Facility)
admin.site.register(Review)

class EntryInlines(admin.TabularInline):
    model = Review

class FacilityAdmin(admin.ModelAdmin):
    inlines = [EntryInlines]
