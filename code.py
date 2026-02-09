import sys

def main():
    def generate_pairings(elements):
        if not elements:
            yield []
            return
        first = elements[0]
        for i in range(1, len(elements)):
            pair = (first, elements[i])
            remaining = elements[1:i] + elements[i+1:]
            for sub in generate_pairings(remaining):
                yield [pair] + sub

    all_elements = [1, 2, 3, 4, 5, 6]
    all_pairings = list(generate_pairings(all_elements))  # Precompute all possibl