from production.models import RetailSize, PanelDepth, CradleDepth, CradleWidth,\
        SprayColor, Coating, Item, Pack, Item, ItemRecipe
from django.db.models import Q
from production.utils import conversions, display
import sys
import pdb


#Displays
#-----------------------------------------------------------------------
class ItemDisplay:
    def __init__(self, sku, description):
        self.sku = sku
        self.description = description

class RecipeDisplay:
    def __init__(self, sku, description, retail_size, panel_depth, cradle_depth, cradle_width, spray_color, coating, case_quantity, pack_quantity):
        self.sku = sku
        self.description = description
        self.retail_size = retail_size
        self.panel_depth = panel_depth
        self.cradle_depth = cradle_depth
        self.cradle_width = cradle_width
        self.spray_color = spray_color
        self.coating = coating
        self.case_quantity = case_quantity
        self.pack_quatity = pack_quantity
#------------------------------------------------------------------------


#Slaves
#------------------------------------------------------------------------
def get_recipe_for_single(item, sku):
    '''
    Description
    -----------
    Gets and returns recipe for items that do not have packs
    '''

    description = item.description
    retail_size = RetailSize.objects.get(itemrecipe__item__id = item.id)
    retail_size = display.retail_size(retail_size)

    panel_depth = PanelDepth.objects.get(itemrecipe__item__id = item.id)
    panel_depth = display.small_measurement(panel_depth)
    case_quantity = item.case_quantity
    try:
        pack_quantity = Pack.objects.get(item__id = item.id).pack_quantity
    except:
        pack_quantity = 1

    try:
        cradle_depth = CradleDepth.objects.get(itemrecipe__item__id = item.id)
        cradle_depth = display.small_measurement(cradle_depth)
        cradle_width = CradleWidth.objects.get(itemrecipe__item__id = item.id)
        cradle_width = display.small_measurement(cradle_width)
    except:
        cradle_width = 'n/a'
        cradle_depth = 'n/a'

    coating = Coating.objects.get(itemrecipe__item__id = item.id).description
    if coating == 'Pastelbord':
        spray_color = SprayColor.objects.get(itemrecipe__item__id = item.id).color
    else:
        spray_color = 'n/a'

    recipe = RecipeDisplay(sku, description, retail_size, panel_depth, cradle_depth, cradle_width, spray_color, coating, case_quantity, pack_quantity)
    return recipe

def get_recipes_for_packs(item, sku):
    '''
    Description
    -----------
    Gets and returns the recipe for a pack whose item is specified by sku
    '''

    description = item.description
    packs = Pack.objects.filter(item__id = item.id)
    recipes = []
    for pack in packs:
        retail_size = RetailSize.objects.get(itemrecipe__pack__item__id = item.id)
        retail_size = display.retail_size(retail_size)

        panel_depth = PanelDepth.objects.get(itemrecipe__pack__item__id = item.id)
        panel_depth = display.small_measurement(panel_depth)
        case_quantity = item.case_quantity
        pack_quantity = Pack.objects.get(item__id = item.id).pack_quantity
        try:
            cradle_depth = CradleDepth.objects.get(itemrecipe__pack__item__id = item.id)
            cradle_width = CradleWidth.objects.get(itemrecipe__pack__item__id = item.id)
            cradle_depth = display.small_measurement(cradle_depth)
            cradle_width = display.small_measurement(cradle_width)
        except:
            cradle_width = 'n/a'
            cradle_depth = 'n/a'

        coating = Coating.objects.get(itemrecipe__pack__item__id = item.id).description
        if coating == 'Pastelbord':
            spray_color = SprayColor.objects.get(itemrecipe__pack__item__id = item.id).color
        else:
            spray_color = 'n/a'

        recipe = RecipeDisplay(sku, description, retail_size, panel_depth, cradle_depth, cradle_width, spray_color, coating, case_quantity, pack_quantity)
        recipes.append(recipe)

    return recipes

def unpack(form):
    '''
    Description
    -----------
    unpacks all of the info from the form so that the items function is not
    so cluttered
    '''

    coatings = form['coatings']
    retail_sizes = form['retail_sizes']
    panel_depths = form['panel_depths']
    cradle_depths = form['cradle_depths']
    cradle_widths = form['cradle_widths']
    spray_colors = form['spray_colors']
    return (coatings, retail_sizes, panel_depths, cradle_depths, cradle_widths,\
            spray_colors)

