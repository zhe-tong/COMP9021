# Written by *** for COMP9021
#
# Implements two functions that both return a string:
# - for line(), the equation of a line that goes through both points
#   provided as arguments;
# - for parabola(), the equation of a parabola that has as roots the
#   values provided as arguments.


def line(point_1, point_2):
    A = point_2[1] - point_1[1]
    B = point_1[0] - point_2[0]
    C = point_1[1] * point_2[0] - point_1[0] * point_2[1]
    if point_1[0] == point_2[0] and point_1[1] == point_2[1]:
        return None
    elif point_1[0] == point_2[0]:
        return str(f'x = {-1 * C / A:.2f}')
    elif point_1[1] == point_2[1]:
        return str(f'y = {-1 * C / B:.2f}')
    elif A / B == 0:
        return str(f'y = {-1 * C / B:.2f}')
    elif C / B == 0:
        return str(f'y = {-1 * A / B:.2f}x')
    elif C / B > 0:
        return str(f'y = {-1 * A / B:.2f}x - {C / B:.2f}')
    elif C / B < 0:
        return str(f'y = {-1 * A / B:.2f}x + {-(C / B):.2f}')

    '''It can be assumed that point_1 and point_2 are both
    tuples of 2 integers.

    The function is meant to return a string that represents the equation
    of a line that goes through both points, in case they are different;
    otherwise, the function returns None.

    - If the line is vertical, then the function returns a string of the
      form 'x = b', with b the representation of a floating point number
      with 2 digits after the decimal point.
    - If the line is horizontal, then the function returns a string of the
      form 'y = b', with b the representation of a floating point number
      with 2 digits after the decimal point.
    - If the line is neither horizontal nor vertical, then
        - either the intercept is 0, in which case the function returns
          a string of the form 'y = ax', with a the representation of a
          floating point number with 2 digits after the decimal point;
        - or the intercept is not 0, in which case the function returns
          a string of the form 'y = ax ± b' with a and b representations
          of floating point numbers with 2 digits after the decimal point,
          and with b positive. 
    '''
    return ''
    ### REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


def parabola(*roots):
    if len(roots) == 0:
        return None
    else:
        temp = list(set(roots))
        if len(temp) > 2:
            return None
        elif len(temp) == 1:
            x1 = int(temp[0]) * 2
            x2 = int(temp[0]) ** 2
            if x1 < 0 and x1 != -1:
                if x2 != 0:
                    return str(f'x^2 + {-x1}x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 + {-x1}x = 0')
            elif x1 == 0:
                if x2 != 0:
                    return str(f'x^2 + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 = 0')
            elif x1 > 0 and x1 != 1:
                if x2 != 0:
                    return str(f'x^2 - {x1}x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 - {x1}x = 0')
            elif x1 == 1:
                if x2 != 0:
                    return str(f'x^2 - x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 - x = 0')
            elif x1 == -1:
                if x2 != 0:
                    return str(f'x^2 + x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 + x = 0')
        elif len(temp) == 2:
            x1 = int(temp[0]) + int(temp[1])
            x2 = int(temp[0]) * int(temp[1])
            if x1 < 0 and x1 != -1:
                if x2 > 0:
                    return str(f'x^2 + {-x1}x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 + {-x1}x = 0')
                elif x2 < 0:
                    return str(f'x^2 + {-x1}x - {-x2} = 0')
            elif x1 == 0:
                if x2 > 0:
                    return str(f'x^2 + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 = 0')
                elif x2 < 0:
                    return str(f'x^2 - {-x2} = 0')
            elif x1 > 0 and x1 != 1:
                if x2 > 0:
                    return str(f'x^2 - {x1}x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 - {x1}x = 0')
                elif x2 < 0:
                    return str(f'x^2 - {x1}x - {-x2} = 0')
            elif x1 == 1:
                if x2 > 0:
                    return str(f'x^2 - x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 - x = 0')
                elif x2 < 0:
                    return str(f'x^2 - x - {-x2} = 0')
            elif x1 == -1:
                if x2 > 0:
                    return str(f'x^2 + x + {x2} = 0')
                elif x2 == 0:
                    return str(f'x^2 + x = 0')
                elif x2 < 0:
                    return str(f'x^2 + x - {-x2} = 0')
    '''It can be assumed that roots consists of nothing but integers.

    The function is supposed to return a string that represents a
    second-order equation with 1 as factor of x^2, such that the roots
    of the equation are precisely the members of the argument root, in
    case such an equation exists; otherwise, the function returns None.

    The returned string should have the form 'x^2 ± bx ± c' with b and
    c positive integers, modulo the following conditions.
    - In case b is 0, ' + bx' is omitted.
    - In case c is 0, '+ c' is omitted.
    - In case b is 1, b is omitted.    
    '''
    return ''
    ### REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE



