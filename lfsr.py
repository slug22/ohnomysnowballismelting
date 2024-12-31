import math
import random
#assuming dice
dice_sides = 60
dice_rolled = 3

max_sum = (dice_sides * dice_rolled) + 1 
def print_radial_histogram(countmap, radius=15):
    # Create a grid 
    grid_size = radius * 4
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    center = grid_size // 2
    isdone = True
    num_points = 110  # doubled from 55
    
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        orig_idx = (i * max_sum) // num_points
        if orig_idx >= max_sum:
            continue
            
        length = min(round(countmap[orig_idx] / 10), radius)
        
        for r in range(length * 2):
            # Adjust x,y calculation for better circle shape
            x = center + round(math.cos(angle) * r * 0.5)
            y = center + round(math.sin(angle) * r * 0.25)              
            if 0 <= x < grid_size and 0 <= y < grid_size:
                grid[y][x] = '+'
                isdone = False
    
    for row in grid:
        if any(c != ' ' for c in row):
            print(''.join(row).rstrip())
    print("\n") 
    if isdone == True:
        
        return isdone


# generate data
for melting in range(100):
    countmap = {i: 0 for i in range(max_sum)}
    for _ in range(10000):
        yuh = 0
        for _ in range(dice_rolled):
            yuh += random.randint(0, dice_sides)
        
        
        
        if yuh > 0 and yuh < max_sum:
            countmap[yuh] += 1
            countmap[yuh] -= melting/100
        
    print_radial_histogram(countmap)
        