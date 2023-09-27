# Written by *** for COMP9021

# Defines:
# - a class: DarkCorridor, implementing 2 special methods
# - another class: Pacer, implementing 3 special methods
#   and (at least) 2 extra methods:
#   * pace()
#   * now_here_in_dark_corridor()
# - a function: compare_stress(), that takes two Pacer objects
#   as arguments.

# Uses the Unicode characters of code point 9654, 9664 and 11036.

from itertools import cycle, chain, islice


# INSERT YOUR CODE HERE
class DarkCorridorError(Exception):
    pass

class DarkCorridor:
    def __init__(self, n):
        self.n = n
        if self.n <= 0:
            raise DarkCorridorError('The length of the corridor should be strictly positive')
    def __len__(self):
        return self.n
    def __repr__(self):
        return f'DarkCorridor({self.n})'

    def __str__(self):
        a = []
        for i in range(self.n):
            a.append(chr(11036))
        a = " ".join(a)
        return f' {a}'

#corridor = DarkCorridor(3)
#print(corridor)
class Pacer:
    student = ''
    step = 0

    def __init__(self, s, c):
        self.student = s
        self.corridor = c

    def __len__(self):
        return len(self.corridor)

    def __repr__(self):
        return f"Pacer('{self.student}', DarkCorridor({len(self.corridor)}))"
    def __str__(self):
        return (f'{self.student} in {self.corridor}')

    def pace(self, n):
        self.n = n
        self.step += self.n
        return self.step
    def now_here_in_dark_corridor(self):
        len_corridor = len(self.corridor)
        b = self.step % (2 * len_corridor)
        res = []
        if 0 <= b < len_corridor:
            for i in range(len_corridor):
                if i == b:
                    res.append(chr(9654))
                else:
                    res.append(chr(11036))
            res = " ".join(res)
            print(f' {res}')
        elif len_corridor <= b < len_corridor * 2:
            for i in range(len_corridor, 2 * len_corridor):
                if i == b:
                    res.append(chr(9664))
                else:
                    res.append(chr(11036))
            res = reversed(res)
            res = " ".join(res)
            print(f' {res}')
def compare_stress(j, k):
    if j.step > k.step:
        print(f'{j.student} ({j.step} steps) is more stressed than {k.student} ({k.step} steps).')
    elif k.step > j.step:
        print(f'{k.student} ({k.step} steps) is more stressed than {j.student} ({j.step} steps).')
    elif j.step == k.step:
        print(f'{j.student} and {k.student} are both as stressed ({j.step} steps).')
#student_before_exam = Pacer('John', corridor)
#print(student_before_exam)