def create_recipe_strings(recipes):
    recipe_strings = []
    for recipe in recipes:
        retail_size = RetailSize.objects.get(pk = recipe.retail_size_id)
        coating = Coating.objects.get(pk = recipe.coating_id)
        panel_depth = PanelDepth.objects.get(pk = recipe.panel_depth_id)
        recipe_string = display.retail_size(retail_size) + "__" + coating.description + "__" + \
                display(panel_depth)
        if coating.description == 'Pastelbord':
            spray = SprayColor.objects.get(pk = recipe.spray_color_id)
            recipe_string += "__" + spray.color
        if recipe.cradle_depth:
            cradle_depth = CradleDepth.objects.get(pk = recipe.cradle_depth_id)
            cradle_width = CradleWidth.objects.get(pk = recipe.cradle_width_id)
            recipe_string += "__cradle_width__" + display(cradle_width) + \
                    "__cradle_depth__" + display(cradle_depth)
        recipe_strings.append({'id': recipe.id, 'recipe': recipe_string})
    return recipe_strings
#-------------------------------------------------------------------------


#Masters
#-------------------------------------------------------------------------
def create_retail_size(size_dict):
    new_size = RetailSize(length = size_dict['length'], width = size_dict['width'],\
            unit_of_measurement = size_dict['unit'], is_active = True)
    new_size.save()
    return

def create_panel_depth(panel_depth_dict):
    new_panel_depth = PanelDepth(measurement = panel_depth_dict['measurement'],\
            unit_of_measurement = panel_depth_dict['unit_of_measurement'],\
            is_active = True)
    new_panel_depth.save()
    return

def create_cradle_depth(cradle_depth_dict):
    new_cradle_depth = CradleDepth(measurement = cradle_depth_dict['measurement'],\
            unit_of_measurement = cradle_depth_dict['unit_of_measurement'],\
            is_active = True)
    new_cradle_depth.save()
    return

def create_cradle_width(cradle_width_dict):
    new_cradle_width = CradleWidth(measurement = cradle_width_dict['measurement'],\
            unit_of_measurement = cradle_width_dict['unit_of_measurement'],\
            is_active = True)
    new_cradle_width.save()
    return

def create_coating(coating_dict):
    new_coating = Coating(description = coating_dict['description'], is_active = True)
    new_coating.save()
    return

def create_spray(spray_dict):
    new_spray = SprayColor(color = spray_dict['color'], is_active = True)
    new_spray.save()
    return

def retail_sizes(is_active):
    retail_sizes = RetailSize.objects.filter(is_active = is_active).order_by('unit_of_measurement', 'width', 'length')
    return [{'id': size.id, 'width': size.width, 'length': size.length, \
            'unit': size.unit_of_measurement} for size in retail_sizes]

def panel_depths(is_active):
    panel_depths = PanelDepth.objects.filter(is_active = is_active).order_by('unit_of_measurement', 'measurement')
    return [{'id': depth.id, 'measurement': display.small_measurement(depth), \
            'unit': depth.unit_of_measurement} for depth in panel_depths]

def cradle_depths(is_active):
    cradle_depths = CradleDepth.objects.filter(is_active = is_active).order_by('unit_of_measurement', 'measurement')
    return [{'id': depth.id, 'measurement': display.small_measurement(depth), \
            'unit': depth.unit_of_measurement} for depth in cradle_depths]

def cradle_widths(is_active):
    cradle_widths = CradleWidth.objects.filter(is_active = is_active).order_by('unit_of_measurement', 'measurement')
    return [{'id': width.id, 'measurement': display.small_measurement(width), \
            'unit': width.unit_of_measurement} for width in cradle_widths]
def coatings(is_active):
    coatings = Coating.objects.filter(is_active = is_active).order_by('description')
    return [{'id': coating.id, 'description': coating.description} for coating in coatings]

def sprays(is_active):
    sprays = SprayColor.objects.filter(is_active = is_active).order_by('color')
    return [{'id': spray.id, 'color': spray.color} for spray in sprays]

