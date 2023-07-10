'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']} '''

# 1st method

'''data = {'1': ['a', 'b'], '2': ['c', 'd']}

keys = list(data.keys())
values = list(data.values())

def generate_combinations(combinations, current_combination, idx):
    if idx == len(keys):
        combinations.append(''.join(current_combination))
        return
    
    for letter in values[idx]:
        current_combination.append(letter)
        generate_combinations(combinations, current_combination, idx + 1)
        current_combination.pop()

combinations = []
generate_combinations(combinations, [], 0)

print("Combinations:")
for combination in combinations:
    print(combination)

'''
# 2nd method

data = {'1': ['a', 'b'], '2': ['c', 'd']}

keys = list(data.keys())
values = list(data.values())

combinations = ['']
for key in keys:
    temp = []
    for comb in combinations:
        for letter in values[keys.index(key)]:
            temp.append(comb + letter)
    combinations = temp

print("Combinations:")
for combination in combinations:
    print(combination)


# 3rd method

'''import itertools

data = {'1': ['a', 'b'], '2': ['c', 'd']}

values = list(data.values())

combinations = list(itertools.product(*values))

print("Combinations:")
for combination in combinations:
    print(''.join(combination))
'''