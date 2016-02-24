#The functions in this module return the wip in a displayable form
from production.models import RetailCutWip, SprayedWip, FramedWip, GluedWip,\
        GradedWip
from datetime import datetime
from production.utils import conversions, display
from production.inventory import get


#Displays
#--------------------------------------------------------------------
class DisplaySizeRow:
    def __init__(self, wip_id, retail_size_id, retail_size, quantity):
        self.wip_id = wip_id
        self.retail_size_id = retail_size_id
        self.retail_size = retail_size
        self.quantity = quantity

class DisplayGradeRow:
    def __init__(self, wip_id, grade, quantity):
        self.wip_id = wip_id
        self.grade = grade
        self.quantity = quantity
#---------------------------------------------------------------------


#Masters
#--------------------------------------------------------------------
def retail_cut_wip(date, is_cradled, coating, panel_depth, wip_type):
    sizes = get.retail_sizes_for_retail_cuts(coating, panel_depth)
    wip_displays = []
    current_date = datetime.strptime(date, '%Y-%m-%d').date()

    for size in sizes:
        try:
            wip = RetailCutWip.objects.get(date__startswith = current_date,\
                    is_cradled = conversions.bool_map[is_cradled], coating_id = \
                    coating, retail_size_id = size[0], panel_depth_id = \
                    panel_depth, type = wip_type)
            wip_displays.append(DisplaySizeRow(wip.id, size[0], size[1],\
                    wip.quantity))
            print "luck"
        except:
            wip_displays.append(DisplaySizeRow(-1, size[0], size[1], 0))

    return wip_displays

def sprayed_wip(date, panel_depth, color, wip_type):
    sizes = get.retail_sizes_for_sprayed(panel_depth, color)
    wip_displays = []
    current_date = datetime.strptime(date, '%Y-%m-%d').date()

    for size in sizes:
        try:
            wip = SprayedWip.objects.get(date__startswith = current_date,\
                    retail_size_id = size[0], panel_depth_id = panel_depth,\
                    spray_color_id = color, type = wip_type)
            wip_displays.append(DisplaySizeRow(wip.id, size[0], size[1],\
                    wip.quantity))
        except:
            wip_displays.append(DisplaySizeRow(-1, size[0], size[1], 0))

    return wip_displays

def framed_wip(date, cradle_depth, wip_type):
    sizes = get.retail_sizes_for_framed(cradle_depth)
    wip_displays = []
    current_date = datetime.strptime(date, '%Y-%m-%d').date()

    for size in sizes:
        try:
            wip = FramedWip.objects.get(date__startswith = current_date,\
                    retail_size_id = size[0], cradle_depth_id = cradle_depth,\
                    type = wip_type)
            wip_displays.append(DisplaySizeRow(wip.id, size[0], size[1],\
                    wip.quantity))
        except:
            wip_displays.append(DisplaySizeRow(-1, size[0], size[1], 0))

    return wip_displays

def glued_wip(date, coating, panel_depth, cradle_depth, wip_type):
    sizes = get.retail_sizes_for_glued(coating, panel_depth, cradle_depth)
    wip_displays = []
    current_date = datetime.strptime(date, '%Y-%m-%d').date()

    for size in sizes:
        try:
            wip = GluedWip.objects.get(date__startswith = current_date,\
                retail_size_id = size[0], coating_id = coating,\
                cradle_depth_id = cradle_depth, panel_depth_id = panel_depth,\
                type = wip_type)
            wip_displays.append(DisplaySizeRow(wip.id, size[0], size[1],\
                wip.quantity))
        except:
            wip_displays.append(DisplaySizeRow(-1, size[0], size[1], 0))

    return wip_displays

def graded_wip(date, coating, panel_depth, coating_size, wip_type):
    grades = get.grades_for_coated_cuts(coating_size)
    wip_displays = []
    current_date = datetime.strptime(date, '%Y-%m-%d').date()

    for grade in grades:
        try:
            wip = GradedWip.objects.get(date__startswith = current_date,\
                coating_id = coating, grade = grade, panel_depth_id = panel_depth,\
                coating_size_id = coating_size, type = wip_type)
            wip_displays.append(DisplayGradeRow(wip.id, grade, wip.quantity))
        except:
            wip_displays.append(DisplayGradeRow(-1, grade, 0))

    return wip_displays
#--------------------------------------------------------------------