def update_retail_size(size_dict):
    retail_sizes = RetailSize.objects.get(pk = size_dict['id'])
    retail_sizes.width = size_dict['width']
    retail_sizes.length = size_dict['length']
    retail_sizes.unit_of_measurement = size_dict['unit']
    retatil_size.is_active = size_dict['is_active']
    retail_sizes.save()
    return

def update_panel_depth(panel_depth_dict):
    panel_depth = PanelDepth.objects.get(pk = panel_depth_dict['id'])
    panel_depth.measurement = panel_depth_dict['measurement']
    panel_depth.unit_of_measurement = panel_depth_dict['unit_of_measurement']
    panel_depth.is_active = panel_depth_dict['is_active']
    panel_depth.save()
    return

def update_cradle_depth(cradle_depth_dict):
    cradle_depth = CradleDepth.objects.get(pk = cradle_depth_dict['id'])
    cradle_depth.measurement = cradle_depth_dict['measurement']
    cradle_depth.unit_of_measurement = cradle_depth_dict['unit_of_measurement']
    cradle_depth.is_active = cradle_depth_dict['is_active']
    cradle_depth.save()
    return

def update_cradle_width(cradle_width_dict):
    cradle_width = CradleWidth.objects.get(pk = cradle_width_dict['id'])
    cradle_width.measurement = cradle_width_dict['measurement']
    cradle_width.unit_of_measurement = cradle_width_dict['unit_of_measurement']
    cradle_width.is_active = cradle_width_dict['is_active']
    cradle_width.save()
    return

def update_coating(coating_dict):
    coating = Coating.objects.get(pk = coating_dict['id'])
    coating.description = coating_dict['description']
    coating.is_active = coating_dict['is_active']
    coating.save()
    return

def update_spray(spray_dict):
    spray = SprayColor.objects.get(pk = spray_dict['id'])
    spray.color = spray_dict['color']
    spray.is_active = spray_dict['is_active']
    spray.save()
    return

def delete_retail_size(id):
    retail_size = RetailSize.objects.get(pk = id)
    retail_size.is_active = False
    retail_size.save()
    return

def delete_panel_depth(id):
    panel_depth = PanelDepth.objects.get(pk = id)
    panel_depth.is_active = False
    panel_depth.save()
    return

def delete_cradle_depth(id):
    cradle_depth = CradleDepth.objects.get(pk = id)
    cradle_depth.is_active = False
    cradle_depth.save()
    return

def delete_cradle_width(id):
    cradle_width = CradleWidth.objects.get(pk = id)
    cradle_width.is_active = False
    cradle_width.save()
    return

def delete_coating(id):
    coating = Coating.objects.get(pk = id)
    coating.is_active = False
    coating.save()
    return

def delete_spray(id):
    spray = SprayColor.objects.get(pk = id)
    spray.is_active = False
    spray.save()
    return

def create_or_update_recipe(recipe_dict, is_active, recipe_id = -1):
    if recipe_id > 0:
        recipe = ItemRecipe.objects.get(pk = recipe_id)
        recipe.coating_id = recipe_dict['coating']
        recipe.retail_size_id = recipe_dict['retail_size']
        recipe.panel_depth_id = recipe_dict['panel_depth']
        coating = Coating.objects.get(pk = recipe_dict['coating'])
        if coating.description == 'Pastelbord':
            recipe.spray_color__id = recipe_dict['spray_color']
        if 'cradle_depth' in recipe_dict:
            recipe.cradle_depth = recipe_dict['cradle_depth']
            recipe.cradle_width = recipe_dict['cradle_width']
        recipe.is_active = is_active
        recipe.save()
    else:
        coating = Coating.objects.get(pk = recipe_dict['coating'])
        if coating.description == 'Pastelbord':
            recipe = ItemRecipe(retail_size_id = recipe_dict['retail_size'],\
                    coating_id = recipe_dict['coating'],\
                    panel_depth_id = recipe_dict['panel_depth'],\
                    spray_color_id = recipe_dict['spray_color'],
                    is_active = True)
        else:
            if 'cradle_depth' in recipe_dict:
                recipe = ItemRecipe(retail_size_id = recipe_dict['retail_size'],\
                    coating_id = recipe_dict['coating'],\
                    panel_depth_id = recipe_dict['panel_depth'],\
                    cradle_depth_id = recipe_dict['cradle_depth'],\
                    cradle_width_id = recipe_dict['cradle_width'],
                    is_active = True)
            else:
                recipe = ItemRecipe(retail_size_id = recipe_dict['retail_size'],\
                    coating_id = recipe_dict['coating'],\
                    panel_depth_id = recipe_dict['panel_depth'],
                    is_active = True)
        recipe.save()
    return

