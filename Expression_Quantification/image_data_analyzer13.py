import sys
import glob
from scipy import stats
import numpy
import os

if len(sys.argv) == 9:		###This script can accept 9 to 29 arguments. [0] = script name [1] = gene [2] = lineage1 [3] = lineage2 [4] = negativeControlLineage [5] = positiveControlLineage [6] = excludedGenerations [7] = excludedCell [8] = min_expression_cutoff [9]-[28] = treatments1-20
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
elif len(sys.argv) == 10:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
elif len(sys.argv) == 11:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
elif len(sys.argv) == 12:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
elif len(sys.argv) == 13:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
elif len(sys.argv) == 14:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
elif len(sys.argv) == 15:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
elif len(sys.argv) == 16:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
elif len(sys.argv) == 17:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
elif len(sys.argv) == 18:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
elif len(sys.argv) == 19:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
elif len(sys.argv) == 20:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
elif len(sys.argv) == 21:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
elif len(sys.argv) == 22:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
elif len(sys.argv) == 23:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
elif len(sys.argv) == 24:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
elif len(sys.argv) == 25:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
	treatment16 = sys.argv[24]
elif len(sys.argv) == 26:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
	treatment16 = sys.argv[24]
	treatment17 = sys.argv[25]
elif len(sys.argv) == 27:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
	treatment16 = sys.argv[24]
	treatment17 = sys.argv[25]
	treatment18 = sys.argv[26]
elif len(sys.argv) == 28:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
	treatment16 = sys.argv[24]
	treatment17 = sys.argv[25]
	treatment18 = sys.argv[26]
	treatment19 = sys.argv[27]
elif len(sys.argv) == 29:
	gene = sys.argv[1]
	lineage1 = sys.argv[2]
	lineage2 = sys.argv[3]
	negativeControlLineage = sys.argv[4]
	positiveControlLineage = sys.argv[5]
	excludedGenerations = sys.argv[6]
	excludedCell = sys.argv[7]
	min_expression_cutoff = sys.argv[8]
	treatment1 = sys.argv[9]
	treatment2 = sys.argv[10]
	treatment3 = sys.argv[11]
	treatment4 = sys.argv[12]
	treatment5 = sys.argv[13]
	treatment6 = sys.argv[14]
	treatment7 = sys.argv[15]
	treatment8 = sys.argv[16]
	treatment9 = sys.argv[17]
	treatment10 = sys.argv[18]
	treatment11 = sys.argv[19]
	treatment12 = sys.argv[20]
	treatment13 = sys.argv[21]
	treatment14 = sys.argv[22]
	treatment15 = sys.argv[23]
	treatment16 = sys.argv[24]
	treatment17 = sys.argv[25]
	treatment18 = sys.argv[26]
	treatment19 = sys.argv[27]
	treatment20 = sys.argv[28]
		
else:
	print ("You must enter the gene name, Wild Type expressing lineage, its sister lineage, a negative control lineage, a positive control lineage, a number of cell generations to exclude, an excluded cell, and a minimum expression level cut off. \nIf no negative control lineage is to be used, type \"none\". \nIf no positive control lineage is to be used, type \"none\". \nIf no excluded cell is to be used, type \"none\". \nIf no minimum expression level cutoff is to be used, type \"none\". \nAlso, enter the names of treatments as indicated in the file name (ie. pop-1i). \nDo not enter more than 20 treatments. Exiting.")
	sys.exit()

def mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)	
fileName = gene + "_image_analysis.csv"
outFile = open(fileName, 'w')
#outFile.write("cell" + "\t" + "20160218_tbx-35_L1" + "\n")
embryos = {}
cellNames = []

inputList = glob.glob("CA*.csv")
#print inputList
for file in inputList:	###Collect desired data from list of CA files.
	inFile = file
	input = open(inFile, 'r')
	input.readline()
	cells = {}
	for line in input:
		line = line.rstrip('\n')
		data = line.split(',')
		info = {"cellTime":data[0], "cell":data[1], "time":data[2], "none":data[3], "global":data[4], "local": data[5], "blot":data[6], "cross":data[7], "z":data[8], "x":data[9], "y":data[10], "size":data[11], "gweight":data[12]}
		#print str(info["cell"]) + "," + str(len(info["cell"]))
		if lineage1 in info["cell"]:
			if lineage2 not in info["cell"]:
				if negativeControlLineage not in info["cell"]:
					if positiveControlLineage not in info["cell"]:
						if excludedCell not in info["cell"]:
							if len(info["cell"]) > len(lineage1) + (int(excludedGenerations) - 1):
								if min_expression_cutoff != "none":
									if float(info["blot"]) >= float(min_expression_cutoff):
										#print ("info[blot] >= 0")
										#print (type(info["blot"]))
										cells[info["cell"]] = str(float(info["blot"])-float(min_expression_cutoff))
									elif float(info["blot"]) < float(min_expression_cutoff):
										#print ("info[blot] < 0")
										#print (type(info["blot"]))
										cells[info["cell"]] = "0"
								else :
									cells[info["cell"]] = info["blot"]
				#embryos["20160218_tbx-35_L1"] = {embryos["20160218_tbx-35_L1"], cells}
				#outFile.write(info["cell"] + "\t"+ info["blot"] + "\n")
		elif lineage2 in info["cell"]:
			if negativeControlLineage not in info["cell"]:
				if positiveControlLineage not in info["cell"]:
					if excludedCell not in info["cell"]:
						if len(info["cell"]) > len(lineage2) + (int(excludedGenerations) - 1):
							if min_expression_cutoff != "none":
								if float(info["blot"]) >= float(min_expression_cutoff):
									cells[info["cell"]] = str(float(info["blot"])-float(min_expression_cutoff))
								elif float(info["blot"]) < float(min_expression_cutoff):
									cells[info["cell"]] = "0"
							else :
								cells[info["cell"]] = info["blot"]
		elif negativeControlLineage in info["cell"]:
			if positiveControlLineage not in info["cell"]:
				if excludedCell not in info["cell"]:
					if len(info["cell"]) > len(negativeControlLineage) + (int(excludedGenerations) - 1):
						if min_expression_cutoff != "none":
							if float(info["blot"]) >= float(min_expression_cutoff):
								cells[info["cell"]] = str(float(info["blot"])-float(min_expression_cutoff))
							elif float(info["blot"]) < float(min_expression_cutoff):
								cells[info["cell"]] = "0"
						else :
							cells[info["cell"]] = info["blot"]
		elif positiveControlLineage in info["cell"]:
			if excludedCell not in info["cell"]:
				if len(info["cell"]) > len(positiveControlLineage) + (int(excludedGenerations) - 1):
					if min_expression_cutoff != "none":
						if float(info["blot"]) >= float(min_expression_cutoff):
							cells[info["cell"]] = str(float(info["blot"])-float(min_expression_cutoff))
						elif float(info["blot"]) < float(min_expression_cutoff):
							cells[info["cell"]] = "0"
					else :
						cells[info["cell"]] = info["blot"]
		#print cells
	embryos[file.lstrip("CA").rstrip(".csv")] = cells
			#outFile.write(info["cell"] + "\t" + info["blot"] + "\n")
	input.close()
#for cell in sorted(embryos["20160218_tbx-35_L2"].keys()):
#	print cell + "\t" + embryos["20160218_tbx-35_L2"][cell]

outFile.write("cells,") #+ embryos.keys.replace(',', '\t') + "\n")
for name in sorted(embryos.keys()):		###Write out WT embryo names.
	if len(sys.argv) == 29:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	if treatment16 not in name:
																		if treatment17 not in name:
																			if treatment18 not in name:
																				if treatment19 not in name:
																					if treatment20 not in name:
																						outFile.write(name + ",")
	elif len(sys.argv) == 28:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	if treatment16 not in name:
																		if treatment17 not in name:
																			if treatment18 not in name:
																				if treatment19 not in name:
																					outFile.write(name + ",")
	elif len(sys.argv) == 27:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	if treatment16 not in name:
																		if treatment17 not in name:
																			if treatment18 not in name:
																				outFile.write(name + ",")
	elif len(sys.argv) == 26:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	if treatment16 not in name:
																		if treatment17 not in name:
																			outFile.write(name + ",")	
	elif len(sys.argv) == 25:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	if treatment16 not in name:
																		outFile.write(name + ",")
	elif len(sys.argv) == 24:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																if treatment15 not in name:
																	outFile.write(name + ",")
	elif len(sys.argv) == 23:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															if treatment14 not in name:
																outFile.write(name + ",")	
	elif len(sys.argv) == 22:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														if treatment13 not in name:
															outFile.write(name + ",")	
	elif len(sys.argv) == 21:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													if treatment12 not in name:
														outFile.write(name + ",")
	elif len(sys.argv) == 20:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												if treatment11 not in name:
													outFile.write(name + ",")	
	elif len(sys.argv) == 19:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											if treatment10 not in name:
												outFile.write(name + ",")
	elif len(sys.argv) == 18:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										if treatment9 not in name:
											outFile.write(name + ",")
	elif len(sys.argv) == 17:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									if treatment8 not in name:
										outFile.write(name + ",")	
	elif len(sys.argv) == 16:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								if treatment7 not in name:
									outFile.write(name + ",")
	elif len(sys.argv) == 15:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							if treatment6 not in name:
								outFile.write(name + ",")		
	elif len(sys.argv) == 14:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						if treatment5 not in name:
							outFile.write(name + ",")
	elif len(sys.argv) == 13:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					if treatment4 not in name:
						outFile.write(name + ",")	
	elif len(sys.argv) == 12:
		if treatment1 not in name:
			if treatment2 not in name:
				if treatment3 not in name:
					outFile.write(name + ",")	
	elif len(sys.argv) == 11:
		if treatment1 not in name:
			if treatment2 not in name:
				outFile.write(name + ",")
	elif len(sys.argv) == 10:
		if treatment1 not in name:
			outFile.write(name + ",")
	elif len(sys.argv) == 9:
		outFile.write(name + ",")																																																																																																																																																								
for name in sorted(embryos.keys()):		###Write out names of embryos for each treatment.
	if len(sys.argv) >= 10:
		if treatment1 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 11:
		if treatment2 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 12:	
		if treatment3 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 13:	
		if treatment4 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 14:	
		if treatment5 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 15:	
		if treatment6 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 16:	
		if treatment7 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 17:	
		if treatment8 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 18:	
		if treatment9 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 19:	
		if treatment10 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 20:	
		if treatment11 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 21:	
		if treatment12 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 22:	
		if treatment13 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 23:	
		if treatment14 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 24:	
		if treatment15 in name:
			outFile.write(name + ",")	
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 25:	
		if treatment16 in name:
			outFile.write(name + ",")	
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 26:	
		if treatment17 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 27:	
		if treatment18 in name:
			outFile.write(name + ",")	
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 28:	
		if treatment19 in name:
			outFile.write(name + ",")
for name in sorted(embryos.keys()):
	if len(sys.argv) >= 29:	
		if treatment20 in name:
			outFile.write(name + ",")
outFile.seek(-1, os.SEEK_CUR)
outFile.write("\n")
for cellss in embryos.values():
	#print cellss
	for cel in cellss.keys():
		if cel not in cellNames:
			cellNames.append(cel)
for name in sorted(cellNames):
	outFile.write(name + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) == 29:		###Write out blot values of WT embryos.
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if treatment16 not in embName:
																			if treatment17 not in embName:
																				if treatment18 not in embName:
																					if treatment19 not in embName:
																						if treatment20 not in embName:
																							if name not in embryos[embName].keys():
																								outFile.write(",")
																							elif name in embryos[embName].keys():
																								outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 28:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if treatment16 not in embName:
																			if treatment17 not in embName:
																				if treatment18 not in embName:
																					if treatment19 not in embName:
																						if name not in embryos[embName].keys():
																							outFile.write(",")
																						elif name in embryos[embName].keys():
																							outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 27:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if treatment16 not in embName:
																			if treatment17 not in embName:
																				if treatment18 not in embName:
																					if name not in embryos[embName].keys():
																						outFile.write(",")
																					elif name in embryos[embName].keys():
																						outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 26:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if treatment16 not in embName:
																			if treatment17 not in embName:
																				if name not in embryos[embName].keys():
																					outFile.write(",")
																				elif name in embryos[embName].keys():
																					outFile.write(embryos[embName][name] + ",")	
		elif len(sys.argv) == 25:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if treatment16 not in embName:
																			if name not in embryos[embName].keys():
																				outFile.write(",")
																			elif name in embryos[embName].keys():
																				outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 24:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if treatment15 not in embName:
																		if name not in embryos[embName].keys():
																			outFile.write(",")
																		elif name in embryos[embName].keys():
																			outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 23:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if treatment14 not in embName:
																	if name not in embryos[embName].keys():
																		outFile.write(",")
																	elif name in embryos[embName].keys():
																		outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 22:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if treatment13 not in embName:
																if name not in embryos[embName].keys():
																	outFile.write(",")
																elif name in embryos[embName].keys():
																	outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 21:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if treatment12 not in embName:
															if name not in embryos[embName].keys():
																outFile.write(",")
															elif name in embryos[embName].keys():
																outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 20:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if treatment11 not in embName:
														if name not in embryos[embName].keys():
															outFile.write(",")
														elif name in embryos[embName].keys():
															outFile.write(embryos[embName][name] + ",")	
		elif len(sys.argv) == 19:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if treatment10 not in embName:
													if name not in embryos[embName].keys():
														outFile.write(",")
													elif name in embryos[embName].keys():
														outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 18:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if treatment9 not in embName:
												if name not in embryos[embName].keys():
													outFile.write(",")
												elif name in embryos[embName].keys():
													outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 17:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if treatment8 not in embName:
											if name not in embryos[embName].keys():
												outFile.write(",")
											elif name in embryos[embName].keys():
												outFile.write(embryos[embName][name] + ",")	
		elif len(sys.argv) == 16:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if treatment7 not in embName:
										if name not in embryos[embName].keys():
											outFile.write(",")
										elif name in embryos[embName].keys():
											outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 15:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if treatment6 not in embName:
									if name not in embryos[embName].keys():
										outFile.write(",")
									elif name in embryos[embName].keys():
										outFile.write(embryos[embName][name] + ",")		
		elif len(sys.argv) == 14:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if treatment5 not in embName:
								if name not in embryos[embName].keys():
									outFile.write(",")
								elif name in embryos[embName].keys():
									outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 13:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if treatment4 not in embName:
							if name not in embryos[embName].keys():
								outFile.write(",")
							elif name in embryos[embName].keys():
								outFile.write(embryos[embName][name] + ",")	
		elif len(sys.argv) == 12:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if treatment3 not in embName:
						if name not in embryos[embName].keys():
							outFile.write(",")
						elif name in embryos[embName].keys():
							outFile.write(embryos[embName][name] + ",")	
		elif len(sys.argv) == 11:
			if treatment1 not in embName:
				if treatment2 not in embName:
					if name not in embryos[embName].keys():
						outFile.write(",")
					elif name in embryos[embName].keys():
						outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 10:
			if treatment1 not in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
		elif len(sys.argv) == 9:
			if name not in embryos[embName].keys():
				outFile.write(",")
			elif name in embryos[embName].keys():
				outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):		###Write out blot values for embryos with each treatment.
		if len(sys.argv) >= 10:
			if treatment1 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 11:
			if treatment2 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 12:
			if treatment3 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 13:
			if treatment4 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 14:
			if treatment5 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 15:
			if treatment6 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 16:
			if treatment7 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 17:
			if treatment8 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")								
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 18:
			if treatment9 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")	
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 19:
			if treatment10 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 20:
			if treatment11 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")							
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 21:
			if treatment12 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")			
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 22:
			if treatment13 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")	
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 23:
			if treatment14 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")			
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 24:
			if treatment15 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")			
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 25:
			if treatment16 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 26:
			if treatment17 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")	
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 27:
			if treatment18 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")											
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 28:
			if treatment19 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")				
	for embName in sorted(embryos.keys()):
		if len(sys.argv) >= 29:
			if treatment20 in embName:
				if name not in embryos[embName].keys():
					outFile.write(",")
				elif name in embryos[embName].keys():
					outFile.write(embryos[embName][name] + ",")				
#	for cellss in embryos.values():
#		for (cel, blot) in cellss.items():
#			if name == cel:
#				outFile.write(blot + "\t")
#		if name not in cellss.keys():
#			outFile.write("\t")
	outFile.seek(-1, os.SEEK_CUR)
	outFile.write("\n")
outFile.write(",\n" + lineage1 + " mean,")
if len(sys.argv) == 29:		###Make dictionary of mean blot values for lineage1 in embryos under each treatment.
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
elif len(sys.argv) == 28:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
elif len(sys.argv) == 27:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
elif len(sys.argv) == 26:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
elif len(sys.argv) == 25:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
elif len(sys.argv) == 24:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
elif len(sys.argv) == 23:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
elif len(sys.argv) == 22:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
elif len(sys.argv) == 21:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
elif len(sys.argv) == 20:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
elif len(sys.argv) == 19:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
elif len(sys.argv) == 18:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
elif len(sys.argv) == 17:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
elif len(sys.argv) == 16:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
elif len(sys.argv) == 15:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
elif len(sys.argv) == 14:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
elif len(sys.argv) == 13:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
elif len(sys.argv) == 12:
	lin1Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
elif len(sys.argv) == 11:
	lin1Means = {"WT":[], treatment1:[], treatment2:[]}	
elif len(sys.argv) == 10:
	lin1Means = {"WT":[], treatment1:[]}	
elif len(sys.argv) == 9:
	lin1Means = {"WT":[]}	
