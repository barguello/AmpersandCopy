from production.models import RetailSize, Coating, PanelDepth, CoatingSize,\
        RetailCuttingPattern, RetailCuttingPatternOutput, OrderItem, Item, Pack
from production.utils.get import on_shelf
from datetime import datetime
from coopr.pyomo import *

# returns the pk for recipe components and the grades to be used as set 
# components
def indices():
    rs_list = RetailSize.objects.all()
    rs = [int(id.pk) for id in rs_list]

    c_list = Coating.objects.all()
    c = [int(id.pk) for id in c_list]

    pd_list = PanelDepth.objects.all()
    pd = [int(id.pk) for id in pd_list]

    cs_list = CoatingSize.objects.all()
    cs = [int(id.pk) for id in cs_list]

    g_list = RetailCuttingPattern.objects.values('grade').distinct()
    g = [int(element['grade']) for element in g_list]

    rcp_list = RetailCuttingPattern.objects.all()
    rcp = [int(id.pk) for id in rcp_list]

    #TODO: make this so that it only gets pending since BOP.  date is currently hardcoded
    oi_list = OrderItem.objects.filter(order__status = 'Order', \
            order__order_date__gt = datetime(2014, 12, 18)).order_by('order__order_date')
    oi = [int(id.pk) for id in oi_list]

    return (rs, c, pd, cs, g, rcp, oi)

# return a dictionary for retail cutting patterns to be used for subindexing rcp
def rcp_subset(g, cs, crad):
    rcp_subset_list = RetailCuttingPattern.objects.filter(grade = g, coating_size = \
            cs, is_for_cradle = True if crad == 1 else False)
    rcp_subset = [int(id.pk) for id in rcp_subset_list]

    return rcp_subset

# return a dictionary for order items to be used for subindexing oi
def oi_subset(rs, c, pd, crad):
    now = datetime.now().date()
    #get lineitems for recipes that pertain to items
    items = Item.objects.filter(item_recipe__retail_size = rs,\
             item_recipe__coating = c,\
             item_recipe__panel_depth = pd,\
             item_recipe__cradle_depth__isnull = False if crad == 1 else True)
    #TODO: make sure to put the right order_status
    order_item_info = OrderItem.objects.filter(order__status = 'Order',\
            item = items)

    #get lineitems for recipes that pertain to packs
    packs = Pack.objects.filter(\
            item_recipe__retail_size = rs,\
            item_recipe__coating = c,\
            item_recipe__panel_depth = pd,\
            item_recipe__cradle_depth__isnull = False if crad == 1 else True)
    for pack in packs:
        item = Item.objects.get(pack = pack)
        # TODO: make sure to put the right order_status
        pack_order_item_info = OrderItem.objects.filter(order__status = 'Order',\
                item = item)
        order_item_info = order_item_info | pack_order_item_info
    #order all lineitems by order_date
    order_item_info.order_by('order__order_date')

    #create a list of order_dates corresponding to each panel
    oi_subset = []
    for element in order_item_info:
        case_quantity = element.item.case_quantity

        pack_quantity = 0
        packs = Pack.objects.filter(item = element.item)
        for pack in packs:
            pack_quantity += pack.pack_quantity

        quantity = case_quantity*pack_quantity
        for i in range(quantity):
            time_gap = element.order.order_date - now
            oi_subset.append(time_gap.days)

    return oi_subset

def cut_outputs(rs, rcp):
    try:
        output = RetailCuttingPatternOutput.objects.get(retail_cutting_pattern = \
                rcp, retail_size = rs).values()
        return output
    except:
        return 0

def terceros(cs, c, pd, g):
    return on_shelf.graded(c,g,pd,cs)

def alpha():
    return 10

def beta():
    return 10

def gamma():
    return 10

def n1():
    return 10

def n2():
    return 10

def n3():
    return 10
