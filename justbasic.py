import math

Weight = int(input('Weight: '))
weight_type = input("( P ) for pound and ( K ) for kg ")

if weight_type.upper() == "P":
    final_weight = Weight * 0.45359237
    unit = 'kg'
else:
    final_weight = Weight / 0.45359237
    unit = 'pound'
print(f"{math.floor(final_weight)} {unit}")
