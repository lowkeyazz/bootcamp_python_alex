import sys


class Vector:
    def __init__(self, vect):
        if type(vect) == list:
            for i in range(len(vect)):
                if type(vect[i]) != float:
                    sys.exit("Type 'float' required ")
            self.values = vect
        elif type(vect) == int:
            if vect < 0:
                sys.exit("Number of elements in vector must be positif ")
            vecti = []
            for i in range(vect):
                vecti.append(float(i))
            self.values = vecti
        elif type(vect) == tuple:
            if len(vect) != 2 or vect[0] > vect[1]:
                sys.exit("wrong declaration")
            vectj = []
            for i in range(vect[0], vect[1]):
                vectj.append(float(i))
            self.values = vectj
        else:
            sys.exit("wrong declaration")
        self.size = len(self.values)

    def __add__(self, vv):
        addedV = Vector(self.size)
        for i in range(self.size):
            addedV.values[i] = 0
        if type(vv) == Vector:
            if self.size != vv.size:
                sys.exit("same size required")
            for i in range(self.size):
                addedV.values[i] = self.values[i]+vv.values[i]
            return addedV
        elif type(vv) == int or type(vv) == float:
            for i in range(self.size):
                addedV.values[i] = self.values[i]+vv
            return addedV
        else:
            sys.exit("Error 404")

    def __radd__(self, vv):
        return Vector.__add__(self, vv)

    def __sub__(self, vv):
        subedV = Vector(self.size)
        for i in range(self.size):
            subedV.values[i] = 0
        if type(vv) == Vector:
            if self.size != vv.size:
                sys.exit("same size required")
            for i in range(self.size):
                subedV.values[i] = self.values[i]-vv.values[i]
            return subedV
        elif type(vv) == int or type(vv) == float:
            for i in range(self.size):
                subedV.values[i] = self.values[i]-vv
            return subedV
        else:
            sys.exit("Error 404")

    def __rsub__(self, vv):
        return Vector.__sub__(self, vv)

    def __truediv__(self, vv):
        if type(vv) == Vector:
            sys.exit("need to divied by a number")
        if vv == 0:
            sys.exit("division by 0 is impossible")
        return Vector.__mul__(self, 1/vv)

    def __rtruediv__(self, vv):
        return Vector.__truediv__(self, vv)

    def __mul__(self, vv):
        mltedV = Vector(self.size)
        for i in range(self.size):
            mltedV.values[i] = 0
        if type(vv) == Vector:
            if self.size != vv.size:
                sys.exit("same size required")
            mltedV = 0
            for i in range(self.size):
                mltedV += self.values[i]*vv.values[i]
            return mltedV
        elif type(vv) == int or type(vv) == float:
            for i in range(self.size):
                mltedV.values[i] = self.values[i]*vv
            return mltedV
        else:
            sys.exit("Error 404")

    def __rmul__(self, vv):
        return Vector.__mul__(self, vv)

    def __str__(self):
        for i in range(self.size):
            print("| {} |".format(self.values[i]))
        return ""

    def __repr__(self):
        for i in range(self.size):
            print("| {} |".format(self.values[i]))
        return ""
