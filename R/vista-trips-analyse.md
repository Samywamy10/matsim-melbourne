---
title: "VISTA analyse"
author: "Maitreya Wagh"
date: "5/22/2018"
output:
  html_document:
    keep_md: yes
---

Here we have a few things. 
a) What does speed of travel depend on 
b) Nightworkers

Today, let's examine the various activities done




```r
Trips <- read.csv("../data/vista/2018-05-23-vista-2013-16/VISTA_2012_16_v1_SA1_CSV/T_VISTA12_16_SA1_V1.csv")
Stops <- read.csv("../data/vista/2018-05-23-vista-2013-16/VISTA_2012_16_v1_SA1_CSV/S_VISTA12_16_SA1_V1.csv")
table(Trips$STOPS)
```

```
## 
##      1      2      3      4      5      6      7      8      9 
## 119324   1451   5610   1164    892    188     45      7      3
```

Analysing trips separately for now


```r
oneStopTrip <- subset(Trips, Trips$STOP == 1)
oneStopTrip$Speed = (oneStopTrip$Dist1/oneStopTrip$Time1)*60
twoStopTrip <- subset(Trips, Trips$STOP == 2)
twoStopTrip$Speed = (twoStopTrip$Dist1/twoStopTrip$Time1)*60
threeStopTrip <- subset(Trips, Trips$STOP == 3)
threeStopTrip$Speed = (threeStopTrip$Dist1/threeStopTrip$Time1)*60
```


```r
library(ggplot2)
Scatterplot<-ggplot(oneStopTrip, aes(oneStopTrip$Mode1, oneStopTrip$Speed, colour=oneStopTrip$TRAVDOW))+geom_point(position="jitter")+geom_boxplot(alpha=0, colour="black")
Scatterplot
```

```
## Warning: Removed 3 rows containing non-finite values (stat_boxplot).
```

```
## Warning: Removed 3 rows containing missing values (geom_point).
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-3-1.png)<!-- -->



```r
library(ggplot2)
Scatterplot<-ggplot(oneStopTrip, aes(oneStopTrip$TRAVDOW, oneStopTrip$Speed, colour=oneStopTrip$TRAVDOW))+geom_point(position="jitter")+facet_grid(~oneStopTrip$Mode1)+geom_boxplot(alpha=0, colour="black")
Scatterplot
```

```
## Warning: Removed 3 rows containing non-finite values (stat_boxplot).
```

```
## Warning: Removed 3 rows containing missing values (geom_point).
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-4-1.png)<!-- -->
We see that day that does not matter much as the plot is very similar

```r
Scatterplot<-ggplot(oneStopTrip, aes(oneStopTrip$TRAVELPERIOD, oneStopTrip$Speed, colour=oneStopTrip$TRAVELPERIOD))+geom_point(position="jitter")+facet_grid(~oneStopTrip$Mode1)+geom_boxplot(alpha=0, colour="black")
Scatterplot
```

```
## Warning: Removed 3 rows containing non-finite values (stat_boxplot).
```

```
## Warning: Removed 3 rows containing missing values (geom_point).
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-5-1.png)<!-- -->


```r
Scatterplot<-ggplot(twoStopTrip, aes(twoStopTrip$TRAVELPERIOD, twoStopTrip$Speed, colour=twoStopTrip$TRAVELPERIOD))+geom_point(position="jitter")+facet_grid(~twoStopTrip$Mode1)+geom_boxplot(alpha=0, colour="black")
Scatterplot
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-6-1.png)<!-- -->


```r
Scatterplot<-ggplot(threeStopTrip, aes(threeStopTrip$TRAVELPERIOD, threeStopTrip$Speed, colour=threeStopTrip$TRAVELPERIOD))+geom_point(position="jitter")+facet_grid(~threeStopTrip$Mode1)+geom_boxplot(alpha=0, colour="black")
Scatterplot
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-7-1.png)<!-- -->






```r
Person <- read.csv("../data/vista/2018-05-23-vista-2013-16/VISTA_2012_16_v1_SA1_CSV/P_VISTA12_16_SA1_V1.csv")
Person$AgeGroup[Person$AGE < 21] <- "Child"
Person$AgeGroup[Person$AGE > 21] <- "Adult"
Person$AgeGroup[Person$AGE < 5] <- "Baby"

table (oneStopTrip$ORIGPLACE1)
```

```
## 
##                                         Accommodation 
##                          3                      54814 
##            Natural Feature                 Not Stated 
##                       2601                          0 
##                      Other         Place of Education 
##                       1940                      10682 
## Place of Personal Business         Recreational Place 
##                       4457                       6651 
##                      Shops               Social Place 
##                      15919                       6675 
##          Transport Feature                  Workplace 
##                       1199                      14383
```

```r
nightwork <- subset(oneStopTrip, oneStopTrip$ORIGPLACE1 == "Workplace")
```


```r
nightperson <- Person[Person$PERSID %in% nightwork$PERSID, ]
nightnonwork <- subset(nightperson, nightperson$ANYWORK == "No")
nightactivities_nonwork <- Trips[Trips$PERSID %in% nightnonwork$PERSID,]
```






c) Activities


```r
StopsFiltered <- Stops[, -c(6,7,9,12,14,15,17,16,18,21,23,25,27:50,61)]
StopsFiltered <- StopsFiltered[, -c(48:57,29,42:44)]
table(StopsFiltered$DESTPURP1)
```

```
## 
##            Accompany Someone                Buy Something 
##                         4173                        13870 
##                  Change Mode                    Education 
##                        21139                         4962 
##                      Go Home                   Not Stated 
##                        50451                            2 
##                Other Purpose            Personal Business 
##                          486                         7163 
## Pick-up or Deliver Something  Pick-up or Drop-off Someone 
##                         1841                         9331 
##                 Recreational                       Social 
##                         6773                        13031 
##                 Work Related 
##                        16476
```

```r
StopsFiltered$AVESPEED <- as.numeric(as.character(StopsFiltered$AVESPEED))
```

```
## Warning: NAs introduced by coercion
```

```r
StopsFiltered$DURATION <- as.numeric(as.character(StopsFiltered$DURATION))
```

```
## Warning: NAs introduced by coercion
```

```r
ActivityAnalysis <- StopsFiltered[, c(6,7,12, 23, 24, 28)]
ActivityAnalysis <- aggregate(. ~ ActivityAnalysis$DESTPURP1 + ActivityAnalysis$TRAVMONTH + ActivityAnalysis$TRAVDOW + ActivityAnalysis$MAINMODE, data = ActivityAnalysis, FUN = mean, na.rm = TRUE)
ActivityAnalysis <- ActivityAnalysis[, -c(5,6,7,9)]
ActivityAnalysis <- ActivityAnalysis[order(ActivityAnalysis$`ActivityAnalysis$TRAVMONTH`, ActivityAnalysis$`ActivityAnalysis$TRAVDOW`, ActivityAnalysis$`ActivityAnalysis$MAINMODE`),]
```


```r
ActivityAnalysisTab <- StopsFiltered[, c(6,7,12, 23, 24, 28)]
ActivityAnalysisTab <- as.data.frame(table(ActivityAnalysisTab$DESTPURP1, ActivityAnalysisTab$MAINMODE))
ActivityAnalysisTab <- ActivityAnalysisTab[order(ActivityAnalysisTab$Var1, -ActivityAnalysisTab$Freq),]
```

Other puprose, Recreational and Social are three categories which 









Finding distribution of activities based on days


```r
ActivityAnalysisDay <- as.data.frame(table(StopsFiltered$DESTPURP1,StopsFiltered$MAINMODE,StopsFiltered$TRAVDOW))
ActivityAnalysisDay <- ActivityAnalysisDay[order(ActivityAnalysisDay$Var1,ActivityAnalysisDay$Var2,ActivityAnalysisDay$Var3),]
ActivityAnalysisDay <- subset(ActivityAnalysisDay[ActivityAnalysisDay$Freq>90,])
table(StopsFiltered$MAINMODE)
```

```
## 
##           Bicycle        Motorcycle             Other        Public Bus 
##              2228               292               401              2325 
##        School Bus              Taxi             Train              Tram 
##               615               407              5699              2203 
##    Vehicle Driver Vehicle Passenger           Walking 
##             68151             31246             36131
```

```r
StopsFiltered$Isweekend <- ifelse(StopsFiltered$TRAVDOW == "Sunday" | StopsFiltered$TRAVDOW == "Saturday", "Weekend", "Weekday")
```




```r
par(mfrow = c(1,2))

