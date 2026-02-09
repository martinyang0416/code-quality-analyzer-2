import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def are_colinear_and_share_endpoint(seg1, seg2):
    points1 = seg1
    points2 = seg2

    common = None
    for p1 in points1:
        for p2 in points2:
            if p1 == p2:
                common = p1
                break
        if common is not None:
            break

    if common is None:
        return None  # No common endpoint

    # Now, check if other points are colinear
    # Get the other po