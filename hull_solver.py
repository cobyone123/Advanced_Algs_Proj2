from hull import hull


def solve_hull(points):
    left_points = len(points) // 2
    left_half = points[:left_points]
    right_half = points[left_points:]

    if len(left_half) == 1:
        return hull(points)

    # use common_tangent as merge function
    retHull = common_tangent(hull(left_half), hull(right_half))
    return retHull


def common_tangent(left, right):
    leftNext = left.get_right_most()
    rightNext = 0

    # Corners used for combining hulls
    UL = 0
    UR = 0
    LL = 0
    LR = 0

    # Find Upper Tangent, go clockwise on right hull, counterclockwise on left hull
    while True:
        while slope(left.points[leftNext], right.points[(rightNext + 1) % len(right.points)]) > slope(
                left.points[leftNext], right.points[rightNext]):
            rightNext = (rightNext + 1) % len(right.points)
            UR += 1
        while slope(left.points[leftNext], right.points[rightNext]) > slope(
                left.points[(leftNext - 1) % len(left.points)], right.points[(rightNext)]):
            leftNext = (leftNext - 1) % len(left.points)
            UL += 1

            # If neither of the slopes match
        if slope(left.points[leftNext], right.points[(rightNext + 1) % len(right.points)]) < slope(
                left.points[leftNext], right.points[rightNext]) and slope(left.points[leftNext],
                                                                          right.points[rightNext]) < slope(
            left.points[(leftNext - 1) % len(left.points)], right.points[(rightNext)]):
            break
        UL = leftNext
        UR = rightNext

    print("top corners:", UL, UR)

    rightNext = 0
    leftNext = left.get_right_most()

    # Find Upper Tangent, go clockwise on left hull, counterclockwise on right hull
    # Modulo for iterating around hull
    while True:
        while slope(left.points[leftNext], right.points[rightNext]) > slope(left.points[leftNext], right.points[
            (rightNext - 1) % len(right.points)]):
            rightNext = (rightNext - 1) % len(right.points)
            LR += 1
        while slope(left.points[leftNext], right.points[rightNext]) < slope(
                left.points[(leftNext + 1) % len(left.points)], right.points[rightNext]):
            leftNext = (leftNext + 1) % len(left.points)
            LL += 1

            # If neither of the slopes match
        if slope(left.points[leftNext], right.points[rightNext]) > slope(left.points[(leftNext + 1) % len(left.points)],
                                                                         right.points[rightNext]) and slope(
            left.points[leftNext], right.points[rightNext]) < slope(left.points[leftNext], right.points[
            (rightNext - 1) % len(right.points)]):
            break
    LL = leftNext
    LR = rightNext

    retPoints = []

    # Append to returning Hull in clockwise order
    for points in left.points[UL:]:
        retPoints.append(points)
    for points in right.points[UR:LR]:
        retPoints.append(points)
    for points in right.points[LL:]:
        retPoints.append(points)
    return hull(retPoints)


def slope(p1, p2):
    return (p1.y() - p2.y()) / (p1.x() - p2.x())
