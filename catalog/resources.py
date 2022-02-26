from catalog.models import Generic, Company, Strength, DosageForm, Medicine
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget


class GenericResource(resources.ModelResource):
    class Meta:
        model = Generic
        fields = ('name',)
        export_order = ('name',)
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped =  True


class StrengthResource(resources.ModelResource):
    class Meta:
        model = Strength
        fields = ('name',)
        export_order = ('name',)
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped =  True


class DosageFormResource(resources.ModelResource):
    class Meta:
        model = DosageForm
        fields = ('name',)
        export_order = ('name',)
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped =  True


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        fields = ('name', 'address',)
        export_order = ('name', 'address',)
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped = True     


class MedicineResource(resources.ModelResource):
    generic_name = fields.Field(
        column_name='generic_name',
        attribute='generic',
        widget=ForeignKeyWidget(Generic, 'name'))
    strength = fields.Field(
        column_name='strength',
        attribute='strength',
        widget=ForeignKeyWidget(Strength, 'name'))
    dosage_form = fields.Field(
        column_name='dosage_form',
        attribute='dosage_form',
        widget=ForeignKeyWidget(DosageForm, 'name'))
    company_name = fields.Field(
        column_name='company_name',
        attribute='company',
        widget=ForeignKeyWidget(Company, 'name'))

    class Meta:
        model = Medicine
        fields = ('name', 'generic_name', 'strength', 'dosage_form', 'company_name', 'unit_identifiers', 'unit_price', 'pack_size', 'pack_price',)
        export_order = ('name', 'generic_name', 'strength', 'dosage_form', 'company_name', 'unit_identifiers', 'unit_price', 'pack_size', 'pack_price',)
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped = True
