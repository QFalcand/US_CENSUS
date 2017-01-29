setwd("~/APT/Exo Datimpact")

appr = read.csv('~/APT/Exo Datimpact/us_census_full/census_income_learn.csv', header = FALSE)
test = read.csv('~/APT/Exo Datimpact/us_census_full/census_income_test.csv', header = FALSE)
#on change les noms de colonnes pour s'y retrouver
names(appr) = c('AAGE', 'ACLSWKR', 'ADTIND', 'ADTOCC', 'AHGA', 'AHRSPAY',
                'AHSCOL', 'AMARITL', 'AMJIND', 'MJOCC', 'ARACE' , 'AREORGN', 'ASEX',
                'AUNMEM', 'AUNTYPE', 'AWKSTAT','CAPGAIN','CAPLOSS','DIVVAL',
                'FILESTAT', 'GRINREG','GRINST', 'HHDFMX', 'HHDREL', 'MARSUPWT', 
                'MIGMTR1','MIGMTR3', 'MIGMTR4','MIGSAME', 'MIGSUN', 'NOEMP','PARENT', 
                'PEFNTVTY', 'PEMNTVTY', 'PENATVTY', 'PRCITSHP', 
                'SEOTR', 'VETQVA', 'VETYN', 'WKSWORK', 'Year', 'Revenu')
names(test) = names(appr)

#on déclare en facteurs les colonnes qui ne sont pas bien détectées
appr$Year = as.factor(appr$Year)
appr$ADTIND = as.factor(appr$ADTIND)
appr$ADTOCC = as.factor(appr$ADTOCC)
appr$SEOTR = as.factor(appr$SEOTR)
appr$VETYN = as.factor(appr$VETYN)

test$Year = as.factor(test$Year)
test$ADTIND = as.factor(test$ADTIND)
test$ADTOCC = as.factor(test$ADTOCC)
test$SEOTR = as.factor(test$SEOTR)
test$VETYN = as.factor(test$VETYN)

#bref descriptif des données 
i = 1
for (colonne in appr){
  print(names(appr)[i])
  resume = summary(colonne)
  print(resume)
  if (" ?" %in% names(resume)){
    cat("Proportion de valeurs manquantes", resume[" ?"]/sum(resume))
  }
  cat('\n\n')
  if (class(colonne) != "factor"){
    boxplot(colonne)
    legend('topleft', names(appr)[i])
  }
  i = i + 1
}
#on a des valeurs ? dans un certain nombre d'entrées : 
#éliminer les lignes correspondantes ou les laisser ou les remplacer par des Not in Universe ?
#le fichier texte décrivant les données fait état de duplicats, les laisser ?


