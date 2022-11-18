# Given an uppercase English String, like "AKZ", add at most one letter to maximize the occurrences of "AZ" subsequences.
# For example, "AKZ" --> "AKAZ” --> return 2 ( 2 subsequences of "AZ")
# 1. calculate current AZs, from left to right, keep As, add current As when meeting Z
# 2. ret += max(As, Zs)