table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
```

```
##                    
##                     Weekday Weekend
##   Bicycle              1728     500
##   Motorcycle            231      61
##   Other                 297     104
##   Public Bus           2028     297
##   School Bus            613       2
##   Taxi                  294     113
##   Train                5115     584
##   Tram                 1945     258
##   Vehicle Driver      53386   14765
##   Vehicle Passenger   21296    9950
##   Walking             29564    6567
```

```r
Wkdpriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekday")
Wkdpriv <- subset(Wkdpriv[(Wkdpriv$MAINMODE == "Vehicle Driver"| Wkdpriv$MAINMODE == "Vehicle Passenger"| Wkdpriv$MAINMODE== "Walking"),])
Wkdpriv <- as.data.frame(table(Wkdpriv$MAINMODE))
Wkdpriv <- subset(Wkdpriv[Wkdpriv$Freq>0,])
cols <- rainbow(nrow(Wkdpriv));
pie(Wkdpriv$Freq, labels = paste0(round(100*Wkdpriv$Freq /sum(Wkdpriv$Freq),2),Wkdpriv$Var1), col = cols, main = "Weekday Private");

table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
```

```
##                    
##                     Weekday Weekend
##   Bicycle              1728     500
##   Motorcycle            231      61
##   Other                 297     104
##   Public Bus           2028     297
##   School Bus            613       2
##   Taxi                  294     113
##   Train                5115     584
##   Tram                 1945     258
##   Vehicle Driver      53386   14765
##   Vehicle Passenger   21296    9950
##   Walking             29564    6567
```

```r
Wkepriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekend")
Wkepriv <- subset(Wkepriv, (Wkepriv$MAINMODE == "Vehicle Driver"| Wkepriv$MAINMODE == "Vehicle Passenger"| Wkepriv$MAINMODE== "Walking"))
Wkepriv <- as.data.frame(table(Wkepriv$MAINMODE))
Wkepriv <- subset(Wkepriv[Wkepriv$Freq>0,])
cols <- rainbow(nrow(Wkepriv));
pie(Wkepriv$Freq, labels = paste0(round(100*Wkepriv$Freq/sum(Wkepriv$Freq),2),Wkepriv$Var1), col = cols, main = "Weekend Private");
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-13-1.png)<!-- -->

```r
#Public transport

par(mfrow = c(1,2))

table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
```

```
##                    
##                     Weekday Weekend
##   Bicycle              1728     500
##   Motorcycle            231      61
##   Other                 297     104
##   Public Bus           2028     297
##   School Bus            613       2
##   Taxi                  294     113
##   Train                5115     584
##   Tram                 1945     258
##   Vehicle Driver      53386   14765
##   Vehicle Passenger   21296    9950
##   Walking             29564    6567
```

```r
Wkdpub <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekday")
Wkdpub <- subset(Wkdpub[(Wkdpub$MAINMODE != "Vehicle Driver"& Wkdpub$MAINMODE != "Vehicle Passenger" & Wkdpub$MAINMODE!= "Walking"),])
Wkdpub <- as.data.frame(table(Wkdpub$MAINMODE))
Wkdpub <- subset(Wkdpub[Wkdpub$Freq>0,])
cols <- rainbow(nrow(Wkdpub));
pie(Wkdpub$Freq, labels = paste0(round(100*Wkdpub$Freq /sum(Wkdpub$Freq),2),Wkdpub$Var1), col = cols, main = "Weekday Public");

table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
```

```
##                    
##                     Weekday Weekend
##   Bicycle              1728     500
##   Motorcycle            231      61
##   Other                 297     104
##   Public Bus           2028     297
##   School Bus            613       2
##   Taxi                  294     113
##   Train                5115     584
##   Tram                 1945     258
##   Vehicle Driver      53386   14765
##   Vehicle Passenger   21296    9950
##   Walking             29564    6567
```

