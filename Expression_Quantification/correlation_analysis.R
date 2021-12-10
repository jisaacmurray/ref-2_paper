library("ggpubr")
library(stringr)
library(dplyr)

args <- commandArgs(trailingOnly=TRUE)

if (length(args) != 3){
  stop("3 arguments must be supplied. Argument 1 is .csv file with data to be analyzed. Argument 2 is the type of correlation analysis to be performed. Argument 3 is the name of the column in the .csv file to which other groups are to be compared.")
}

df <- read.csv(args[1], header = TRUE, sep = ",", row.names = 1)

df <- sapply(df, as.numeric)

#my_data <- select(mtcars, mpg, disp, hp, drat, wt, qsec)

#print(as.numeric(unlist(df["ref.2_e1_prox_mean"])))
#print(as.numeric(unlist(df["X20201029_tbx.37_38_multisite_concatemer_ref.2_e1_418_long_adjacent_regions_2_L1"])))
#print(as.numeric(unlist((df)[as.numeric(c(args[4]))])))
#print(df[,34])
#class(df["ref.2_e1_prox_mean"])

#cor(as.numeric(unlist((df)[as.numeric(args[3])])), as.numeric(unlist((df)[as.numeric(args[4])])), method = args[2], use =  "complete.obs")
#correlation_matrix <- cor(df[,as.numeric(args[3])], df[,as.numeric(args[4])], method = args[2], use =  "complete.obs")
correlation_matrix <- cor(df, method = args[2], use = "pairwise.complete.obs")
#cor(df, use = "pairwise.complete.obs")

#print(correlation_matrix[,"ref.2_e1_prox_mean"])

write.csv(correlation_matrix[,args[3]], paste0(args[2], "_correlation.csv"), row.names = TRUE)