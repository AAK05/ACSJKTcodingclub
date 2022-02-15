def circle_area(radius):
    from mpmath import mp
    mp.dps = 10
    pi = float(mp.pi)
    area = pi * float(radius)**2
    return area

def circle_perimeter(radius):
    from mpmath import mp
    mp.dps = 10
    pi = float(mp.pi)
    perimeter = pi * 2 * float(radius)
