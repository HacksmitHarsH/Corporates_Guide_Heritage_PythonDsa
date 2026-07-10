def remove_duplicates_manual(input_list):
    seen = set()
    result = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# --- Example Usage ---
input_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Output: {remove_duplicates_manual(input_list)}")