#lin1MeansYear = {"2015":{"WT":[], "pop-1i":[], "sys-1i":[]}, "2016":{"WT":[], "pop-1i":[], "sys-1i":[]}}
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) == 29:		###Write out means of lineage1 blot values of WT embryos and place them in a dictionary.
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				if treatment19 not in embryo:
																					if treatment20 not in embryo:
																						for (cel, blot) in embryos[embryo].items():
																							if lineage1 in cel:
																								meanNames.append(float(blot))
																						if len(meanNames) > 0:
																							outFile.write(str(mean(meanNames)) + ",")
																							lin1Means["WT"].append(float(mean(meanNames)))
																						else :
																							outFile.write(",")

	elif len(sys.argv) == 28:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				if treatment19 not in embryo:
																					for (cel, blot) in embryos[embryo].items():
																						if lineage1 in cel:
																							meanNames.append(float(blot))
																					if len(meanNames) > 0:
																						outFile.write(str(mean(meanNames)) + ",")
																						lin1Means["WT"].append(float(mean(meanNames)))
																					else :
																						outFile.write(",")

	elif len(sys.argv) == 27:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				for (cel, blot) in embryos[embryo].items():
																					if lineage1 in cel:
																						meanNames.append(float(blot))
																				if len(meanNames) > 0:
																					outFile.write(str(mean(meanNames)) + ",")
																					lin1Means["WT"].append(float(mean(meanNames)))
																				else :
																					outFile.write(",")

	elif len(sys.argv) == 26:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			for (cel, blot) in embryos[embryo].items():
																				if lineage1 in cel:
																					meanNames.append(float(blot))
																			if len(meanNames) > 0:
																				outFile.write(str(mean(meanNames)) + ",")
																				lin1Means["WT"].append(float(mean(meanNames)))
																			else :
																				outFile.write(",")
	
	elif len(sys.argv) == 25:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		for (cel, blot) in embryos[embryo].items():
																			if lineage1 in cel:
																				meanNames.append(float(blot))
																		if len(meanNames) > 0:
																			outFile.write(str(mean(meanNames)) + ",")
																			lin1Means["WT"].append(float(mean(meanNames)))
																		else :
																			outFile.write(",")

	elif len(sys.argv) == 24:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	for (cel, blot) in embryos[embryo].items():
																		if lineage1 in cel:
																			meanNames.append(float(blot))
																	if len(meanNames) > 0:
																		outFile.write(str(mean(meanNames)) + ",")
																		lin1Means["WT"].append(float(mean(meanNames)))
																	else :
																		outFile.write(",")

	elif len(sys.argv) == 23:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																for (cel, blot) in embryos[embryo].items():
																	if lineage1 in cel:
																		meanNames.append(float(blot))
																if len(meanNames) > 0:
																	outFile.write(str(mean(meanNames)) + ",")
																	lin1Means["WT"].append(float(mean(meanNames)))
																else :
																	outFile.write(",")

	elif len(sys.argv) == 22:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															for (cel, blot) in embryos[embryo].items():
																if lineage1 in cel:
																	meanNames.append(float(blot))
															if len(meanNames) > 0:
																outFile.write(str(mean(meanNames)) + ",")
																lin1Means["WT"].append(float(mean(meanNames)))
															else :
																outFile.write(",")
	
	elif len(sys.argv) == 21:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														for (cel, blot) in embryos[embryo].items():
															if lineage1 in cel:
																meanNames.append(float(blot))
														if len(meanNames) > 0:
															outFile.write(str(mean(meanNames)) + ",")
															lin1Means["WT"].append(float(mean(meanNames)))
														else :
															outFile.write(",")

	elif len(sys.argv) == 20:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													for (cel, blot) in embryos[embryo].items():
														if lineage1 in cel:
															meanNames.append(float(blot))
													if len(meanNames) > 0:
														outFile.write(str(mean(meanNames)) + ",")
														lin1Means["WT"].append(float(mean(meanNames)))
													else :
														outFile.write(",")
	
	elif len(sys.argv) == 19:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												for (cel, blot) in embryos[embryo].items():
													if lineage1 in cel:
														meanNames.append(float(blot))
												if len(meanNames) > 0:
													outFile.write(str(mean(meanNames)) + ",")
													lin1Means["WT"].append(float(mean(meanNames)))
												else :
													outFile.write(",")

	elif len(sys.argv) == 18:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											for (cel, blot) in embryos[embryo].items():
												if lineage1 in cel:
													meanNames.append(float(blot))
											if len(meanNames) > 0:
												outFile.write(str(mean(meanNames)) + ",")
												lin1Means["WT"].append(float(mean(meanNames)))
											else :
												outFile.write(",")

	elif len(sys.argv) == 17:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										for (cel, blot) in embryos[embryo].items():
											if lineage1 in cel:
												meanNames.append(float(blot))
										if len(meanNames) > 0:
											outFile.write(str(mean(meanNames)) + ",")
											lin1Means["WT"].append(float(mean(meanNames)))
										else :
											outFile.write(",")

	elif len(sys.argv) == 16:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									for (cel, blot) in embryos[embryo].items():
										if lineage1 in cel:
											meanNames.append(float(blot))
									if len(meanNames) > 0:
										outFile.write(str(mean(meanNames)) + ",")
										lin1Means["WT"].append(float(mean(meanNames)))
									else :
										outFile.write(",")

	elif len(sys.argv) == 15:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								for (cel, blot) in embryos[embryo].items():
									if lineage1 in cel:
										meanNames.append(float(blot))
								if len(meanNames) > 0:
									outFile.write(str(mean(meanNames)) + ",")
									lin1Means["WT"].append(float(mean(meanNames)))
								else :
									outFile.write(",")
	
	elif len(sys.argv) == 14:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							for (cel, blot) in embryos[embryo].items():
								if lineage1 in cel:
									meanNames.append(float(blot))
							if len(meanNames) > 0:
								outFile.write(str(mean(meanNames)) + ",")
								lin1Means["WT"].append(float(mean(meanNames)))
							else :
								outFile.write(",")

	elif len(sys.argv) == 13:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						for (cel, blot) in embryos[embryo].items():
							if lineage1 in cel:
								meanNames.append(float(blot))
						#print len(meanNames)
						if len(meanNames) > 0:
							outFile.write(str(mean(meanNames)) + ",")
							lin1Means["WT"].append(float(mean(meanNames)))
						else :
							outFile.write(",")	

	elif len(sys.argv) == 12:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					for (cel, blot) in embryos[embryo].items():
						if lineage1 in cel:
							meanNames.append(float(blot))
					if len(meanNames) > 0:
						outFile.write(str(mean(meanNames)) + ",")
						lin1Means["WT"].append(float(mean(meanNames)))
					else :
						outFile.write(",")

	elif len(sys.argv) == 11:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				for (cel, blot) in embryos[embryo].items():
					if lineage1 in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					lin1Means["WT"].append(float(mean(meanNames)))
				else :
					outFile.write(",")

	elif len(sys.argv) == 10:
		if treatment1 not in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means["WT"].append(float(mean(meanNames)))
			else :
				outFile.write(",")

	elif len(sys.argv) == 9:
		for (cel, blot) in embryos[embryo].items():
			if lineage1 in cel:
				meanNames.append(float(blot))
		if len(meanNames) > 0:
			outFile.write(str(mean(meanNames)) + ",")
			lin1Means["WT"].append(float(mean(meanNames)))
		else :
			outFile.write(",")

for embryo in sorted(embryos.keys()):		###Write out lineage1 blot value means for each treatment and place them in a dictionary.
	meanNames = []
	if len(sys.argv) >= 10:
		if treatment1 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment1].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 11:
		if treatment2 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment2].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 12:
		if treatment3 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment3].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 13:
		if treatment4 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment4].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 14:
		if treatment5 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment5].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 15:
		if treatment6 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment6].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 16:
		if treatment7 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment7].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 17:
		if treatment8 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment8].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 18:
		if treatment9 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment9].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 19:
		if treatment10 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment10].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 20:
		if treatment11 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment11].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 21:
		if treatment12 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment12].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 22:
		if treatment13 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment13].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 23:
		if treatment14 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment14].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 24:
		if treatment15 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment15].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 25:
		if treatment16 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment16].append(float(mean(meanNames)))
			else :
				outFile.write(",")				
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 26:
		if treatment17 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment17].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 27:
		if treatment18 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment18].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 28:
		if treatment19 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment19].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 29:
		if treatment20 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage1 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin1Means[treatment20].append(float(mean(meanNames)))
			else :
				outFile.write(",")									


#	if "2015" in embryo:
#		if "pop-1i" in embryo:
#			lin1MeansYear["2015"]["pop-1i"].append(float(mean(meanNames)))
#		elif "sys-1i" in embryo:
#			lin1MeansYear["2015"]["sys-1i"].append(float(mean(meanNames)))
#		else:
#			lin1MeansYear["2015"]["WT"].append(float(mean(meanNames)))
#	elif "2016" in embryo:
#		if "pop-1i" in embryo:
#			lin1MeansYear["2016"]["pop-1i"].append(float(mean(meanNames)))
#		elif "sys-1i" in embryo:
#			lin1MeansYear["2016"]["sys-1i"].append(float(mean(meanNames)))
#		else:
#			lin1MeansYear["2016"]["WT"].append(float(mean(meanNames)))
	#print "Next Embryo"
	#print meanNames
outFile.seek(-1, os.SEEK_CUR)
outFile.write("\n" + lineage2 + " mean,")
#lin2MeansYear = {"2015":{"WT":[], "pop-1i":[], "sys-1i":[]}, "2016":{"WT":[], "pop-1i":[], "sys-1i":[]}}
if len(sys.argv) == 29:		###Make dictionary of mean blot values for lineage2 in embryos under each treatment.
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
elif len(sys.argv) == 28:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
elif len(sys.argv) == 27:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
elif len(sys.argv) == 26:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
elif len(sys.argv) == 25:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
elif len(sys.argv) == 24:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
elif len(sys.argv) == 23:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
elif len(sys.argv) == 22:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
elif len(sys.argv) == 21:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
elif len(sys.argv) == 20:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
elif len(sys.argv) == 19:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
elif len(sys.argv) == 18:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
elif len(sys.argv) == 17:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
elif len(sys.argv) == 16:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
elif len(sys.argv) == 15:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
elif len(sys.argv) == 14:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
elif len(sys.argv) == 13:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
elif len(sys.argv) == 12:
	lin2Means = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
elif len(sys.argv) == 11:
	lin2Means = {"WT":[], treatment1:[], treatment2:[]}	
elif len(sys.argv) == 10:
	lin2Means = {"WT":[], treatment1:[]}	
elif len(sys.argv) == 9:
	lin2Means = {"WT":[]}	
		
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) == 29:		###Write out means of lineage2 blot values of WT embryos and place them in a dictionary.
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				if treatment19 not in embryo:
																					if treatment20 not in embryo:
																						for (cel, blot) in embryos[embryo].items():
																							if lineage2 in cel:
																								meanNames.append(float(blot))
																						if len(meanNames) > 0:
																							outFile.write(str(mean(meanNames)) + ",")
																							lin2Means["WT"].append(float(mean(meanNames)))
																						else :
																							outFile.write(",")

	elif len(sys.argv) == 28:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				if treatment19 not in embryo:
																					for (cel, blot) in embryos[embryo].items():
																						if lineage2 in cel:
																							meanNames.append(float(blot))
																					if len(meanNames) > 0:
																						outFile.write(str(mean(meanNames)) + ",")
																						lin2Means["WT"].append(float(mean(meanNames)))
																					else :
																						outFile.write(",")

	elif len(sys.argv) == 27:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			if treatment18 not in embryo:
																				for (cel, blot) in embryos[embryo].items():
																					if lineage2 in cel:
																						meanNames.append(float(blot))
																				if len(meanNames) > 0:
																					outFile.write(str(mean(meanNames)) + ",")
																					lin2Means["WT"].append(float(mean(meanNames)))
																				else :
																					outFile.write(",")

	elif len(sys.argv) == 26:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		if treatment17 not in embryo:
																			for (cel, blot) in embryos[embryo].items():
																				if lineage2 in cel:
																					meanNames.append(float(blot))
																			if len(meanNames) > 0:
																				outFile.write(str(mean(meanNames)) + ",")
																				lin2Means["WT"].append(float(mean(meanNames)))
																			else :
																				outFile.write(",")
	
	elif len(sys.argv) == 25:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	if treatment16 not in embryo:
																		for (cel, blot) in embryos[embryo].items():
																			if lineage2 in cel:
																				meanNames.append(float(blot))
																		if len(meanNames) > 0:
																			outFile.write(str(mean(meanNames)) + ",")
																			lin2Means["WT"].append(float(mean(meanNames)))
																		else :
																			outFile.write(",")

	elif len(sys.argv) == 24:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																if treatment15 not in embryo:
																	for (cel, blot) in embryos[embryo].items():
																		if lineage2 in cel:
																			meanNames.append(float(blot))
																	if len(meanNames) > 0:
																		outFile.write(str(mean(meanNames)) + ",")
																		lin2Means["WT"].append(float(mean(meanNames)))
																	else :
																		outFile.write(",")

	elif len(sys.argv) == 23:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															if treatment14 not in embryo:
																for (cel, blot) in embryos[embryo].items():
																	if lineage2 in cel:
																		meanNames.append(float(blot))
																if len(meanNames) > 0:
																	outFile.write(str(mean(meanNames)) + ",")
																	lin2Means["WT"].append(float(mean(meanNames)))
																else :
																	outFile.write(",")

	elif len(sys.argv) == 22:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														if treatment13 not in embryo:
															for (cel, blot) in embryos[embryo].items():
																if lineage2 in cel:
																	meanNames.append(float(blot))
															if len(meanNames) > 0:
																outFile.write(str(mean(meanNames)) + ",")
																lin2Means["WT"].append(float(mean(meanNames)))
															else :
																outFile.write(",")
	
	elif len(sys.argv) == 21:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													if treatment12 not in embryo:
														for (cel, blot) in embryos[embryo].items():
															if lineage2 in cel:
																meanNames.append(float(blot))
														if len(meanNames) > 0:
															outFile.write(str(mean(meanNames)) + ",")
															lin2Means["WT"].append(float(mean(meanNames)))
														else :
															outFile.write(",")

	elif len(sys.argv) == 20:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												if treatment11 not in embryo:
													for (cel, blot) in embryos[embryo].items():
														if lineage2 in cel:
															meanNames.append(float(blot))
													if len(meanNames) > 0:
														outFile.write(str(mean(meanNames)) + ",")
														lin2Means["WT"].append(float(mean(meanNames)))
													else :
														outFile.write(",")
	
	elif len(sys.argv) == 19:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											if treatment10 not in embryo:
												for (cel, blot) in embryos[embryo].items():
													if lineage2 in cel:
														meanNames.append(float(blot))
												if len(meanNames) > 0:
													outFile.write(str(mean(meanNames)) + ",")
													lin2Means["WT"].append(float(mean(meanNames)))
												else :
													outFile.write(",")

	elif len(sys.argv) == 18:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										if treatment9 not in embryo:
											for (cel, blot) in embryos[embryo].items():
												if lineage2 in cel:
													meanNames.append(float(blot))
											if len(meanNames) > 0:
												outFile.write(str(mean(meanNames)) + ",")
												lin2Means["WT"].append(float(mean(meanNames)))
											else :
												outFile.write(",")

	elif len(sys.argv) == 17:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									if treatment8 not in embryo:
										for (cel, blot) in embryos[embryo].items():
											if lineage2 in cel:
												meanNames.append(float(blot))
										if len(meanNames) > 0:
											outFile.write(str(mean(meanNames)) + ",")
											lin2Means["WT"].append(float(mean(meanNames)))
										else :
											outFile.write(",")

	elif len(sys.argv) == 16:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								if treatment7 not in embryo:
									for (cel, blot) in embryos[embryo].items():
										if lineage2 in cel:
											meanNames.append(float(blot))
									if len(meanNames) > 0:
										outFile.write(str(mean(meanNames)) + ",")
										lin2Means["WT"].append(float(mean(meanNames)))
									else :
										outFile.write(",")

	elif len(sys.argv) == 15:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							if treatment6 not in embryo:
								for (cel, blot) in embryos[embryo].items():
									if lineage2 in cel:
										meanNames.append(float(blot))
								if len(meanNames) > 0:
									outFile.write(str(mean(meanNames)) + ",")
									lin2Means["WT"].append(float(mean(meanNames)))
								else :
									outFile.write(",")
	
	elif len(sys.argv) == 14:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						if treatment5 not in embryo:
							for (cel, blot) in embryos[embryo].items():
								if lineage2 in cel:
									meanNames.append(float(blot))
							if len(meanNames) > 0:
								outFile.write(str(mean(meanNames)) + ",")
								lin2Means["WT"].append(float(mean(meanNames)))
							else :
								outFile.write(",")

	elif len(sys.argv) == 13:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					if treatment4 not in embryo:
						for (cel, blot) in embryos[embryo].items():
							if lineage2 in cel:
								meanNames.append(float(blot))
						if len(meanNames) > 0:
							outFile.write(str(mean(meanNames)) + ",")
							lin2Means["WT"].append(float(mean(meanNames)))
						else :
							outFile.write(",")

	elif len(sys.argv) == 12:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				if treatment3 not in embryo:
					for (cel, blot) in embryos[embryo].items():
						if lineage2 in cel:
							meanNames.append(float(blot))
					if len(meanNames) > 0:
						outFile.write(str(mean(meanNames)) + ",")
						lin2Means["WT"].append(float(mean(meanNames)))
					else :
						outFile.write(",")

	elif len(sys.argv) == 11:
		if treatment1 not in embryo:
			if treatment2 not in embryo:
				for (cel, blot) in embryos[embryo].items():
					if lineage2 in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					lin2Means["WT"].append(float(mean(meanNames)))
				else :
					outFile.write(",")

	elif len(sys.argv) == 10:
		if treatment1 not in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means["WT"].append(float(mean(meanNames)))
			else :
				outFile.write(",")

	elif len(sys.argv) == 9:
		for (cel, blot) in embryos[embryo].items():
			if lineage2 in cel:
				meanNames.append(float(blot))
		if len(meanNames) > 0:
			outFile.write(str(mean(meanNames)) + ",")
			lin2Means["WT"].append(float(mean(meanNames)))
		else :
			outFile.write(",")

for embryo in sorted(embryos.keys()):		###Write out lineage2 blot value means for each treatment and place them in a dictionary.
	meanNames = []
	if len(sys.argv) >= 10:
		if treatment1 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment1].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 11:
		if treatment2 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment2].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 12:
		if treatment3 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment3].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 13:
		if treatment4 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment4].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 14:
		if treatment5 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment5].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 15:
		if treatment6 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment6].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 16:
		if treatment7 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment7].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 17:
		if treatment8 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment8].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 18:
		if treatment9 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment9].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 19:
		if treatment10 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment10].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 20:
		if treatment11 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment11].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 21:
		if treatment12 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment12].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 22:
		if treatment13 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment13].append(float(mean(meanNames)))
			else :
				outFile.write(",")				
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 23:
		if treatment14 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment14].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 24:
		if treatment15 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment15].append(float(mean(meanNames)))
			else :
				outFile.write(",")					
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 25:
		if treatment16 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment16].append(float(mean(meanNames)))
			else :
				outFile.write(",")				
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 26:
		if treatment17 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment17].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 27:
		if treatment18 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment18].append(float(mean(meanNames)))
			else :
				outFile.write(",")	
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 28:
		if treatment19 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment19].append(float(mean(meanNames)))
			else :
				outFile.write(",")
for embryo in sorted(embryos.keys()):
	meanNames = []
	if len(sys.argv) >= 29:
		if treatment20 in embryo:
			for (cel, blot) in embryos[embryo].items():
				if lineage2 in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				lin2Means[treatment20].append(float(mean(meanNames)))
			else :
				outFile.write(",")									

