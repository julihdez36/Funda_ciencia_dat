# Primer ejercicio Forbes 2000 --------------------------------------------


# 2021 GLOBAL 2000
#
# Variables (campos o features)
# - ranking   : Ranking
# - Name    : Name de la compania
# - Country      : Country de procedencia de la compania
# - Sales    : Sales
# - Profits : Profits
# - Assets   : Assets
# - Market_value     : Market_value de la compania en el mercado
#
# Nota: cifras en millones de dolares
#
# Fuente: https://www.forbes.com/lists/global2000/#7e9e39675ac0

# Establecer directorio e importar datos

setwd("C:/Users/Julian/Desktop/Ciencia de datos/Inteligencia de negocios/1. Forbes")
getwd()
list.files()

forbes <- read.csv("Forbes 2000 2021.csv", sep = ";" )
View(forbes)

names(forbes)
names(forbes)<-c("Rank","Name","Country","Sales","Profits","Assets","Market_value")
dim(forbes) #observaciones y variables

class(forbes) 
str(forbes)
head(forbes, n=5)
tail(forbes, n=10)



forbes$Sales<-gsub('[,]','',forbes$Sales)
forbes$Sales<-as.numeric(gsub('[$]','',forbes$Sales))
sum(is.na(forbes$Sales))

forbes$Profits<-gsub('[,]','',forbes$Profits)
forbes$Profits<-gsub('[$]','',forbes$Profits)
forbes$Profits<-as.numeric(forbes$Profits)
sum(is.na(forbes$Profits))

forbes$Assets<-gsub('[,]','',forbes$Assets)
forbes$Assets<-gsub('[$]','',forbes$Assets)

sum(is.na(forbes$Assets))
forbes$ej<-as.numeric(forbes$Assets)
forbes[!complete.cases(forbes),]
forbes$Assets<-forbes$ej
forbes$ej<-NULL

forbes$Market_value<-gsub('[,]','',forbes$Market_value)
forbes$Market_value<-as.numeric(gsub('[$]','',forbes$Market_value))

sapply(X = forbes,FUN = mean)

#¿Hay datos faltantes?
any(is.na(forbes))
complete.cases(forbes)

forbes[complete.cases(forbes)==F,]
forbes[!complete.cases(forbes),]#espacio en blanco, cuáles son incompletas
#podemos ver la base fuente para revisar

#Porcentaje de datos faltantes

100*sum(!complete.cases(forbes))/2000

#Remover datos faltantes
forbes<-forbes[complete.cases(forbes),]
dim(forbes)

write.csv(x = forbes,file = 'forbes_cons.csv')
summary(forbes)
## 1999 registros y 7 variable

mean(forbes$Sales)
mean(forbes$Assets)

sapply(X = forbes,FUN = mean)
sort(tapply(X = forbes$Sales,INDEX = forbes$Country,FUN = sum))

#adjuntar base de datos, util cuando sólo hay una base
attach(forbes) #fija la base y deja buscar dentro de ella

#detach()
Sales


# Exploración de la base --------------------------------------------------

#Compañias mas valiosas

#Cuantil o percentil, Market_value que acumula porcentaje de la información
names(forbes)
#Compañias con Assets y Market_value superiores al percentil 99
?quantile
p99v<-quantile(x=Market_value, probs = .99) #probs. acumula probabilidad 99
p99a<-quantile(x=Assets, probs = .99)

forbes[(Market_value>p99v & Assets>p99a)==T,]

p90v<-quantile(x=Market_value, probs = .90) #probs. acumula probabilidad 99
p90a<-quantile(x=Assets, probs = .90)
p90s<-quantile(x=Sales, probs = .90)
p90p<-quantile(x=Profits, probs = .90)

nrow(forbes[(Market_value>p90v & Assets>p90a & Sales>p90s & Profits>p90p)==T,])

--------------------------------------------
# Recordemos la lógica de los operadores lógico
# T&F=F 
#F&F=F
#T&T=T
#------------------------------------------------

forbes[(Market_value>p99v) | (Assets>p99a),c("Name","Country")]

forbes[(Market_value>p99v) & (Assets>p99a),c("Name","Country")]


# Datos de las empresas colombiana ----------------------------------------

forbes[Country=="Colombia",] 

