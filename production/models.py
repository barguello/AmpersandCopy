# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from production.utils import display


# class AuthGroup(models.Model):
#
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey('AuthPermission')
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group_permissions'
#
#
# class AuthPermission(models.Model):
#
#     name = models.CharField(max_length=50)
#     content_type = models.ForeignKey('DjangoContentType')
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_permission'
#
#
# class AuthUser(models.Model):
#
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75)
#     is_staff = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_groups'
#
#
# class AuthUserUserPermissions(models.Model):
#
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_user_permissions'


class CoatCuttingPattern(models.Model):
    
    cutting_instructions = models.TextField(blank=True)
    panel_depth = models.ForeignKey('PanelDepth')

    class Meta:
        managed = True
        db_table = 'coat_cutting_pattern'


class CoatCuttingPatternOutput(models.Model):
    
    quantity = models.IntegerField()
    coat_cutting_pattern = models.ForeignKey(CoatCuttingPattern)
    coating_size = models.ForeignKey('CoatingSize')

    class Meta:
        managed = True
        db_table = 'coat_cutting_pattern_output'


class CoatCuttingSheet(models.Model):
    
    created = models.DateTimeField()
    coat_cutting_sheet_entry = models.ForeignKey('CoatCuttingSheetEntry')
    panel_depth = models.ForeignKey('PanelDepth')

    class Meta:
        managed = True
        db_table = 'coat_cutting_sheet'


class CoatCuttingSheetEntry(models.Model):
    
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'coat_cutting_sheet_entry'


class CoatCuttingSheetInstruction(models.Model):
    
    quantity = models.IntegerField()
    output_string = models.CharField(max_length=90)
    coat_cutting_sheet = models.ForeignKey(CoatCuttingSheet)
    coat_cutting_pattern = models.ForeignKey(CoatCuttingPattern)

    class Meta:
        managed = True
        db_table = 'coat_cutting_sheet_instruction'


class Coating(models.Model):
    
    description = models.CharField(unique=True, max_length=64)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
            return self.description

    class Meta:
        managed = True
        db_table = 'coating'


class CoatingSize(models.Model):
    
    length = models.DecimalField(max_digits=10, decimal_places=5)
    width = models.DecimalField(max_digits=10, decimal_places=5)
    unit_of_measurement = models.CharField(max_length=2)

    def __unicode__(self):
        return str(self.width) + " x " + str(self.length) + " " + self.unit_of_measurement

    class Meta:
        managed = True
        db_table = 'coating_size'


class CradleDepth(models.Model):
    
    measurement = models.DecimalField(max_digits=10, decimal_places=5)
    unit_of_measurement = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return display.small_measurement(self)

    class Meta:
        managed = True
        db_table = 'cradle_depth'


class CradleWidth(models.Model):
    
    measurement = models.DecimalField(max_digits=10, decimal_places=5)
    unit_of_measurement = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return display.small_measurement(self)

    class Meta:
        managed = True
        db_table = 'cradle_width'


class Customer(models.Model):
    
    name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'customer'

    def __unicode__(self):
        return self.name


# class DjangoAdminLog(models.Model):
#
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#     user = models.ForeignKey(AuthUser)
#
#     class Meta:
#         managed = True
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'django_content_type'
#
#
# class DjangoMigrations(models.Model):
#
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40, default="default_session_key")
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_session'


class FinishedGoodsInventory(models.Model):
    
    date = models.DateField()
    quantity = models.IntegerField()
    item = models.ForeignKey('Item')
    type = models.CharField(max_length=29)

    class Meta:
        managed = True
        db_table = 'finished_goods_inventory'


class FramedWip(models.Model):
    
    date = models.DateTimeField()
    quantity = models.IntegerField()
    retail_size = models.ForeignKey('RetailSize')
    cradle_depth = models.ForeignKey(CradleDepth)
    type = models.CharField(max_length=29)

    class Meta:
        managed = True
        db_table = 'framed_wip'


class GluedWip(models.Model):
    
    date = models.DateTimeField()
    quantity = models.IntegerField()
    retail_size = models.ForeignKey('RetailSize')
    coating = models.ForeignKey(Coating, null=True)
    cradle_depth = models.ForeignKey(CradleDepth)
    panel_depth = models.ForeignKey('PanelDepth')
    spray_color = models.ForeignKey('SprayColor', blank=True, null=True)
    type = models.CharField(max_length=29)

    class Meta:
        managed = True
        db_table = 'glued_wip'


class GradedWip(models.Model):
    
    date = models.DateField()
    quantity = models.IntegerField()
    coating = models.ForeignKey(Coating, null=True)
    grade = models.CharField(max_length=8, blank=True)
    panel_depth = models.ForeignKey('PanelDepth')
    coating_size = models.ForeignKey(CoatingSize)
    type = models.CharField(max_length=29)

    class Meta:
        managed = True
        db_table = 'graded_wip'


class Item(models.Model):
    
    ampersand_sku = models.CharField(unique=True, max_length=45)
    description = models.TextField()
    case_quantity = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'item'


