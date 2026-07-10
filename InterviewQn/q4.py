def count_frequencies(lst):
    frequency_dict = {}
    
    for element in lst:
        # If element exists, increment it. If not, start at 0 and add 1.
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
        
    return frequency_dict

# Example Usage
numbers = [1, 2, 2, 3, 1, 4, 2]
frequencies = count_frequencies(numbers)

print("Standard Dictionary Method:")
for element, count in frequencies.items():
    print(f"{element} → {count}")