#subset(forbes,subset = Country=="Colombia")

# Datos de las compañias de sudamerica

table(Country)
which(table(Country)==max(table(Country)))
suda<-c("Argentina","Bolivia","Brazil","Chile","Colombia",
        "Ecuador","Guyana","Paraguay","Peru","Surinam","Uruguay",
        "Venezuela")

c(6,7,1,5,4,2,3)%in%c(1,2,3) #Los primeros estan en los segundos?
#Miremos otros ejemplos

Country%in%suda
forbes[Country%in%suda,c("Name","Country")]

fg_suda<-forbes[Country%in%suda,]

#Ordenar por Market_value
fg_suda[order(fg_suda$Sales,decreasing = T),c("Country","Market_value","Name","Sales")]

# arrange lo hace mas sencillo
library(dplyr)
fg_suda %>% 
  arrange(desc(Market_value)) %>% 
  select(Country,Name,Market_value)

# Conteo: variables cualitativas ------------------------------------------

# tabla de frecuencias absolutas

tabla<-table(Country)
class(tabla)
length(tabla) # Cuántos Countryes distintos hay (61)
dim(tabla)

#Tabla ordenada descendentemente de acuerdo a la frecuencia

tabla<-tabla[order(tabla,decreasing = T)] #que Countryes tiene mas empresas
tabla

#Posicion de colombia de acuerdo a la cantidad de compañias

tabla[names(tabla)=="Colombia"]
which(names(tabla)=="Colombia") #cuál es la posición en la que aparece T

which(names(tabla)=="Mexico")
which(names(tabla)=="Germany")


# Top 5 de Countryes ---------------------------------------------------------

head(tabla, n=5)
tail(tabla, n=5)

top5<-tabla[1:5]
top5_rel<-round(top5/1999,digits = 3) #porcentaje de concentracion empresas por Countryes
top5_rel
cb<-cumsum(top5_rel)
cbind(top5_rel,cb)
sum(top5_rel) #concentración de estos 5 Countryes
sum(top5)/1999


# Visualizaciones con libreria base ---------------------------------------

windows() #quartz()

# Barplot -----------------------------------------------------------------
barplot(height = top5_rel)

barplot(sort(table(fg_suda$Country),decreasing = T))

#Todos los graficos y las rutinas se pueden personalizar al nivel de detalle que desee
windows()
bp<-barplot(height = top5_rel,names.arg = c("US","CN","JP","UK","SK"),
            col = "purple",border = "blue",xlab = "Paises",ylab = "Porcentaje",
            main = "Países Top 5 Forbes Globe 2000", font.main=8,ylim = c(0,0.4),
            density = 50)

#font.main= fuente del texto. Buscar en google.
# density = densidad de las lineas

text(bp,top5_rel,round(top5_rel,1),cex=1,pos=3,col="blue",font=4,
     labels = paste0(round(top5_rel,1),"%"))
#cex tamanio
#pos posicion
#font fuente

bp2<-barplot(height = 100*top5_rel,names.arg = c("US","JP","CN","UK","SK"),
            col = "purple",border = "blue",xlab = "Country",ylab = "Porcentaje",
            main = "Países Top 5 Forbes Globe 2000", font.main=8,ylim = c(0,32))


# Variables cuantitativas -------------------------------------------------

plot(forbes)
names(forbes)

plot(Profits, type = "l", xlim = c(0,500),
     main = "Profits in fobes Global 2000",
     xlab = "Empresas de Forbes 2000", ylab = "Profits") #Dispersión indexado

options(scipen=999) #quitar notacion cientifica
plot(Profits,Assets, ylim = c(0,200000),xlim = c(0,50000))

hist(Profits, main = "Histograma de Profits", col = heat.colors(8),
     ylab = "Frecuencia absoluta",xlab = "Profits")

boxplot(fg_suda$Sales~fg_suda$Country)

##base de datos solo con variables cuantitativas
fg_cuanti<-forbes[,c("Sales","Profits","Assets","Market_value")]
fg_cuanti

#resumen multivariado
str(fg_cuanti)
summary(fg_cuanti)
var(forbes$Sales)
round(sum(forbes$Sales-mean(forbes$Sales)),3)
sd(forbes$Sales)
sqrt(var(forbes$Sales))

