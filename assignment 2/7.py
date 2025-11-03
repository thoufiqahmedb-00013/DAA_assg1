import math

def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def brute(points):
    min_val = float('inf')
    closest = (None, None)
    size = len(points)
    for i in range(size):
        for j in range(i + 1, size):
            dist = euclidean(points[i], points[j])
            if dist < min_val:
                min_val = dist
                closest = (points[i], points[j])
    return min_val, closest

def strip_min(strip, limit):
    min_val = limit
    closest = (None, None)
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_val:
                dist = euclidean(strip[i], strip[j])
                if dist < min_val:
                    min_val = dist
                    closest = (strip[i], strip[j])
            else:
                break
    return min_val, closest

def find_closest(data):
    size = len(data)
    if size <= 3:
        return brute(data)

    mid = size // 2
    mid_pt = data[mid]

    left_dist, left_pair = find_closest(data[:mid])
    right_dist, right_pair = find_closest(data[mid:])

    if left_dist < right_dist:
        min_val = left_dist
        closest = left_pair
    else:
        min_val = right_dist
        closest = right_pair

    strip = [pt for pt in data if abs(pt[0] - mid_pt[0]) < min_val]
    strip_dist, strip_pair = strip_min(strip, min_val)

    if strip_dist < min_val:
        return strip_dist, strip_pair
    else:
        return min_val, closest

if __name__ == "__main__":
    coords = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (7, 2), (20, 25)]
    coords.sort(key=lambda x: x[0])
    result_dist, result_pair = find_closest(coords)
    print(f"Closest Pair: {result_pair}")
    print(f"Minimum Distance: {result_dist:.3f}")