'''Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]'''

#------------ 1st method --------------

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = {}
for d in data:
    item = d['item']
    amount = d.get('amount')
    combined_values[item] = combined_values.get(item, 0) + amount

print("Combined values:", combined_values)




#------------ 2nd method -----------------

"""def combine_values(dictionaries, key):
    combined_dict = {}
    for d in dictionaries:
        item = d[key]
        amount = d.get('amount', 0)
        combined_dict[item] = combined_dict.get(item, 0) + amount
    return combined_dict


data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


combined_values = combine_values(data, 'item')
print("Combined values:", combined_values)"""
