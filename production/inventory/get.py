#These functions return retail sizes that are actually in a recipe for the
#for the parameters of the function
from production.models import ItemRecipe, RetailSize, Coating, PanelDepth,\
        CradleWidth, CradleDepth, SprayColor, CoatingSize,\
        RetailCuttingPattern
from production.utils import display


def retail_sizes_for_retail_cuts(coating, panel_depth):
    us_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'in').filter(itemrecipe__coating = coating,\
            itemrecipe__panel_depth = panel_depth).distinct()
    uk_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'cm').filter(itemrecipe__coating = coating,\
            itemrecipe__panel_depth = panel_depth).distinct()

    us_size_list = [(int(size.id), display.retail_size(size)) for size in \
            us_retail_sizes]
    uk_size_list = [(int(size.id), display.retail_size(size)) for size in \
            uk_retail_sizes]
    size_list = us_size_list + uk_size_list
    return size_list

def retail_sizes_for_sprayed(panel_depth, color):
    us_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'in').filter(itemrecipe__spray_color = color,\
            itemrecipe__panel_depth = panel_depth).distinct()
    uk_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'cm').filter(itemrecipe__spray_color = color,\
            itemrecipe__panel_depth = panel_depth).distinct()

    us_size_list = [(int(size.id), display.retail_size(size)) for size in \
            us_retail_sizes]
    uk_size_list = [(int(size.id), display.retail_size(size)) for size in \
            uk_retail_sizes]
    size_list = us_size_list + uk_size_list
    return size_list

def retail_sizes_for_framed(cradle_depth):
    us_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'in').filter(itemrecipe__cradle_depth =\
            cradle_depth).distinct()
    uk_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'cm').filter(itemrecipe__cradle_depth =\
            cradle_depth).distinct()

    us_size_list = [(int(size.id), display.retail_size(size)) for size in \
            us_retail_sizes]
    uk_size_list = [(int(size.id), display.retail_size(size)) for size in \
            uk_retail_sizes]
    size_list = us_size_list + uk_size_list
    return size_list

def retail_sizes_for_glued(coating, panel_depth, cradle_depth):
    us_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'in').filter(itemrecipe__coating = coating,\
            itemrecipe__panel_depth = panel_depth, itemrecipe__cradle_depth = \
            cradle_depth).distinct()
    uk_retail_sizes = RetailSize.objects.order_by('length', 'width').filter(\
            unit_of_measurement = 'cm').filter(itemrecipe__coating = coating,\
            itemrecipe__panel_depth = panel_depth, itemrecipe__cradle_depth = \
            cradle_depth).distinct()

    us_size_list = [(int(size.id), display.retail_size(size)) for size in \
            us_retail_sizes]
    uk_size_list = [(int(size.id), display.retail_size(size)) for size in \
            uk_retail_sizes]
    size_list = us_size_list + uk_size_list
    return size_list

def grades_for_coated_cuts(coating_size):
    patterns = RetailCuttingPattern.objects.order_by('grade').filter(\
            coating_size_id = coating_size)
    grades = set()
    grades_add = grades.add
    grade_list = [str(pattern.grade) for pattern in patterns if not \
            (str(pattern.grade) in  grades or grades_add(str(pattern.grade)))]
    grade_list.reverse()
    return grade_list