```r
Wkepub <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekend")
Wkepub <- subset(Wkepub, (Wkepub$MAINMODE != "Vehicle Driver"& Wkepub$MAINMODE != "Vehicle Passenger"& Wkepub$MAINMODE!= "Walking"))
Wkepub <- as.data.frame(table(Wkepub$MAINMODE))
Wkepub <- subset(Wkepub[Wkepub$Freq>0,])
cols <- rainbow(nrow(Wkepub));
pie(Wkepub$Freq, labels = paste0(round(100*Wkepub$Freq/sum(Wkepub$Freq),2),Wkepub$Var1), col = cols, main = "Weekend Public") 
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-13-2.png)<!-- -->

```r
# par(mfrow = c(1,3))
# table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
# Wkdpriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekday")
# Wkdpriv <- subset(Wkdpriv[(Wkdpriv$MAINMODE == "Vehicle Driver"| Wkdpriv$MAINMODE == "Vehicle Passenger"| Wkdpriv$MAINMODE== "Walking"),])
# Wkdpriv <- as.data.frame(table(Wkdpriv$MAINMODE))
# percentlabels<- round(100*Wkdpriv$Freq /sum(Wkdpriv$Freq), 1)
# percentlabels <- paste(percentlabels, Wkdpriv$Var1)
# pielabels<- paste(percentlabels, "%", sep="")
# pie(Wkdpriv$Freq, labels = pielabels, col = rainbow(length(pielabels)))
# 
# table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
# Wkepriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekend")
# Wkepriv <- subset(Wkepriv, (Wkepriv$MAINMODE == "Vehicle Driver"| Wkepriv$MAINMODE == "Vehicle Passenger"| Wkepriv$MAINMODE== "Walking"))
# Wkepriv <- as.data.frame(table(Wkepriv$MAINMODE))
# percentlabels<- round(100*Wkepriv$Freq /sum(Wkepriv$Freq), 1)
# percentlabels <- paste(percentlabels, Wkepriv$Var1)
# pielabels<- paste(percentlabels, "%", sep="")
# pie(Wkepriv$Freq, labels = pielabels, col = rainbow(length(pielabels)))
# plot.new()
# legend("left",legend=pielabels, fill=grey.colors(3), box.lty=0, title="Mode")
# 
# par(mfrow = c(1,2))
# 
# table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
# Wkdpriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekday")
# Wkdpriv <- subset(Wkdpub, (Wkdpub$MAINMODE == "Vehicle Driver"| Wkdpub$MAINMODE == "Vehicle Passenger"| Wkdpub$MAINMODE== "Walking"))Wkdpriv <- as.data.frame(table(Wkdpriv$MAINMODE))
# Wkdpriv$Freq = Wkdpriv$Freq
# percentlabels<- round(100*Wkdpriv$Freq /sum(Wkdpriv$Freq), 1)
# percentlabels <- paste(percentlabels, Wkdpriv$Var1)
# pielabels<- paste(percentlabels, "%", sep="")
# pie(Wkdpriv$Freq, labels = pielabels, col = rainbow(length(pielabels)))
# 
# table(StopsFiltered$MAINMODE, StopsFiltered$Isweekend)
# Wkepriv <- subset(StopsFiltered, StopsFiltered$Isweekend == "Weekend")
# Wkepriv <- subset(Wkepub, (Wkepub$MAINMODE == "Vehicle Driver"| Wkepub$MAINMODE == "Vehicle Passenger"| Wkepub$MAINMODE== "Walking"))
# Wkepriv <- as.data.frame(table(Wkepriv$MAINMODE))
# Wkepriv$Freq = Wkepriv$Freq
# percentlabels<- round(100*Wkepriv$Freq /sum(Wkepriv$Freq), 1)
# percentlabels <- paste(percentlabels, Wkepriv$Var1)
# pielabels<- paste(percentlabels, "%", sep="")
# pie(Wkepriv$Freq, labels = pielabels, col = rainbow(length(pielabels)))
```



```r
par(mfrow = c(1,2))
priv <- subset(StopsFiltered[(StopsFiltered$MAINMODE == "Vehicle Driver"| StopsFiltered$MAINMODE == "Vehicle Passenger"| StopsFiltered$MAINMODE== "Walking"),])
g <- ggplot(priv, aes(priv$MAINMODE))
g + geom_bar(aes(fill = priv$TRAVDOW))
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-14-1.png)<!-- -->

```r
pub <- subset(StopsFiltered[(StopsFiltered$MAINMODE != "Vehicle Driver"& StopsFiltered$MAINMODE != "Vehicle Passenger" & StopsFiltered$MAINMODE!= "Walking"),])
g <- ggplot(pub, aes(pub$MAINMODE))
g + geom_bar(aes(fill = pub$TRAVDOW))
```

![](vista-trips-analyse_files/figure-html/unnamed-chunk-14-2.png)<!-- -->
