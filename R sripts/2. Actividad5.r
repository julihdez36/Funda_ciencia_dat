#Directorio de trabajo ----

setwd('C:\\Users\\USUARIO\\Desktop\\Trabajo\\Iberoamericana\\Cursos\\Fundamentos a la ciencia de datos\\Actividad 5')
getwd()
list.files()

# Importación 
#install.packages('readxl')

library(readxl)
df <- read_excel("Información del curso(1-35).xlsx")
View(df)

colnames(df)

df <- df[,c(1,9,12,15,18,21,24,27)]

df$Estatura

remplazo <- function(x){
  x <-gsub('[años | Cm | cm | mts | , | . ]','',x)
  return(x)
}

df[,c(3,4)] <- apply(df[,c(3,4)],MARGIN = 2,FUN = remplazo)

df[,c(3,4)] <- apply(df[,c(3,4)],MARGIN = 2,FUN = as.numeric)


comversion_metros <- function(vector){
  y <- vector / 100
  return(y)
}

df$Estatura <- comversion_metros(as.numeric(df$Estatura))

colnames(df) <- c('ID','Sexo','Edad','Estatura','Ciudad',
                  'Musica_fav','Sit_sent','Deporte')

# Taller -----

# 1. Tablas de frecuencia

table(df$Sexo) # Frecuencia absoluta
100*prop.table(table(df$Sexo)) # Frecuencia relativa

table(df$Ciudad)

# 2.


barplot(table(df$Sexo),main = 'Gráfico de barras por sexo',
        ylab = 'Frecuencia',xlab = 'Sexo', col = 'purple', 
        horiz = T, xlim = c(0,30), density = 30,cex.names = par("cex.axis"))
grid(col = 'grey')

pie(prop.table(table(df$Sexo)),main = 'Diagrama de sectores',col = c('Tomato','Dark Salmon'))

# 3.

hist(df$Edad, col = 'white', main = 'Histograma edad')
boxplot(df$Edad,col = 'white', main = 'Boxplot edad',
        range = 1.5)

table(df$Edad)
mean(df$Edad)

bx <- boxplot(df$Edad,col = 'white', main = 'Boxplot edad',
        range = 0.5)
bx$out

# 4. 

summary(df$Estatura)
min(df$Estatura)
max(df$Estatura)
median(df$Estatura)
mean(df$Estatura)
quantile(df$Estatura)

# 5. dispersion

var(df$Estatura)
sd(df$Estatura)
100* sd(df$Estatura) / mean(df$Estatura) # >15% es dispersa

write.csv(x = df,file = 'df_final.csv')
