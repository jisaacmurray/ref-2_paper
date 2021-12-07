#setwd("Over500All")
#library("gplots")
source("functions.R")
source("PlotDefectSummaries.R")
source("PlotPositionDevs.R")
source("AnalyzeDivTimes.R")
source("AnalyzePositions.R")
source("AnalyzeRotation.R")

library(rgl)
library(gdata)
library(plotrix)


ref2_peak=ReadPeakExpression("CA20160203_ref-2_L2.csv")


StartDir=getwd()
ref2_cc_dev = AnalyzeDivTimes("ref2_mutant")
setwd(StartDir)

ref2_dev=AnalyzePositions("ref2_mutant", Expression=ref2_peak, CalculateNeighbors=TRUE)
##Can change to this once NN scores are calculated
##ref2_dev=AnalyzePositions("ref2_mutant", Expression=ref2_peak, CalculateNeighbors=FALSE)
setwd(StartDir)
AnalyzeRotation("ref2_mutant", ref2_peak)
setwd(StartDir)
##PlotDefectSummaries("ref2_mutant", ref2_peak, minDivTime=50)
PlotDefectSummaries("ref2_mutant", ref2_peak,sig=5,microns=5,expCutoff=100,minDivTime=70)

setwd(StartDir)
ref2MeanPosDevs = PlotDeviationsList(Name="ref2_mutant",exp=ref2_peak, t=200)
PlotExpVsDev("ref2_mutant",outfile="ref-2_mutant_ExpVsDev.pdf",exp=ref2_peak)
PlotExpVsDev("Richard_et_al_plus_comma_WT",outfile="WT_ExpVsDev_ref-2_exp.pdf",exp=ref2_peak)



