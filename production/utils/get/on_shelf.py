from production.models import GradedWip, RetailCutWip, FramedWip, GluedWip,\
        SprayedWip, FinishedGoodsInventory, Coating, Item, Pack,\
        RetailCuttingSheetInstruction
from production.utils import conversions
from datetime import datetime
from django.db.models import Sum
import helper


# returns the number of graded terceros on shelf
def graded(coating, grade, panel_depth, coating_size):
    now, BOP_date = helper.get_times()
    throughput = GradedWip.objects.filter(coating = coating, grade = grade,\
            panel_depth = panel_depth, coating_size = coating_size,\
            date__gt = BOP_date, date__lt = now).aggregate(Sum('quantity'))\
            ['quantity__sum']
    finished_goods = RetailCuttingSheetInstruction.objects.filter(\
            retail_cutting_sheet_entry__coating = coating,\
            retail_cutting_sheet_entry__panel_depth =panel_depth, \
            retail_cutting_pattern__grade = grade, \
            retail_cutting_pattern__coating_size = coating_size,\
            retail_cutting_sheet_entry__retail_cutting_sheet__created__gt = \
            BOP_date, retail_cutting_sheet_entry__retail_cutting_sheet__created__lt = \
            now).aggregate(Sum('quantity'))['quantity__sum']

    return throughput - finished_goods

# returns the number of flats on shelf
def flats(is_cradled, coating, retail_size, panel_depth):
    now, BOP_date = helper.get_times()
    description = Coating.objects.get(pk = coating).description
    throughput = RetailCutWip.objects.filter(is_cradled = conversions.bool_map(\
            is_cradled), coating = coating, retail_size = retail_size, panel_depth = \
            panel_depth, date__gt = BOP_date, date__lt = now).aggregate\
            (Sum('quantity'))['quantity__sum']

    if description == 'Pastelbord':
        finished_goods = SprayedWip.objects.filter(retail_size = retail_size,\
                panel_depth = panel_depth, date__gt = BOP_date,\
                date__lt = now).aggregate(Sum('quantity'))['quantity__sum']
    elif conversions.bool_map(is_cradled):
        finished_goods = GluedWip.objects.filter(retail_size = retail_size,\
                coating = coating, panel_depth = panel_depth, date__gt = BOP_date,\
                date__lt = now).aggregate(Sum('quantity'))['quantity__sum']
    else:
        finished_goods = helper.get_finished_goods_from_inventory(is_cradled,\
                retail_size, coating, panel_depth, [], [])

    return throughput - finished_goods

# returns the number of sprayed panels on shelf
def sprayed(retail_size, panel_depth, color):
    now, BOP_date = helper.get_times()
    pastelbord = Coating.objects.get(description = 'Pastelbord')
    throughput = SprayedWip.objects.filter(retail_size = retail_size,\
            panel_depth = panel_depth, spray_color = color, date__gt = BOP_date,\
            date__lt = now).aggregate(Sum('quantity'))['quantity__sum']
    finished_goods = helper.get_finished_goods_from_inventory(False, retail_size,\
            pastelbord, panel_depth, [], color)
    return throuput - finished_goods

# returns the number of glued panels on shelf
def glued(retail_size, coating, cradle_depth, panel_depth):
    now, BOP_date = helper.get_times()
    throughput = GluedWip.objects.filter(retail_size = retail_size, coating = coating,\
            cradle_depth = cradle_depth, panel_depth = panel_depth,\
            date__gt = BOP_date, date__lt = now).aggregate(Sum('quantity'))\
            ['quantity_sum']
    finished_goods = helper.get_finished_goods_from_inventory(True, retail_size,\
            coating, panel_depth, cradle_depth, [])

    return throughput - finished_goods

# returns the number of framed panels on shelf
def framed(retail_size, cradle_depth):
    now, BOP_date = helper.get_times()
    throughput = FramedWip.objects.filter(retail_size = retail_size,\
            cradle_depth = cradle_depth, date__gt = BOP_date, date__lt = now).\
            aggregate(Sum('quantity'))
    finished_goods = gluedWip.objects.filter(retail_size = retail_size, \
            cradle_depth = cradle_depth, date__gt = BOP_date, date__lt = now).\
            aggregate(Sum('quantity'))

    return throughput - finished_goods
