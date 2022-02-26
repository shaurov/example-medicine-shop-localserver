from django.db import models
from django.template.defaultfilters import slugify


class Generic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Generic'
        verbose_name_plural = 'Generics'
        
    def __str__(self):
        return str(self.name)

    #auto generate slug from name field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Generic, self).save(*args, **kwargs)


class Strength(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Strength'
        verbose_name_plural = 'Strengths'

    def __str__(self):
        return str(self.name)


class DosageForm(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Dosage Form'
        verbose_name_plural = 'Dosage Forms'
    
    def __str__(self):
        return str(self.name)


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return str(self.name)

    #auto generate slug from name field and remove Ltd., Mfg.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace('Ltd.', '').replace('Mfg.', ''))
        super(Company, self).save(*args, **kwargs)


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic = models.ForeignKey(Generic, on_delete=models.CASCADE)
    strength = models.ForeignKey(Strength, on_delete=models.CASCADE)
    dosage_form = models.ForeignKey(DosageForm, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    unit_identifiers = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pack_size = models.PositiveSmallIntegerField(blank=True, null=True)
    pack_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        unique_together = [['name', 'generic', 'strength', 'dosage_form', 'company']]
    
    #calculate unit_price from pack_price and pack_size, else calculate pack_price from unit_price and pack_size only if pack_price is null, calculate pack_size to round from unit_price and pack_price
    def save(self, *args, **kwargs):
        if self.pack_size and self.pack_price:
            self.unit_price = self.pack_price / int(self.pack_size)
        elif self.pack_price is None and self.pack_size and self.unit_price:
            self.pack_price = self.unit_price * int(self.pack_size)
        if self.pack_size is None and self.pack_price and self.unit_price:
            self.pack_size = round(self.pack_price / self.unit_price)
        super(Medicine, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
