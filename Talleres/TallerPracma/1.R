
library(pracma)
library(Matrix)



crearMatriz <- function(){
  return (matrix(data = floor(runif(36, min=15, max=20)), nrow = 6, ncol = 6))
   
}


con=0
A = crearMatriz()
con=norm(A)*norm(inv(A))

while(con<1000){
  A = crearMatriz()
  con=norm(A)*norm(inv(A))
}

A
b = c(1,2,3,4,5,6)


print(con)

n=4
D1<-eye(n, m = n)
D2<-ones(n, m = n)
D3<-zeros(n, m = n)
print(D1)
print(D2)
print(D3)

#T = -D^-1(L + U)

D=Diag(A)
l=tril(A,k=-1)
u=triu(A,k=1)
D=diag(D)

D

D=inv(D)


T=(-D)%*%(l+u)
T