class ItemRecipe(models.Model):
    
    coating = models.ForeignKey(Coating, null=True)
    cradle_depth = models.ForeignKey(CradleDepth, blank=True, null=True)
    panel_depth = models.ForeignKey('PanelDepth')
    retail_size = models.ForeignKey('RetailSize')
    cradle_width = models.ForeignKey(CradleWidth, blank=True, null=True)
    spray_color = models.ForeignKey('SprayColor', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        display_string =display.small_measurement(self.panel_depth) +  " panel--" + display.retail_size(self.retail_size) +\
                "--" + self.coating.description
        if self.spray_color:
            display_string += "--" + self.spray_color.color
        if self.cradle_depth:
            display_string += "--cradled-> depth: " + display.small_measurement(self.cradle_depth) +\
                    ", width: " + display.small_measurement(self.cradle_width)
        return display_string

    def verbose_name(self):
        display_string =display.small_measurement(self.panel_depth) + " panel--" + display.retail_size(self.retail_size) +\
                "--" + self.coating.description
        if self.spray_color:
            display_string += "--" + self.spray_color.color
        if self.cradle_depth:
            display_string += "--cradled->depth: " + display.small_measurement(self.cradle_depth) +\
                    ", width: " + display.small_measurement(self.cradle_width)
        return display_string

    class Meta:
        managed = True
        db_table = 'item_recipe'


class Order(models.Model):
    
    invoice_number = models.IntegerField(unique=True)
    po_number = models.CharField(db_column='PO_number', max_length=45, blank=True)  # Field name made lowercase.
    promised_date = models.DateField()
    order_date = models.DateField()
    production_date = models.DateField(blank=True, null=True)
    referral = models.CharField(max_length=45, blank=True)
    status = models.CharField(max_length=45)
    customer = models.ForeignKey(Customer)

    class Meta:
        managed = True
        db_table = 'order'

    def save(self, *args, **kwargs):
        if not self.production_date:
            self.production_date = self.order_date
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    
    quantity = models.DecimalField(max_digits=10, decimal_places=5)
    retail_amount = models.CharField(max_length=45, blank=True)
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)

    class Meta:
        managed = True
        db_table = 'order_item'


class Pack(models.Model):
    
    pack_quantity = models.IntegerField()
    item_recipe = models.ForeignKey(ItemRecipe, blank=True, null=True)
    item = models.ForeignKey(Item)

    class Meta:
        managed = True
        db_table = 'pack'


class PanelDepth(models.Model):
    
    measurement = models.DecimalField(max_digits=10, decimal_places=5)
    unit_of_measurement = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return display.small_measurement(self)

    class Meta:
        managed = True
        db_table = 'panel_depth'


class RetailCutWip(models.Model):
    
    date = models.DateTimeField()
    quantity = models.IntegerField()
    is_cradled = models.IntegerField(null=True)
    coating = models.ForeignKey(Coating, null=True)
    retail_size = models.ForeignKey('RetailSize', null=True)
    panel_depth = models.ForeignKey(PanelDepth, null=True)
    type = models.CharField(max_length=29, null=True)
    retail_cutting_sheet = models.ForeignKey('RetailCuttingSheet', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'retail_cut_wip'


class RetailCuttingPattern(models.Model):
    
    cutting_instructions = models.TextField(blank=True)
    grade = models.CharField(max_length=10000, blank=True)
    coating_size = models.ForeignKey(CoatingSize)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'retail_cutting_pattern'

    def get_siblings(self, cutting_instructions=None):
        """Find Cutting Pattern similar to the current object"""
        cutting_instructions = cutting_instructions or self.cutting_instructions
        return RetailCuttingPattern.objects.filter(cutting_instructions=cutting_instructions).exclude(pk=self.pk)


class RetailCuttingPatternOutput(models.Model):
    
    quantity = models.IntegerField()
    retail_cutting_pattern = models.ForeignKey(RetailCuttingPattern)
    retail_size = models.ForeignKey('RetailSize', null=True)
    is_primary = models.IntegerField(null=True)
    is_for_cradle = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = 'retail_cutting_pattern_output'


class RetailCuttingSheet(models.Model):
    
    created = models.DateTimeField()
    coating = models.ForeignKey(Coating, null=True)
    panel_depth = models.ForeignKey(PanelDepth)

    class Meta:
        managed = True
        db_table = 'retail_cutting_sheet'


class RetailCuttingSheetEntry(models.Model):
    
    created = models.DateTimeField()
    is_cradled = models.IntegerField()
    retail_cutting_sheet = models.ForeignKey(RetailCuttingSheet)

    class Meta:
        managed = True
        db_table = 'retail_cutting_sheet_entry'


class RetailCuttingSheetInstruction(models.Model):
    
    output_string = models.CharField(max_length=90)
    quantity = models.IntegerField()
    retail_cutting_sheet_entry = models.ForeignKey(RetailCuttingSheetEntry)
    retail_cutting_pattern = models.ForeignKey(RetailCuttingPattern)

    class Meta:
        managed = True
        db_table = 'retail_cutting_sheet_instruction'


class RetailSize(models.Model):
    
    width = models.DecimalField(max_digits=10, decimal_places=5)
    length = models.DecimalField(max_digits=10, decimal_places=5)
    unit_of_measurement = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return display.retail_size(self)

    class Meta:
        managed = True
        ordering = ('unit_of_measurement', 'width', 'length')
        db_table = 'retail_size'


class SprayColor(models.Model):
    
    color = models.CharField(unique=True, max_length=64)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
            return self.color

    class Meta:
        managed = True
        db_table = 'spray_color'


class SprayedWip(models.Model):
    
    date = models.DateTimeField()
    quantity = models.IntegerField()
    retail_size = models.ForeignKey(RetailSize)
    panel_depth = models.ForeignKey(PanelDepth)
    spray_color = models.ForeignKey(SprayColor)
    type = models.CharField(max_length=29)

    class Meta:
        managed = True
        db_table = 'sprayed_wip'
