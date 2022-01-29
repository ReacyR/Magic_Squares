import numpy as np


def magic_square_tester(mgc_sqr, target_value):

    """
    Given an array that is a solved magic square & a target value, return a dictionary with the keys being
    the rows, coloumns, & diagonals and the values being a bool of the sum of that row, column, or diagonal
    compared to the target value.

    If your solution returns any False values, uncomment the corresponding print statement and re-run to see
    the sum of the diagonals, columns, or rows to help track down where your answer went wrong.
    """

    solution_dict = {}
    angles = ['Top Left Diagonal', 'Bottom Left Diagonal'] #this list will be the keys of the solution dictionary

    #traverse the diagonals of the array and get the sum of all numbers there-in and compare that sum to the target value
    top_left_diag = sum([mgc_sqr[n][n] for n in range(len(mgc_sqr))]) == target_value
    #print(f'Top left diagonal sum: {sum([mgc_sqr[n][n] for n in range(len(mgc_sqr))])}')
    
    bottom_left_diag = sum([mgc_sqr[x][len(mgc_sqr)-x-1] for x in range(len(mgc_sqr))]) == target_value
    #print(f'Bottom left diagonal sum: {sum([mgc_sqr[x][len(mgc_sqr)-x-1] for x in range(len(mgc_sqr))])}')

    #this list of the bools of the sums compared to the target value will be the values of the solution dictionary
    array_bools = [top_left_diag, bottom_left_diag]

    columns = [mgc_sqr[:, n] for n in range(len(mgc_sqr))] #list of all the columns in the array

    for r in range(len(mgc_sqr)): #add a row to the angles list for each row in the magic square
        angles.append(f'Row-{r}')

    for c in range(len(mgc_sqr)): #add a column to the angles list for each column in the magic square
        angles.append(f'Col-{c}')

    for n in range(len(mgc_sqr)): #sum and compare each row to the target value
        row = sum(mgc_sqr[n]) == target_value
        #print(f'Row-{n} sum: {sum(mgc_sqr[n])}')  
        array_bools.append(row)

    for cols in range(len(mgc_sqr)): #sum and compare each column to the target value
        col = sum(columns[cols]) == target_value
        #print(f'Col-{cols} sum: {sum(columns[cols])}')  
        array_bools.append(col)

    for i in range(len(array_bools)): #build solution dictionary from the angles and array_bools lists
        solution_dict[angles[i]] = array_bools[i]

    print(mgc_sqr)

    return print(solution_dict)


t_sqr_1 = [[16, 3, 2, 13],
           [5, 10, 11, 8],
           [9, 6, 7, 12],
           [4, 15, 14, 1]] #target is 34

t_sqr_2 = [[2, 7, 12, 13], [16, 9, 6, 3], [5, 6, 15, 10], [11, 14, 1, 8]] #target is 34 (returns a few False values)

t_sqr_3 = [[28, 9, 19, 94],
           [95, 18, 6, 31],
           [7, 30, 96, 17],
           [20, 95, 27, 8]] #target is 150 (returns a couple False values)

t_sqr_4 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]] #target is 15

test_square_1 = np.array(t_sqr_1)
test_square_2 = np.array(t_sqr_2)
test_square_3 = np.array(t_sqr_3)
test_square_4 = np.array(t_sqr_4)


magic_square_tester(test_square_1, 34)
