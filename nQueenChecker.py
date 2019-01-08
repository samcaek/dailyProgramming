# N-Queens solution checker...


# Brute force:
def qcheck(row_list):
    if(len(set(row_list)) != len(row_list)): return False # Same Row Check
    
    counter = 0
    for y in row_list[counter:-1]:
        x_dist = list(range(len(row_list[counter:])))
        y_dist = list(map(lambda x:abs(x-y), row_list[counter:]))
        same_diag = list(map(int.__sub__, x_dist[1:], y_dist[1:]))
        
        if 0 in same_diag: return False
        counter += 1
    
    return True    
        



# Test Cases
#qcheck([4, 2, 7, 3, 6, 8, 5, 1]) # => true
#qcheck([2, 5, 7, 4, 1, 8, 6, 3]) # => true
#qcheck([5, 3, 1, 4, 2, 8, 6, 3]) # => false   (b3 and h3 are on the same row)
#qcheck([5, 8, 2, 4, 7, 1, 3, 6]) # => false   (b8 and g3 are on the same diagonal)
#qcheck([4, 3, 1, 8, 1, 3, 5, 2]) # => false   (multiple problems)