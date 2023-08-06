import numpy as np
import numpy.matlib


class Factor(object):
    """ Factores
    Los factores son usado para representar the CPDs en la red bayesiana.
      - name (str): Nombre del factor.
      - var (list): Lista de las variables en el factor. 
      - card (list): Lista de las cardinalidades 
      - val (list): Tabla de valores del tamaño de prod(card)
    """

    def __init__(self):
        self.name = None
        self.var = None
        self.card = None
        self.val = None

    def getVar(self):
        return self.var

    def getCard(self):
        return self.card

    def getVal(self):
        return self.val

    def setVar(self, var):
        self.var = np.array(var)

    def setCard(self, card):
        self.card = np.array(card, dtype="i")

    def setVal(self, val):
        self.val = np.array(val)

    def input(self, var, card, val):
        self.var = np.array(var)
        self.card = np.array(card, dtype="i")
        self.val = np.array(val)

    def __str__(self):
        return self.name


def FactorProduct(A, B):
    """ Realiza el producto entre A y B
      - .var    Vector de variables
      - .card   Vector de cardinalidades
      - .val    Tabla de valores 
    Args:
      - A (Factor): Factor A
      - B (Factor): Factor B
    Returns:
      - C (Factor): Retorna factor C
    """
    C = Factor()
    # Chequear por factores vacíos
    if A.var == np.array([]):
        C = B
        return C
    if B.var == np.array([]):
        C = A
        return C
    else:
        dummy = np.intersect1d(A.var, B.var)
        if dummy == np.array([]):
            print("Dimensionality mismatch in factors")


        C.var = np.union1d(A.var, B.var)

        # Construye el mappeo entre variables 

        dummy, ixA = ismember(A.var, C.var)
        mapA = A.var[dummy]
        dummy, ixB = ismember(B.var, C.var)
        mapB = B.var[dummy]

        # Coloca la cardinalidad de las variables en C 
        C.card = np.zeros(len(C.var))
        C.card[ixA] = A.card
        C.card[ixB] = B.card


        C.val = np.zeros(np.prod(C.card).astype(int))

        assignment = IndexToAssignment(np.arange(np.prod(C.card)), C.card)
        indxA = AssignmentToIndex(assignment[:, ixA], A.card).astype(int)
        indxB = AssignmentToIndex(assignment[:, ixB], B.card).astype(int)

 
        for i in range(int(np.prod(C.card))):
            C.val[i] = A.val[indxA[i]] * B.val[indxB[i]]

        return C


def FactorMarginalization(A, V):
    # Marginación de factores Suma las variables dadas de un factor.

    

    B = Factor()

    if A.var == np.array([]) and V == np.array([]):
        B = A
        return B
    else:
  
        B.var, mapB = setdiff(A.var, V)

        if B.var == np.array([]):
            print("Error")
        else:

            B.card = A.card[mapB]
            B.val = np.zeros(np.prod(B.card).astype(int))

            assignment = IndexToAssignment(np.arange(np.prod(A.card)), A.card)
            indxB = AssignmentToIndex(assignment[:, mapB], B.card).astype(int)

            for i in range(int(len(indxB))):
                B.val[indxB[i]] += A.val[i]

            return B


def ObserveEvidence(F, E):
     #Observar evidencia: Modifica un vector de factores dada alguna evidencia.
     
    # Itera por toda la evidencia
    for i in range(int(np.shape(E)[0])):
        v = E[i][0]  # variable
        x = E[i][1]  # valor


        for j in range(len(F)):

            indx = indices(F[j].var, lambda x: x == v)

            if indx != []:

                if x > F[j].card[indx] or x < 0:
                    print("Error: Invalid evidence, X_" + str(v) + " = " + str(x))

                assignment = IndexToAssignment(np.arange(np.prod(F[j].card)), F[j].card)
                idnxF = indices(F[j].var, lambda x: x == v)

                A = np.array([assignment[0]])
                for i in range(len(assignment)):
                    if assignment[i][idnxF] != x:
                        A = np.append(A, [assignment[i]], 0)

                A = np.delete(A, 0, 0)
                F[j] = SetValueOfAssignment(
                    F[j],
                    A,
                    0,
                )

                if F[j].val == np.array([]):
                    print(
                        ""
                        + str(j)
                        + " Hace una variable imposible"
                    )
    return F


def SetValueOfAssignment(F, A, v, VO=None):
    if VO == None:

        indx = AssignmentToIndex(A, F.card).astype(int)

    else:
        map = [0] * len(F.var)
        for i in range(int(len(F.var))):
            map[i] = indices(VO, lambda x: x == F.var[i])
        indx = AssignmentToIndex(A[map], F.card).astype(int)
    F.val[indx.astype(int)] = v

    return F


def ComputeJointDistribution(F):
    """ 
    calcula la distribución conjunta definida por un conjunto de factores dados
    """

    Joint = Factor()

    if F == []:
        print("Error: lista de factores vacías")
    elif len(F) == 1:
        print("Error: Solo un factor")
    else:
        F.reverse()
        Joint = FactorProduct(F[0], F[1])
        if len(F) > 2:
            for i in range(2, len(F)):
                Joint = FactorProduct(Joint, F[i])
        return Joint


def ComputeMarginal(V, F, E):
    """
    Calcula la marginal sobre un conjunto de variables dadas.
    """

    # Distribución Conjunta
    J = ComputeJointDistribution(F)

    # Calcular la evidencia observada
    E = ObserveEvidence([J], E)

    # Devuelve un factor renormalizado
    R = RenormalizeFactor(E[0])

    # Guarda los resultados en lista 
    M = []
    for i in range(len(V)):
        D = R
        for ii in range(len(R.var)):
            if R.var[ii] != V[i]:
                D = FactorMarginalization(D, [R.var[ii]])
        M.append(D)
    return M


def RenormalizeFactor(F):
    if F.val == np.array([]):
        print("Error: Factor is empty")
    else:
        if np.sum(F.val) != 1:
            sum = np.sum(F.val)
            for i in range(len(F.val)):
                F.val[i] = F.val[i] * sum ** (-1)
        return F


def indices(a, func):
    return [i for (i, val) in enumerate(a) if func(val)]


def setdiff(a, b):
    tf = np.in1d(a, b)
    for i in range(len(tf)):
        if tf[i] == True:
            tf[i] = False
        else:
            tf[i] = True
    d = np.setdiff1d(a, b)
    index = np.array([np.where(a != b)])[0][0]
    return d, index


def AssignmentToIndex(A, D):

    if np.any(A.shape == 1):
        I = (
            np.dot(
                np.cumprod(np.append([1], D[:-1])), (np.reshape(A, -1, order="F") - 1)
            )
            - 1
        )
    else:
        I = np.sum(
            np.matlib.repmat(np.cumprod(np.append([1], D[:-1])), A.shape[0], 1)
            * (A - 1),
            1,
        )
    return I


def ismember(a, b):
    tf = np.in1d(a, b) 
    u = np.unique(a[tf])
    index = np.array([(np.where(b == i))[0][-1] if t else 0 for i, t in zip(a, tf)])
    return tf, index


def IndexToAssignment(I, D):

    I = I[np.newaxis].T
    A = (
        np.mod(
            np.floor(
                np.matlib.repmat(I, 1, len(D))
                / np.matlib.repmat(np.cumprod(np.append([1], D[:-1])), len(I), 1)
            ),
            np.matlib.repmat(D, len(I), 1),
        )
        + 1
    )
    return A


def intersect(a, b):
    return list(set(a) & set(b))
