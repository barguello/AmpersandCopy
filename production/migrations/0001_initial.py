# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoatCuttingPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cutting_instructions', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'coat_cutting_pattern',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoatCuttingPatternOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('coat_cutting_pattern', models.ForeignKey(to='production.CoatCuttingPattern')),
            ],
            options={
                'db_table': 'coat_cutting_pattern_output',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoatCuttingSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'coat_cutting_sheet',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoatCuttingSheetEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'coat_cutting_sheet_entry',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoatCuttingSheetInstruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('output_string', models.CharField(max_length=90)),
                ('coat_cutting_pattern', models.ForeignKey(to='production.CoatCuttingPattern')),
                ('coat_cutting_sheet', models.ForeignKey(to='production.CoatCuttingSheet')),
            ],
            options={
                'db_table': 'coat_cutting_sheet_instruction',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(unique=True, max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'coating',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoatingSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.DecimalField(max_digits=10, decimal_places=5)),
                ('width', models.DecimalField(max_digits=10, decimal_places=5)),
                ('unit_of_measurement', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'coating_size',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CradleDepth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measurement', models.DecimalField(max_digits=10, decimal_places=5)),
                ('unit_of_measurement', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'cradle_depth',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CradleWidth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measurement', models.DecimalField(max_digits=10, decimal_places=5)),
                ('unit_of_measurement', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'cradle_width',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinishedGoodsInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=29)),
            ],
            options={
                'db_table': 'finished_goods_inventory',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FramedWip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=29)),
                ('cradle_depth', models.ForeignKey(to='production.CradleDepth')),
            ],
            options={
                'db_table': 'framed_wip',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GluedWip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=29)),
                ('coating', models.ForeignKey(to='production.Coating', null=True)),
                ('cradle_depth', models.ForeignKey(to='production.CradleDepth')),
            ],
            options={
                'db_table': 'glued_wip',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GradedWip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('grade', models.CharField(max_length=8, blank=True)),
                ('type', models.CharField(max_length=29)),
                ('coating', models.ForeignKey(to='production.Coating', null=True)),
                ('coating_size', models.ForeignKey(to='production.CoatingSize')),
            ],
            options={
                'db_table': 'graded_wip',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ampersand_sku', models.CharField(unique=True, max_length=45)),
                ('description', models.TextField()),
                ('case_quantity', models.IntegerField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'item',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('coating', models.ForeignKey(to='production.Coating', null=True)),
                ('cradle_depth', models.ForeignKey(blank=True, to='production.CradleDepth', null=True)),
                ('cradle_width', models.ForeignKey(blank=True, to='production.CradleWidth', null=True)),
            ],
            options={
                'db_table': 'item_recipe',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_number', models.IntegerField(unique=True)),
                ('po_number', models.CharField(max_length=45, db_column='PO_number', blank=True)),
                ('promised_date', models.DateField()),
                ('order_date', models.DateField()),
                ('production_date', models.DateField(null=True, blank=True)),
                ('referral', models.CharField(max_length=45, blank=True)),
                ('status', models.CharField(max_length=45)),
                ('customer', models.ForeignKey(to='production.Customer')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.DecimalField(max_digits=10, decimal_places=5)),
                ('retail_amount', models.CharField(max_length=45, blank=True)),
                ('item', models.ForeignKey(to='production.Item')),
                ('order', models.ForeignKey(to='production.Order')),
            ],
            options={
                'db_table': 'order_item',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_quantity', models.IntegerField()),
                ('item', models.ForeignKey(to='production.Item')),
                ('item_recipe', models.ForeignKey(blank=True, to='production.ItemRecipe', null=True)),
            ],
            options={
                'db_table': 'pack',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PanelDepth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measurement', models.DecimalField(max_digits=10, decimal_places=5)),
                ('unit_of_measurement', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'panel_depth',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCuttingPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cutting_instructions', models.TextField(blank=True)),
                ('grade', models.CharField(max_length=10000, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('coating_size', models.ForeignKey(to='production.CoatingSize')),
            ],
            options={
                'db_table': 'retail_cutting_pattern',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCuttingPatternOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('is_primary', models.IntegerField(null=True)),
                ('is_for_cradle', models.IntegerField(null=True)),
                ('retail_cutting_pattern', models.ForeignKey(to='production.RetailCuttingPattern')),
            ],
            options={
                'db_table': 'retail_cutting_pattern_output',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCuttingSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('coating', models.ForeignKey(to='production.Coating', null=True)),
                ('panel_depth', models.ForeignKey(to='production.PanelDepth')),
            ],
            options={
                'db_table': 'retail_cutting_sheet',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCuttingSheetEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('is_cradled', models.IntegerField()),
                ('retail_cutting_sheet', models.ForeignKey(to='production.RetailCuttingSheet')),
            ],
            options={
                'db_table': 'retail_cutting_sheet_entry',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCuttingSheetInstruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('output_string', models.CharField(max_length=90)),
                ('quantity', models.IntegerField()),
                ('retail_cutting_pattern', models.ForeignKey(to='production.RetailCuttingPattern')),
                ('retail_cutting_sheet_entry', models.ForeignKey(to='production.RetailCuttingSheetEntry')),
            ],
            options={
                'db_table': 'retail_cutting_sheet_instruction',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailCutWip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('is_cradled', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=29, null=True)),
                ('coating', models.ForeignKey(to='production.Coating', null=True)),
                ('panel_depth', models.ForeignKey(to='production.PanelDepth', null=True)),
                ('retail_cutting_sheet', models.ForeignKey(blank=True, to='production.RetailCuttingSheet', null=True)),
            ],
            options={
                'db_table': 'retail_cut_wip',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RetailSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.DecimalField(max_digits=10, decimal_places=5)),
                ('length', models.DecimalField(max_digits=10, decimal_places=5)),
                ('unit_of_measurement', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('unit_of_measurement', 'width', 'length'),
                'db_table': 'retail_size',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SprayColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(unique=True, max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'spray_color',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SprayedWip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=29)),
                ('panel_depth', models.ForeignKey(to='production.PanelDepth')),
                ('retail_size', models.ForeignKey(to='production.RetailSize')),
                ('spray_color', models.ForeignKey(to='production.SprayColor')),
            ],
            options={
                'db_table': 'sprayed_wip',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='retailcutwip',
            name='retail_size',
            field=models.ForeignKey(to='production.RetailSize', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='retailcuttingpatternoutput',
            name='retail_size',
            field=models.ForeignKey(to='production.RetailSize', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemrecipe',
            name='panel_depth',
            field=models.ForeignKey(to='production.PanelDepth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemrecipe',
            name='retail_size',
            field=models.ForeignKey(to='production.RetailSize'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemrecipe',
            name='spray_color',
            field=models.ForeignKey(blank=True, to='production.SprayColor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gradedwip',
            name='panel_depth',
            field=models.ForeignKey(to='production.PanelDepth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gluedwip',
            name='panel_depth',
            field=models.ForeignKey(to='production.PanelDepth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gluedwip',
            name='retail_size',
            field=models.ForeignKey(to='production.RetailSize'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gluedwip',
            name='spray_color',
            field=models.ForeignKey(blank=True, to='production.SprayColor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='framedwip',
            name='retail_size',
            field=models.ForeignKey(to='production.RetailSize'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='finishedgoodsinventory',
            name='item',
            field=models.ForeignKey(to='production.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coatcuttingsheet',
            name='coat_cutting_sheet_entry',
            field=models.ForeignKey(to='production.CoatCuttingSheetEntry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coatcuttingsheet',
            name='panel_depth',
            field=models.ForeignKey(to='production.PanelDepth'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coatcuttingpatternoutput',
            name='coating_size',
            field=models.ForeignKey(to='production.CoatingSize'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coatcuttingpattern',
            name='panel_depth',
            field=models.ForeignKey(to='production.PanelDepth'),
            preserve_default=True,
        ),
    ]
