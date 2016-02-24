#This module is used to aid in formatting of depth/widths and rectangular sizes
from production.utils import conversions

def format_number(number):
    return str(('%f' % number).rstrip('0').rstrip('.'))

def small_measurement(measurement):
    if measurement.unit_of_measurement == 'in':
        return str(conversions.dec_to_frac[measurement.measurement]) + ' in'
    else:
        return str(('%f' % measurement.measurement).rstrip('0').rstrip('.')) + ' ' + measurement.unit_of_measurement

def retail_size(size):
    if size.unit_of_measurement == 'in':
        length = format_number(size.length)
        width = format_number(size.width)
        return width + ' x ' + length + ' in'
    else:
        return format_number(size.width) + ' x ' + format_number(size.length) + ' cm'

def tercero_size(size):
    if size.unit_of_measurement == 'in':
        length = format_number(size.length)
        width = format_number(size.width)
        return width + ' x ' + length + ' in'
    else:
        return format_number(size.width) + ' x ' + format_number(size.length) + ' cm'
