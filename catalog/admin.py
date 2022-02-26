from django.contrib import admin
from catalog.models import Generic, Company, Strength, DosageForm, Medicine
from catalog.resources import GenericResource, CompanyResource, StrengthResource, DosageFormResource, MedicineResource
from import_export.admin import ImportExportModelAdmin


class GenericAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GenericResource
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class StrengthAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StrengthResource
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name',)
    ordering = ('name',)


class DosageFormAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DosageFormResource
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name',)
    ordering = ('name',)


class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CompanyResource
    list_display = ('name', 'slug', 'address', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug', 'address')
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MedicineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MedicineResource
    list_display = ('name', 'generic', 'strength', 'dosage_form', 'company', 'unit_identifiers', 'unit_price', 'pack_size', 'pack_price', 'is_active')
    list_filter = ('dosage_form', 'is_active',)
    search_fields = ('name', 'generic__name', 'company__name')
    ordering = ('name',)

    
admin.site.register(Generic, GenericAdmin)
admin.site.register(Strength, StrengthAdmin)
admin.site.register(DosageForm, DosageFormAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Medicine, MedicineAdmin)

