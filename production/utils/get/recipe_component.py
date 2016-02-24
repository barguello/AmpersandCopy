#This module can be used to get a list of the different recipe components
#ordered and formatted appropriately

from production.models import RetailSize, Coating, PanelDepth, CradleDepth, CradleWidth, SprayColor, CoatingSize

from production.utils import display

def retail_sizes():
    us_retail_sizes = RetailSize.objects.order_by('width', 'length').filter(unit_of_measurement = 'in')

    uk_retail_sizes = RetailSize.objects.order_by('width', 'length').filter(unit_of_measurement = 'cm')

    us_size_list = [(int(size.id), display.retail_size(size)) for size in us_retail_sizes]
    uk_size_list = [(int(size.id), display.retail_size(size)) for size in uk_retail_sizes]
    size_list = us_size_list + uk_size_list
    return size_list

def coating_cut_sizes():
    coat_cut_sizes = CoatingSize.objects.order_by('width', 'length')
    size_list = [(int(size.id), display.retail_size(size)) for size in coat_cut_sizes]
    return size_list

def coatings():
    coatings = Coating.objects.order_by('description')
    coating_list = [(int(coating.id), coating.description) for coating in coatings]
    return coating_list

def panel_depths():
    panel_depths = PanelDepth.objects.order_by('measurement')
    panel_depth_list = [(int(depth.id), display.small_measurement(depth))
                        for depth in panel_depths]
    return panel_depth_list

def cradle_depths():
    cradle_depths = CradleDepth.objects.order_by('measurement')
    cradle_depth_list = [(int(depth.id), display.small_measurement(depth))
                        for depth in cradle_depths]
    return cradle_depth_list

def cradle_widths():
    cradle_widths = CradleWidth.objects.order_by('measurement')
    cradle_width_list = [(int(width.id), display.small_measurement(width))
                        for width in cradle_widths]
    return cradle_width_list

def spray_colors():
    spray_colors = SprayColor.objects.order_by('color')
    spray_color_list = [(int(color.id), color.color) for color in spray_colors]
    return spray_color_list

def grades():
    return [['',''],['48', '48'],['45', '45'],['40','40'],['36', '36'],['36c', '36c'],['32','32'],['30','30'],['30c','30c'],['24','24'],['24c','24c'],['20','20'],['18','18'],['12','12'],['10','10']];
