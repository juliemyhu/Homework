
from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melons, attributes in melons.items():
    	print (melons)
    	for attribute, value in attributes.items():
    		print (f'{attribute}: {value}')
	# for i in melon_names:
   		# print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
print_melon(melons)