#	if "2015" in embryo:
#		if "pop-1i" in embryo:
#			lin2MeansYear["2015"]["pop-1i"].append(float(mean(meanNames)))
#		elif "sys-1i" in embryo:
#			lin2MeansYear["2015"]["sys-1i"].append(float(mean(meanNames)))
#		else:
#			lin2MeansYear["2015"]["WT"].append(float(mean(meanNames)))
#	elif "2016" in embryo:
#		if "pop-1i" in embryo:
#			lin2MeansYear["2016"]["pop-1i"].append(float(mean(meanNames)))
#		elif "sys-1i" in embryo:
#			lin2MeansYear["2016"]["sys-1i"].append(float(mean(meanNames)))
#		else:
#			lin2MeansYear["2016"]["WT"].append(float(mean(meanNames)))
outFile.seek(-1, os.SEEK_CUR)
outFile.write("\n,")

if negativeControlLineage != "none":
	outFile.write("\n" + negativeControlLineage + " mean,")
	#lin2MeansYear = {"2015":{"WT":[], "pop-1i":[], "sys-1i":[]}, "2016":{"WT":[], "pop-1i":[], "sys-1i":[]}}
	if len(sys.argv) == 29:		###Make dictionary of mean blot values for negativeControlLineage in embryos under each treatment.
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
	elif len(sys.argv) == 28:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
	elif len(sys.argv) == 27:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
	elif len(sys.argv) == 26:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
	elif len(sys.argv) == 25:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
	elif len(sys.argv) == 24:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
	elif len(sys.argv) == 23:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
	elif len(sys.argv) == 22:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
	elif len(sys.argv) == 21:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
	elif len(sys.argv) == 20:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
	elif len(sys.argv) == 19:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
	elif len(sys.argv) == 18:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
	elif len(sys.argv) == 17:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
	elif len(sys.argv) == 16:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
	elif len(sys.argv) == 15:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
	elif len(sys.argv) == 14:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
	elif len(sys.argv) == 13:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
	elif len(sys.argv) == 12:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
	elif len(sys.argv) == 11:
		negativeControlLineageMeans = {"WT":[], treatment1:[], treatment2:[]}	
	elif len(sys.argv) == 10:
		negativeControlLineageMeans = {"WT":[], treatment1:[]}	
	elif len(sys.argv) == 9:
		negativeControlLineageMeans = {"WT":[]}	
		
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) == 29:		###Write out means of negativeControlLineage blot values of WT embryos and place them in a dictionary.
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					if treatment19 not in embryo:
																						if treatment20 not in embryo:
																							for (cel, blot) in embryos[embryo].items():
																								if negativeControlLineage in cel:
																									meanNames.append(float(blot))
																							if len(meanNames) > 0:
																								outFile.write(str(mean(meanNames)) + ",")
																								negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																							else :
																								outFile.write(",")

		elif len(sys.argv) == 28:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					if treatment19 not in embryo:
																						for (cel, blot) in embryos[embryo].items():
																							if negativeControlLineage in cel:
																								meanNames.append(float(blot))
																						if len(meanNames) > 0:
																							outFile.write(str(mean(meanNames)) + ",")
																							negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																						else :
																							outFile.write(",")

		elif len(sys.argv) == 27:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					for (cel, blot) in embryos[embryo].items():
																						if negativeControlLineage in cel:
																							meanNames.append(float(blot))
																					if len(meanNames) > 0:
																						outFile.write(str(mean(meanNames)) + ",")
																						negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																					else :
																						outFile.write(",")

		elif len(sys.argv) == 26:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				for (cel, blot) in embryos[embryo].items():
																					if negativeControlLineage in cel:
																						meanNames.append(float(blot))
																				if len(meanNames) > 0:
																					outFile.write(str(mean(meanNames)) + ",")
																					negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																				else :
																					outFile.write(",")
	
		elif len(sys.argv) == 25:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			for (cel, blot) in embryos[embryo].items():
																				if negativeControlLineage in cel:
																					meanNames.append(float(blot))
																			if len(meanNames) > 0:
																				outFile.write(str(mean(meanNames)) + ",")
																				negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																			else :
																				outFile.write(",")

		elif len(sys.argv) == 24:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		for (cel, blot) in embryos[embryo].items():
																			if negativeControlLineage in cel:
																				meanNames.append(float(blot))
																		if len(meanNames) > 0:
																			outFile.write(str(mean(meanNames)) + ",")
																			negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																		else :
																			outFile.write(",")

		elif len(sys.argv) == 23:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	for (cel, blot) in embryos[embryo].items():
																		if negativeControlLineage in cel:
																			meanNames.append(float(blot))
																	if len(meanNames) > 0:
																		outFile.write(str(mean(meanNames)) + ",")
																		negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																	else :
																		outFile.write(",")

		elif len(sys.argv) == 22:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																for (cel, blot) in embryos[embryo].items():
																	if negativeControlLineage in cel:
																		meanNames.append(float(blot))
																if len(meanNames) > 0:
																	outFile.write(str(mean(meanNames)) + ",")
																	negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
																else :
																	outFile.write(",")
	
		elif len(sys.argv) == 21:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															for (cel, blot) in embryos[embryo].items():
																if negativeControlLineage in cel:
																	meanNames.append(float(blot))
															if len(meanNames) > 0:
																outFile.write(str(mean(meanNames)) + ",")
																negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
															else :
																outFile.write(",")

		elif len(sys.argv) == 20:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														for (cel, blot) in embryos[embryo].items():
															if negativeControlLineage in cel:
																meanNames.append(float(blot))
														if len(meanNames) > 0:
															outFile.write(str(mean(meanNames)) + ",")
															negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
														else :
															outFile.write(",")
	
		elif len(sys.argv) == 19:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													for (cel, blot) in embryos[embryo].items():
														if negativeControlLineage in cel:
															meanNames.append(float(blot))
													if len(meanNames) > 0:
														outFile.write(str(mean(meanNames)) + ",")
														negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
													else :
														outFile.write(",")

		elif len(sys.argv) == 18:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												for (cel, blot) in embryos[embryo].items():
													if negativeControlLineage in cel:
														meanNames.append(float(blot))
												if len(meanNames) > 0:
													outFile.write(str(mean(meanNames)) + ",")
													negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
												else :
													outFile.write(",")

		elif len(sys.argv) == 17:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											for (cel, blot) in embryos[embryo].items():
												if negativeControlLineage in cel:
													meanNames.append(float(blot))
											if len(meanNames) > 0:
												outFile.write(str(mean(meanNames)) + ",")
												negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
											else :
												outFile.write(",")

		elif len(sys.argv) == 16:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										for (cel, blot) in embryos[embryo].items():
											if negativeControlLineage in cel:
												meanNames.append(float(blot))
										if len(meanNames) > 0:
											outFile.write(str(mean(meanNames)) + ",")
											negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
										else :
											outFile.write(",")

		elif len(sys.argv) == 15:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									for (cel, blot) in embryos[embryo].items():
										if negativeControlLineage in cel:
											meanNames.append(float(blot))
									if len(meanNames) > 0:
										outFile.write(str(mean(meanNames)) + ",")
										negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
									else :
										outFile.write(",")
	
		elif len(sys.argv) == 14:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								for (cel, blot) in embryos[embryo].items():
									if negativeControlLineage in cel:
										meanNames.append(float(blot))
								if len(meanNames) > 0:
									outFile.write(str(mean(meanNames)) + ",")
									negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
								else :
									outFile.write(",")

		elif len(sys.argv) == 13:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							for (cel, blot) in embryos[embryo].items():
								if negativeControlLineage in cel:
									meanNames.append(float(blot))
							if len(meanNames) > 0:
								outFile.write(str(mean(meanNames)) + ",")
								negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
							else :
								outFile.write(",")

		elif len(sys.argv) == 12:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						for (cel, blot) in embryos[embryo].items():
							if negativeControlLineage in cel:
								meanNames.append(float(blot))
						if len(meanNames) > 0:
							outFile.write(str(mean(meanNames)) + ",")
							negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
						else :
							outFile.write(",")

		elif len(sys.argv) == 11:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					for (cel, blot) in embryos[embryo].items():
						if negativeControlLineage in cel:
							meanNames.append(float(blot))
					if len(meanNames) > 0:
						outFile.write(str(mean(meanNames)) + ",")
						negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
					else :
						outFile.write(",")

		elif len(sys.argv) == 10:
			if treatment1 not in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
				else :
					outFile.write(",")

		elif len(sys.argv) == 9:
			for (cel, blot) in embryos[embryo].items():
				if negativeControlLineage in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				negativeControlLineageMeans["WT"].append(float(mean(meanNames)))
			else :
				outFile.write(",")

	for embryo in sorted(embryos.keys()):		###Write out negativeControlLineage blot value means for each treatment and place them in a dictionary.
		meanNames = []
		if len(sys.argv) >= 10:
			if treatment1 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment1].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 11:
			if treatment2 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment2].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 12:
			if treatment3 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment3].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 13:
			if treatment4 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment4].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 14:
			if treatment5 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment5].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 15:
			if treatment6 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment6].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 16:
			if treatment7 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment7].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 17:
			if treatment8 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment8].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 18:
			if treatment9 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment9].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 19:
			if treatment10 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment10].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 20:
			if treatment11 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment11].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 21:
			if treatment12 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment12].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 22:
			if treatment13 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment13].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 23:
			if treatment14 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment14].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 24:
			if treatment15 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment15].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 25:
			if treatment16 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment16].append(float(mean(meanNames)))
				else :
					outFile.write(",")				
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 26:
			if treatment17 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment17].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 27:
			if treatment18 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment18].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 28:
			if treatment19 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment19].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 29:
			if treatment20 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if negativeControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					negativeControlLineageMeans[treatment20].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	outFile.seek(-1, os.SEEK_CUR)
	outFile.write("\n,")												

	#	if "2015" in embryo:
	#		if "pop-1i" in embryo:
	#			lin2MeansYear["2015"]["pop-1i"].append(float(mean(meanNames)))
	#		elif "sys-1i" in embryo:
	#			lin2MeansYear["2015"]["sys-1i"].append(float(mean(meanNames)))
	#		else:
	#			lin2MeansYear["2015"]["WT"].append(float(mean(meanNames)))
	#	elif "2016" in embryo:
	#		if "pop-1i" in embryo:
	#			lin2MeansYear["2016"]["pop-1i"].append(float(mean(meanNames)))
	#		elif "sys-1i" in embryo:
	#			lin2MeansYear["2016"]["sys-1i"].append(float(mean(meanNames)))
	#		else:
	#			lin2MeansYear["2016"]["WT"].append(float(mean(meanNames)))
	

if positiveControlLineage != "none":
	outFile.write("\n" + positiveControlLineage + " mean,")
	#lin2MeansYear = {"2015":{"WT":[], "pop-1i":[], "sys-1i":[]}, "2016":{"WT":[], "pop-1i":[], "sys-1i":[]}}
	if len(sys.argv) == 29:		###Make dictionary of mean blot values for positiveControlLineage in embryos under each treatment.
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
	elif len(sys.argv) == 28:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
	elif len(sys.argv) == 27:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
	elif len(sys.argv) == 26:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
	elif len(sys.argv) == 25:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
	elif len(sys.argv) == 24:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
	elif len(sys.argv) == 23:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
	elif len(sys.argv) == 22:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
	elif len(sys.argv) == 21:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
	elif len(sys.argv) == 20:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
	elif len(sys.argv) == 19:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
	elif len(sys.argv) == 18:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
	elif len(sys.argv) == 17:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
	elif len(sys.argv) == 16:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
	elif len(sys.argv) == 15:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
	elif len(sys.argv) == 14:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
	elif len(sys.argv) == 13:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
	elif len(sys.argv) == 12:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
	elif len(sys.argv) == 11:
		positiveControlLineageMeans = {"WT":[], treatment1:[], treatment2:[]}	
	elif len(sys.argv) == 10:
		positiveControlLineageMeans = {"WT":[], treatment1:[]}	
	elif len(sys.argv) == 9:
		positiveControlLineageMeans = {"WT":[]}	
		
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) == 29:		###Write out means of positiveControlLineage blot values of WT embryos and place them in a dictionary.
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					if treatment19 not in embryo:
																						if treatment20 not in embryo:
																							for (cel, blot) in embryos[embryo].items():
																								if positiveControlLineage in cel:
																									meanNames.append(float(blot))
																							if len(meanNames) > 0:
																								outFile.write(str(mean(meanNames)) + ",")
																								positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																							else :
																								outFile.write(",")

		elif len(sys.argv) == 28:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					if treatment19 not in embryo:
																						for (cel, blot) in embryos[embryo].items():
																							if positiveControlLineage in cel:
																								meanNames.append(float(blot))
																						if len(meanNames) > 0:
																							outFile.write(str(mean(meanNames)) + ",")
																							positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																						else :
																							outFile.write(",")

		elif len(sys.argv) == 27:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				if treatment18 not in embryo:
																					for (cel, blot) in embryos[embryo].items():
																						if positiveControlLineage in cel:
																							meanNames.append(float(blot))
																					if len(meanNames) > 0:
																						outFile.write(str(mean(meanNames)) + ",")
																						positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																					else :
																						outFile.write(",")

		elif len(sys.argv) == 26:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			if treatment17 not in embryo:
																				for (cel, blot) in embryos[embryo].items():
																					if positiveControlLineage in cel:
																						meanNames.append(float(blot))
																				if len(meanNames) > 0:
																					outFile.write(str(mean(meanNames)) + ",")
																					positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																				else :
																					outFile.write(",")
	
		elif len(sys.argv) == 25:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		if treatment16 not in embryo:
																			for (cel, blot) in embryos[embryo].items():
																				if positiveControlLineage in cel:
																					meanNames.append(float(blot))
																			if len(meanNames) > 0:
																				outFile.write(str(mean(meanNames)) + ",")
																				positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																			else :
																				outFile.write(",")

		elif len(sys.argv) == 24:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	if treatment15 not in embryo:
																		for (cel, blot) in embryos[embryo].items():
																			if positiveControlLineage in cel:
																				meanNames.append(float(blot))
																		if len(meanNames) > 0:
																			outFile.write(str(mean(meanNames)) + ",")
																			positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																		else :
																			outFile.write(",")

		elif len(sys.argv) == 23:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																if treatment14 not in embryo:
																	for (cel, blot) in embryos[embryo].items():
																		if positiveControlLineage in cel:
																			meanNames.append(float(blot))
																	if len(meanNames) > 0:
																		outFile.write(str(mean(meanNames)) + ",")
																		positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																	else :
																		outFile.write(",")

		elif len(sys.argv) == 22:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															if treatment13 not in embryo:
																for (cel, blot) in embryos[embryo].items():
																	if positiveControlLineage in cel:
																		meanNames.append(float(blot))
																if len(meanNames) > 0:
																	outFile.write(str(mean(meanNames)) + ",")
																	positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
																else :
																	outFile.write(",")
	
		elif len(sys.argv) == 21:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														if treatment12 not in embryo:
															for (cel, blot) in embryos[embryo].items():
																if positiveControlLineage in cel:
																	meanNames.append(float(blot))
															if len(meanNames) > 0:
																outFile.write(str(mean(meanNames)) + ",")
																positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
															else :
																outFile.write(",")

		elif len(sys.argv) == 20:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													if treatment11 not in embryo:
														for (cel, blot) in embryos[embryo].items():
															if positiveControlLineage in cel:
																meanNames.append(float(blot))
														if len(meanNames) > 0:
															outFile.write(str(mean(meanNames)) + ",")
															positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
														else :
															outFile.write(",")
	
		elif len(sys.argv) == 19:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												if treatment10 not in embryo:
													for (cel, blot) in embryos[embryo].items():
														if positiveControlLineage in cel:
															meanNames.append(float(blot))
													if len(meanNames) > 0:
														outFile.write(str(mean(meanNames)) + ",")
														positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
													else :
														outFile.write(",")

		elif len(sys.argv) == 18:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											if treatment9 not in embryo:
												for (cel, blot) in embryos[embryo].items():
													if positiveControlLineage in cel:
														meanNames.append(float(blot))
												if len(meanNames) > 0:
													outFile.write(str(mean(meanNames)) + ",")
													positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
												else :
													outFile.write(",")

		elif len(sys.argv) == 17:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										if treatment8 not in embryo:
											for (cel, blot) in embryos[embryo].items():
												if positiveControlLineage in cel:
													meanNames.append(float(blot))
											if len(meanNames) > 0:
												outFile.write(str(mean(meanNames)) + ",")
												positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
											else :
												outFile.write(",")

		elif len(sys.argv) == 16:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									if treatment7 not in embryo:
										for (cel, blot) in embryos[embryo].items():
											if positiveControlLineage in cel:
												meanNames.append(float(blot))
										if len(meanNames) > 0:
											outFile.write(str(mean(meanNames)) + ",")
											positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
										else :
											outFile.write(",")

		elif len(sys.argv) == 15:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								if treatment6 not in embryo:
									for (cel, blot) in embryos[embryo].items():
										if positiveControlLineage in cel:
											meanNames.append(float(blot))
									if len(meanNames) > 0:
										outFile.write(str(mean(meanNames)) + ",")
										positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
									else :
										outFile.write(",")
	
		elif len(sys.argv) == 14:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							if treatment5 not in embryo:
								for (cel, blot) in embryos[embryo].items():
									if positiveControlLineage in cel:
										meanNames.append(float(blot))
								if len(meanNames) > 0:
									outFile.write(str(mean(meanNames)) + ",")
									positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
								else :
									outFile.write(",")

		elif len(sys.argv) == 13:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						if treatment4 not in embryo:
							for (cel, blot) in embryos[embryo].items():
								if positiveControlLineage in cel:
									meanNames.append(float(blot))
							if len(meanNames) > 0:
								outFile.write(str(mean(meanNames)) + ",")
								positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
							else :
								outFile.write(",")

		elif len(sys.argv) == 12:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					if treatment3 not in embryo:
						for (cel, blot) in embryos[embryo].items():
							if positiveControlLineage in cel:
								meanNames.append(float(blot))
						if len(meanNames) > 0:
							outFile.write(str(mean(meanNames)) + ",")
							positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
						else :
							outFile.write(",")

		elif len(sys.argv) == 11:
			if treatment1 not in embryo:
				if treatment2 not in embryo:
					for (cel, blot) in embryos[embryo].items():
						if positiveControlLineage in cel:
							meanNames.append(float(blot))
					if len(meanNames) > 0:
						outFile.write(str(mean(meanNames)) + ",")
						positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
					else :
						outFile.write(",")

		elif len(sys.argv) == 10:
			if treatment1 not in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
				else :
					outFile.write(",")

		elif len(sys.argv) == 9:
			for (cel, blot) in embryos[embryo].items():
				if positiveControlLineage in cel:
					meanNames.append(float(blot))
			if len(meanNames) > 0:
				outFile.write(str(mean(meanNames)) + ",")
				positiveControlLineageMeans["WT"].append(float(mean(meanNames)))
			else :
				outFile.write(",")

	for embryo in sorted(embryos.keys()):		###Write out positiveControlLineage blot value means for each treatment and place them in a dictionary.
		meanNames = []
		if len(sys.argv) >= 10:
			if treatment1 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment1].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 11:
			if treatment2 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment2].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 12:
			if treatment3 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment3].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 13:
			if treatment4 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment4].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 14:
			if treatment5 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment5].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 15:
			if treatment6 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment6].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 16:
			if treatment7 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment7].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 17:
			if treatment8 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment8].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 18:
			if treatment9 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment9].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 19:
			if treatment10 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment10].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 20:
			if treatment11 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment11].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 21:
			if treatment12 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment12].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 22:
			if treatment13 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment13].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 23:
			if treatment14 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment14].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 24:
			if treatment15 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment15].append(float(mean(meanNames)))
				else :
					outFile.write(",")					
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 25:
			if treatment16 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment16].append(float(mean(meanNames)))
				else :
					outFile.write(",")				
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 26:
			if treatment17 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment17].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 27:
			if treatment18 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment18].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 28:
			if treatment19 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment19].append(float(mean(meanNames)))
				else :
					outFile.write(",")
	for embryo in sorted(embryos.keys()):
		meanNames = []
		if len(sys.argv) >= 29:
			if treatment20 in embryo:
				for (cel, blot) in embryos[embryo].items():
					if positiveControlLineage in cel:
						meanNames.append(float(blot))
				if len(meanNames) > 0:
					outFile.write(str(mean(meanNames)) + ",")
					positiveControlLineageMeans[treatment20].append(float(mean(meanNames)))
				else :
					outFile.write(",")	
	outFile.seek(-1, os.SEEK_CUR)
	outFile.write("\n,")											

	#	if "2015" in embryo:
	#		if "pop-1i" in embryo:
	#			lin2MeansYear["2015"]["pop-1i"].append(float(mean(meanNames)))
	#		elif "sys-1i" in embryo:
	#			lin2MeansYear["2015"]["sys-1i"].append(float(mean(meanNames)))
	#		else:
	#			lin2MeansYear["2015"]["WT"].append(float(mean(meanNames)))
	#	elif "2016" in embryo:
	#		if "pop-1i" in embryo:
	#			lin2MeansYear["2016"]["pop-1i"].append(float(mean(meanNames)))
	#		elif "sys-1i" in embryo:
	#			lin2MeansYear["2016"]["sys-1i"].append(float(mean(meanNames)))
	#		else:
	#			lin2MeansYear["2016"]["WT"].append(float(mean(meanNames)))

