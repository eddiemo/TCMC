class Polynom(object):
    koefs = []
    char = 2

    def __init__(self, deg = 0, num = 0, char = 2):
        self.char = char
        koefs = [num] * (deg + 1)

    @staticmethod
    def inverse(a, p):
        a0 = a
        a1 = p
        x0 = 1
        y0 = 0,
        x1 = 0
        y1 = 1
        while a1 != 0:
            q = a0 / a1
            temp = a1; a1 = a0 - a1 * q; a0 = temp
            temp = x1; x1 = x0 - x1 * q; x0 = temp
            temp = y1; y1 = y0 - y1 * q; y0 = temp
        while x0 < 0:
            x0 += p
        return x0

    @staticmethod
    def NODnum(a, p):
        a0 = a; a1 = p
        while a1 != 0:
            temp = a1
            a1 = a0 % a1
            a0 = temp
        while a0 < 0:
            a0 += p
        return a0

    @staticmethod
    def NODpol(a, b):
        a0 = Polynom(); a1 = Polynom()
        if (a < b):
            a0 = b
            a1 = a
        else:
            a0 = a
            a1 = b
        while (not(a1.getDeg() == 0 and a1.koefs[0] == 0)):
            temp = a1; a1 = a0 % a1; a0 = temp
        return a0

    def __str__(self):
        first = True
        ans = ''
        for i in range(len(self.koefs) - 1, -1, -1):
            if self.koefs[i] != 0:
                if not first:
                    ans += ' + '
                ans += self.koefs[i]
                if i == 1:
                    ans += ' * x'
                elif (i > 1):
                    ans += ' * x^' + str(i)
                first = False
        if (len(self.koefs) == 1) and self.koefs[0] == 0:
            ans += str(0)
        return ans

    def degree(self):
        cnt = 0
        for i in range(len(self.koefs) - 1, -1, -1):
            if self.koefs[i] != 0:
                cnt = i
                break
        return cnt

    def __eq__(self, other):
        if self == other:
            return True
        if other == None or type(self) != type(other):
            return False
        if self.koefs != other.koefs:
            return False
        return True

    def __lt__(self, other):
        if len(self.koefs) < len(other.koefs):
            return True
        elif len(self.koefs) >= len(other.koefs):
            return False
        for i in range(other.degree(), -1, -1):
            if self.koefs[i] < other.koefs[i]:
                return True
        return False

    def __truediv__(self, other):
        if len(self.koefs) < len(other.koefs) or Polynom.NODnum(other.koefs[-1], self.char) != 1:
            return Polynom(deg = 0, char = self.char)
        new = Polynom(deg = self.degree() - other.degree(), char=self.char)
        rest = Polynom(deg=self.degree(), char=self.char)
        for i in range(len(self.koefs)):
            rest.koefs[i] = self.koefs[i]
        restdeg = len(self.koefs) - 1; divdeg = other.degree()
        inv = Polynom.inverse(other.koefs[-1], self.char)
        while (len(rest.koefs) >= len(other.koefs)):
            newdeg = restdeg - divdeg
            new.koefs[newdeg] = (inv * rest.koefs[restdeg]) % self.char
            for i in range(divdeg + 1):
                rest.koefs[i + newdeg] = (rest.koefs[i + newdeg] - other.koefs[i] * new.koefs[newdeg]) % self.char
            while len(rest.koefs) > 1 and rest.koefs[-1] == 0:
                rest.koefs.pop()
            restdeg = len(rest.koefs) - 1
            if rest.koefs[-1] == 0:
                break
        return new

    def __mul__(self, other):
        new = Polynom(deg = len(other.koefs) + len(self.koefs) + 1,num = 0, char = self.char)
        for i in range(len(self.koefs)):
            for j in range(len(other.koefs)):
                new.koefs[i + j] = (new.koefs[i + j] + (self.koefs[i] * other.koefs[j])) % self.char
        while len(new.koefs) > 1 and new.koefs[len(new.koefs) - 1] == 0:
            new.koefs.pop()
        return new

    def __mod__(self, other):
        if len(self.koefs) < len(other.koefs) or Polynom.NODnum(other.koefs[-1], self.char) != 1:
            return self
        new = Polynom(deg=self.degree(), char=self.char)
        for i in range(len(self.koefs)):
            new.koefs[i] = self.koefs[i]
        resdeg = len(self.koefs) - 1; divdeg = other.degree()
        inv = Polynom.inverse(other.koefs[-1], self.char)
        while (len(new.koefs) >= len(other.koefs)):
            newdeg = resdeg - divdeg
            coef = (inv * new.koefs[resdeg]) % self.char
            for i in range(divdeg + 1):
                new.koefs[i + newdeg] = (new.koefs[i + newdeg] - other.koefs[i] * coef) % self.char
            while len(new.koefs) > 1 and new.koefs[-1] == 0:
                new.koefs.pop()
            resdeg = len(new.koefs) - 1
            if new.koefs[-1] == 0:
                break
        while len(new.koefs) > 1 and new.koefs[-1] == 0:
            new.koefs.pop()
        return new

    def __pow__(self, power):
        new = Polynom(deg=self.degree(), char=self.char)
        for i in range(len(self.koefs)):
            new.koefs[i] = self.koefs[i]
        for i in range(1, power):
            new = new * self
        return new

    def __add__(self, other):
        new = Polynom(deg = len(self.koefs), char = self.char)
        if self.degree() >= other.degree():
            for i in range(len(self.koefs)):
                new.koefs[i] = self.koefs[i]
            mlen = len(other.koefs)
        else:
            for i in range(len(other.coefs)):
                new.koefs[i] = other.koefs[i]
            new.char = other.char
            mlen = len(self.koefs)
        for i in range(mlen):
            new.koefs[i] = (self.koefs[i] + other.koefs[i]) % self.char
        while len(new.koefs) > 0 and new.koefs[len(new.koefs) - 1] == 0:
            new.koefs.pop()
        return new

    def addConst(self, x):
        new = Polynom(deg=self.degree(), char=self.char)
        for i in range(len(self.koefs)):
            new.koefs[i] = self.koefs[i]
        new.koefs[0] += x
        return new

    def __sub__(self, other):
        if self.degree() > other.degree():
            new = Polynom(deg = self.degree(), char = other.char)
        else:
            new = Polynom(deg = other.degree(), char = other.char)
        if self.degree() >= other.degree():
            for i in range(self.degree() + 1):
                new.koefs[i] = self.koefs[i]
            for i in range(other.degree() + 1):
                new.koefs[i] = (new.koefs[i] - other.koefs[i]) % other.char
        else:
            for i in range(other.degree() + 1):
                new.koefs[i] = other.char - other.koefs[i]
            for i in range(other.degree() + 1):
                new.koefs[i] = (new.koefs[i] + other.koefs[i]) % other.char
        while len(new.koefs) > 0 and new.koefs[len(new.koefs) - 1] == 0:
            new.koefs.pop()
        return new

f = Polynom(deg = 2, char = 2)
f.koefs = [1, 0, 1]
g = Polynom(deg = 1, char = 2)
g.koefs = [0, 1]
print(str(f * g))