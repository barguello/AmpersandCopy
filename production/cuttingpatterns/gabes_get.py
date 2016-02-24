from production.models import RetailSize, RetailCuttingPatternOutput, RetailCuttingPattern, RetailCuttingSheet, RetailCuttingSheetEntry, RetailCuttingSheetInstruction, Coating, PanelDepth, RetailCutWip
from production.utils.get import recipe_component
from production.utils import display
import math
import datetime
from production.utils import conversions


class CuttingPatternsDisplay:
    def __init__(self, outputs, cutting_pattern_id, cuttingPatternInstructions, 
                 numberOfCoatingBoardsNeeded):
        self.outputs = outputs
        self.cutting_pattern_id = cutting_pattern_id
        self.cuttingPatternInstructions = cuttingPatternInstructions
        self.numberOfCoatingBoardsNeeded = numberOfCoatingBoardsNeeded

class OutputDisplay:
    def __init__(self, retailSize, retailSizeId, quantity, isCradled):
        self.retailSize = retailSize
        self.retailSizeId = retailSizeId
        self.quantity = quantity
        self.isCradled = isCradled

class RetailCuttingSheetDisplay:
    def __init__(self, sheetId, entries):
        self.sheetId = sheetId
        self.entries = entries

class RetailCuttingSheetEntryDisplay:
    def __init__(self, entry_id, instructions, coating, coating_id, panel_depth, panel_depth_id, is_cradled):
        self.entry_id = entry_id
        self.instructions = instructions
        self.coating = coating
        self.coating_id = coating_id
        self.panel_depth = panel_depth
        self.panel_depth_id = panel_depth_id
        self.is_cradled = is_cradled

class RetailCuttingSheetInstructionDisplay:
    def __init__(self, quantity, output, instruction):
        self.quantity = quantity
        self.output = output
        self.instruction = instruction

class RetailCuttingSheetSummaryDisplay:
    def __init__(self, requiredTerceros, outputTotals):
        self.requiredTerceros = requiredTerceros
        self.outputTotals = outputTotals

class CuttingSheetTercroRequired:
    def __init__(self, tercero, grade, quantity):
        self.tercero = tercero
        self.grade = grade
        self.quantity = quantity

class CuttingSheetOutputQuantity:
    def __init__(self, retailSize, isCradled, quantity):
        self.retailSize = retailSize
        self.isCradled = isCradled
        self.quantity = quantity

def cutting_patterns(isForCradle, retailSizeId, desiredQuantity):
    '''
    Description
    -----------
    Returns all cutting patterns that have the retail size specified by
    retailSizeId in them.  isForCradle and desiredQuantity just go along for 
    the ride so that they are persisted into WIP
    '''

    #get all desired cutting pattern outputs
    cutting_pattern_outputs = RetailCuttingPatternOutput.objects.\
            filter(retail_size_id = retailSizeId,\
            retail_cutting_pattern__is_for_cradle = conversions.bool_map[isForCradle])

    primary_cuts = []
    secondary_cuts = []
    for output in cutting_pattern_outputs:
        quantity = output.quantity
        #get the outputs for the current output's cutting pattern and create \
        #display for family
        output_family = RetailCuttingPatternOutput.objects.\
                        filter(retail_cutting_pattern_id = \
                        output.retail_cutting_pattern.id)
        output_displays = [OutputDisplay(display.retail_size(\
                           sibling.retail_size), sibling.retail_size.id, sibling.quantity, 'flat')\
                           for sibling in output_family]
        if output.is_primary:
            primary_cuts.append(CuttingPatternsDisplay\
                    (output_displays, output.retail_cutting_pattern.id,
                    output.retail_cutting_pattern.
                    cutting_instructions, math.ceil(int(desiredQuantity)/quantity)))
        else:
            secondary_cuts.append(CuttingPatternsDisplay(\
                    output_displays, output.retail_cutting_pattern.id,
                    output.retail_cutting_pattern.\
                    cutting_instructions, math.ceil(int(desiredQuantity)/quantity)))
    return primary_cuts + secondary_cuts

def new_sheet():
    '''
    Description
    -----------
    creates a new retail cutting sheet and returns the id
    '''

    current_datetime = datetime.datetime.now()
    new_sheet = RetailCuttingSheet(created = current_datetime)
    new_sheet.save()
    return new_sheet.id

