#exercicio3
def main():
  import math
  x0 = input("Digite X0, o inicio do intervalo ")  
  x0 = float(x0)
  xn = input("Digite XN, o fim do intervalo ")  
  xn = float(xn)
  n = input("Digite n, o numero de pontos entre X0 e XN: ")  
  n = int(n)
  lb = math.pi*math.pi
  a=[]
  b=[]
  d=[]
  x=[]
  y=[]
  z=[]
  c=[]
  xi=[]
  ui=[]
  uj=[]
  yi=[]
  um=[]
  delta=[]
  deltao=[]
  h=(xn-x0)/(n+1)
  ai=2*(1/h+lb*h/3)
  i=1
  for i in range(n):
    a.append(ai)
  bi=-1/h+lb*h/6
  i=1
  for i in range(n-1):
    b.append(bi)
  i=0
  for i in range(n):

        d.append((-4*math.sin(math.pi*(i+1)*h)+2*math.sin(math.pi*h*(i+1)-math.pi*h)+2*math.sin(math.pi*h*(i+1)+math.pi*h))/(-h))
   

#resolver o sisteminha
  i=0
  for i in range(n-1):
    a[i+1]=a[i+1]-b[i]*b[i]/a[i]
  z.append(d[0])
  k=1
  while k<n:
    z.append(d[k]-z[k-1]*b[k-1]/a[k-1])
    k=k+1
  k=0
  while k<n:
    y.append(z[k]/a[k])
    k=k+1
  i=0
  k=n-1
  x.append(y[n-1])
  while k>0:
    x.append(y[k-1]-x[i]*b[k-1]/a[k-1])
    k=k-1
    i=i+1
  i=n-1
  c.append(0)
  while i>=0:
    c.append(x[i])
    i=i-1
  c.append(0)
 
  #acabou de resolver o sisteminha vamos testar nos nos

  i=1
  for i in range(n):
    ui.append(math.sin(math.pi*(x0+i*h)))
  i=1
  for i in range(n):
    delta.append(abs(c[i]-ui[i]))
  print ("erro no nó", max(delta))

  #achar pontos xi
  i=0
  for i in range(n+2):
    xi.append(x0+i*h)
  #i=0
  #for i in range(n+2):
    #print(i,xi[i])
    

  #achar pontos yi
  i=0
  for i in range(n+1):
    j=0
    for j in range(10):
      yi.append(x0+i*h+j*h/10)  
  yi.append(1)
  #i=0
  #for i in range(10*(n+1)+1):
    #print(i,xi[int(i/10)],yi[i])
    
 
  #achar pontos u(yi) verdadeiros
  i=0
  for i in range(n+1):
    j=0
    for j in range(10):
      uj.append(math.sin(math.pi*(x0+i*h+j*h/10)))
  uj.append(0)
  #i=0
  #for i in range(10*(n+1)+1):
    #print(i,uj[i])
    

  #achar pontos ubarra(yi) estimados
  i=0
  for i in range(n+1):
    j=0
    for j in range(10):
      um.append(c[i]+(c[i+1]-c[i])/h*(x0+i*h+j*h/10 -xi[i]))  
  um.append(0)
  #imprimir a diferença
  i=0
  for i in range(10*(n+1)+1):
   print(i,uj[i],um[i])
  i=0
  for i in range(10*n):
    deltao.append(abs(um[i]-uj[i]))
  print ("erro max", max(deltao))    
 
    
 
#precisa dessa indentação
if __name__ == "__main__":
    main()
