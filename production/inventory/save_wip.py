#The functions in this module update wip quantity or save it
from production.models import RetailCutWip, SprayedWip, FramedWip, GluedWip,\
        GradedWip, Coating
from datetime import datetime
from production.utils import conversions

def retail_cut_wip(wip_displays, date, is_cradled, coating, panel_depth, wip_type):
    for wip in wip_displays:
        if int(wip.wip_id) == -1:
            new_wip = RetailCutWip(date = date, quantity = \
                    wip.quantity, is_cradled = is_cradled,\
                    coating_id = coating, retail_size_id = \
                    wip.retail_size_id, panel_depth_id = panel_depth,
                    type = wip_type)
            new_wip.save()
        else:
            saved_wip = RetailCutWip.objects.get(pk = wip.wip_id)
            saved_wip.quantity = wip.quantity
            saved_wip.save()

def sprayed_wip(wip_displays, date, color, panel_depth, wip_type):
    for wip in wip_displays:
        if int(wip.wip_id) == -1:
            new_wip = SprayedWip(date = date, quantity = wip.quantity,\
                    retail_size_id = wip.retail_size_id, panel_depth_id = \
                    panel_depth, spray_color_id = color, type = wip_type)
            new_wip.save()
        else:
            pdb.set_trace()
            saved_wip = SprayedWip.objects.get(pk = wip.wip_id)
            saved_wip.quantity = wip.quantity
            saved_wip.save()

def framed_wip(wip_displays, date, cradle_depth, wip_type):
    for wip in wip_displays:
        if int(wip.wip_id) == -1:
            new_wip = FramedWip(date = date, quantity = wip.quantity,\
                    retail_size_id = wip.retail_size_id, cradle_depth_id = \
                    cradle_depth, type = wip_type)
            new_wip.save()
        else:
            saved_wip = FramedWip.objects.get(pk = wip.wip_id)
            saved_wip.quantity = wip.quantity
            saved_wip.save()

def glued_wip(wip_displays, date, coating, cradle_depth, panel_depth, wip_type,\
        color = -1):
    for wip in wip_displays:
        if int(wip.wip_id) == -1:
            new_wip = GluedWip(date = date, quantity = wip.quantity,\
                    retail_size_id = wip.retail_size_id, coating_id = coating,\
                    cradle_depth_id = cradle_depth, panel_depth_id = panel_depth,\
                    type = wip_type)
            new_wip.save()
        else:
            saved_wip = GluedWip.objects.get(pk = wip.wip_id)
            saved_wip.quantity = wip.quantity
            saved_wip.save()

def graded_wip(wip_displays, date, coating, panel_depth, coating_size, wip_type):
    for wip in wip_displays:
        if int(wip.wip_id) == -1:
            new_wip = GradedWip(date = date, quantity = wip.quantity,\
                    coating_id = coating, grade = wip.grade, panel_depth_id = \
                    panel_depth, coating_size_id = coating_size, type = \
                    wip_type)
            new_wip.save()
        else:
            saved_wip = GradedWip.objects.get(pk = wip.wip_id)
            saved_wip.quantity = wip.quantity
            saved_wip.save()