(sd(forbes$Sales)/mean(forbes$Sales))*100 # Coeficiente de variación
max(Sales)-min(Sales)

# entre 0% y 15% la dispersion es moderada, por encima es alta

a<-apply(fg_cuanti, MARGIN = 2,FUN = function(y) (sd(y)/mean(y))*100)
barplot(a,main = "Coeficiente de variación",ylab = "CV%",xlab = "Variable",
        col = colorRampPalette(c('blue', 'white', 'red'))(4))

#----------------------
#Graficos: examinar la distribución de una variable
windows(width = 10,height = 5)
par(mfrow=c(2,1)) #Fila columna

#Diagrama de caja

attach(fg_cuanti)
b<-boxplot(x=Profits,horizontal = T,bowex=.5,cex=.8,
           border = "blue",col = "lightblue",xlab="Profits")


#Histograma
h<-hist(x=Profits,freq = F,nclass = 50,border = "blue",col = "lightblue",
        xlab = "Profits",ylab = "Densidad",main = "")
#Titulo
title(main = "Profits compañias Forbes Globe 2000",font.main=4,
      outer = T,line = -2)

class(h)
summary(h)
h$counts

# Vamos a ver datos atipicos
## Rango intercuartílico

q3.Profits<-quantile(x=Profits,probs = .75)
q1.Profits<-quantile(x=Profits,probs = .25)
RI.Profits<-as.numeric(q3.Profits-q1.Profits) 
RI.Profits
IQR(Profits)

#Cantidad de datos atipicos superiores (test de Tukey)
sum(Profits>q3.Profits+1.5*RI.Profits) #F es 0 y T es 1
round(210*100/1999,2) #209 empresas atipicas, representan el 10.46%

sum(Profits<q1.Profits-1.5*RI.Profits)
round(91*100/1999,2)
#Cantidad de datos extremos
sum(Profits>q3.Profits+3*RI.Profits) #128datos extremos
round(128*100/1999,2) #6.35% de las empresas son extremos superiores

#Datos de compañias extremas superiores
ext<-forbes[Profits>q3.Assets+3*RI.Assets, c("Name","Country","Profits")]
#Organicemoslo descendentemente por las Profits
ext<-ext[order(ext$Profits,decreasing = T),]
View(ext)

# Miremos si hay relación entre las variables
windows()
plot(x=Sales,y=Profits)

m<-sum((Sales-mean(Sales))*(Profits-mean(Profits)))/sum((Sales-mean(Sales))^2)
b<-mean(Profits)-m*mean(Sales)

plot(x=Sales,y=Profits,cex=1.2,pch=16,col="darkgreen",
     ylab = "Profits (billones US)",xlab = "Sales (billones US)",
     main = "Profits frente a Sales")
grid(col='black')
abline(v=mean(Sales),col='red')
abline(h=mean(Profits),col='blue')
abline(a=b,b=m,col="red",lty=3,lwd=2)

#prisma de dispersogramas

pairs(fg_cuanti)
pairs(fg_cuanti,pch=16,cex=0.8,gap=0,xaxt="n",
      col="blue")

#Veamos qué mas opciones tenemos (gráficos interAssets)
install.packages("threejs")
library(threejs)
scatterplot3js(x=forbes$Sales,
               y=forbes$Profits,
               z=forbes$Assets, size = .2)

#-------------------------- 
#Qué tan fuerte o qué direccion tienen las variables

#Covarianza
#el signo de la variable indica el ripo de relación entre las variables
#La unidad de medida es mixta
cov(Sales,Profits)
cov(fg_cuanti)
#Matriz de covarianzas
View(cov(fg_cuanti))
isSymmetric(cov(fg_cuanti)) #simetria de la matriz

#Coeficiente de correlación de pearson
## coeficiente entre -1 y 1
cor(Sales,Profits)
View(round(cor(fg_cuanti),2))

#Ver correlacione sgráficas
# install.packages("corrplot")
library(corrplot)
windows()
cor(fg_cuanti)
cor.mtest(fg_cuanti)
corrplot(cor(fg_cuanti),diag = T)



coercion <- function(x){
  x <- gsub('[,]','',x)
  x <- gsub("[$]","",x)
  x <- as.numeric(x)
  return(x)
}


     