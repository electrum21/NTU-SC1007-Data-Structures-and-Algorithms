def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1   # skip duplicates
                while left < right and nums[right] == nums[right-1]:
                    right -= 1  # skip duplicates
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 0, 0]))              # [[0, 0, 0]]
print(three_sum([1, 2, 3]))              # []


def three_sum(nums):
    # result = set()

    # for i in range(len(nums)):
    #     seen = set()
    #     for j in range(i + 1, len(nums)):
    #         complement = -(nums[i] + nums[j])  # need this to sum to 0
    #         if complement in seen:
    #             triplet = tuple(sorted([nums[i], nums[j], complement]))
    #             result.add(triplet)  # set avoids duplicate triplets
    #         seen.add(nums[j])

    # return [list(t) for t in result]




    result = set()

    for i in range(len(nums)):
        seen = set()
        for j in range(i+1, len(nums)):
            complement = -(nums[i] + nums[j])
            if complement in seen:
                result.add(tuple(sorted([nums[i], nums[j], complement])))
            seen.add(complement)

    return [list(t) for t in result]






print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 0, 0]))              # [[0, 0, 0]]
print(three_sum([1, 2, 3]))              # []