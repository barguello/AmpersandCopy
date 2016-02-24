from production.models import PanelDepth, CoatCuttingPattern, CoatCuttingPatternOutput, CoatingSize
import math
import pandas


def get_data_from_file():
    df = pandas.read_csv('coating_cutting_patterns.csv')

    instructions = []
    panel_depths = []
    description = []
    boards = []
    panel_depth_unit = []
    for index, row in df.iterrows():
        instructions.append(row.CuttingInstructions)
        panel_depths.append(row.PanelDepth)
        panel_depth_unit.append(row.PanelUnit)
        boards.append([])
        board_columns = row.iloc[5:]
        column_number = 0
        for index, column in board_columns.iteritems():
            if type(column) == float and math.isnan(column):
                break

            if column_number%4 == 0:
                quantity = column
            elif column_number%4 == 1:
                width = column
            elif column_number%4 == 2:
                length = column
            else:
                units = column
            column_number += 1

            if column_number%4 == 0:
                boards[-1].append([quantity, length, width, units])

    return (instructions, panel_depths,  panel_depth_unit, boards)

def populate():
    instructions, panel_depths, panel_units, boards = get_data_from_file()
    for index, instruction in enumerate(instructions):
        panel_depth = PanelDepth.objects.get(measurement = panel_depths[index], unit_of_measurement = panel_units[index])

        new_pattern = CoatCuttingPattern(cutting_instructions = instruction, panel_depth = panel_depth)
        new_pattern.save()

        for board in boards[index]:
            try:
                new_size = CoatingSize.objects.get(length = board[1], width = board[2], unit_of_measurement = board[3])
            except:
                new_size = CoatingSize(length = board[1], width = board[2], unit_of_measurement = board[3])
                new_size.save()

            new_output = CoatCuttingPatternOutput(quantity = board[0], coating_size = new_size, coat_cutting_pattern = new_pattern)
            new_output.save()
