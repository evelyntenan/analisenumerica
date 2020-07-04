#exercicio1

def main():
  import math
  x0 = input("Digite X0, o inicio do intervalo ")  
  x0 = float(x0)
  xn = input("Digite XN, o fim do intervalo ")  
  xn = float(xn)
  n = input("Digite n, o numero de pontos entre X0 e XN: ")  
  n = int(n)
  lb = 0
  a=[]
  b=[]
  d=[]
  xi=[]
  x=[]
  y=[]
  z=[]
  c=[]
  ui=[]
  delta=[]
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
  for i in range(n+2):
    xi.append(x0+i*h)
  i=1
  for i in range(n):
    d.append(h)
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
  while i>=0:
    c.append(x[i])
    i=i-1  
  i=0
  for i in range(n):
    ui.append(0.5*xi[i+1]*(1-xi[i+1]))
  i=1
  for i in range(n):
    print("c", i," = ",c[i-1])
  i=1
  for i in range(n):
    print("u", i," = ",ui[i-1])
  i=1
  for i in range(n):
    delta.append(abs(c[i-1]-ui[i-1]))
  print ("erro", max(delta))
    
 
#precisa dessa indentação
if __name__ == "__main__":
    main()
