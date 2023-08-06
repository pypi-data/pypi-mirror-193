import sys
from .nodes import *
from operator import mul

class Network(object):

  def __init__(self, name):
    self.name = repEmptySpace(name)
    self.nodes = []
    self.evidence = []
    self.marginal = None

  def __str__(self):
    return self.name

  def addNode(self, node):
    #Agrega un nodo a la red
    self.nodes.append(node)

  def addNodes(self,nodes):
    # Agrega una lista de nodos a la red
    for node in nodes:
      self.addNode(node)

  def setEvidence(self,name,value):
    #Coloca la evidencia para elemento de un nodo

    for node in self.nodes:
      if name == str(node):
        var = node.getIdNum()
        outcomes = node.getOutcomes()
        if type(value) is str:
          for outcome in outcomes:
            if value == outcome:
              val = j+1
        elif type(value) is int:
          val = value
        self.evidence.append([var,val])    

  def getEvidence(self):
    #Retorna la informacion sobre la evidencia
    if self.evidence == []:
      evidence = [[0,0]]
    else:
      evidence = self.evidence
    return evidence

  def reset(self):
    #Reinicia todos los valores 
    self.evidence = []
    self.marginal = None
    for node in self.nodes:
      node.setBeliefs(node.getProbabilities())
      node.setCard([])
      var = np.append(node.getVar(),node.getArcConnectionId()).tolist()
      node.setVar(var)
      node.setVal(node.transformProbabilities())

  def computeBeliefs(self):
    #Calcular las creencias de la red
    
    order = []
    factors = []
    marginal = []

    for node in self.nodes:
      factor = Factor()
      order.append(node.getIdNum())
      node.setVal(node.transformProbabilities())
      var, card, val = node.getInput()
      factor.input(var,card,val)
      factors.append(factor)

    evidence = self.getEvidence()

    for factor in factors:
      subfactors = []
      suborder = factor.var
      for idNum in suborder:
        node = self.nodes[int(idNum)-1]
        subfactor = Factor()
        var, card, val = node.getInput()

        subfactor.input(var,card,val)
        subfactors.append(subfactor)

      if len(suborder) != 1:
        M = ComputeMarginal(suborder, subfactors, evidence)
        for idx,idNum in enumerate(suborder):
          node = self.nodes[int(idNum)-1]
          beliefs = M[idx].val
          card = M[idx].card
          var = M[idx].var
          node.setBeliefs(beliefs)
          node.setCard(card)
          node.setVar(var)
          node.setVal(beliefs)

  def getBeliefs(self,vars=None):
    #Retorna las creencias de la red
    beliefs = []
    if vars != None:
      for mar in self.marginal:
        for var in vars:
          if str(mar[0]) == var:
            beliefs.append(mar[1])
    else:
      for mar in self.marginal:
        beliefs.append(mar[1])
    return beliefs


  def writeFile(self,filename):
    # Escribe un archivo output
    # https://www.edureka.co/blog/bayesian-networks/ (referencia 1)
    # https://www.youtube.com/watch?v=23hPg88pZBo (referencia 2)
    # https://www.youtube.com/watch?v=THgHwS-zVt8 (Referencia 3)
    self.checkInput()
    if filename == None:
      filename = self.name+'.xdsl'

    f = open(filename,'w')
    f.writelines(self.writeHeader())
    for node in self.nodes:
      f.write(node.printNode())
    f.writelines(self.writeBody())
    for node in self.nodes:
      f.write(node.printExtension())
    f.writelines(self.writeFooter())
    f.close()

  def writeHeader(self):
    header = ['<?xml version="1.0" encoding="ISO-8859-1"?>\n',
              '<smile version="1.0" id="'+self.name+'" numsamples="1000" discsamples="10000">\n',
              '\t<nodes>\n']
    return header

  def writeBody(self):
    body = ['\t</nodes>\n','\t<extensions>\n','\t\t<genie version="1.0" app="py2GeNIe 2013" name="'+self.name+'" faultnameformat="nodestate">\n']
    return body

  def writeFooter(self):
    footer = ['\t\t</genie>\n','\t</extensions>\n','</smile>']
    return footer

  def checkInput(self):
    if self.nodes == []:
      sys.exit("Error: No hay nodos conectado!")
    else:
      for node in self.nodes:
        if node.getOutcomes() == []:
          sys.exit("Error: Node '"+str(node)+"' No tiene salidas!")
        m,n = node.getTableSize()
        nodeLen = m*n
        if len(node.getProbabilities()) != nodeLen:
          sys.exit("Error: Las probabilidades para '"+str(node)+"' no se parecen!\n       El largo de las probabilidades deberia ser "+str(nodeLen)+" pero es "+str(len(node.getProbabilities())))
        n = n+0.0
        if str(sum(node.getProbabilities())) != str(n):
          print("Error: En las probabilidades para '"+str(node)+"' no suma 1.0!")



