from django.contrib import admin
from .models import Facility, Review

class ReviewInline(admin.TabularInline):
    model = Review

class FacilityAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Review)
