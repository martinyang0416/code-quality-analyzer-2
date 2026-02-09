def maxScoreSightseeingPair(A):
    max_so_far = A[0] + 0  # A[i] + i for i=0
    result = 0
    for j in range(1, len(A)):
        current_score = max_so_far + (A[j] - j)
        if current_score > result:
            result = current_score
        # Update max_so_far for next iterations
        current_i_value = A[j] + j
        if current_i_value > max_so_far:
            max_so_far = current_i_value
    return result