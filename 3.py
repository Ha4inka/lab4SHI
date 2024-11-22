import numpy as np
def elements_by_indices(array, indices):
    return array[indices]

array = np.array([10, 20, 30, 40, 50])
indices = [1, 3]
selected_elements = elements_by_indices(array, indices)
print(selected_elements)

def elements_by_condition(array, value, condition="greater"):
    if condition == "greater":
        return array[array > value]
    elif condition == "less":
        return array[array < value]

value = 25
greater_elements = elements_by_condition(array, value, "greater")
less_elements = elements_by_condition(array, value, "less")
print("Більші:", greater_elements)
print("Менші:", less_elements)