class Node(object):
  #Elemento nodo para la red bayesiana

  nextIdNum = 1
  def __init__(self, name):
    self.name = repEmptySpace(name)
    self.caption = name
    self.idNum = Node.nextIdNum
    self.nodeId = 'Node_'+str(self.idNum)
    Node.nextIdNum += 1
    self.outcomes = []
    self.probabilities = []
    self.nextIdOut = 0
    self.arcConnection = []
    self.var = []
    self.card = []
    self.val = []
    self.var.append(self.idNum)
    self.beliefs = None

    self.interior_color = 'e5f6f7'
    self.outline_color = '0000bb'
    self.font_color = '000000'
    self.font_name = 'Arial'
    self.font_size = 8
    self.node_size = [0,0,125,65]
    self.node_position = [0,0,125,65]
    self.bar_active = True


  def __repr__(self):
    return self.name

  def getIdNum(self):
    return self.idNum

  def getName(self):
    return self.name

  def setCard(self,card):

    self.card = card

  def getCard(self):

    return self.card

  def setVar(self,var):

    self.var = var

  def getVar(self):

    return self.var

  def setVal(self,val):

    self.val = val

  def getVal(self):

    return self.val

  def setBeliefs(self,beliefs):
    self.beliefs = beliefs

  def getBeliefs(self):

    return self.beliefs

  def addOutcome(self,name):

    self.outcomes.append(repEmptySpace(name))

  def addOutcomes(self,names):

    for name in names:
      self.outcomes.append(repEmptySpace(name))

  def getOutcomes(self):

    return self.outcomes

  def setProbabilities(self,probabilities):
    #Lista de probabilidades para el nodo
    self.probabilities = probabilities
    self.val = self.transformProbabilities()
    self.beliefs = probabilities

  def transformProbabilities(self):
    #Transforma las probabilidades del nodo
    card = self.getCard()
    probabilities = self.probabilities

    if len(card) != 1:
      card.insert(len(card), card.pop(0))
      assignment = IndexToAssignment(np.arange(np.prod(card)),card)
      assignment = assignment.tolist()
      for i in range(len(card)-1,-1,-1):
        assignment.sort(key=lambda x: x[i])

      for i,item in enumerate(assignment):
        item.append(probabilities[i])

      assignment.sort(key=lambda x: x[len(card)-1])

      for i in range(len(card)-1):
        assignment.sort(key=lambda x: x[i])

      probabilities = []
      for item in assignment:
        probabilities.append(item[-1])

    return probabilities

  def getProbabilities(self):
    #Retorna la lista de probabilidades
    return self.probabilities

  def getProbability(self,index):

    return self.probabilities[index]

  def getArcConnection(self):
    return self.arcConnection

  def getArcConnectionId(self):
    ids = []
    for connection in self.arcConnection:
      ids.append(connection[1])
    return ids

  def addArcConnection(self,name,id,size):
    self.arcConnection.append([name,id,size])
    self.var.append(id)

  def getTableSize(self):

    if self.arcConnection == []:
      size = (self.getSize(),1)
    else:
      n = 1
      for connection in self.arcConnection:
        n *= connection[2]
      size = (self.getSize(),n)
    return size

  def getCard(self):

    if self.card == []:
      card = []
      if self.arcConnection == []:
        card.append(self.getSize())
      else:
        card.append(self.getSize())
        for connection in self.arcConnection:
          card.append(connection[2])
    else:
      card = self.card.tolist()
    return card

  def getInput(self):

    card = self.getCard()
    return self.var, card, self.val

  def getTable(self):
    return self.tableSize

  def getSize(self):
    return len(self.outcomes)

  def printNode(self):
    # print node
    commentNode = '\t\t<!-- create node "'+self.caption+'" -->\n'
    initNode = '\t\t<cpt id="'+self.name+'" >\n'
    commentOutcomes = '\t\t\t<!-- setting names of outcomes -->\n'
    initOutcomes = ''
    for outcome in self.outcomes:
      initOutcomes += '\t\t\t<state id="'+outcome+'" />\n'

    if self.arcConnection != []:
      # print arc
      commentArc = '\t\t\t<!-- add arcs -->\n'
      initArc = '\t\t\t<parents>'
      for connection in self.arcConnection:
        initArc += connection[0]+' '
      endArc =  '</parents>\n'
    else:
      commentArc = ''
      initArc = ''
      endArc = ''

    # print probabilidades
    commentProbabilities = '\t\t\t<!-- setting probabilities -->\n'
    initProbabilities = '\t\t\t<probabilities>'
    for i,probability in enumerate(self.probabilities):
      initProbabilities += str(probability)+' '
    endProbabilities = '</probabilities>\n'
    endNode = '\t\t</cpt>\n'
    print_node =  commentNode+initNode+commentOutcomes+initOutcomes+commentArc+initArc+endArc+commentProbabilities+initProbabilities+endProbabilities+endNode
    return print_node

  def printExtension(self):
    initExtensions = '\t\t\t<node id="'+self.name+'">\n'
    initName = '\t\t\t\t<name>'+self.caption+'</name>\n'
    initIcolor = '\t\t\t\t<interior color="'+self.interior_color+'" />\n'
    initOcolor = '\t\t\t\t<outline color="'+self.outline_color+'" />\n'
    initFont = '\t\t\t\t<font color="'+self.font_color+'" name="'+self.font_name+'" size="'+str(self.font_size)+'" />\n'
    initPos = '\t\t\t\t<position>'+str(self.node_position[0])+' '+str(self.node_position[1])+' '+str(self.node_position[2])+' '+str(self.node_position[3])+'</position>\n'
    initBar = ''
    if self.bar_active == True:
      initBar = '\t\t\t\t<barchart active="true" width="'+str(self.node_size[2])+'" height="'+str(self.node_size[3])+'" />\n'
    endExtensions = '\t\t\t</node>\n'
    return initExtensions+initName+initIcolor+initOcolor+initFont+initPos+initBar+endExtensions

  def printProbabilities(self):
    commentProbabilities = '// setting probabilities for "'+self.name+'"\ntheProbs.Flush();\n'
    initProbabilities = 'theProbs.SetSize('+str(len(self.probability))+');\n'
    for i,probability in enumerate(self.probability):
      initProbabilities += 'theProbs['+str(i)+'] = '+str(probability)+';\n'
    endProbabilities = 'theNet.GetNode('+self.nodeId+')->Definition()->SetDefinition(theProbs);\n\n'
    print_prob = commentProbabilities+initProbabilities+endProbabilities
    return print_prob

  def getName(self):
    return self.name

  def getNodeId(self):
    return self.nodeId

  def setInteriorColor(self,interior_color):

    self.interior_color = interior_color

  def setOutlineColor(self,outline_color):

    self.outline_color = outline_color

  def setFontColor(self,font_color):

    self.font_color = font_color

  def setFontName(self,font_name):

    self.font_name = font_name

  def setFontSize(self,font_size):

    self.font_size = font_size

  def setNodeSize(self,x,y):

    self.node_size[2] = x
    self.node_size[3] = y

  def setNodePosition(self,x,y):

    self.node_position[0] = x
    self.node_position[1] = y
    self.node_position[2] = x+self.node_size[2]
    self.node_position[3] = y+self.node_size[3]

  def getNodePosition(self):
    return self.node_position

  def setBarActive(self, bar_active):
        
    self.bar_active = bar_active

class Arc(object):


  def __init__(self, from_node, to_node):
    self.from_node = from_node
    self.to_node = to_node
    self.to_node.addArcConnection(self.from_node.getName(),self.from_node.getIdNum(),self.from_node.getSize())

  def __repr__(self):
    return self.name

def repEmptySpace(string):
  return string.replace(' ', '_')

def chunks(l, n):

  for i in range(0, len(l), n):
    yield l[i:i+n]