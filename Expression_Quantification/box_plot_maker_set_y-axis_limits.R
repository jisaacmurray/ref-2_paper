library('beeswarm')

args <- commandArgs(trailingOnly=TRUE)

if (length(args) < 7){
  stop("7 arguments must be supplied. Argument 1 is the name of the input .csv file. Argument 2 is the title of the plot. Argument 3 is the x axis label. Argument 4 is the y axis label. Argument 5 is the y axis minimum limit. Argument 6 is the y axis maximum limit. Arguments 7 and following are experimental groups being plotted as indicated in input .csv file.", call. = FALSE) 
}

df_difference <- read.csv(args[1], header = TRUE, sep = ",", row.names = 1)

#print(df_difference)

df_difference_plot <- df_difference[,args[7:length(args)]]

#print(df_difference_plot)
#print(colnames(df_difference_plot))
#print(class(df_difference_plot))

if (length(args) > 7){
boxplot(df_difference_plot, boxlty = 0, whisklty = 1, staplelty = 0, medcol="black", vertical = TRUE, main=args[2], xlab=args[3], ylab=args[4], ylim=c(as.numeric(args[5]),as.numeric(args[6])), xaxt='n', yaxt='n'); axis(1, at=c(1:ncol(df_difference_plot)), labels=FALSE, lty=0, tck=0); axis(2, lty=1, tck=0.025); text(x = 1:ncol(df_difference_plot),
                                                                                                                                                                                                                                                                                    y = par("usr")[3] - 0.45,
                                                                                                                                                                                                                                                                                    labels = colnames(df_difference_plot),
                                                                                                                                                                                                                                                                                    xpd = NA,
                                                                                                                                                                                                                                                                                    ## Rotate the labels by 35 degrees.
                                                                                                                                                                                                                                                                                    srt = 35, adj=0.965,
                                                                                                                                                                                                                                                                                    cex = 1.2)
} else if (length(args) == 7){
  boxplot(df_difference_plot, boxlty = 0, whisklty = 1, staplelty = 0, medcol="black", vertical = TRUE, main=args[2], xlab=args[3], ylab=args[4], ylim=c(as.numeric(args[5]),as.numeric(args[6])), xaxt='n', yaxt='n'); axis(1, at=c(1), labels=FALSE, lty=0, tck=0); axis(2, lty=1, tck=0.025); text(x = 1,
                                                                                                                                                                                                                                                                              y = par("usr")[3] - 0.45,
                                                                                                                                                                                                                                                                              labels = args[7],
                                                                                                                                                                                                                                                                              xpd = NA,
                                                                                                                                                                                                                                                                              ## Rotate the labels by 35 degrees.
                                                                                                                                                                                                                                                                              srt = 35, adj=0.965,
                                                                                                                                                                                                                                                                              cex = 1.2)
}

beeswarm(df_difference_plot, method="swarm", vertical=TRUE, pch=16, col=1:1, add=T)

#text("Expression Difference" ~ "Fragment", labels=df_difference[,1], data=df_difference, cex=0.5, pos=4)