if negativeControlLineage != "none":
	outFile.write("\n" + lineage1 + " adjusted mean,")
	if len(sys.argv) == 29:		###Make dictionary of adjusted mean blot values for lineage1 in embryos under each treatment.
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
	elif len(sys.argv) == 28:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
	elif len(sys.argv) == 27:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
	elif len(sys.argv) == 26:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
	elif len(sys.argv) == 25:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
	elif len(sys.argv) == 24:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
	elif len(sys.argv) == 23:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
	elif len(sys.argv) == 22:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
	elif len(sys.argv) == 21:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
	elif len(sys.argv) == 20:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
	elif len(sys.argv) == 19:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
	elif len(sys.argv) == 18:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
	elif len(sys.argv) == 17:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
	elif len(sys.argv) == 16:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
	elif len(sys.argv) == 15:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
	elif len(sys.argv) == 14:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
	elif len(sys.argv) == 13:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
	elif len(sys.argv) == 12:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
	elif len(sys.argv) == 11:
		lin1MeansAdjusted = {"WT":[], treatment1:[], treatment2:[]}	
	elif len(sys.argv) == 10:
		lin1MeansAdjusted = {"WT":[], treatment1:[]}	
	elif len(sys.argv) == 9:
		lin1MeansAdjusted = {"WT":[]}	
	embr = 0
	while embr <= len(lin1Means["WT"]) - 1:
		lin1MeansAdjusted["WT"].append(lin1Means["WT"][embr] - negativeControlLineageMeans["WT"][embr])
		outFile.write(str(lin1MeansAdjusted["WT"][embr]) + ",")
		embr = embr + 1
		#print embr
	if len(sys.argv) >= 10:		###Make dictionary with adjusted means for lineage1
		if len(lin1Means[treatment1]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment1]) - 1:
				lin1MeansAdjusted[treatment1].append(lin1Means[treatment1][embr] - negativeControlLineageMeans[treatment1][embr])
				outFile.write(str(lin1MeansAdjusted[treatment1][embr]) + ",")
				embr = embr + 1
				#print embr
	if len(sys.argv) >= 11:
		if len(lin1Means[treatment2]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment2]) - 1:
				lin1MeansAdjusted[treatment2].append(lin1Means[treatment2][embr] - negativeControlLineageMeans[treatment2][embr])
				outFile.write(str(lin1MeansAdjusted[treatment2][embr]) + ",")
				embr = embr + 1
				#print embr
	if len(sys.argv) >= 12:
		if len(lin1Means[treatment3]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment3]) - 1:
				lin1MeansAdjusted[treatment3].append(lin1Means[treatment3][embr] - negativeControlLineageMeans[treatment3][embr])
				outFile.write(str(lin1MeansAdjusted[treatment3][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 13:
		if len(lin1Means[treatment4]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment4]) - 1:
				lin1MeansAdjusted[treatment4].append(lin1Means[treatment4][embr] - negativeControlLineageMeans[treatment4][embr])
				outFile.write(str(lin1MeansAdjusted[treatment4][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 14:
		if len(lin1Means[treatment5]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment5]) - 1:
				lin1MeansAdjusted[treatment5].append(lin1Means[treatment5][embr] - negativeControlLineageMeans[treatment5][embr])
				outFile.write(str(lin1MeansAdjusted[treatment5][embr]) + ",")
				embr = embr + 1	
	if len(sys.argv) >= 15:
		if len(lin1Means[treatment6]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment6]) - 1:
				lin1MeansAdjusted[treatment6].append(lin1Means[treatment6][embr] - negativeControlLineageMeans[treatment6][embr])
				outFile.write(str(lin1MeansAdjusted[treatment6][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 16:
		if len(lin1Means[treatment7]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment7]) - 1:
				lin1MeansAdjusted[treatment7].append(lin1Means[treatment7][embr] - negativeControlLineageMeans[treatment7][embr])
				outFile.write(str(lin1MeansAdjusted[treatment7][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 17:
		if len(lin1Means[treatment8]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment8]) - 1:
				lin1MeansAdjusted[treatment8].append(lin1Means[treatment8][embr] - negativeControlLineageMeans[treatment8][embr])
				outFile.write(str(lin1MeansAdjusted[treatment8][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 18:
		if len(lin1Means[treatment9]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment9]) - 1:
				lin1MeansAdjusted[treatment9].append(lin1Means[treatment9][embr] - negativeControlLineageMeans[treatment9][embr])
				outFile.write(str(lin1MeansAdjusted[treatment9][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 19:
		if len(lin1Means[treatment10]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment10]) - 1:
				lin1MeansAdjusted[treatment10].append(lin1Means[treatment10][embr] - negativeControlLineageMeans[treatment10][embr])
				outFile.write(str(lin1MeansAdjusted[treatment10][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 20:
		if len(lin1Means[treatment11]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment11]) - 1:
				lin1MeansAdjusted[treatment11].append(lin1Means[treatment11][embr] - negativeControlLineageMeans[treatment11][embr])
				outFile.write(str(lin1MeansAdjusted[treatment11][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 21:
		if len(lin1Means[treatment12]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment12]) - 1:
				lin1MeansAdjusted[treatment12].append(lin1Means[treatment12][embr] - negativeControlLineageMeans[treatment12][embr])
				outFile.write(str(lin1MeansAdjusted[treatment12][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 22:
		if len(lin1Means[treatment13]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment13]) - 1:
				lin1MeansAdjusted[treatment13].append(lin1Means[treatment13][embr] - negativeControlLineageMeans[treatment13][embr])
				outFile.write(str(lin1MeansAdjusted[treatment13][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 23:
		if len(lin1Means[treatment14]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment14]) - 1:
				lin1MeansAdjusted[treatment14].append(lin1Means[treatment14][embr] - negativeControlLineageMeans[treatment14][embr])
				outFile.write(str(lin1MeansAdjusted[treatment14][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 24:
		if len(lin1Means[treatment15]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment15]) - 1:
				lin1MeansAdjusted[treatment15].append(lin1Means[treatment15][embr] - negativeControlLineageMeans[treatment15][embr])
				outFile.write(str(lin1MeansAdjusted[treatment15][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 25:
		if len(lin1Means[treatment16]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment16]) - 1:
				lin1MeansAdjusted[treatment16].append(lin1Means[treatment16][embr] - negativeControlLineageMeans[treatment16][embr])
				outFile.write(str(lin1MeansAdjusted[treatment16][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 26:
		if len(lin1Means[treatment17]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment17]) - 1:
				lin1MeansAdjusted[treatment17].append(lin1Means[treatment17][embr] - negativeControlLineageMeans[treatment17][embr])
				outFile.write(str(lin1MeansAdjusted[treatment17][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 27:
		if len(lin1Means[treatment18]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment18]) - 1:
				lin1MeansAdjusted[treatment18].append(lin1Means[treatment18][embr] - negativeControlLineageMeans[treatment18][embr])
				outFile.write(str(lin1MeansAdjusted[treatment18][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 28:
		if len(lin1Means[treatment19]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment19]) - 1:
				lin1MeansAdjusted[treatment19].append(lin1Means[treatment19][embr] - negativeControlLineageMeans[treatment19][embr])
				outFile.write(str(lin1MeansAdjusted[treatment19][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 29:
		if len(lin1Means[treatment20]) > 0:
			embr = 0
			while embr <= len(lin1Means[treatment20]) - 1:
				lin1MeansAdjusted[treatment20].append(lin1Means[treatment20][embr] - negativeControlLineageMeans[treatment20][embr])
				outFile.write(str(lin1MeansAdjusted[treatment20][embr]) + ",")
				embr = embr + 1
	outFile.seek(-1, os.SEEK_CUR)
	outFile.write("\n")

if negativeControlLineage != "none":
	outFile.write(lineage2 + " adjusted mean,")
	if len(sys.argv) == 29:		###Make dictionary of adjusted mean blot values for lineage2 in embryos under each treatment.
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[], treatment20:[]}
	elif len(sys.argv) == 28:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[], treatment19:[]}
	elif len(sys.argv) == 27:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[], treatment18:[]}
	elif len(sys.argv) == 26:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[], treatment17:[]}
	elif len(sys.argv) == 25:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[], treatment16:[]}
	elif len(sys.argv) == 24:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[], treatment15:[]}
	elif len(sys.argv) == 23:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[], treatment14:[]}
	elif len(sys.argv) == 22:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[], treatment13:[]}
	elif len(sys.argv) == 21:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[], treatment12:[]}
	elif len(sys.argv) == 20:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[], treatment11:[]}
	elif len(sys.argv) == 19:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[], treatment10:[]}
	elif len(sys.argv) == 18:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[], treatment9:[]}
	elif len(sys.argv) == 17:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[], treatment8:[]}
	elif len(sys.argv) == 16:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[], treatment7:[]}
	elif len(sys.argv) == 15:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[], treatment6:[]}
	elif len(sys.argv) == 14:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[], treatment5:[]}
	elif len(sys.argv) == 13:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[], treatment4:[]}	
	elif len(sys.argv) == 12:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[], treatment3:[]}	
	elif len(sys.argv) == 11:
		lin2MeansAdjusted = {"WT":[], treatment1:[], treatment2:[]}	
	elif len(sys.argv) == 10:
		lin2MeansAdjusted = {"WT":[], treatment1:[]}	
	elif len(sys.argv) == 9:
		lin2MeansAdjusted = {"WT":[]}	
	embr = 0
	while embr <= len(lin2Means["WT"]) - 1:
		lin2MeansAdjusted["WT"].append(lin2Means["WT"][embr] - negativeControlLineageMeans["WT"][embr])
		outFile.write(str(lin2MeansAdjusted["WT"][embr]) + ",")
		embr = embr + 1
	if len(sys.argv) >= 10:		###Make dictionary with adjusted means for lineage2
		if len(lin2Means[treatment1]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment1]) - 1:
				lin2MeansAdjusted[treatment1].append(lin2Means[treatment1][embr] - negativeControlLineageMeans[treatment1][embr])
				outFile.write(str(lin2MeansAdjusted[treatment1][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 11:
		if len(lin2Means[treatment2]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment2]) - 1:
				lin2MeansAdjusted[treatment2].append(lin2Means[treatment2][embr] - negativeControlLineageMeans[treatment2][embr])
				outFile.write(str(lin2MeansAdjusted[treatment2][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 12:
		if len(lin2Means[treatment3]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment3]) - 1:
				lin2MeansAdjusted[treatment3].append(lin2Means[treatment3][embr] - negativeControlLineageMeans[treatment3][embr])
				outFile.write(str(lin2MeansAdjusted[treatment3][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 13:
		if len(lin2Means[treatment4]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment4]) - 1:
				lin2MeansAdjusted[treatment4].append(lin2Means[treatment4][embr] - negativeControlLineageMeans[treatment4][embr])
				outFile.write(str(lin2MeansAdjusted[treatment4][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 14:
		if len(lin2Means[treatment5]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment5]) - 1:
				lin2MeansAdjusted[treatment5].append(lin2Means[treatment5][embr] - negativeControlLineageMeans[treatment5][embr])
				outFile.write(str(lin2MeansAdjusted[treatment5][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 15:
		if len(lin2Means[treatment6]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment6]) - 1:
				lin2MeansAdjusted[treatment6].append(lin2Means[treatment6][embr] - negativeControlLineageMeans[treatment6][embr])
				outFile.write(str(lin2MeansAdjusted[treatment6][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 16:
		if len(lin2Means[treatment7]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment7]) - 1:
				lin2MeansAdjusted[treatment7].append(lin2Means[treatment7][embr] - negativeControlLineageMeans[treatment7][embr])
				outFile.write(str(lin2MeansAdjusted[treatment7][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 17:
		if len(lin2Means[treatment8]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment8]) - 1:
				lin2MeansAdjusted[treatment8].append(lin2Means[treatment8][embr] - negativeControlLineageMeans[treatment8][embr])
				outFile.write(str(lin2MeansAdjusted[treatment8][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 18:
		if len(lin2Means[treatment9]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment9]) - 1:
				lin2MeansAdjusted[treatment9].append(lin2Means[treatment9][embr] - negativeControlLineageMeans[treatment9][embr])
				outFile.write(str(lin2MeansAdjusted[treatment9][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 19:
		if len(lin2Means[treatment10]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment10]) - 1:
				lin2MeansAdjusted[treatment10].append(lin2Means[treatment10][embr] - negativeControlLineageMeans[treatment10][embr])
				outFile.write(str(lin2MeansAdjusted[treatment10][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 20:
		if len(lin2Means[treatment11]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment11]) - 1:
				lin2MeansAdjusted[treatment11].append(lin2Means[treatment11][embr] - negativeControlLineageMeans[treatment11][embr])
				outFile.write(str(lin2MeansAdjusted[treatment11][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 21:
		if len(lin2Means[treatment12]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment12]) - 1:
				lin2MeansAdjusted[treatment12].append(lin2Means[treatment12][embr] - negativeControlLineageMeans[treatment12][embr])
				outFile.write(str(lin2MeansAdjusted[treatment12][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 22:
		if len(lin2Means[treatment13]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment13]) - 1:
				lin2MeansAdjusted[treatment13].append(lin2Means[treatment13][embr] - negativeControlLineageMeans[treatment13][embr])
				outFile.write(str(lin2MeansAdjusted[treatment13][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 23:
		if len(lin2Means[treatment14]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment14]) - 1:
				lin2MeansAdjusted[treatment14].append(lin2Means[treatment14][embr] - negativeControlLineageMeans[treatment14][embr])
				outFile.write(str(lin2MeansAdjusted[treatment14][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 24:
		if len(lin2Means[treatment15]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment15]) - 1:
				lin2MeansAdjusted[treatment15].append(lin2Means[treatment15][embr] - negativeControlLineageMeans[treatment15][embr])
				outFile.write(str(lin2MeansAdjusted[treatment15][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 25:
		if len(lin2Means[treatment16]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment16]) - 1:
				lin2MeansAdjusted[treatment16].append(lin2Means[treatment16][embr] - negativeControlLineageMeans[treatment16][embr])
				outFile.write(str(lin2MeansAdjusted[treatment16][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 26:
		if len(lin2Means[treatment17]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment17]) - 1:
				lin2MeansAdjusted[treatment17].append(lin2Means[treatment17][embr] - negativeControlLineageMeans[treatment17][embr])
				outFile.write(str(lin2MeansAdjusted[treatment17][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 27:
		if len(lin2Means[treatment18]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment18]) - 1:
				lin2MeansAdjusted[treatment18].append(lin2Means[treatment18][embr] - negativeControlLineageMeans[treatment18][embr])
				outFile.write(str(lin2MeansAdjusted[treatment18][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 28:
		if len(lin2Means[treatment19]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment19]) - 1:
				lin2MeansAdjusted[treatment19].append(lin2Means[treatment19][embr] - negativeControlLineageMeans[treatment19][embr])
				outFile.write(str(lin2MeansAdjusted[treatment19][embr]) + ",")
				embr = embr + 1
	if len(sys.argv) >= 29:
		if len(lin2Means[treatment20]) > 0:
			embr = 0
			while embr <= len(lin2Means[treatment20]) - 1:
				lin2MeansAdjusted[treatment20].append(lin2Means[treatment20][embr] - negativeControlLineageMeans[treatment20][embr])
				outFile.write(str(lin2MeansAdjusted[treatment20][embr]) + ",")
				embr = embr + 1
	outFile.seek(-1, os.SEEK_CUR)			
	

#outFile.write("\n" + lineage1 + " t-test\tWT mean +/- stdev\tpop-1i mean +/- stdev\tWT to pop-1i\n\t"  + str(mean(lin1Means["WT"])) + "+/-" + str(numpy.std(lin1Means["WT"], axis=0)) + "\t" + str(mean(lin1Means["pop-1i"])) + "+/-" + str(numpy.std(lin1Means["pop-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin1Means["WT"], lin1Means["pop-1i"])) + "\n" + lineage2 +" t-test\tWT mean +/- stdev\tpop-1i mean +/- stdev\tsys-1i mean +/- stdev\tWT to pop-1i\tWT to sys-1i\n\t" + str(mean(lin2Means["WT"])) + "+/-" + str(numpy.std(lin2Means["WT"], axis=0)) + "\t" + str(mean(lin2Means["pop-1i"])) + "+/-" + str(numpy.std(lin2Means["pop-1i"], axis=0)) + "\t" + str(mean(lin2Means["sys-1i"])) + "+/-" + str(numpy.std(lin2Means["sys-1i"], axis=0)) + "\t" +str(stats.ttest_ind(lin2Means["WT"], lin2Means["pop-1i"])) + "\t" + str(stats.ttest_ind(lin2Means["WT"], lin2Means["sys-1i"])) + "\n")
#outFile.write("\n" + lineage1 + " t-test\tWT mean +/- stdev\tpop-1i mean +/- stdev\tWT to pop-1i\n\t"  + str(mean(lin1Means["WT"])) + "+/-" + str(numpy.std(lin1Means["WT"], axis=0)) + "\t" + str(mean(lin1Means["pop-1i"])) + "+/-" + str(numpy.std(lin1Means["pop-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin1Means["WT"], lin1Means["pop-1i"])) + "\n" + lineage2 +" t-test\tWT mean +/- stdev\tpop-1i mean +/- stdev\tsys-1i mean +/- stdev\tlit-1i mean +/- stdev\tWT to pop-1i\tWT to sys-1i\n\tWT to lit-1i\n\t" + str(mean(lin2Means["WT"])) + "+/-" + str(numpy.std(lin2Means["WT"], axis=0)) + "\t" + str(mean(lin2Means["pop-1i"])) + "+/-" + str(numpy.std(lin2Means["pop-1i"], axis=0)) + "\t" + str(mean(lin2Means["sys-1i"])) + "+/-" + str(numpy.std(lin2Means["sys-1i"], axis=0)) + "\t" + str(mean(lin2Means["lit-1i"])) + "+/-" + str(numpy.std(lin2Means["lit-i"], axis=0)) + "\t" + str(stats.ttest_ind(lin2Means["WT"], lin2Means["pop-1i"])) + "\t" + str(stats.ttest_ind(lin2Means["WT"], lin2Means["sys-1i"])) + str(stats.ttest_ind(lin2Means["WT"], lin2Means["lit-1i"])) + "\n")

outFile.write("\n,\n" + lineage1 + " mean +/- stdev,WT mean +/- stdev,")
if len(sys.argv) >= 10:		###Write column titles of treatments for raw treatment means and standard deviations.
	if len(lin1Means[treatment1]) > 0:
		outFile.write(treatment1 + " mean +/- stdev,")
if len(sys.argv) >= 11:
	if len(lin1Means[treatment2]) > 0:
		outFile.write(treatment2 + " mean +/- stdev,")
if len(sys.argv) >= 12:
	if len(lin1Means[treatment3]) > 0:
		outFile.write(treatment3 + " mean +/- stdev,")
if len(sys.argv) >= 13:
	if len(lin1Means[treatment4]) > 0:
		outFile.write(treatment4 + " mean +/- stdev,")
if len(sys.argv) >= 14:
	if len(lin1Means[treatment5]) > 0:
		outFile.write(treatment5 + " mean +/- stdev,")
if len(sys.argv) >= 15:
	if len(lin1Means[treatment6]) > 0:
		outFile.write(treatment6 + " mean +/- stdev,")
if len(sys.argv) >= 16:
	if len(lin1Means[treatment7]) > 0:
		outFile.write(treatment7 + " mean +/- stdev,")
if len(sys.argv) >= 17:
	if len(lin1Means[treatment8]) > 0:
		outFile.write(treatment8 + " mean +/- stdev,")
if len(sys.argv) >= 18:
	if len(lin1Means[treatment9]) > 0:
		outFile.write(treatment9 + " mean +/- stdev,")
if len(sys.argv) >= 19:
	if len(lin1Means[treatment10]) > 0:
		outFile.write(treatment10 + " mean +/- stdev,")
if len(sys.argv) >= 20:
	if len(lin1Means[treatment11]) > 0:
		outFile.write(treatment11 + " mean +/- stdev,")
if len(sys.argv) >= 21:
	if len(lin1Means[treatment12]) > 0:
		outFile.write(treatment12 + " mean +/- stdev,")
if len(sys.argv) >= 22:
	if len(lin1Means[treatment13]) > 0:
		outFile.write(treatment13 + " mean +/- stdev,")
if len(sys.argv) >= 23:
	if len(lin1Means[treatment14]) > 0:
		outFile.write(treatment14 + " mean +/- stdev,")
if len(sys.argv) >= 24:
	if len(lin1Means[treatment15]) > 0:
		outFile.write(treatment15 + " mean +/- stdev,")
if len(sys.argv) >= 25:
	if len(lin1Means[treatment16]) > 0:
		outFile.write(treatment16 + " mean +/- stdev,")
if len(sys.argv) >= 26:
	if len(lin1Means[treatment17]) > 0:
		outFile.write(treatment17 + " mean +/- stdev,")
if len(sys.argv) >= 27:
	if len(lin1Means[treatment18]) > 0:
		outFile.write(treatment18 + " mean +/- stdev,")
if len(sys.argv) >= 28:
	if len(lin1Means[treatment19]) > 0:
		outFile.write(treatment19 + " mean +/- stdev,")
if len(sys.argv) >= 29:
	if len(lin1Means[treatment20]) > 0:
		outFile.write(treatment20 + " mean +/- stdev,")

if negativeControlLineage != "none":
	if len(sys.argv) >= 9:
		if len(lin1Means["WT"]) > 0:
			outFile.write("WT adjusted mean +/- stdev,")
	if len(sys.argv) >= 10:		###Write column titles of treatments for adjusted treatment means and standard deviations.
		if len(lin1Means[treatment1]) > 0:
			outFile.write(treatment1 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 11:
		if len(lin1Means[treatment2]) > 0:
			outFile.write(treatment2 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 12:
		if len(lin1Means[treatment3]) > 0:
			outFile.write(treatment3 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 13:
		if len(lin1Means[treatment4]) > 0:
			outFile.write(treatment4 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 14:
		if len(lin1Means[treatment5]) > 0:
			outFile.write(treatment5 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 15:
		if len(lin1Means[treatment6]) > 0:
			outFile.write(treatment6 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 16:
		if len(lin1Means[treatment7]) > 0:
			outFile.write(treatment7 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 17:
		if len(lin1Means[treatment8]) > 0:
			outFile.write(treatment8 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 18:
		if len(lin1Means[treatment9]) > 0:
			outFile.write(treatment9 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 19:
		if len(lin1Means[treatment10]) > 0:
			outFile.write(treatment10 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 20:
		if len(lin1Means[treatment11]) > 0:
			outFile.write(treatment11 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 21:
		if len(lin1Means[treatment12]) > 0:
			outFile.write(treatment12 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 22:
		if len(lin1Means[treatment13]) > 0:
			outFile.write(treatment13 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 23:
		if len(lin1Means[treatment14]) > 0:
			outFile.write(treatment14 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 24:
		if len(lin1Means[treatment15]) > 0:
			outFile.write(treatment15 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 25:
		if len(lin1Means[treatment16]) > 0:
			outFile.write(treatment16 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 26:
		if len(lin1Means[treatment17]) > 0:
			outFile.write(treatment17 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 27:
		if len(lin1Means[treatment18]) > 0:
			outFile.write(treatment18 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 28:
		if len(lin1Means[treatment19]) > 0:
			outFile.write(treatment19 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 29:
		if len(lin1Means[treatment20]) > 0:
			outFile.write(treatment20 + " adjusted mean +/- stdev,")
outFile.seek(-1, os.SEEK_CUR)

#if len(sys.argv) >= 7:		###Write column titles of treatments for WT to treatment t-tests.
#	if len(lin1Means[treatment1]) > 0:
#		outFile.write("WT to " + treatment1 + "\t")
#if len(sys.argv) >= 8:
#	if len(lin1Means[treatment2]) > 0:
#		outFile.write("WT to " + treatment2 + "\t")
#if len(sys.argv) >= 9:
#	if len(lin1Means[treatment3]) > 0:
#		outFile.write("WT to " + treatment3 + "\t")
#if len(sys.argv) >= 10:
#	if len(lin1Means[treatment4]) > 0:
#		outFile.write("WT to " + treatment4 + "\t")
#if len(sys.argv) >= 11:
#	if len(lin1Means[treatment5]) > 0:
#		outFile.write("WT to " + treatment5 + "\t")
#if len(sys.argv) >= 12:
#	if len(lin1Means[treatment6]) > 0:
#		outFile.write("WT to " + treatment6 + "\t")
#if len(sys.argv) >= 13:
#	if len(lin1Means[treatment7]) > 0:
#		outFile.write("WT to " + treatment7 + "\t")
#if len(sys.argv) >= 14:
#	if len(lin1Means[treatment8]) > 0:
#		outFile.write("WT to " + treatment8 + "\t")
#if len(sys.argv) >= 15:
#	if len(lin1Means[treatment9]) > 0:
#		outFile.write("WT to " + treatment9 + "\t")
#if len(sys.argv) >= 16:
#	if len(lin1Means[treatment10]) > 0:
#		outFile.write("WT to " + treatment10 + "\t")
#if len(sys.argv) >= 17:
#	if len(lin1Means[treatment11]) > 0:
#		outFile.write("WT to " + treatment11 + "\t")
#if len(sys.argv) >= 18:
#	if len(lin1Means[treatment12]) > 0:
#		outFile.write("WT to " + treatment12 + "\t")
#if len(sys.argv) >= 19:
#	if len(lin1Means[treatment13]) > 0:
#		outFile.write("WT to " + treatment13 + "\t")
#if len(sys.argv) >= 20:
#	if len(lin1Means[treatment14]) > 0:
#		outFile.write("WT to " + treatment14 + "\t")
#if len(sys.argv) >= 21:
#	if len(lin1Means[treatment15]) > 0:
#		outFile.write("WT to " + treatment15 + "\t")
#if len(sys.argv) >= 22:
#	if len(lin1Means[treatment16]) > 0:
#		outFile.write("WT to " + treatment16 + "\t")
#if len(sys.argv) >= 23:
#	if len(lin1Means[treatment17]) > 0:
#		outFile.write("WT to " + treatment17 + "\t")
#if len(sys.argv) >= 24:
#	if len(lin1Means[treatment18]) > 0:
#		outFile.write("WT to " + treatment18 + "\t")
#if len(sys.argv) >= 25:
#	if len(lin1Means[treatment19]) > 0:
#		outFile.write("WT to " + treatment19 + "\t")
#if len(sys.argv) >= 26:
#	if len(lin1Means[treatment20]) > 0:
#		outFile.write("WT to " + treatment20 + "\t")

outFile.write("\n," + str(mean(lin1Means["WT"])) + "+/-" + str(numpy.std(lin1Means["WT"], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 10:		###Write lineage1 treatment raw means.
	if len(lin1Means[treatment1]) > 0:
		outFile.write(str(mean(lin1Means[treatment1])) + "+/-" + str(numpy.std(lin1Means[treatment1], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 11:
	if len(lin1Means[treatment2]) > 0:
		outFile.write(str(mean(lin1Means[treatment2])) + "+/-" + str(numpy.std(lin1Means[treatment2], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 12:
	if len(lin1Means[treatment3]) > 0:
		outFile.write(str(mean(lin1Means[treatment3])) + "+/-" + str(numpy.std(lin1Means[treatment3], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 13:
	if len(lin1Means[treatment4]) > 0:
		outFile.write(str(mean(lin1Means[treatment4])) + "+/-" + str(numpy.std(lin1Means[treatment4], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 14:
	if len(lin1Means[treatment5]) > 0:
		outFile.write(str(mean(lin1Means[treatment5])) + "+/-" + str(numpy.std(lin1Means[treatment5], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 15:
	if len(lin1Means[treatment6]) > 0:
		outFile.write(str(mean(lin1Means[treatment6])) + "+/-" + str(numpy.std(lin1Means[treatment6], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 16:
	if len(lin1Means[treatment7]) > 0:
		outFile.write(str(mean(lin1Means[treatment7])) + "+/-" + str(numpy.std(lin1Means[treatment7], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 17:
	if len(lin1Means[treatment8]) > 0:
		outFile.write(str(mean(lin1Means[treatment8])) + "+/-" + str(numpy.std(lin1Means[treatment8], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 18:
	if len(lin1Means[treatment9]) > 0:
		outFile.write(str(mean(lin1Means[treatment9])) + "+/-" + str(numpy.std(lin1Means[treatment9], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 19:
	if len(lin1Means[treatment10]) > 0:
		outFile.write(str(mean(lin1Means[treatment10])) + "+/-" + str(numpy.std(lin1Means[treatment10], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 20:
	if len(lin1Means[treatment11]) > 0:
		outFile.write(str(mean(lin1Means[treatment11])) + "+/-" + str(numpy.std(lin1Means[treatment11], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 21:
	if len(lin1Means[treatment12]) > 0:
		outFile.write(str(mean(lin1Means[treatment12])) + "+/-" + str(numpy.std(lin1Means[treatment12], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 22:
	if len(lin1Means[treatment13]) > 0:
		outFile.write(str(mean(lin1Means[treatment13])) + "+/-" + str(numpy.std(lin1Means[treatment13], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 23:
	if len(lin1Means[treatment14]) > 0:
		outFile.write(str(mean(lin1Means[treatment14])) + "+/-" + str(numpy.std(lin1Means[treatment14], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 24:
	if len(lin1Means[treatment15]) > 0:
		outFile.write(str(mean(lin1Means[treatment15])) + "+/-" + str(numpy.std(lin1Means[treatment15], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 25:
	if len(lin1Means[treatment16]) > 0:
		outFile.write(str(mean(lin1Means[treatment16])) + "+/-" + str(numpy.std(lin1Means[treatment16], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 26:
	if len(lin1Means[treatment17]) > 0:
		outFile.write(str(mean(lin1Means[treatment17])) + "+/-" + str(numpy.std(lin1Means[treatment17], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 27:
	if len(lin1Means[treatment18]) > 0:
		outFile.write(str(mean(lin1Means[treatment18])) + "+/-" + str(numpy.std(lin1Means[treatment18], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 28:
	if len(lin1Means[treatment19]) > 0:
		outFile.write(str(mean(lin1Means[treatment19])) + "+/-" + str(numpy.std(lin1Means[treatment19], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 29:
	if len(lin1Means[treatment20]) > 0:
		outFile.write(str(mean(lin1Means[treatment20])) + "+/-" + str(numpy.std(lin1Means[treatment20], axis=0, ddof = 1)) + ",")




if negativeControlLineage != "none":
	outFile.write(str(mean(lin1MeansAdjusted["WT"])) + "+/-" + str(numpy.std(lin1MeansAdjusted["WT"], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 10:		###Write lineage1 treatment adjusted means.  Means are adjusted by subtracting the mean blot values for negativeControlLineage in WT embryos.
		if len(lin1Means[treatment1]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment1])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment1], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 11:
		if len(lin1Means[treatment2]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment2])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment2], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 12:
		if len(lin1Means[treatment3]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment3])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment3], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 13:
		if len(lin1Means[treatment4]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment4])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment4], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 14:
		if len(lin1Means[treatment5]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment5])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment5], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 15:
		if len(lin1Means[treatment6]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment6])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment6], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 16:
		if len(lin1Means[treatment7]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment7])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment7], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 17:
		if len(lin1Means[treatment8]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment8])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment8], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 18:
		if len(lin1Means[treatment9]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment9])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment9], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 19:
		if len(lin1Means[treatment10]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment10])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment10], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 20:
		if len(lin1Means[treatment11]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment11])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment11], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 21:
		if len(lin1Means[treatment12]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment12])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment12], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 22:
		if len(lin1Means[treatment13]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment13])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment13], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 23:
		if len(lin1Means[treatment14]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment14])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment14], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 24:
		if len(lin1Means[treatment15]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment15])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment15], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 25:
		if len(lin1Means[treatment16]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment16])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment16], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 26:
		if len(lin1Means[treatment17]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment17])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment17], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 27:
		if len(lin1Means[treatment18]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment18])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment18], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 28:
		if len(lin1Means[treatment19]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment19])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment19], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 29:
		if len(lin1Means[treatment20]) > 0:
			outFile.write(str(mean(lin1MeansAdjusted[treatment20])) + "+/-" + str(numpy.std(lin1MeansAdjusted[treatment20], axis=0, ddof = 1)) + ",")
outFile.seek(-1, os.SEEK_CUR)			
#print "lineage 1 means are " 
#print lin1Means
#print "negative control lineage means are " 
#print negativeControlLineageMeans
#print "Adjusted lineage 1 means are " 
#print lin1MeansAdjusted

#if negativeControlLineage == "none":		
#	if len(sys.argv) >= 7:		###Write lineage1 WT to treatment t-test.
#		if len(lin1Means[treatment1]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1Means["WT"], lin1Means[treatment20])) + "\t")
#			
#if negativeControlLineage != "none":		
#	if len(sys.argv) >= 7:		###Write adjusted lineage1 WT to treatment t-test.
#		if len(lin1Means[treatment1]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			outFile.write(str(stats.ttest_ind(lin1MeansAdjusted["WT"], lin1MeansAdjusted[treatment20])) + "\t")


outFile.write("\n" + lineage2 + " mean +/- stdev,WT mean +/- stdev,")
if len(sys.argv) >= 10:		###Write column titles of treatments for lineage2 treatment raw means and standard deviations.
	if len(lin2Means[treatment1]) > 0:
		outFile.write(treatment1 + " mean +/- stdev,")
if len(sys.argv) >= 11:
	if len(lin2Means[treatment2]) > 0:
		outFile.write(treatment2 + " mean +/- stdev,")
if len(sys.argv) >= 12:
	if len(lin2Means[treatment3]) > 0:
		outFile.write(treatment3 + " mean +/- stdev,")
if len(sys.argv) >= 13:
	if len(lin2Means[treatment4]) > 0:
		outFile.write(treatment4 + " mean +/- stdev,")
if len(sys.argv) >= 14:
	if len(lin2Means[treatment5]) > 0:
		outFile.write(treatment5 + " mean +/- stdev,")
if len(sys.argv) >= 15:
	if len(lin2Means[treatment6]) > 0:
		outFile.write(treatment6 + " mean +/- stdev,")
if len(sys.argv) >= 16:
	if len(lin2Means[treatment7]) > 0:
		outFile.write(treatment7 + " mean +/- stdev,")
if len(sys.argv) >= 17:
	if len(lin2Means[treatment8]) > 0:
		outFile.write(treatment8 + " mean +/- stdev,")
if len(sys.argv) >= 18:
	if len(lin2Means[treatment9]) > 0:
		outFile.write(treatment9 + " mean +/- stdev,")
if len(sys.argv) >= 19:
	if len(lin2Means[treatment10]) > 0:
		outFile.write(treatment10 + " mean +/- stdev,")
if len(sys.argv) >= 20:
	if len(lin2Means[treatment11]) > 0:
		outFile.write(treatment11 + " mean +/- stdev,")
if len(sys.argv) >= 21:
	if len(lin2Means[treatment12]) > 0:
		outFile.write(treatment12 + " mean +/- stdev,")
if len(sys.argv) >= 22:
	if len(lin2Means[treatment13]) > 0:
		outFile.write(treatment13 + " mean +/- stdev,")
if len(sys.argv) >= 23:
	if len(lin2Means[treatment14]) > 0:
		outFile.write(treatment14 + " mean +/- stdev,")
if len(sys.argv) >= 24:
	if len(lin2Means[treatment15]) > 0:
		outFile.write(treatment15 + " mean +/- stdev,")
if len(sys.argv) >= 25:
	if len(lin2Means[treatment16]) > 0:
		outFile.write(treatment16 + " mean +/- stdev,")
if len(sys.argv) >= 26:
	if len(lin2Means[treatment17]) > 0:
		outFile.write(treatment17 + " mean +/- stdev,")
if len(sys.argv) >= 27:
	if len(lin2Means[treatment18]) > 0:
		outFile.write(treatment18 + " mean +/- stdev,")
if len(sys.argv) >= 28:
	if len(lin2Means[treatment19]) > 0:
		outFile.write(treatment19 + " mean +/- stdev,")
if len(sys.argv) >= 29:
	if len(lin2Means[treatment20]) > 0:
		outFile.write(treatment20 + " mean +/- stdev,")
		
if negativeControlLineage != "none":
	if len(sys.argv) >= 9:
		if len(lin2Means["WT"]) > 0:
			outFile.write("WT adjusted mean +/- stdev,")
	if len(sys.argv) >= 10:		###Write column titles of treatments for lineage2 treatment adjusted means and standard deviations.
		if len(lin2Means[treatment1]) > 0:
			outFile.write(treatment1 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 11:
		if len(lin2Means[treatment2]) > 0:
			outFile.write(treatment2 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 12:
		if len(lin2Means[treatment3]) > 0:
			outFile.write(treatment3 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 13:
		if len(lin2Means[treatment4]) > 0:
			outFile.write(treatment4 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 14:
		if len(lin2Means[treatment5]) > 0:
			outFile.write(treatment5 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 15:
		if len(lin2Means[treatment6]) > 0:
			outFile.write(treatment6 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 16:
		if len(lin2Means[treatment7]) > 0:
			outFile.write(treatment7 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 17:
		if len(lin2Means[treatment8]) > 0:
			outFile.write(treatment8 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 18:
		if len(lin2Means[treatment9]) > 0:
			outFile.write(treatment9 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 19:
		if len(lin2Means[treatment10]) > 0:
			outFile.write(treatment10 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 20:
		if len(lin2Means[treatment11]) > 0:
			outFile.write(treatment11 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 21:
		if len(lin2Means[treatment12]) > 0:
			outFile.write(treatment12 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 22:
		if len(lin2Means[treatment13]) > 0:
			outFile.write(treatment13 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 23:
		if len(lin2Means[treatment14]) > 0:
			outFile.write(treatment14 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 24:
		if len(lin2Means[treatment15]) > 0:
			outFile.write(treatment15 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 25:
		if len(lin2Means[treatment16]) > 0:
			outFile.write(treatment16 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 26:
		if len(lin2Means[treatment17]) > 0:
			outFile.write(treatment17 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 27:
		if len(lin2Means[treatment18]) > 0:
			outFile.write(treatment18 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 28:
		if len(lin2Means[treatment19]) > 0:
			outFile.write(treatment19 + " adjusted mean +/- stdev,")
	if len(sys.argv) >= 29:
		if len(lin2Means[treatment20]) > 0:
			outFile.write(treatment20 + " adjusted mean +/- stdev,")
outFile.seek(-1, os.SEEK_CUR)

#if len(sys.argv) >= 7:		###Write column titles of treatments for lineage2 WT to treatment t-tests.
#	if len(lin2Means[treatment1]) > 0:
#		outFile.write("WT to " + treatment1 + "\t")
#if len(sys.argv) >= 8:
#	if len(lin2Means[treatment2]) > 0:
#		outFile.write("WT to " + treatment2 + "\t")
#if len(sys.argv) >= 9:
#	if len(lin2Means[treatment3]) > 0:
#		outFile.write("WT to " + treatment3 + "\t")
#if len(sys.argv) >= 10:
#	if len(lin2Means[treatment4]) > 0:
#		outFile.write("WT to " + treatment4 + "\t")
#if len(sys.argv) >= 11:
#	if len(lin2Means[treatment5]) > 0:
#		outFile.write("WT to " + treatment5 + "\t")
#if len(sys.argv) >= 12:
#	if len(lin2Means[treatment6]) > 0:
#		outFile.write("WT to " + treatment6 + "\t")
#if len(sys.argv) >= 13:
#	if len(lin2Means[treatment7]) > 0:
#		outFile.write("WT to " + treatment7 + "\t")
#if len(sys.argv) >= 14:
#	if len(lin2Means[treatment8]) > 0:
#		outFile.write("WT to " + treatment8 + "\t")
#if len(sys.argv) >= 15:
#	if len(lin2Means[treatment9]) > 0:
#		outFile.write("WT to " + treatment9 + "\t")
#if len(sys.argv) >= 16:
#	if len(lin2Means[treatment10]) > 0:
#		outFile.write("WT to " + treatment10 + "\t")
#if len(sys.argv) >= 17:
#	if len(lin2Means[treatment11]) > 0:
#		outFile.write("WT to " + treatment11 + "\t")
#if len(sys.argv) >= 18:
#	if len(lin2Means[treatment12]) > 0:
#		outFile.write("WT to " + treatment12 + "\t")
#if len(sys.argv) >= 19:
#	if len(lin2Means[treatment13]) > 0:
#		outFile.write("WT to " + treatment13 + "\t")
#if len(sys.argv) >= 20:
#	if len(lin2Means[treatment14]) > 0:
#		outFile.write("WT to " + treatment14 + "\t")
#if len(sys.argv) >= 21:
#	if len(lin2Means[treatment15]) > 0:
#		outFile.write("WT to " + treatment15 + "\t")
#if len(sys.argv) >= 22:
#	if len(lin2Means[treatment16]) > 0:
#		outFile.write("WT to " + treatment16 + "\t")
#if len(sys.argv) >= 23:
#	if len(lin2Means[treatment17]) > 0:
#		outFile.write("WT to " + treatment17 + "\t")
#if len(sys.argv) >= 24:
#	if len(lin2Means[treatment18]) > 0:
#		outFile.write("WT to " + treatment18 + "\t")
#if len(sys.argv) >= 25:
#	if len(lin2Means[treatment19]) > 0:
#		outFile.write("WT to " + treatment19 + "\t")
#if len(sys.argv) >= 26:
#	if len(lin2Means[treatment20]) > 0:
#		outFile.write("WT to " + treatment20 + "\t")

outFile.write("\n," + str(mean(lin2Means["WT"])) + "+/-" + str(numpy.std(lin2Means["WT"], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 10:		###Write lineage2 treatment raw means.
	if len(lin2Means[treatment1]) > 0:
		outFile.write(str(mean(lin2Means[treatment1])) + "+/-" + str(numpy.std(lin2Means[treatment1], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 11:
	if len(lin2Means[treatment2]) > 0:
		outFile.write(str(mean(lin2Means[treatment2])) + "+/-" + str(numpy.std(lin2Means[treatment2], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 12:
	if len(lin2Means[treatment3]) > 0:
		outFile.write(str(mean(lin2Means[treatment3])) + "+/-" + str(numpy.std(lin2Means[treatment3], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 13:
	if len(lin2Means[treatment4]) > 0:
		outFile.write(str(mean(lin2Means[treatment4])) + "+/-" + str(numpy.std(lin2Means[treatment4], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 14:
	if len(lin2Means[treatment5]) > 0:
		outFile.write(str(mean(lin2Means[treatment5])) + "+/-" + str(numpy.std(lin2Means[treatment5], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 15:
	if len(lin2Means[treatment6]) > 0:
		outFile.write(str(mean(lin2Means[treatment6])) + "+/-" + str(numpy.std(lin2Means[treatment6], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 16:
	if len(lin2Means[treatment7]) > 0:
		outFile.write(str(mean(lin2Means[treatment7])) + "+/-" + str(numpy.std(lin2Means[treatment7], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 17:
	if len(lin2Means[treatment8]) > 0:
		outFile.write(str(mean(lin2Means[treatment8])) + "+/-" + str(numpy.std(lin2Means[treatment8], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 18:
	if len(lin2Means[treatment9]) > 0:
		outFile.write(str(mean(lin2Means[treatment9])) + "+/-" + str(numpy.std(lin2Means[treatment9], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 19:
	if len(lin2Means[treatment10]) > 0:
		outFile.write(str(mean(lin2Means[treatment10])) + "+/-" + str(numpy.std(lin2Means[treatment10], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 20:
	if len(lin2Means[treatment11]) > 0:
		outFile.write(str(mean(lin2Means[treatment11])) + "+/-" + str(numpy.std(lin2Means[treatment11], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 21:
	if len(lin2Means[treatment12]) > 0:
		outFile.write(str(mean(lin2Means[treatment12])) + "+/-" + str(numpy.std(lin2Means[treatment12], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 22:
	if len(lin2Means[treatment13]) > 0:
		outFile.write(str(mean(lin2Means[treatment13])) + "+/-" + str(numpy.std(lin2Means[treatment13], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 23:
	if len(lin2Means[treatment14]) > 0:
		outFile.write(str(mean(lin2Means[treatment14])) + "+/-" + str(numpy.std(lin2Means[treatment14], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 24:
	if len(lin2Means[treatment15]) > 0:
		outFile.write(str(mean(lin2Means[treatment15])) + "+/-" + str(numpy.std(lin2Means[treatment15], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 25:
	if len(lin2Means[treatment16]) > 0:
		outFile.write(str(mean(lin2Means[treatment16])) + "+/-" + str(numpy.std(lin2Means[treatment16], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 26:
	if len(lin2Means[treatment17]) > 0:
		outFile.write(str(mean(lin2Means[treatment17])) + "+/-" + str(numpy.std(lin2Means[treatment17], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 27:
	if len(lin2Means[treatment18]) > 0:
		outFile.write(str(mean(lin2Means[treatment18])) + "+/-" + str(numpy.std(lin2Means[treatment18], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 28:
	if len(lin2Means[treatment19]) > 0:
		outFile.write(str(mean(lin2Means[treatment19])) + "+/-" + str(numpy.std(lin2Means[treatment19], axis=0, ddof = 1)) + ",")
if len(sys.argv) >= 29:
	if len(lin2Means[treatment20]) > 0:
		outFile.write(str(mean(lin2Means[treatment20])) + "+/-" + str(numpy.std(lin2Means[treatment20], axis=0, ddof = 1)) + ",")




if negativeControlLineage != "none":
	outFile.write(str(mean(lin2MeansAdjusted["WT"])) + "+/-" + str(numpy.std(lin2MeansAdjusted["WT"], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 10:		###Write lineage2 treatment adjusted means.
		if len(lin2Means[treatment1]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment1])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment1], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 11:
		if len(lin2Means[treatment2]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment2])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment2], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 12:
		if len(lin2Means[treatment3]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment3])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment3], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 13:
		if len(lin2Means[treatment4]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment4])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment4], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 14:
		if len(lin2Means[treatment5]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment5])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment5], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 15:
		if len(lin2Means[treatment6]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment6])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment6], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 16:
		if len(lin2Means[treatment7]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment7])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment7], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 17:
		if len(lin2Means[treatment8]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment8])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment8], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 18:
		if len(lin2Means[treatment9]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment9])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment9], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 19:
		if len(lin2Means[treatment10]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment10])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment10], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 20:
		if len(lin2Means[treatment11]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment11])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment11], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 21:
		if len(lin2Means[treatment12]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment12])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment12], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 22:
		if len(lin2Means[treatment13]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment13])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment13], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 23:
		if len(lin2Means[treatment14]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment14])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment14], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 24:
		if len(lin2Means[treatment15]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment15])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment15], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 25:
		if len(lin2Means[treatment16]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment16])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment16], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 26:
		if len(lin2Means[treatment17]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment17])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment17], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 27:
		if len(lin2Means[treatment18]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment18])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment18], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 28:
		if len(lin2Means[treatment19]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment19])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment19], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 29:
		if len(lin2Means[treatment20]) > 0:
			outFile.write(str(mean(lin2MeansAdjusted[treatment20])) + "+/-" + str(numpy.std(lin2MeansAdjusted[treatment120], axis=0, ddof = 1)) + ",")
outFile.seek(-1, os.SEEK_CUR)		

#if negativeControlLineage == "none":
#	if len(sys.argv) >= 7:		###Write lineage2 WT to treatment t-test.
#		if len(lin2Means[treatment1]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2Means["WT"], lin2Means[treatment20])) + "\t")

#if negativeControlLineage != "none":		
#	if len(sys.argv) >= 7:		###Write adjusted lineage2 WT to treatment t-test.
#		if len(lin2Means[treatment1]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			outFile.write(str(stats.ttest_ind(lin2MeansAdjusted["WT"], lin2MeansAdjusted[treatment20])) + "\t")

if negativeControlLineage != "none":			
	outFile.write("\n" + negativeControlLineage + " mean +/- stdev,WT mean +/- stdev,")
	if len(sys.argv) >= 10:		###Write column titles of treatments for negativeControlLineage treatment means and standard deviations.
		if len(negativeControlLineageMeans[treatment1]) > 0:
			outFile.write(treatment1 + " mean +/- stdev,")
	if len(sys.argv) >= 11:
		if len(negativeControlLineageMeans[treatment2]) > 0:
			outFile.write(treatment2 + " mean +/- stdev,")
	if len(sys.argv) >= 12:
		if len(negativeControlLineageMeans[treatment3]) > 0:
			outFile.write(treatment3 + " mean +/- stdev,")
	if len(sys.argv) >= 13:
		if len(negativeControlLineageMeans[treatment4]) > 0:
			outFile.write(treatment4 + " mean +/- stdev,")
	if len(sys.argv) >= 14:
		if len(negativeControlLineageMeans[treatment5]) > 0:
			outFile.write(treatment5 + " mean +/- stdev,")
	if len(sys.argv) >= 15:
		if len(negativeControlLineageMeans[treatment6]) > 0:
			outFile.write(treatment6 + " mean +/- stdev,")
	if len(sys.argv) >= 16:
		if len(negativeControlLineageMeans[treatment7]) > 0:
			outFile.write(treatment7 + " mean +/- stdev,")
	if len(sys.argv) >= 17:
		if len(negativeControlLineageMeans[treatment8]) > 0:
			outFile.write(treatment8 + " mean +/- stdev,")
	if len(sys.argv) >= 18:
		if len(negativeControlLineageMeans[treatment9]) > 0:
			outFile.write(treatment9 + " mean +/- stdev,")
	if len(sys.argv) >= 19:
		if len(negativeControlLineageMeans[treatment10]) > 0:
			outFile.write(treatment10 + " mean +/- stdev,")
	if len(sys.argv) >= 20:
		if len(negativeControlLineageMeans[treatment11]) > 0:
			outFile.write(treatment11 + " mean +/- stdev,")
	if len(sys.argv) >= 21:
		if len(negativeControlLineageMeans[treatment12]) > 0:
			outFile.write(treatment12 + " mean +/- stdev,")
	if len(sys.argv) >= 22:
		if len(negativeControlLineageMeans[treatment13]) > 0:
			outFile.write(treatment13 + " mean +/- stdev,")
	if len(sys.argv) >= 23:
		if len(negativeControlLineageMeans[treatment14]) > 0:
			outFile.write(treatment14 + " mean +/- stdev,")
	if len(sys.argv) >= 24:
		if len(negativeControlLineageMeans[treatment15]) > 0:
			outFile.write(treatment15 + " mean +/- stdev,")
	if len(sys.argv) >= 25:
		if len(negativeControlLineageMeans[treatment16]) > 0:
			outFile.write(treatment16 + " mean +/- stdev,")
	if len(sys.argv) >= 26:
		if len(negativeControlLineageMeans[treatment17]) > 0:
			outFile.write(treatment17 + " mean +/- stdev,")
	if len(sys.argv) >= 27:
		if len(negativeControlLineageMeans[treatment18]) > 0:
			outFile.write(treatment18 + " mean +/- stdev,")
	if len(sys.argv) >= 28:
		if len(negativeControlLineageMeans[treatment19]) > 0:
			outFile.write(treatment19 + " mean +/- stdev,")
	if len(sys.argv) >= 29:
		if len(negativeControlLineageMeans[treatment20]) > 0:
			outFile.write(treatment20 + " mean +/- stdev,")	
	outFile.seek(-1, os.SEEK_CUR)		
			
#	if len(sys.argv) >= 6:		###Write column titles of treatments for lineage1 to negativeControlLineage t-tests.
#		if len(lin1Means["WT"]) > 0:
#			if len(negativeControlLineageMeans["WT"]) > 0:
#				outFile.write(lineage1 + " WT to " + negativeControlLineage + " WT\t")
#	if len(sys.argv) >= 7:		
#		if len(lin1Means[treatment1]) > 0:
#			if len(negativeControlLineageMeans[treatment1]) > 0:
#				outFile.write(lineage1 + " " + treatment1 + " to " + negativeControlLineage + " " + treatment1 + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			if len(negativeControlLineageMeans[treatment2]) > 0:
#				outFile.write(lineage1 + " " + treatment2 + " to " + negativeControlLineage + " " + treatment2 + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			if len(negativeControlLineageMeans[treatment3]) > 0:
#				outFile.write(lineage1 + " " + treatment3 + " to " + negativeControlLineage + " " + treatment3 + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			if len(negativeControlLineageMeans[treatment4]) > 0:
#				outFile.write(lineage1 + " " + treatment4 + " to " + negativeControlLineage + " " + treatment4 + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			if len(negativeControlLineageMeans[treatment5]) > 0:
#				outFile.write(lineage1 + " " + treatment5 + " to " + negativeControlLineage + " " + treatment5 + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			if len(negativeControlLineageMeans[treatment6]) > 0:
#				outFile.write(lineage1 + " " + treatment6 + " to " + negativeControlLineage + " " + treatment6 + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			if len(negativeControlLineageMeans[treatment7]) > 0:
#				outFile.write(lineage1 + " " + treatment7 + " to " + negativeControlLineage + " " + treatment7 + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			if len(negativeControlLineageMeans[treatment8]) > 0:
#				outFile.write(lineage1 + " " + treatment8 + " to " + negativeControlLineage  + " " + treatment8 + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			if len(negativeControlLineageMeans[treatment9]) > 0:
#				outFile.write(lineage1 + " " + treatment9 + " to " + negativeControlLineage  + " " + treatment9 + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			if len(negativeControlLineageMeans[treatment10]) > 0:
#				outFile.write(lineage1 + " " + treatment10 + " to " + negativeControlLineage + " " + treatment10 + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			if len(negativeControlLineageMeans[treatment11]) > 0:
#				outFile.write(lineage1 + " " + treatment11 + " to " + negativeControlLineage + " " + treatment11 + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			if len(negativeControlLineageMeans[treatment12]) > 0:
#				outFile.write(lineage1 + " " + treatment12 + " to " + negativeControlLineage + " " + treatment12 + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			if len(negativeControlLineageMeans[treatment13]) > 0:
#				outFile.write(lineage1 + " " + treatment13 + " to " + negativeControlLineage + " " + treatment13 + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			if len(negativeControlLineageMeans[treatment14]) > 0:
#				outFile.write(lineage1 + " " + treatment14 + " to " + negativeControlLineage + " " + treatment14 + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			if len(negativeControlLineageMeans[treatment15]) > 0:
#				outFile.write(lineage1 + " " + treatment15 + " to " + negativeControlLineage + " " + treatment15 + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			if len(negativeControlLineageMeans[treatment16]) > 0:
#				outFile.write(lineage1 + " " + treatment16 + " to " + negativeControlLineage + " " + treatment16 + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			if len(negativeControlLineageMeans[treatment17]) > 0:
#				outFile.write(lineage1 + " " + treatment17 + " to " + negativeControlLineage + " " + treatment17 + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			if len(negativeControlLineageMeans[treatment18]) > 0:
#				outFile.write(lineage1 + " " + treatment18 + " to " + negativeControlLineage + " " + treatment18 + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			if len(negativeControlLineageMeans[treatment19]) > 0:
#				outFile.write(lineage1 + " " + treatment19 + " to " + negativeControlLineage + " " + treatment19 + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			if len(negativeControlLineageMeans[treatment20]) > 0:
#				outFile.write(lineage1 + " " + treatment20 + " to " + negativeControlLineage + " " + treatment20 + "\t")
				
#	if len(sys.argv) >= 6:		###Write column titles of treatments for lineage2 to negativeControlLineage t-tests.
#		if len(lin2Means["WT"]) > 0:
#			if len(negativeControlLineageMeans["WT"]) > 0:
#				outFile.write(lineage2 + " WT to " + negativeControlLineage + " WT\t")
#	if len(sys.argv) >= 7:		
#		if len(lin2Means[treatment1]) > 0:
#			if len(negativeControlLineageMeans[treatment1]) > 0:
#				outFile.write(lineage2 + " " + treatment1 + " to " + negativeControlLineage + " " + treatment1 + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			if len(negativeControlLineageMeans[treatment2]) > 0:
#				outFile.write(lineage2 + " " + treatment2 + " to " + negativeControlLineage + " " + treatment2 + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			if len(negativeControlLineageMeans[treatment3]) > 0:
#				outFile.write(lineage2 + " " + treatment3 + " to " + negativeControlLineage + " " + treatment3 + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			if len(negativeControlLineageMeans[treatment4]) > 0:
#				outFile.write(lineage2 + " " + treatment4 + " to " + negativeControlLineage + " " + treatment4 + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			if len(negativeControlLineageMeans[treatment5]) > 0:
#				outFile.write(lineage2 + " " + treatment5 + " to " + negativeControlLineage + " " + treatment5 + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			if len(negativeControlLineageMeans[treatment6]) > 0:
#				outFile.write(lineage2 + " " + treatment6 + " to " + negativeControlLineage + " " + treatment6 + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			if len(negativeControlLineageMeans[treatment7]) > 0:
#				outFile.write(lineage2 + " " + treatment7 + " to " + negativeControlLineage + " " + treatment7 + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			if len(negativeControlLineageMeans[treatment8]) > 0:
#				outFile.write(lineage2 + " " + treatment8 + " to " + negativeControlLineage + " " + treatment8 + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			if len(negativeControlLineageMeans[treatment9]) > 0:
#				outFile.write(lineage2 + " " + treatment9 + " to " + negativeControlLineage + " " + treatment9 + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			if len(negativeControlLineageMeans[treatment10]) > 0:
#				outFile.write(lineage2 + " " + treatment10 + " to " + negativeControlLineage + " " + treatment10 + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			if len(negativeControlLineageMeans[treatment11]) > 0:
#				outFile.write(lineage2 + " " + treatment11 + " to " + negativeControlLineage + " " + treatment11 + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			if len(negativeControlLineageMeans[treatment12]) > 0:
#				outFile.write(lineage2 + " " + treatment12 + " to " + negativeControlLineage + " " + treatment12 + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			if len(negativeControlLineageMeans[treatment13]) > 0:
#				outFile.write(lineage2 + " " + treatment13 + " to " + negativeControlLineage + " " + treatment13 + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			if len(negativeControlLineageMeans[treatment14]) > 0:
#				outFile.write(lineage2 + " " + treatment14 + " to " + negativeControlLineage + " " + treatment14 + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			if len(negativeControlLineageMeans[treatment15]) > 0:
#				outFile.write(lineage2 + " " + treatment15 + " to " + negativeControlLineage + " " + treatment15 + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			if len(negativeControlLineageMeans[treatment16]) > 0:
#				outFile.write(lineage2 + " " + treatment16 + " to " + negativeControlLineage + " " + treatment16 + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			if len(negativeControlLineageMeans[treatment17]) > 0:
#				outFile.write(lineage2 + " " + treatment17 + " to " + negativeControlLineage + " " + treatment17 + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			if len(negativeControlLineageMeans[treatment18]) > 0:
#				outFile.write(lineage2 + " " + treatment18 + " to " + negativeControlLineage + " " + treatment18 + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			if len(negativeControlLineageMeans[treatment19]) > 0:
#				outFile.write(lineage2 + " " + treatment19 + " to " + negativeControlLineage + " " + treatment19 + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			if len(negativeControlLineageMeans[treatment20]) > 0:
#				outFile.write(lineage2 + " " + treatment20 + " to " + negativeControlLineage + " " + treatment20 + "\t")

	outFile.write("\n," + str(mean(negativeControlLineageMeans["WT"])) + "+/-" + str(numpy.std(negativeControlLineageMeans["WT"], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 10:		###Write negativeControlLineage means.
		if len(negativeControlLineageMeans[treatment1]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment1])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment1], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 11:
		if len(negativeControlLineageMeans[treatment2]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment2])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment2], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 12:
		if len(negativeControlLineageMeans[treatment3]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment3])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment3], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 13:
		if len(negativeControlLineageMeans[treatment4]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment4])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment4], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 14:
		if len(negativeControlLineageMeans[treatment5]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment5])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment5], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 15:
		if len(negativeControlLineageMeans[treatment6]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment6])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment6], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 16:
		if len(negativeControlLineageMeans[treatment7]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment7])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment7], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 17:
		if len(negativeControlLineageMeans[treatment8]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment8])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment8], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 18:
		if len(negativeControlLineageMeans[treatment9]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment9])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment9], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 19:
		if len(negativeControlLineageMeans[treatment10]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment10])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment10], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 20:
		if len(negativeControlLineageMeans[treatment11]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment11])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment11], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 21:
		if len(negativeControlLineageMeans[treatment12]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment12])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment12], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 22:
		if len(negativeControlLineageMeans[treatment13]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment13])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment13], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 23:
		if len(negativeControlLineageMeans[treatment14]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment14])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment14], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 24:
		if len(negativeControlLineageMeans[treatment15]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment15])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment15], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 25:
		if len(negativeControlLineageMeans[treatment16]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment16])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment16], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 26:
		if len(negativeControlLineageMeans[treatment17]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment17])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment17], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 27:
		if len(negativeControlLineageMeans[treatment18]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment18])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment18], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 28:
		if len(negativeControlLineageMeans[treatment19]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment19])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment19], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 29:
		if len(negativeControlLineageMeans[treatment20]) > 0:
			outFile.write(str(mean(negativeControlLineageMeans[treatment20])) + "+/-" + str(numpy.std(negativeControlLineageMeans[treatment20], axis=0, ddof = 1)) + ",")	
	outFile.seek(-1, os.SEEK_CUR)		

#	if len(sys.argv) >= 6:		
#		if len(lin1Means["WT"]) > 0:
#			if len(negativeControlLineageMeans["WT"]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans["WT"], lin1Means["WT"])) + "\t")
#	if len(sys.argv) >= 7:		###Write lineage1 to negativeControlLineage t-test.
#		if len(lin1Means[treatment1]) > 0:
#			if len(negativeControlLineageMeans[treatment1]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment1], lin1Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			if len(negativeControlLineageMeans[treatment2]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment2], lin1Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			if len(negativeControlLineageMeans[treatment3]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment3], lin1Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			if len(negativeControlLineageMeans[treatment4]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment4], lin1Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			if len(negativeControlLineageMeans[treatment5]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment5], lin1Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			if len(negativeControlLineageMeans[treatment6]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment6], lin1Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			if len(negativeControlLineageMeans[treatment7]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment7], lin1Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			if len(negativeControlLineageMeans[treatment8]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment8], lin1Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			if len(negativeControlLineageMeans[treatment9]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment9], lin1Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			if len(negativeControlLineageMeans[treatment10]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment10], lin1Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			if len(negativeControlLineageMeans[treatment11]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment11], lin1Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			if len(negativeControlLineageMeans[treatment12]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment12], lin1Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			if len(negativeControlLineageMeans[treatment13]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment13], lin1Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			if len(negativeControlLineageMeans[treatment14]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment14], lin1Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			if len(negativeControlLineageMeans[treatment15]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment15], lin1Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			if len(negativeControlLineageMeans[treatment16]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment16], lin1Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			if len(negativeControlLineageMeans[treatment17]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment17], lin1Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			if len(negativeControlLineageMeans[treatment18]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment18], lin1Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			if len(negativeControlLineageMeans[treatment19]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment19], lin1Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			if len(negativeControlLineageMeans[treatment20]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment20], lin1Means[treatment20])) + "\t")
				
#	if len(sys.argv) >= 6:		
#		if len(lin2Means["WT"]) > 0:
#			if len(negativeControlLineageMeans["WT"]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans["WT"], lin2Means["WT"])) + "\t")
#	if len(sys.argv) >= 7:		###Write lineage2 to negativeControlLineage t-test.
#		if len(lin2Means[treatment1]) > 0:
#			if len(negativeControlLineageMeans[treatment1]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment1], lin2Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			if len(negativeControlLineageMeans[treatment2]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment2], lin2Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			if len(negativeControlLineageMeans[treatment3]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment3], lin2Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			if len(negativeControlLineageMeans[treatment4]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment4], lin2Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			if len(negativeControlLineageMeans[treatment5]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment5], lin2Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			if len(negativeControlLineageMeans[treatment6]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment6], lin2Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			if len(negativeControlLineageMeans[treatment7]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment7], lin2Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			if len(negativeControlLineageMeans[treatment8]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment8], lin2Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			if len(negativeControlLineageMeans[treatment9]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment9], lin2Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			if len(negativeControlLineageMeans[treatment10]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment10], lin2Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			if len(negativeControlLineageMeans[treatment11]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment11], lin2Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			if len(negativeControlLineageMeans[treatment12]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment12], lin2Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			if len(negativeControlLineageMeans[treatment13]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment13], lin2Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			if len(negativeControlLineageMeans[treatment14]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment14], lin2Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			if len(negativeControlLineageMeans[treatment15]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment15], lin2Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			if len(negativeControlLineageMeans[treatment16]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment16], lin2Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			if len(negativeControlLineageMeans[treatment17]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment17], lin2Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			if len(negativeControlLineageMeans[treatment18]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment18], lin2Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			if len(negativeControlLineageMeans[treatment19]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment19], lin2Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			if len(negativeControlLineageMeans[treatment20]) > 0:
#				outFile.write(str(stats.ttest_ind(negativeControlLineageMeans[treatment20], lin2Means[treatment20])) + "\t")

if positiveControlLineage != "none":			
	outFile.write("\n" + positiveControlLineage + " t-test,WT mean +/- stdev,")
	if len(sys.argv) >= 10:		###Write column titles of treatments for positiveControlLineage treatment means and standard deviations.
		if len(positiveControlLineageMeans[treatment1]) > 0:
			outFile.write(treatment1 + " mean +/- stdev,")
	if len(sys.argv) >= 11:
		if len(positiveControlLineageMeans[treatment2]) > 0:
			outFile.write(treatment2 + " mean +/- stdev,")
	if len(sys.argv) >= 12:
		if len(positiveControlLineageMeans[treatment3]) > 0:
			outFile.write(treatment3 + " mean +/- stdev,")
	if len(sys.argv) >= 13:
		if len(positiveControlLineageMeans[treatment4]) > 0:
			outFile.write(treatment4 + " mean +/- stdev,")
	if len(sys.argv) >= 14:
		if len(positiveControlLineageMeans[treatment5]) > 0:
			outFile.write(treatment5 + " mean +/- stdev,")
	if len(sys.argv) >= 15:
		if len(positiveControlLineageMeans[treatment6]) > 0:
			outFile.write(treatment6 + " mean +/- stdev,")
	if len(sys.argv) >= 16:
		if len(positiveControlLineageMeans[treatment7]) > 0:
			outFile.write(treatment7 + " mean +/- stdev,")
	if len(sys.argv) >= 17:
		if len(positiveControlLineageMeans[treatment8]) > 0:
			outFile.write(treatment8 + " mean +/- stdev,")
	if len(sys.argv) >= 18:
		if len(positiveControlLineageMeans[treatment9]) > 0:
			outFile.write(treatment9 + " mean +/- stdev,")
	if len(sys.argv) >= 19:
		if len(positiveControlLineageMeans[treatment10]) > 0:
			outFile.write(treatment10 + " mean +/- stdev,")
	if len(sys.argv) >= 20:
		if len(positiveControlLineageMeans[treatment11]) > 0:
			outFile.write(treatment11 + " mean +/- stdev,")
	if len(sys.argv) >= 21:
		if len(positiveControlLineageMeans[treatment12]) > 0:
			outFile.write(treatment12 + " mean +/- stdev,")
	if len(sys.argv) >= 22:
		if len(positiveControlLineageMeans[treatment13]) > 0:
			outFile.write(treatment13 + " mean +/- stdev,")
	if len(sys.argv) >= 23:
		if len(positiveControlLineageMeans[treatment14]) > 0:
			outFile.write(treatment14 + " mean +/- stdev,")
	if len(sys.argv) >= 24:
		if len(positiveControlLineageMeans[treatment15]) > 0:
			outFile.write(treatment15 + " mean +/- stdev,")
	if len(sys.argv) >= 25:
		if len(positiveControlLineageMeans[treatment16]) > 0:
			outFile.write(treatment16 + " mean +/- stdev,")
	if len(sys.argv) >= 26:
		if len(positiveControlLineageMeans[treatment17]) > 0:
			outFile.write(treatment17 + " mean +/- stdev,")
	if len(sys.argv) >= 27:
		if len(positiveControlLineageMeans[treatment18]) > 0:
			outFile.write(treatment18 + " mean +/- stdev,")
	if len(sys.argv) >= 28:
		if len(positiveControlLineageMeans[treatment19]) > 0:
			outFile.write(treatment19 + " mean +/- stdev,")
	if len(sys.argv) >= 29:
		if len(positiveControlLineageMeans[treatment20]) > 0:
			outFile.write(treatment20 + " mean +/- stdev,")	
	outFile.seek(-1, os.SEEK_CUR)		
			
#	if len(sys.argv) >= 6:		###Write column titles of treatments for lineage1 to positiveControlLineage WT t-tests.
#		if len(lin1Means["WT"]) > 0:
#			if len(positiveControlLineageMeans["WT"]) > 0:
#				outFile.write(lineage1 + " WT to " + positiveControlLineage + " WT\t")
#	if len(sys.argv) >= 7:		
#		if len(lin1Means[treatment1]) > 0:
#			if len(positiveControlLineageMeans[treatment1]) > 0:
#				outFile.write(lineage1 + " " + treatment1 + " to " + positiveControlLineage + " " + treatment1 + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			if len(positiveControlLineageMeans[treatment2]) > 0:
#				outFile.write(lineage1 + " " + treatment2 + " to " + positiveControlLineage + " " + treatment2 + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			if len(positiveControlLineageMeans[treatment3]) > 0:
#				outFile.write(lineage1 + " " + treatment3 + " to " + positiveControlLineage + " " + treatment3 + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			if len(positiveControlLineageMeans[treatment4]) > 0:
#				outFile.write(lineage1 + " " + treatment4 + " to " + positiveControlLineage + " " + treatment4 + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			if len(positiveControlLineageMeans[treatment5]) > 0:
#				outFile.write(lineage1 + " " + treatment5 + " to " + positiveControlLineage + " " + treatment5 + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			if len(positiveControlLineageMeans[treatment6]) > 0:
#				outFile.write(lineage1 + " " + treatment6 + " to " + positiveControlLineage + " " + treatment6 + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			if len(positiveControlLineageMeans[treatment7]) > 0:
#				outFile.write(lineage1 + " " + treatment7 + " to " + positiveControlLineage + " " + treatment7 + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			if len(positiveControlLineageMeans[treatment8]) > 0:
#				outFile.write(lineage1 + " " + treatment8 + " to " + positiveControlLineage + " " + treatment8 + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			if len(positiveControlLineageMeans[treatment9]) > 0:
#				outFile.write(lineage1 + " " + treatment9 + " to " + positiveControlLineage + " " + treatment9 + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			if len(positiveControlLineageMeans[treatment10]) > 0:
#				outFile.write(lineage1 + " " + treatment10 + " to " + positiveControlLineage + " " + treatment10 + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			if len(positiveControlLineageMeans[treatment11]) > 0:
#				outFile.write(lineage1 + " " + treatment11 + " to " + positiveControlLineage + " " + treatment11 + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			if len(positiveControlLineageMeans[treatment12]) > 0:
#				outFile.write(lineage1 + " " + treatment12 + " to " + positiveControlLineage + " " + treatment12 + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			if len(positiveControlLineageMeans[treatment13]) > 0:
#				outFile.write(lineage1 + " " + treatment13 + " to " + positiveControlLineage + " " + treatment13 + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			if len(positiveControlLineageMeans[treatment14]) > 0:
#				outFile.write(lineage1 + " " + treatment14 + " to " + positiveControlLineage + " " + treatment14 + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			if len(positiveControlLineageMeans[treatment15]) > 0:
#				outFile.write(lineage1 + " " + treatment15 + " to " + positiveControlLineage + " " + treatment15 + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			if len(positiveControlLineageMeans[treatment16]) > 0:
#				outFile.write(lineage1 + " " + treatment16 + " to " + positiveControlLineage + " " + treatment16 + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			if len(positiveControlLineageMeans[treatment17]) > 0:
#				outFile.write(lineage1 + " " + treatment17 + " to " + positiveControlLineage + " " + treatment17 + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			if len(positiveControlLineageMeans[treatment18]) > 0:
#				outFile.write(lineage1 + " " + treatment18 + " to " + positiveControlLineage + " " + treatment18 + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			if len(positiveControlLineageMeans[treatment19]) > 0:
#				outFile.write(lineage1 + " " + treatment19 + " to " + positiveControlLineage + " " + treatment19 + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			if len(positiveControlLineageMeans[treatment20]) > 0:
#				outFile.write(lineage1 + " " + treatment20 + " to " + positiveControlLineage + " " + treatment20 + "\t")
				
#	if len(sys.argv) >= 6:		###Write column titles of treatments for lineage2 to positiveControlLineage WT t-tests.
#		if len(lin2Means["WT"]) > 0:
#			if len(positiveControlLineageMeans["WT"]) > 0:
#				outFile.write(lineage2 + " WT to " + positiveControlLineage + " WT\t")
#	if len(sys.argv) >= 7:		
#		if len(lin2Means[treatment1]) > 0:
#			if len(positiveControlLineageMeans[treatment1]) > 0:
#				outFile.write(lineage2 + " " + treatment1 + " to " + positiveControlLineage + " " + treatment1 + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			if len(positiveControlLineageMeans[treatment2]) > 0:
#				outFile.write(lineage2 + " " + treatment2 + " to " + positiveControlLineage + " " + treatment2 + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			if len(positiveControlLineageMeans[treatment3]) > 0:
#				outFile.write(lineage2 + " " + treatment3 + " to " + positiveControlLineage + " " + treatment3 + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			if len(positiveControlLineageMeans[treatment4]) > 0:
#				outFile.write(lineage2 + " " + treatment4 + " to " + positiveControlLineage + " " + treatment4 + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			if len(positiveControlLineageMeans[treatment5]) > 0:
#				outFile.write(lineage2 + " " + treatment5 + " to " + positiveControlLineage + " " + treatment5 + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			if len(positiveControlLineageMeans[treatment6]) > 0:
#				outFile.write(lineage2 + " " + treatment6 + " to " + positiveControlLineage + " " + treatment6 + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			if len(positiveControlLineageMeans[treatment7]) > 0:
#				outFile.write(lineage2 + " " + treatment7 + " to " + positiveControlLineage + " " + treatment7 + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			if len(positiveControlLineageMeans[treatment8]) > 0:
#				outFile.write(lineage2 + " " + treatment8 + " to " + positiveControlLineage + " " + treatment8 + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			if len(positiveControlLineageMeans[treatment9]) > 0:
#				outFile.write(lineage2 + " " + treatment9 + " to " + positiveControlLineage + " " + treatment9 + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			if len(positiveControlLineageMeans[treatment10]) > 0:
#				outFile.write(lineage2 + " " + treatment10 + " to " + positiveControlLineage + " " + treatment10 + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			if len(positiveControlLineageMeans[treatment11]) > 0:
#				outFile.write(lineage2 + " " + treatment11 + " to " + positiveControlLineage + " " + treatment11 + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			if len(positiveControlLineageMeans[treatment12]) > 0:
#				outFile.write(lineage2 + " " + treatment12 + " to " + positiveControlLineage + " " + treatment12 + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			if len(positiveControlLineageMeans[treatment13]) > 0:
#				outFile.write(lineage2 + " " + treatment13 + " to " + positiveControlLineage + " " + treatment13 + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			if len(positiveControlLineageMeans[treatment14]) > 0:
#				outFile.write(lineage2 + " " + treatment14 + " to " + positiveControlLineage + " " + treatment14 + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			if len(positiveControlLineageMeans[treatment15]) > 0:
#				outFile.write(lineage2 + " " + treatment15 + " to " + positiveControlLineage + " " + treatment15 + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			if len(positiveControlLineageMeans[treatment16]) > 0:
#				outFile.write(lineage2 + " " + treatment16 + " to " + positiveControlLineage + " " + treatment16 + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			if len(positiveControlLineageMeans[treatment17]) > 0:
#				outFile.write(lineage2 + " " + treatment17 + " to " + positiveControlLineage + " " + treatment17 + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			if len(positiveControlLineageMeans[treatment18]) > 0:
#				outFile.write(lineage2 + " " + treatment18 + " to " + positiveControlLineage + " " + treatment18 + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			if len(positiveControlLineageMeans[treatment19]) > 0:
#				outFile.write(lineage2 + " " + treatment19 + " to " + positiveControlLineage + " " + treatment19 + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			if len(positiveControlLineageMeans[treatment20]) > 0:
#				outFile.write(lineage2 + " " + treatment20 + " to " + positiveControlLineage + " " + treatment20 + "\t")

	outFile.write("\n," + str(mean(positiveControlLineageMeans["WT"])) + "+/-" + str(numpy.std(positiveControlLineageMeans["WT"], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 10:		###Write positiveControlLineage means.
		if len(positiveControlLineageMeans[treatment1]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment1])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment1], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 11:
		if len(positiveControlLineageMeans[treatment2]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment2])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment2], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 12:
		if len(positiveControlLineageMeans[treatment3]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment3])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment3], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 13:
		if len(positiveControlLineageMeans[treatment4]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment4])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment4], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 14:
		if len(positiveControlLineageMeans[treatment5]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment5])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment5], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 15:
		if len(positiveControlLineageMeans[treatment6]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment6])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment6], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 16:
		if len(positiveControlLineageMeans[treatment7]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment7])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment7], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 17:
		if len(positiveControlLineageMeans[treatment8]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment8])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment8], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 18:
		if len(positiveControlLineageMeans[treatment9]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment9])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment9], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 19:
		if len(positiveControlLineageMeans[treatment10]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment10])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment10], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 20:
		if len(positiveControlLineageMeans[treatment11]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment11])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment11], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 21:
		if len(positiveControlLineageMeans[treatment12]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment12])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment12], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 22:
		if len(positiveControlLineageMeans[treatment13]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment13])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment13], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 23:
		if len(positiveControlLineageMeans[treatment14]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment14])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment14], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 24:
		if len(positiveControlLineageMeans[treatment15]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment15])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment15], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 25:
		if len(positiveControlLineageMeans[treatment16]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment16])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment16], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 26:
		if len(positiveControlLineageMeans[treatment17]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment17])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment17], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 27:
		if len(positiveControlLineageMeans[treatment18]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment18])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment18], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 28:
		if len(positiveControlLineageMeans[treatment19]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment19])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment19], axis=0, ddof = 1)) + ",")
	if len(sys.argv) >= 29:
		if len(positiveControlLineageMeans[treatment20]) > 0:
			outFile.write(str(mean(positiveControlLineageMeans[treatment20])) + "+/-" + str(numpy.std(positiveControlLineageMeans[treatment20], axis=0, ddof = 1)) + ",")	
	outFile.seek(-1, os.SEEK_CUR)		

#	if len(sys.argv) >= 6:		
#		if len(lin1Means["WT"]) > 0:
#			if len(positiveControlLineageMeans["WT"]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans["WT"], lin1Means["WT"])) + "\t")
#	if len(sys.argv) >= 7:		###Write lineage1 to positiveControlLineage WT t-test.
#		if len(lin1Means[treatment1]) > 0:
#			if len(positiveControlLineageMeans[treatment1]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment1], lin1Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin1Means[treatment2]) > 0:
#			if len(positiveControlLineageMeans[treatment2]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment2], lin1Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin1Means[treatment3]) > 0:
#			if len(positiveControlLineageMeans[treatment3]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment3], lin1Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin1Means[treatment4]) > 0:
#			if len(positiveControlLineageMeans[treatment4]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment4], lin1Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin1Means[treatment5]) > 0:
#			if len(positiveControlLineageMeans[treatment5]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment5], lin1Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin1Means[treatment6]) > 0:
#			if len(positiveControlLineageMeans[treatment6]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment6], lin1Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin1Means[treatment7]) > 0:
#			if len(positiveControlLineageMeans[treatment7]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment7], lin1Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin1Means[treatment8]) > 0:
#			if len(positiveControlLineageMeans[treatment8]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment8], lin1Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin1Means[treatment9]) > 0:
#			if len(positiveControlLineageMeans[treatment9]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment9], lin1Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin1Means[treatment10]) > 0:
#			if len(positiveControlLineageMeans[treatment10]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment10], lin1Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin1Means[treatment11]) > 0:
#			if len(positiveControlLineageMeans[treatment11]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment11], lin1Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin1Means[treatment12]) > 0:
#			if len(positiveControlLineageMeans[treatment12]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment12], lin1Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin1Means[treatment13]) > 0:
#			if len(positiveControlLineageMeans[treatment13]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment13], lin1Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin1Means[treatment14]) > 0:
#			if len(positiveControlLineageMeans[treatment14]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment14], lin1Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin1Means[treatment15]) > 0:
#			if len(positiveControlLineageMeans[treatment15]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment15], lin1Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin1Means[treatment16]) > 0:
#			if len(positiveControlLineageMeans[treatment16]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment16], lin1Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin1Means[treatment17]) > 0:
#			if len(positiveControlLineageMeans[treatment17]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment17], lin1Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin1Means[treatment18]) > 0:
#			if len(positiveControlLineageMeans[treatment18]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment18], lin1Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin1Means[treatment19]) > 0:
#			if len(positiveControlLineageMeans[treatment19]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment19], lin1Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin1Means[treatment20]) > 0:
#			if len(positiveControlLineageMeans[treatment20]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment20], lin1Means[treatment20])) + "\t")
				
#	if len(sys.argv) >= 6:		
#		if len(lin2Means["WT"]) > 0:
#			if len(positiveControlLineageMeans["WT"]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans["WT"], lin2Means["WT"])) + "\t")
#	if len(sys.argv) >= 7:		###Write lineage2 to positiveControlLineage WT t-test.
#		if len(lin2Means[treatment1]) > 0:
#			if len(positiveControlLineageMeans[treatment1]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment1], lin2Means[treatment1])) + "\t")
#	if len(sys.argv) >= 8:
#		if len(lin2Means[treatment2]) > 0:
#			if len(positiveControlLineageMeans[treatment2]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment2], lin2Means[treatment2])) + "\t")
#	if len(sys.argv) >= 9:
#		if len(lin2Means[treatment3]) > 0:
#			if len(positiveControlLineageMeans[treatment3]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment3], lin2Means[treatment3])) + "\t")
#	if len(sys.argv) >= 10:
#		if len(lin2Means[treatment4]) > 0:
#			if len(positiveControlLineageMeans[treatment4]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment4], lin2Means[treatment4])) + "\t")
#	if len(sys.argv) >= 11:
#		if len(lin2Means[treatment5]) > 0:
#			if len(positiveControlLineageMeans[treatment5]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment5], lin2Means[treatment5])) + "\t")
#	if len(sys.argv) >= 12:
#		if len(lin2Means[treatment6]) > 0:
#			if len(positiveControlLineageMeans[treatment6]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment6], lin2Means[treatment6])) + "\t")
#	if len(sys.argv) >= 13:
#		if len(lin2Means[treatment7]) > 0:
#			if len(positiveControlLineageMeans[treatment7]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment7], lin2Means[treatment7])) + "\t")
#	if len(sys.argv) >= 14:
#		if len(lin2Means[treatment8]) > 0:
#			if len(positiveControlLineageMeans[treatment8]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment8], lin2Means[treatment8])) + "\t")
#	if len(sys.argv) >= 15:
#		if len(lin2Means[treatment9]) > 0:
#			if len(positiveControlLineageMeans[treatment9]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment9], lin2Means[treatment9])) + "\t")
#	if len(sys.argv) >= 16:
#		if len(lin2Means[treatment10]) > 0:
#			if len(positiveControlLineageMeans[treatment10]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment10], lin2Means[treatment10])) + "\t")
#	if len(sys.argv) >= 17:
#		if len(lin2Means[treatment11]) > 0:
#			if len(positiveControlLineageMeans[treatment11]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment11], lin2Means[treatment11])) + "\t")
#	if len(sys.argv) >= 18:
#		if len(lin2Means[treatment12]) > 0:
#			if len(positiveControlLineageMeans[treatment12]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment12], lin2Means[treatment12])) + "\t")
#	if len(sys.argv) >= 19:
#		if len(lin2Means[treatment13]) > 0:
#			if len(positiveControlLineageMeans[treatment13]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment13], lin2Means[treatment13])) + "\t")
#	if len(sys.argv) >= 20:
#		if len(lin2Means[treatment14]) > 0:
#			if len(positiveControlLineageMeans[treatment14]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment14], lin2Means[treatment14])) + "\t")
#	if len(sys.argv) >= 21:
#		if len(lin2Means[treatment15]) > 0:
#			if len(positiveControlLineageMeans[treatment15]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment15], lin2Means[treatment15])) + "\t")
#	if len(sys.argv) >= 22:
#		if len(lin2Means[treatment16]) > 0:
#			if len(positiveControlLineageMeans[treatment16]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment16], lin2Means[treatment16])) + "\t")
#	if len(sys.argv) >= 23:
#		if len(lin2Means[treatment17]) > 0:
#			if len(positiveControlLineageMeans[treatment17]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment17], lin2Means[treatment17])) + "\t")
#	if len(sys.argv) >= 24:
#		if len(lin2Means[treatment18]) > 0:
#			if len(positiveControlLineageMeans[treatment18]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment18], lin2Means[treatment18])) + "\t")
#	if len(sys.argv) >= 25:
#		if len(lin2Means[treatment19]) > 0:
#			if len(positiveControlLineageMeans[treatment19]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment19], lin2Means[treatment19])) + "\t")
#	if len(sys.argv) >= 26:
#		if len(lin2Means[treatment20]) > 0:
#			if len(positiveControlLineageMeans[treatment20]) > 0:
#				outFile.write(str(stats.ttest_ind(positiveControlLineageMeans[treatment20], lin2Means[treatment20])) + "\t")


outFile.write("\n")
#outFile.write("\n" + lineage1 + " t-test 2015 to 2016\tWT 2015 mean +/- stdev\tWT 2016 mean +/- stdev\tWT t-test\tpop-1i 2015 mean +/- stdev\tpop-1i 2016 mean +/- stdev\tpop-1i t-test\tsys-1i 2015 mean +/- stdev\tsys-1i 2016 mean +/- stdev\tsys-1i t-test\n\t" + str(mean(lin1MeansYear["2015"]["WT"])) + "+/-" + str(numpy.std(lin1MeansYear["2015"]["WT"], axis=0)) + "\t" + str(mean(lin1MeansYear["2016"]["WT"])) + "+/-" + str(numpy.std(lin1MeansYear["2016"]["WT"], axis=0)) + "\t" + str(stats.ttest_ind(lin1MeansYear["2015"]["WT"], lin1MeansYear["2016"]["WT"])) + "\t" + str(mean(lin1MeansYear["2015"]["pop-1i"])) + "+/-" + str(numpy.std(lin1MeansYear["2015"]["pop-1i"], axis=0)) + "\t" + str(mean(lin1MeansYear["2016"]["pop-1i"])) + "+/-" + str(numpy.std(lin1MeansYear["2016"]["pop-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin1MeansYear["2015"]["pop-1i"], lin1MeansYear["2016"]["pop-1i"])) + "\t" + str(mean(lin1MeansYear["2015"]["sys-1i"])) + "+/-" + str(numpy.std(lin1MeansYear["2015"]["sys-1i"], axis=0)) + "\t" + str(mean(lin1MeansYear["2016"]["sys-1i"])) + "+/-" + str(numpy.std(lin1MeansYear["2016"]["sys-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin1MeansYear["2015"]["sys-1i"], lin1MeansYear["2016"]["sys-1i"])) + "\n")
#outFile.write(lineage2 + " t-test 2015 to 2016\tWT 2015 mean +/- stdev\tWT 2016 mean +/- stdev\tWT t-test\tpop-1i 2015 mean +/- stdev\tpop-1i 2016 mean +/- stdev\tpop-1i t-test\tsys-1i 2015 mean +/- stdev\tsys-1i 2016 mean +/- stdev\tsys-1i t-test\n\t" + str(mean(lin2MeansYear["2015"]["WT"])) + "+/-" + str(numpy.std(lin2MeansYear["2015"]["WT"], axis=0)) + "\t" + str(mean(lin2MeansYear["2016"]["WT"])) + "+/-" + str(numpy.std(lin2MeansYear["2016"]["WT"], axis=0)) + "\t" + str(stats.ttest_ind(lin2MeansYear["2015"]["WT"], lin2MeansYear["2016"]["WT"])) + "\t" + str(mean(lin2MeansYear["2015"]["pop-1i"])) + "+/-" + str(numpy.std(lin2MeansYear["2015"]["pop-1i"], axis=0)) + "\t" + str(mean(lin2MeansYear["2016"]["pop-1i"])) + "+/-" + str(numpy.std(lin2MeansYear["2016"]["pop-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin2MeansYear["2015"]["pop-1i"], lin2MeansYear["2016"]["pop-1i"])) + "\t" + str(mean(lin2MeansYear["2015"]["sys-1i"])) + "+/-" + str(numpy.std(lin2MeansYear["2015"]["sys-1i"], axis=0)) + "\t" + str(mean(lin2MeansYear["2016"]["sys-1i"])) + "+/-" + str(numpy.std(lin2MeansYear["2016"]["sys-1i"], axis=0)) + "\t" + str(stats.ttest_ind(lin2MeansYear["2015"]["sys-1i"], lin2MeansYear["2016"]["sys-1i"])) + "\n")		
#outFile.write("\n" + lineage1 + " t-test 2015\t
#for (embryo, cellss) in embryos.items():
#	tTest1 = []
#	print embryo
#	outFile.write(embryo + " t-test\t")
#	for (cel, blot) in cellss.items():
#		if lineage1 in cel:
#			tTest1.append(float(blot))
#			for (embryo, cellss) in embryos.items():
#				print embryo
#				tTest2 = []
#				for (cel, blot) in cellss.items():
#					if lineage1 in cel:
#						tTest2.append(float(blot))
#				outFile.write(str(stats.ttest_ind(tTest1, tTest2)) + "\t")
#				print stats.ttest_ind(tTest1, tTest2)
#	outFile.write("\n")
#outFile.write("\n")
#lineage2	
outFile.close()
#print embryos