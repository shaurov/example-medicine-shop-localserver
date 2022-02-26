from rest_framework import serializers
from catalog.models import Generic, Company, Strength, DosageForm, Medicine


class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generic
        fields = ('id', 'name', 'slug', 'is_active')
        ordering = ('name',)


class StrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strength
        fields = ('id', 'name')
        ordering = ('name',)


class DosageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageForm
        fields = ('id', 'name')
        ordering = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'address', 'is_active')
        ordering = ('name',)


class MedicineSerializer(serializers.ModelSerializer):
    generic = GenericSerializer(read_only=True)
    strength = StrengthSerializer(read_only=True)
    dosage_form = DosageFormSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Medicine
        fields = ('id', 'name', 'generic', 'strength', 'dosage_form', 'company', 'unit_identifiers', 'unit_price', 'pack_size', 'pack_price', 'is_active')
        ordering = ('name',)


#flatten MedicineSerializer nested fields
class MedicineSerializerFlattened(serializers.ModelSerializer):
    generic_name = serializers.CharField(source='generic.name', read_only=True)
    strength_name = serializers.CharField(source='strength.name', read_only=True)
    dosage_form_name = serializers.CharField(source='dosage_form.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Medicine
        fields = ('id', 'name', 'generic_name', 'strength_name', 'dosage_form_name', 'company_name', 'unit_identifiers', 'unit_price', 'pack_size', 'pack_price', 'is_active')
        ordering = ('name',)
