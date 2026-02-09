def generate_partitions():
    elements = [1, 2, 3, 4, 5, 6]
    partitions = []

    def backtrack(current_elements, current_partition):
        if not current_elements:
            partitions.append(current_partition)
            return
        first = current_elements[0]
        remaining = current_elements[1:]
        for i in range(len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            new_partition = current_partiti