def recipes(form, is_active):
    coatings, retail_sizes, panel_depths, cradle_depths, cradle_widths,\
            spray_colors = unpack(form)
    recipes = ItemRecipe.objects.filter(**{f: e for f,e in (\
            ('coating__in', coatings),
            ('retail_size__in', retail_sizes),
            ('panel_depth__in', panel_depths),
            ('cradle_depth__in', cradle_depths),
            ('cradle_width__in', cradle_widths),
            ('spray_color__in', spray_colors),
            ('is_active', is_active))
            if e})

    recipe_strings = create_recipe_strings(recipes)
    return recipe_strings

def delete_recipe(recipe_id):
    recipe = ItemRecipe.objects.get(pk = id)
    recipe.is_active = False
    recipe.save()
    return

def items(form, is_active):
    coatings, retail_sizes, panel_depths, cradle_depths, cradle_widths,\
            spray_colors = unpack(form)
    recipes = ItemRecipe.objects.filter(**{f: e for f,e in (\
            ('coating__in', coatings),
            ('retail_size__in', retail_sizes),
            ('panel_depth__in', panel_depths),
            ('cradle_depth__in', cradle_depths),
            ('cradle_width__in', cradle_widths),
            ('spray_color__in', spray_colors),
            ('is_active', is_active))
            if e})
    recipe_ids = [recipe.id for recipe in recipes]
    packs = Pack.objects.filter(item_recipe_id__in = recipe_ids).order_by(item_id)
    items = {}
    for pack in packs:
        item_id = pack.item_id
        if item_id not in items:
            item = Item.objects.get(pk = item_id)
            sku = item.ampersand_sku
            case_quantity = item.case_quantity
            if item.is_active == is_active:
                items[item_id] = {'sku': sku, 'case_quantity': case_quantity, 'packs':[]}
        if item.is_active == is_active:
            items[item_id]['packs'].append({pack.id: {'pack_quantity': pack.pack_quantity}})

def recipe(sku):
    '''
    Description
    -----------
    Returns recipe from a sku

    '''

    item = Item.objects.get(ampersand_sku = sku)
    recipes = get_recipes_for_packs(item, sku)
    return recipes

def recipe_from_id(recipe_id):
    recipe = ItemRecipe.objects.get(pk = recipe_id)
    recipe_dict = {'coating': recipe.coating_id, 'retail_size': recipe.retail_size_id,\
            'panel_depth': recipe.panel_depth_id}
    coating = Coating.objects.get(pk = recipe.coating_id)
    if coating.description == 'Pastelbord':
        recipe_dict['spray_color'] = recipe.spray_color_id
    if recipe.cradle_depth:
        recipe_dict['cradle_depth'] = recipe.cradle_depth_id
        recipe_dict['cradle_width'] = recipe.cradle_width_id
    return recipe_dict

def items(form):
    '''
    Description
    -----------
    Returns sku and description of item from recipe
    ''' 

    coatings, retail_sizes, panel_depths, cradle_depths, cradle_widths,\
            spray_colors = unpack(form)
    item_recipes = ItemRecipe.objects.filter(**{f: e for f,e in (\
            ('coating__in', coatings),
            ('retail_size__in', retail_sizes),
            ('panel_depth__in', panel_depths),
            ('cradle_depth__in', cradle_depths),
            ('cradle_width__in', cradle_widths),
            ('spray_color__in', spray_colors))
            if e})

    packs = Pack.objects.filter(item_recipe__in = item_recipes)
    pack_items = Item.objects.filter(pack__in = packs)

    item_displays = []
    for item in pack_items:
        item_displays.append(ItemDisplay(item.ampersand_sku, item.description))

    return item_displays
#--------------------------------------------------------------------
