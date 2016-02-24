from production.models import RetailCuttingPattern, RetailCuttingPatternOutput, RetailSize, CoatingSize
import pandas
import math
import production.utils.display
import sys


def get_data_from_file(filename):
    ''' parses the retail cut file '''
    df = pandas.read_csv(filename)

    coating_sizes = []
    grades = []
    centered = []
    instructions = []
    cradled = []
    boards = []
    for index, row in df.iterrows():
        # for linking the cutting pattern to a tercero
        try:
            new_size = CoatingSize.objects.get(length = row.TerceroLength, width = row.TerceroWidth)
        except CoatingSize.DoesNotExist:
            new_size = CoatingSize(length = row.TerceroLength, width = row.TerceroWidth, unit_of_measurement = 'in')
            new_size.save()

        coating_sizes.append(new_size)
        # getting grade, cutting instructions, and retail cuts
        grades.append(str(row.Grade))
        instructions.append(row.CuttingInstruction)
        cradled.append(row.Cradled)
        boards.append([])
        # iterating over the retail cut columns to save retail cuts
        board_columns = row.iloc[5:]
        column_number = 0
        for index, column in board_columns.iteritems():
            if type(column) == float and math.isnan(column):
                break

            if column_number%5 == 0:
                is_cradled = True if column == 1 else False
            elif column_number%5 == 1:
                quantity = column
            elif column_number%5 == 2:
                length = column
            elif column_number%5 == 3:
                width = column
            else:
                units = column
            column_number += 1

            # this saves the retail cut since column_number%5 == 0 at the end of a cycle
            if column_number%5 == 0:
                boards[-1].append([is_cradled, quantity, length, width, units])

    return (coating_sizes, grades, instructions, cradled, boards)

def populate_from(filename):
    ''' saves the cutting pattern to the Ampersand database'''
    coating_sizes, grades, instructions, cradled, boards = get_data_from_file(filename)

    for index, instruction in enumerate(instructions):
        new_retail_cutting_pattern = RetailCuttingPattern(cutting_instructions = instruction, grade = grades[index], coating_size = coating_sizes[index], is_active = True)
        new_retail_cutting_pattern.save()

        # is_primary is used to label the very first retail cut as primary and all else as secondary
        is_primary = True
        # save both cutting pattern and cutting pattern outputs
        # note that a new retail size is created here if it doesn't already exist
        for board in boards[index]:
            retail_size = RetailSize.objects.filter(length = max(board[2], board[3]), width = min(board[2], board[3]), unit_of_measurement = board[4])
            if retail_size:
                new_retail_cutting_pattern_output = RetailCuttingPatternOutput(quantity = board[1], retail_cutting_pattern = new_retail_cutting_pattern, retail_size = retail_size[0], is_primary = is_primary, is_for_cradle = board[0])
            else:
                new_retail_size = RetailSize(length = max(board[2], board[3]), width = min(board[2], board[3]), unit_of_measurement = board[4], is_active = True)
                RetailSize.save(new_retail_size)
                new_retail_cutting_pattern_output = RetailCuttingPatternOutput(quantity = board[1], retail_cutting_pattern = new_retail_cutting_pattern, retail_size = new_retail_size, is_primary = is_primary, is_for_cradle = board[0])

            new_retail_cutting_pattern_output.save()
            is_primary = False
