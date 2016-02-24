#This script will populate the different recipe components for us.
#Note that, since this is a script, Django does not choose update or save new
#  for us; it simply tries to save new and gets and error if it tries to save
#  a duplicate

import pandas
from production.models import RetailSize, Coating, PanelDepth, CradleWidth, CradleDepth, SprayColor, CoatingSize
import math
import pdb


def populate():
    df = pandas.read_csv('recipe_component_data.csv')

    for index, dimension in enumerate(df.length.values):
        new_retail_size = RetailSize(length = dimension, width = df.width[index],
                                     unit_of_measurement = df.unit[index], is_active = True)
        new_retail_size.save()

    for index, depth in enumerate(df.panel_depth.values):
        if pandas.isnull(depth):
            break
        new_panel_depth = PanelDepth(measurement = depth, unit_of_measurement = df.
                                     panel_depth_unit[index], is_active = True)
        new_panel_depth.save()

    for index, depth in enumerate(df.cradle_depth.values):
        if pandas.isnull(depth):
            break
        new_cradle_depth = CradleDepth(measurement = depth, unit_of_measurement = df.
                                       cradle_depth_unit[index], is_active = True)
        new_cradle_depth.save()

    for index, width in enumerate(df.cradle_width.values):
        if pandas.isnull(width):
            break
        new_cradle_width = CradleWidth(measurement = width, unit_of_measurement = df.
                                       cradle_width_unit[index], is_active = True)
        new_cradle_width.save()

    for index, width in enumerate(df.coating_width.values):
        if pandas.isnull(width):
            break
        new_coating_width = CoatingSize(length = df.coating_length[index], width = width,
                                        unit_of_measurement = df.coating_unit[index])
        new_coating_width.save()

    for spray_color in df.spray_color.values:
        if pandas.isnull(spray_color):
            break
        new_spray_color = SprayColor(color = spray_color, is_active = True)
        new_spray_color.save()

    for coating in df.coating.values:
        if pandas.isnull(coating):
            break
        new_coating = Coating(description = coating, is_active = True)
        new_coating.save()

