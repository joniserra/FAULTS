import random
import stochastic.processes.discrete as sto

layerN=[]
for i in range(0,20): #Loop for improving presition: the calculation is repeated 20 times
    MC=sto.MarkovChain(transition=[[0.806795, 0.193205], [0.806795, 0.193205]])#Here the value of alpha (and its complementary) should be written twice.
    lista2=MC.sample(100000) #A list with 0 and 1 are done. Each 0 is a single layer of the one we want to calculate, while 1 is the layer which  generates stacking faults
    #print(lista2)
    total=" "
    for i in lista2:
        total=total+str(i)
    #print total  
    total=total[1:]    
    numero=0
    #print(total)
    
    i0="0"
    listofsequences=[] #It reads  lista2 and whenever there is a transition, it is registered
    contador=0
    for i in total:
        if i ==i0:
            contador=contador+1
            continue
        else:
            i0=i
            listofsequences.append(contador)
            contador=0
    layerN.append(100000/len(listofsequences))
suma=0

for j in layerN:
    suma=suma+float(j)
sumafinal=suma/20    
    
print("Average number of layers: "+str("{:.2f}".format(sumafinal)))
