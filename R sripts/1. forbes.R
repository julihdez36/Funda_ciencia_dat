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

str(forbes)


# Data cleansing  ---------------------------------------------------------


# Cambiar tipado del conjunto de datos

numeric_format <- function(x){
                    x <- as.numeric(gsub('[$,]','',x))
                    return(x)
                  }

forbes[,4:7] <- apply(forbes[,4:7],MARGIN = 2,FUN = numeric_format)

str(forbes)

# Revisemos datos faltantes

any(is.na(forbes))

forbes[!complete.cases(forbes),] 

# Nuestro dato faltante es Bank of Greece, valoremos la posibilidad de imputar

forbes[forbes$Country == 'Greece',]

#Realizamos una imputación por media movil del grupo Greece
#Imputación simple

library(dplyr)

forbes <- forbes %>% 
  mutate(Assets = ifelse(Country == 'Greece', 
                         replace(Assets, is.na(Assets), mean(Assets, na.rm = TRUE)), 
                         Assets))

forbes[forbes$Country == 'Greece',]

obj_check <- forbes[forbes$Country == 'Greece',]
mean(obj_check$Assets, na.rm = T)

forbes[!complete.cases(forbes),]['Assets'] <- mean(obj_check$Assets, na.rm = T)
forbes[forbes$Country == 'Greece',]

#Cargamos el data set si queremos
# write.csv(x = forbes,file = 'forbes_cons.csv')


# Análisis exploratorio de datos ------------------------------------------

# Caracteristicas del conjunto de datos

# tabla de frecuencias absolutas

fre_abs <- table(forbes$Country)
length(fre_abs) # 61 paises tienen empresas en el ranking

#Top de paises con mas empresas rankeadas

fre_abs <- sort(fre_abs,decreasing = T)
head(fre_abs,10)

# Porcentaje de concentración de empresas por paises

freq_rel <- sort(prop.table(table(forbes$Country))*100,decreasing = T)

cumsum(freq_rel) #Frecuencia relativa acumulada

top <- cbind(fre_abs[1:10],freq_rel[1:10],cumsum(freq_rel)[1:10])
colnames(top) <-  c('ni','fi','Fi')
top <- as.data.frame(top)
top # Tabla de frecuencia
# Sólo 3 paises tienen el 55% de empresas mas importantes del mundo
# United states, China and Japan

#Posicion de colombia de acuerdo a la cantidad de compañias

fre_abs[names(fre_abs)=="Colombia"]
which(names(fre_abs)=="Colombia") #Posición 45 de Colombia

#Otras posiciones de paises

which(names(fre_abs)=="Mexico") # 26
which(names(fre_abs)=="Germany") #8

# Empresas sudamericanas

suda<-c("Argentina","Bolivia","Brazil","Chile","Colombia",
        "Ecuador","Guyana","Paraguay","Peru","Surinam","Uruguay",
        "Venezuela")

fb_suda<-forbes[forbes$Country%in%suda,]

# Métodos numéricos -------------------------------------------------------

summary(forbes)

colMeans(forbes[4:7])
apply(forbes[4:7], 2, median)
apply(forbes[4:7], 2, var)
apply(forbes[4:7], 2, sd)

CV <- function(x){
  coef = sd(x) / mean(x)
  return(coef)
}

CV(forbes$Sales)

apply(forbes[4:7],2,CV)

#Compañias mas valiosas

#¿Cómo definir las compañias mas valiosas?

#Compañias con Assets y Market_value superiores al percentil 99

p99v<-quantile(x=forbes$Market_value, probs = .99) #probs. acumula probabilidad 99
p99a<-quantile(x=forbes$Assets, probs = .99)

forbes[(forbes$Market_value>p99v & forbes$Assets>p99a),]

forbes[(forbes$Market_value>p99v) | (forbes$Assets>p99a),c("Name","Country")]


#Ordenar por Market_value

fb_suda %>% 
  arrange(desc(Market_value)) %>% 
  select(Country,Name,Market_value)


# Visualizaciones con libreria base ---------------------------------------

windows() #quartz()

# Barplot -----------------------------------------------------------------
barplot(height = top$fi)

barplot(sort(table(fb_suda$Country),decreasing = T))

#Todos los graficos y las rutinas se pueden personalizar al nivel de detalle que desee

windows()
bp<-barplot(height = top$fi[1:5],names.arg = c("US","CN","JP","UK","SK"),
            col = "purple",border = "blue",xlab = "Paises",ylab = "Porcentaje",
            main = "Países Top 5 Forbes Globe 2000", font.main=8, ylim = c(0,35),
            density = 50)
