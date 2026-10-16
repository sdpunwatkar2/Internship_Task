from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates,
    missing_number,
    two_sum_first_pair,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_sum,
    all_unique_pairs,
)

# Each question is tested with the example from the task and an additional case.

print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 additional:", word_frequency("red blue red"))

print("Q2:", character_frequency("banana"))
print("Q2 additional:", character_frequency("hello"))

print("Q3:", first_non_repeating_character("swiss"))
print("Q3 additional:", first_non_repeating_character("aabb"))

print("Q4:", are_anagrams("listen", "silent"))
print("Q4 additional:", are_anagrams("hello", "world"))

print("Q5:", first_repeating_character("programming"))
print("Q5 additional:", first_repeating_character("abc"))

print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 additional:", move_zeros_to_end([0, 0, 5, 6]))

print("Q7:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q7 additional:", second_highest_distinct([8, 8, 8]))

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 additional:", remove_duplicates([1, 1, 2, 3, 2]))

print("Q9:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 additional:", missing_number([1, 3, 4], 4))

print("Q10:", two_sum_first_pair([2, 7, 11, 15], 9))
print("Q10 additional:", two_sum_first_pair([1, 2, 3], 10))

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 additional:", closest_to_zero([-4, 4, 7]))

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 additional:", common_elements([2, 2, 3, 1], [1, 2]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 additional:", rotate_right([1, 2, 3], 5))

print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 additional:", max_consecutive_sum([-5, -2, -7]))

print("Q15:", all_unique_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 additional:", all_unique_pairs([1, 2, 3, 4], 20))
