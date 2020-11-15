import pandas as pd

# This open modal specifications for models of bloom, viscosity and yield
modal_specs = pd.read_excel('./knowledge_module/modal_specs/modal_specs.xlsx')
modal_specs['placeholder'] = modal_specs['placeholder'].map(lambda x: round(x, 3))
modal_specs['value'] = modal_specs['value'].map(lambda x: round(x, 3))
#print(modal_specs)