import itertools

class Solution:
    def brute_force_tsp(self, distance_matrices):
        """
        Finds the shortest route for a drone starting and ending at index 0.
        :param distance_matrix: 2D list where distance_matrix[i][j] is distance from i to j.
        :return: [min_distance, best_route]
        """
        # results = []

        # for distance_matrix in distance_matrices:
        #     n = len(distance_matrix)
        #     locations = list(range(n))
        #     min_distance = float('inf')
        #     best_route = None

        #     for perm in itertools.permutations(locations[1:]): # e.g. permutations('ABC') yields ABC, ACB, BAC, BCA, CAB, CBA.
        #         route = [0] + list(perm) + [0]
        #         total_distance = 0
        #         for i in range(len(route) - 1):
        #             total_distance += distance_matrix[route[i]][route[i + 1]]
        #         if total_distance < min_distance:
        #             min_distance = total_distance
        #             best_route = route

        #     results.append([min_distance, best_route])

        results = []

        for distance_matrix in distance_matrices:
            n = len(distance_matrix)
            locations = list(range(n))
            min_distance = float('inf')
            best_route = None

            for perm in itertools.permutations(locations[1:]):
                route = [0] + list(perm) + [0]
                total_distance = 0
                for i in range(len(route) - 1):
                    total_distance += distance_matrix[route[i]][route[i+1]]
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_route = route
        
            results.append([min_distance, best_route])

        return results

# Initialize your solution
sol = Solution()

test_matrices = [
    # Case 1: 3 nodes (Equilateral)
    [
        [0, 10, 10],
        [10, 0, 10],
        [10, 10, 0]
    ],
    # Case 2: 4 nodes (Symmetric Diamond)
    [
        [0, 10, 15, 20],
        [10, 0, 35, 15],
        [15, 35, 0, 10],
        [20, 15, 10, 0]
    ],
    # Case 3: 4 nodes (Asymmetric)
    [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
]

results = sol.brute_force_tsp(test_matrices)

for i, (dist, route) in enumerate(results):
    print(f"Test Case {i+1}:")
    print(f"  Shortest Distance: {dist}")
    print(f"  Best Route: {route}\n")