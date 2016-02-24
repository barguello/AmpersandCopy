from production.models import GradedWip, FinishedGoodsInventory, Item, Pack,\
OrderItem
from datetime import datetime


#return both now and BOP inventory date
def get_times():
    now = datetime.now()
    BOP_date = GradedWip.objects.order_by('-date').filter(type = \
            'Beginning of Period Inventory')[0].date
    return (now, BOP_date)

# returns the number of finished_goods since BOP inventory date for the given
# recipe components
#
# note: this is a slave function for retail_cuts, sprayed, and glued
def get_finished_goods_from_inventory(is_cradled, retail_size, coating,\
        panel_depth, cradle_depth, color):

    now, BOP_date = get_times()
    finished_goods_item_info = FinishedGoodsInventory.objects.filter(\
            item__item_recipe_cradle_depth__isnull = \
            conversions.bool_map(is_cradled), date__gt = BOP_date, date__lt = now,\
            **{f: e for f,e in\
            (('item__item_recipe__coating', coating),\
            ('item__item_recipe__retail_size', retail_size),\
            ('item__item_recipe__panel_depth', panel_depth),\
            ('item__item_recipe__cradle_depth', cradle_depth),\
            ('item__item_recipe__spray_color', color))\
            if e})

    finished_goods = finished_goods_item_info.item.case_quantity*\
            finished_goods_item_info.aggregate(Sum('quantity'))['quantity__sum']

    finished_goods_packs = Pack.objects.filter(**{f: e for f,e in (\
            ('item_recipe__coating', coating),\
            ('item_recipe__retail_size', retail_size),\
            ('item_recipe__panel_depth', panel_depth),\
            ('item_recipe__cradle_depth', cradle_depth),\
            ('item_recipe__spray_color', color))\
            if e})

    for pack in finished_goods_packs:
        item = Item.objects.get(pack = pack)
        finished_goods_quantity = FinishedGoodsInventory.objects.filter(\
                item = item, date__gt = BOP_date, date_lt = now).aggregate(\
                Sum('quantity'))['quantity_sum']
        finished_goods += finished_goods_quantity*item.case_quantity*\
                pack.pack_quantity

    return finished_goods

# returns demand for for items with the given recipe components between the
# BOP inventory date and shortage_date
#
# note: the panels that are in demand are those 'pending' and ordered before the
#       shortage date along with those which are no longer 'pending' yet placed
#       between BOP inventory and now
def get_demand(shortage_date, is_cradled, retail_size,\
        coating, panel_depth, cradle_depth, color):

    now, BOP_date = get_times()
    order_item_info = OrderItem.objects.filter((Q(order__status = 'Pending') &\
            Q(order__promised_date__lt = shortage_date)) | (~Q(order__status = \
            'Pending') & Q(order__order_date__gt = BOP_date) &\
            Q(order__order_date__lt = now)), item__recipe_cradle_depth__isnull = \
            conversions.bool_map(is_cradled), **{f: e for f,e in(\
            ('item__item_recipe__coating', coating),\
            ('item__item_recipe__retail_size', retail_size),\
            ('item__item_recipe__panel_depth', panel_depth),\
            ('item__item_recipe__cradle_depth', cradle_depth),\
            ('item__item_recipe__spray_color', color))
            if e})

    demand = order_item_info.item.case_quantity*\
            order_item_info.aggregate(Sum('quantity'))['quantity__sum']

    packs = Pack.objects.filter(**{f: e for f,e in(\
            ('item_recipe__coating', coating),\
            ('item_recipe__retail_size', retail_size),\
            ('item_recipe__panel_depth', panel_depth),\
            ('item_recipe__cradle_depth', cradle_depth),\
            ('item_recipe__spray_color', color))
            if e})

    for pack in packs:
        item = Item.objects.get(pack = pack)
        order_item_quantity = OrderItem.objects.filter((Q(order_status = 'Pending')\
                & Q(order__promised_date__lt = shortage_date)) | (~Q(order__status = \
                'Pending') & Q(order__order_date__gt = BOP_date) & \
                Q(order__order_date__lt = now)), item = item).\
                aggregate(Sum('quantity'))['quantity_sum']
        demand += order_item_quantity*item.case_quantity*\
                pack.pack_quantity

    return demand