def get_current_sheet_summary():
    '''
    Description
    -----------
    Returns an object containing the summary info of the required terceros
    and cumulative outputs of the most recent sheet
    '''
    terceroReqA = CuttingSheetTercroRequired("25", "48", 4)
    terceroReqB = CuttingSheetTercroRequired("25", "40", 2)
    outputQuantityA = CuttingSheetOutputQuantity("10x10", "flat", 25)
    outputQuantityB = CuttingSheetOutputQuantity("10x8", "flat", 10)
    outputQuantityC = CuttingSheetOutputQuantity("16x20", "cradled", 8)
    outputQuantityD = CuttingSheetOutputQuantity("12x12", "flat", 4)
    outputQuantityE = CuttingSheetOutputQuantity("8x8", "flat", 2)
    terceros = []
    outputs = []
    terceros.append(terceroReqA)
    terceros.append(terceroReqB)
    outputs.append(outputQuantityA)
    outputs.append(outputQuantityB)
    outputs.append(outputQuantityC)
    outputs.append(outputQuantityD)
    outputs.append(outputQuantityE)

    return RetailCuttingSheetSummaryDisplay(terceros, outputs)

def get_current_sheet():
    '''
    Description
    -----------
    Returns the latest cutting sheet along with all of its information.
    If none exists, a new cutting sheet is created
    '''

    latestSheet = RetailCuttingSheet.objects.first()
    if (not latestSheet):
        new_sheet()

    latestSheet = RetailCuttingSheet.objects.order_by('-id')[0]

    entries = RetailCuttingSheetEntry.objects.filter(retail_cutting_sheet__id  = latestSheet.id)

    entry_list = []
    for entry in entries:
        instructions = RetailCuttingSheetInstruction.objects.filter(retail_cutting_sheet_entry__id = entry.id)
        instruction_list = []
        for instruction in instructions:
            new_instruction = RetailCuttingSheetInstructionDisplay(instruction.quantity,
                instruction.output_string,
                RetailCuttingPattern.objects.filter(id = instruction.retail_cutting_pattern_id)[0].cutting_instructions,
                )
            instruction_list.append(new_instruction)
        new_entry_display = RetailCuttingSheetEntryDisplay(entry.id, instruction_list,
                entry.coating.description, entry.coating.id,
                display.small_measurement(entry.panel_depth),
                entry.panel_depth_id, entry.is_cradled)
        entry_list.append(new_entry_display)

    return RetailCuttingSheetDisplay(latestSheet.id, entry_list)

def add_to_sheet(cutting_sheet_id, coating_id, panel_depth_id, is_cradled, instructions):
    '''
    Description
    -----------
    Adds the entries to the database and sends back all current entries for
    cutting_sheet_id
    '''

    current_datetime = datetime.datetime.now()

    new_entry = RetailCuttingSheetEntry(created = current_datetime,
                                        coating_id = coating_id,
                                        panel_depth_id = panel_depth_id,
                                        is_cradled = is_cradled,
                                        retail_cutting_sheet_id = cutting_sheet_id)
    new_entry.save()
    for instruction in instructions:
        new_sheet_instruction = RetailCuttingSheetInstruction(output_string = instruction.output,
        quantity = instruction.quantity,
        retail_cutting_sheet_entry_id = new_entry.id,
        retail_cutting_pattern_id = instruction.retail_cutting_pattern_id,)
        new_sheet_instruction.save()

    entry_list = get_current_sheet()
    return entry_list

def save_sheet():
    '''
    Description
    -----------
    Saves the most recently-saved retail cutting sheet into retail cut WIP
    To be used in the Cutting Patterns page once a cutting sheet has been
    finalized
    '''

    sheet = get_current_sheet()
    sheet_id = sheet.sheetId
    entries = sheet.entries
    wip = []
    for entry in entries:
        coating_id = entry.coating_id
        is_cradled = entry.is_cradled
        panel_depth_id = entry.panel_depth_id
        current_date_time = datetime.datetime.now()
        wip_type = 'daily'
        instructions = RetailCuttingSheetInstruction.objects.filter(retail_cutting_sheet_entry_id = entry.entry_id)
        for instruction in instructions:
            quantity = instruction.quantity
            retail_cutting_pattern = RetailCuttingPattern.objects.filter(retailcuttingsheetinstruction = instruction.id)
            outputs = RetailCuttingPatternOutput.objects.filter(retail_cutting_pattern = retail_cutting_pattern)
            for output in outputs:
                total_quantity = quantity*output.quantity
                retail_size = RetailSize.objects.get(pk = output.retail_size_id)
                new_wip_entry = RetailCutWip(date_time = current_date_time, quantity = total_quantity, is_cradled = is_cradled, coating_id = coating_id, retail_size_id = retail_size.id, panel_depth_id = panel_depth_id, type = wip_type, retail_cutting_sheet_id = sheet_id)
                new_wip_entry.save()
