from django.contrib import admin
from .models import Facility, Review

# class ReviewInlines(admin.TabularInline):
#     model = Review

# class FacilityAdmin(admin.ModelAdmin):
#     inlines = [ReviewInlines]

admin.site.register(Facility)
admin.site.register(Review)
