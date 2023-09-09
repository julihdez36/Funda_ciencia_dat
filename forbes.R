# Proyecto Forbes

# Establecemos diretorio --------------------------------------------------

setwd('C:/Users/USUARIO/Desktop/Ciencia de datos/Diplomado/Project forbes')
getwd()
list.files()


# Importación base y exploración ------------------------------------------

forbes21 <- read.csv(file = "Forbes 2000 2021.csv", sep = ';')

summary(forbes21)
str(forbes21)


# Limpieza ----------------------------------------------------------------

colnames(forbes21)<-c('Rank','Company','Country','Sales','Profits',
                      'Assets','Market_value')

remplazo <- function(x){
  x <-gsub('[,|$]','',x)
  return(x)
}

forbes21[,c(4:7)] <- apply(X = forbes21[,c(4:7)],MARGIN = 2,FUN = remplazo)

#ctrl+shift+r
# Coercionar --------------------------------------------------------------

forbes21[,4:7]<- apply(X = forbes21[,4:7],MARGIN = 2,FUN = as.numeric)


# Datos perdidos NA -------------------------------------------------------

sum(is.na(forbes21))

forbes21[!complete.cases(forbes21),]

# cuál es el porcentaje de datos vacios

100*sum(!complete.cases(forbes21))/nrow(forbes21)
# Si los vacios son menores al 1%, podemos eliminarlos

forbes21 <- forbes21[complete.cases(forbes21),]

str(forbes21)

#Hemos terminado la limpieza de los datos
# Extracción - Tranformación - Carga

write.csv(x = forbes21,file = 'frobesfinal.csv')


# Análisis exploratorio de datos ------------------------------------------

# EDA: intentar sacar información
# datos != información

forbes21 <- read.csv(file = "frobesfinal.csv")

forbes21 <- forbes21[,-1]

#Exploremos
str(forbes21)
summary(forbes21)

# Compañias mas valiosas para Forbes
# Assets, profits, sales, market value

# Percentil

# Las empresas con mas ganancias

x <- hist(forbes21$Profits)
x
x$breaks
x$counts
rbind(x$breaks,x$counts)

#Percentil 99

quantile(x = forbes21$Profits)
p99p <- quantile(x = forbes21$Profits, probs = .99)

forbes21[forbes21$Profits > p99p, c("Company","Country")]

# 1% mas alto en valor de mercado

p99mv <- quantile(x = forbes21$Market_value, probs = .99)
forbes21[forbes21$Market_value > p99mv, c('Company','Country')]

hist(forbes21$Market_value)

# del 1% mas alto en valor de mercado, cuales estan
# en el 10% con mas ventas

p99s <- quantile(forbes21$Sales,probs = .99)

forbes21[forbes21$Market_value > p99mv & forbes21$Sales > p99s,
         c('Company','Country')]

# Métodos numéricos

max(forbes21$Sales)

apply(forbes21[,4:7], MARGIN = 2, min)
apply(forbes21[,4:7], MARGIN = 2, max)
apply(forbes21[,4:7], MARGIN = 2, mean)
apply(forbes21[,4:7], MARGIN = 2, median)
apply(forbes21[,4:7], MARGIN = 2, var)
apply(forbes21[,4:7], MARGIN = 2, sd) #super importa
apply(forbes21[,4:7], MARGIN = 2, cv) #super importa

cv <- function(x){
  coeficiente = sd(x)/mean(x)
  return(coeficiente)
}

# Hay empresas colombianos

forbes21[forbes21$Country == 'Colombia',]
forbes21[forbes21$Country == 'Argentina',]

#Las empresas sudamericanas

suda<-c("Argentina","Bolivia","Brazil","Chile","Colombia",
        "Ecuador","Guyana","Paraguay","Peru","Surinam","Uruguay",
        "Venezuela")

forbes21$Country %in% suda

c(6,7,1,5,4,2,3)%in%c(1,2,3)

table_country <-table(forbes21$Country) # Tabla de frecuencia

x <- c(6,7,1,5,4,2,3)
x
order(x) # Indexación
sort(x) # valores ordenados

sort(table_country,decreasing = T)

#Empresas sudamericanas

f_suda <- forbes21[forbes21$Country %in% suda,]

table(f_suda$Country)
sort(table(f_suda$Country), decreasing = T)

forbes21[forbes21$Country == 'Venezuela',]

barplot(table(f_suda$Country), col = 'purple',density = 60,
        main = 'Empresas por paises sudamericanos',xlab = 'pais',
        ylab = 'Frecuencia')

# boxplot

hist(f_suda$Sales)
boxplot(f_suda$Sales ~ f_suda$Country, col = heat.colors(6),
        main = 'Boxplot de ventas por paises', ylab = 'Ventas')
grid(col='black')


#Veamos qué mas opciones tenemos (gráficos interAssets)
install.packages("threejs")
library(threejs)
scatterplot3js(x=forbes21$Sales,
               y=forbes21$Profits,
               z=forbes21$Assets, size = .2)