bp; grid()

#font.main= fuente del texto. Buscar en google.
# density = densidad de las lineas

text(bp,top$fi[1:5],round(top$fi[1:5],1),cex=1,pos=3,col="blue",font=4,
     labels = paste0(round(top$fi[1:5],1),"%"))

#cex tamanio
#pos posicion
#font fuente

bp2<-barplot(height = top$fi[1:5],names.arg = c("US","JP","CN","UK","SK"),
            col = "purple",border = "blue",xlab = "Country",ylab = "Porcentaje",
            main = "Países Top 5 Forbes Globe 2000", font.main=8,ylim = c(0,32))
bp2

# Variables cuantitativas -------------------------------------------------

plot(forbes[4:7])

plot(forbes$Profits, type = "l", xlim = c(0,500),
     main = "Profits in fobes Global 2000",
     xlab = "Empresas de Forbes 2000", ylab = "Profits") #Dispersión indexado

options(scipen=999) #quitar notacion cientifica
plot(forbes$Profits,forbes$Assets, ylim = c(0,200000),xlim = c(0,50000))

hist(forbes$Profits, main = "Histograma de Profits", col = heat.colors(8),
     ylab = "Frecuencia absoluta",xlab = "Profits")

boxplot(fb_suda$Sales~fb_suda$Country)

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

b<-boxplot(x=fg_cuanti$Profits,horizontal = T,bowex=.5,cex=.8,
           border = "blue",col = "lightblue",xlab="Profits")


#Histograma
h<-hist(x=fg_cuanti$Profits,freq = F,nclass = 50,border = "blue",col = "lightblue",
        xlab = "Profits",ylab = "Densidad",main = "")
#Titulo
title(main = "Profits compañias Forbes Globe 2000",font.main=4,
      outer = T,line = -2)

class(h)
summary(h)
h$counts

# Vamos a ver datos atipicos
## Rango intercuartílico

q3.Profits<-quantile(x=fg_cuanti$Profits,probs = .75)
q1.Profits<-quantile(x=fg_cuanti$Profits,probs = .25)
RI.Profits<-as.numeric(q3.Profits-q1.Profits) 
RI.Profits
IQR(fg_cuanti$Profits)

#Cantidad de datos atipicos superiores (test de Tukey)
sum(fg_cuanti$Profits>q3.Profits+1.5*RI.Profits) #F es 0 y T es 1
round(210*100/1999,2) #209 empresas atipicas, representan el 10.46%

sum(fg_cuanti$Profits<q1.Profits-1.5*RI.Profits)
round(91*100/1999,2)
#Cantidad de datos extremos
sum(fg_cuanti$Profits>q3.Profits+3*RI.Profits) #128datos extremos
round(128*100/1999,2) #6.35% de las empresas son extremos superiores

#Datos de compañias extremas superiores
ext<-forbes[fg_cuanti$Profits>q3.Assets+3*RI.Assets, c("Name","Country","Profits")]

#Organicemoslo descendentemente por las Profits
ext<-ext[order(ext$Profits,decreasing = T),]
View(ext)

# Miremos si hay relación entre las variables
windows()
plot(x=Sales,y=Profits)

m<-sum((Sales-mean(Sales))*(Profits-mean(Profits)))/sum((Sales-mean(Sales))^2)
b<-mean(Profits)-m*mean(Sales)

plot(x=fg_cuanti$Sales,y=fg_cuanti$Profits,cex=1.2,pch=16,col="darkgreen",
     ylab = "Profits (billones US)",xlab = "Sales (billones US)",
     main = "Profits frente a Sales")
grid(col='black')
abline(v=mean(fg_cuanti$Sales),col='red')
abline(h=mean(fg_cuanti$Profits),col='blue')
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
cov(fg_cuanti$Sales,fg_cuanti$Profits)
cov(fg_cuanti)
#Matriz de covarianzas
cov(fg_cuanti)
isSymmetric(cov(fg_cuanti)) #simetria de la matriz

#Coeficiente de correlación de pearson
## coeficiente entre -1 y 1
cor(fg_cuanti$Sales,fg_cuanti$Profits)
round(cor(fg_cuanti),2)

#Ver correlacione sgráficas
# install.packages("corrplot")
library(corrplot)
windows()
cor(fg_cuanti)
cor.mtest(fg_cuanti)
corrplot(cor(fg_cuanti),diag = T)






     