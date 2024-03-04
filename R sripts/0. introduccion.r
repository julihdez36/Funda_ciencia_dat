# Curso análisis de datos en R

# usar nombres significativos
# mayusculas y minusculas representan caracteres diferentes
# es permitido usar puntos '.' y guiones bajos '_'
# no usar nombres que inicien con numeros
# no usar nombres reservados: c, t, seq, sum, mean, plot,
# usar '=' o '<-' para definir objetos
#Los objetos se guardan en la memoria ram, evite saturarla

#La comunidad de software libre es muy grande (R y Python), 
## aquello que no sepa, se puede buscar en foros o páginas

rep(1,5) #Experimentacion con cada código.
#No necesitmaos compilado, podemos jugar en la consola
rep(c(1,2),c(3,5))

class(x) #clase de un objeto
str(x)  #estructura para objeto
length(x) #longitud
#feature=caracteristicas, variables
rm(l,valor,y,z,A) #No es necesario concatenar

valor <- c(249.5, 464.8, 624.4, 210.4, 1897.2)

# algunas funciones basicas
min(valor)
max(valor)
sum(valor)
mean(valor)
sort(valor, decreasing = T) #ordenar de forma ascendente

# Matrices
ventas <- c(190.5, 136.2, 245.5, 173.5, 229.7)

ganancias <- c(45.8, 40.4, 42.5, 39.3, 49.3)

activos <- c(4914.7, 3689.3, 873.7, 4301.7, 510.3)

valor <- c(249.5, 464.8, 624.4, 210.4, 1897.2)

A<-matrix(data = c(ventas,ganancias),nrow = length(ventas),
       ncol = 2,byrow = F)
B<-matrix(data = c(activos,valor),nrow = length(ventas),
          ncol = 2,byrow = F)

#Lo usual es colocar las observaciones o los individuos (estancias)
#en las filas o los features en las columnas

class(A)
dim(A) #util con filas o data frame
nrow(A)
ncol(A)
length(A)

A+2
A+B
A*B #elemento a elemento
A%*%t(B) #multiplicación de matrices
dim(A%*%t(B)) 

#Unir A y B por columnas
FG10<-cbind(A,B)
FG10
rbind(A,B) #no tiene sentido este objeto
rm(A,B) #optimizar memoria
#Todas las rutinas se hacen con (), pero para filtrar uso []
FG10[2,1]
FG10[1,]
FG10[,-c(1,2)]
rm(FG10)

#Las matrices sólo aceptan valores numéricos
## Vamos a trabajar con los objetos que por defecto se importan los datos en r
## Es decir, los data frame. Acá si puedo mezclar variables cualitativas o cuantitativas
#aunque ambas sean estrcuturas rectangulares, son diferentes objetos

#Data frame

pais <- c("China", "US", "US", "China", "Saudi Arabia")

ventas <- c(190.5, 136.2, 245.5, 173.5, 229.7)

ganancias <- c(45.8, 40.4, 42.5, 39.3, 49.3)

activos <- c(4914.7, 3689.3, 873.7, 4301.7, 510.3)

valor <- c(249.5, 464.8, 624.4, 210.4, 1897.2)

class(pais)
class(ventas)

FG5 <- data.frame(pais, ventas, ganancias, activos, valor)
FG5 #las columnas ya aparecen con nombres

# asignar nombres a las variables
colnames(FG5) <- c("country", "sales", "profits", "assets", "value")

# asignar nombres a los registros
rownames(FG5) <- c("ICBC", "JPMorgan Chase", 
                   "Berkshire Hathaway", "China Construction Bank", 
                   "Saudi Aramco")

dim(FG5)
nrow(FG5) #numero de observaciones
ncol(FG5) #numero de variables

#obtener variables con $
FG5$sales
mean(FG5$sales)
FG5[ , c(2, 4)] #datos de las ventas y los activos
FG5[,c("country","sales","profits")]
colMeans(FG5[,-c(1)]) #promedio de las variables numéricas

#En las bases de datos, siempre hay datos faltantes
is.na(FG5) # hay algun NA?
class(is.na(FG5))
any(is.na(FG5)) #no hay ningun verdadero

#Ejemplo
## remplazar algunos valores
FG5[2,3]<-NA
FG5[5,]<-NA
FG5
is.na(FG5)
any(is.na(FG5))

subset(FG5,subset = complete.cases(FG5)==T)

# identificar registros completos
reg_na<-complete.cases(FG5) #revisa por filas si la info esta completa
class(reg_na)
as.numeric(reg_na)#lo traduce a lenguaje computaciona;
sum(as.numeric(reg_na)) # suma cuantos hay perdidos
sum(reg_na)

#base de datos de los completos
FG5_completo<-FG5[reg_na,]
FG5_completo

# base de datos incompleta
FG5[!reg_na,]

