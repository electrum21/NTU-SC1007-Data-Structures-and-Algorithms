import itertools

def brute_force_knapsack(weights, values, W):
    n = len(weights)
    max_value = 0
    best_combination = (0,) * n # Creates (0, 0, 0, 0) for 4 items

    for combination in itertools.product([0,1], repeat=n): # The code sees n=4 items. 
        # itertools.product([0,1], repeat=4) creates a list of every possible way to pick or leave these items. 
        # There are 2^4 = 16$ total combinations.
        total_weight = sum(weights[i] for i in range(n) if combination[i] == 1)
        total_value = sum(values[i] for i in range(n) if combination[i] == 1)

        if total_weight <= W and total_value > max_value:
            max_value = total_value
            best_combination = combination
    
    selected_items = [(weights[i], values[i]) for i in range(n) if best_combination[i] == 1]
    total_selected_weight = sum(item[0] for item in selected_items)

    return max_value, selected_items, total_selected_weight


# --- Test Cases ---

def run_tests():
    test_cases = [
        {
            "name": "Example from prompt",
            "W": 50,
            "weights": [10, 20, 30, 5, 15],
            "values": [60, 100, 120, 30, 80]
        },
        {
            "name": "Limited Capacity (Small W)",
            "W": 10,
            "weights": [5, 4, 6, 3],
            "values": [10, 40, 30, 50]
        },
        {
            "name": "All items fit",
            "W": 100,
            "weights": [10, 20],
            "values": [100, 200]
        },
        {
            "name": "No items fit",
            "W": 5,
            "weights": [10, 20],
            "values": [100, 200]
        }
    ]

    for case in test_cases:
        res = brute_force_knapsack(case["weights"], case["values"], case["W"])
        print(f"--- {case['name']} ---")
        print(f"Max Value: {res[0]}")
        print(f"Selected (w, v): {res[1]}")
        print(f"Total Weight: {res[2]}\n")

run_tests()