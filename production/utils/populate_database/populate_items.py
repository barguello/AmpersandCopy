from production.models import Item, Pack, ItemRecipe, RetailSize, Coating, PanelDepth, CradleWidth, CradleDepth, SprayColor
from production.utils import conversions
import pandas


def get_measurements(row):
    panel_depth = row['Panel Depth']
    cradle_depth = row['Cradle Depth']
    cradle_width = row['Cradle Width']

    #English vs metric -- " is for inches
    if panel_depth[-1] == '"':
        panel_depth = PanelDepth.objects.filter(measurement = conversions.
                                                frac_to_dec[panel_depth[:-1]],
                                 unit_of_measurement = 'in')[0]
    else:
        panel_depth = PanelDepth.objects.filter(measurement = panel_depth[:-2],
                                 unit_of_measurement = panel_depth[-2:])[0]

    if row['Cradle Depth'] == '-':
        cradle_depth = 'none'
        cradle_width = 'none'
    else:
        if cradle_depth[-1] == '"':
            cradle_depth = CradleDepth.objects.get(measurement = conversions.\
                                                   frac_to_dec[cradle_depth[:-1]],\
                                                   unit_of_measurement = 'in')
            cradle_width = CradleWidth.objects.get(measurement = conversions.\
                                                   frac_to_dec[cradle_width[:-1]],
                                                   unit_of_measurement = 'in')
        else:
            cradle_depth = CradleDepth.objects.get(measurement = cradle_depth[:-2],
                                       unit_of_measurement = cradle_depth[-2:])
            cradle_width = CradleWidth.objects.get(measurement = cradle_width[:-2],
                                       unit_of_measurement = cradle_width[-2:])

    return (panel_depth, cradle_depth, cradle_width)

def get_recipe_components(row, unit):
    retail_size = RetailSize.objects.filter(length = row['length'], width = row['width'],
                                            unit_of_measurement = unit)[0]
    coating = Coating.objects.get(description = row['description'])
    panel_depth, cradle_depth, cradle_width = get_measurements(row)

    if row['description'] == 'Pastelbord':
        if row['Color'] == 'white':
            color = SprayColor.objects.get(color = 'white')
        else:
            color = SprayColor.objects.get(color = row['Color'])
    else:
        color = 'none'

    return (retail_size, coating, color, panel_depth, cradle_depth, cradle_width)

def get_recipe(row, unit):
    retail_size, coating, color, panel_depth, cradle_depth, cradle_width = get_recipe_components(row, unit)

    #branch by cradle or flat
    if cradle_depth == 'none':
        #branch by pastelbord or not
        if row['description'] == 'Pastelbord':
                new_recipe = ItemRecipe(coating = coating, panel_depth = panel_depth,
                                        retail_size = retail_size,\
                                        spray_color = color, is_active = True)
        else:
            new_recipe = ItemRecipe(coating = coating, panel_depth = panel_depth,
                                    retail_size = retail_size, is_active = True)

    else:
        #branch by pastelbord or not
        if row['description'] == 'Pastelbord':
            new_recipe = ItemRecipe(coating = coating, panel_depth = panel_depth,
                                    retail_size = retail_size,\
                                    spray_color = color, cradle_depth = cradle_depth,
                                    cradle_width = cradle_width, is_active = True)
        else:
            new_recipe = ItemRecipe(coating = coating, panel_depth = panel_depth,
                                    retail_size = retail_size, cradle_depth = cradle_depth,
                                    cradle_width = cradle_width, is_active = True)
    new_recipe.save()
    return new_recipe

def from_file(file_path, unit):
    '''imports items and recipes from file_path when the retail_size unit_of_measurement
    is unit

    Description
    -----------
    The csv given by file_path needs to be in absolutely the same format as US_master.csv
    Since width and length unit_of_measurement are not labeled, the unit will be given by
    the unit parameter

    Parameters
    ----------
    :param file_path: path to csv being parsed
    :param unit: unit of retail_size measurement

    :rtype file_path: string
    :rtype unit: string
    '''

    df = pandas.read_csv(file_path)

    for row in df.iterrows():
        row = row[1]
        recipe = get_recipe(row, unit)

        #branch by whether or not it's a pack and create the pack and/or item as appropriate
        new_item = Item(ampersand_sku = row['SKU'], description = row['Description'],
                            case_quantity = row['Case'], is_active = True)
        new_item.save()
        new_pack = Pack(pack_quantity = row['Pack'], item_recipe = recipe, item = new_item)
        new_pack.save()
