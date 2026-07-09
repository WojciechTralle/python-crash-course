# exercise 8-15
# solution with importing specific function from the module
from printing_functions import print_models, show_completed_models


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
