nums1 = []
middle_index = len(nums1) // 2

if len(nums1) % 2 != 0:
    middle_index += 1

part1 = nums1[:middle_index]
part2 = nums1[middle_index:]

result = [part1, part2]
print(result)

nums2 = [1]
middle_index = len(nums2) // 2

if len(nums2) % 2 != 0:
    middle_index += 1

part1 = nums2[:middle_index]
part2 = nums2[middle_index:]

result = [part1, part2]
print(result)

nums3 = [1,2,3]
middle_index = len(nums3) // 2

if len(nums3) % 2 != 0:
    middle_index += 1

part1 = nums3[:middle_index]
part2 = nums3[middle_index:]

result = [part1, part2]
print(result)

nums4 = [1,2,3,4]
middle_index = len(nums4) // 2

if len(nums4) % 2 != 0:
    middle_index += 1

part1 = nums4[:middle_index]
part2 = nums4[middle_index:]

result = [part1, part2]
print(result)