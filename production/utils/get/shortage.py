from production.models import GradedWip, RetailCutWip, FramedWip, GluedWip,\
        SprayedWip, FinishedGoodsInventory, Coating, Item, Pack, OrderItem
from production.utils import conversions
from datetime import datetime
from django.db.models import Sum, Q
import helper


# note: the panels that are part of the shortage are those 'pending' and ordered 
#       before the shortage date along with those which are no longer 'pending'
#       yet placed between BOP inventory and now

# shortage for panels
def retail_cuts(shortage_date, is_cradled, coating, retail_size, panel_depth):
    now, BOP_date = helper.get_times()
    description = Coating.objects.get(pk = coating).description
    throughput = RetailCutWip.objects.filter(is_cradled = conversions.bool_map(\
            is_cradled), coating = coating, retail_size = retail_size, panel_depth = \
            panel_depth, date__gt = BOP_date, date__lt = now).aggregate\
            (Sum('quantity'))['quantity__sum']

    if description == 'Pastelbord':
        demand = helper.get_demand(shortage_date, False, retail_size,\
                coating, panel_depth, [], [])
    elif conversions.bool_map(is_cradled):
        demand = helper.get_demand(shortage_date, True, retail_size,\
                coating, panel_depth, [], [])
    else:
        demand = helper.get_demand(shortage_date, False, retail_size,\
                coating, panel_depth, [], [])

    return demand - throughput

# shortage for sprayed panels
def sprayed(shortage_date, retail_size, panel_depth, color):
    now, BOP_date = helper.get_times()
    pastelbord = Coating.objects.get(description = 'Pastelbord')
    throughput = SprayedWip.objects.filter(retail_size = retail_size,\
            panel_depth = panel_depth, spray_color = color, date__gt = BOP_date,\
            date__lt = now).aggregate(Sum('quantity'))['quantity__sum']
    demand = helper.get_demand(shortage_date, False, retail_size,\
            pastelbord, panel_depth, [], color)

    return demand - throughput

# shortage for glued panels
def glued(shortage_date, retail_size, coating, cradle_depth, panel_depth):
    now, BOP_date = helper.get_times()
    throughput = GluedWip.objects.filter(retail_size = retail_size, coating = coating,\
            cradle_depth = cradle_depth, panel_depth = panel_depth,\
            date__gt = BOP_date, date__lt = now).aggregate(Sum('quantity'))\
            ['quantity_sum']
    demand = helper.get_demand(shortage_date, True, retail_size,\
            coating, panel_depth, cradle_depth, [])

    return demand - throughput

# shortage for framed panels
def framed(shortage_date, retail_size, cradle_depth):
    now, BOP_date = helper.get_times()
    throughput = FramedWip.objects.filter(retail_size = retail_size,\
            cradle_depth = cradle_depth, date__gt = BOP_date, date__lt = now).\
            aggregate(Sum('quantity'))
    demand = helper.get_demand(shortage_date, True, retail_size,\
            [], [], cradle_depth, [])

    return demand - throughput
