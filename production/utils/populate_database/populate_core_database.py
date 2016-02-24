from production.utils.populate_database import populate_recipe_components, populate_items, populate_coat_cutting_patterns, populate_retail_cutting_patterns
from production.utils import conversions


#populates the core database with recipe components, items, and cutting patterns
populate_recipe_components.populate()
populate_items.from_file('US_master.csv', 'in')
populate_items.from_file('UK_master.csv', 'cm')
populate_coat_cutting_patterns.populate()
populate_retail_cutting_patterns.populate_from("retail_cutting_patterns_15.csv")
populate_retail_cutting_patterns.populate_from("retail_cutting_patterns_18.csv")
populate_retail_cutting_patterns.populate_from("retail_cutting_patterns_25.csv")
populate_retail_cutting_patterns.populate_from("retail_cutting_patterns_32.csv")
populate_retail_cutting_patterns.populate_from("retail_cutting_patterns_39.csv")
