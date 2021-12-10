# Scripts for Dec 2021 Submission

Scripts for Dec 2021 Submission scripts are used to organize the expression values and calculate the mean expression values of expression reporters in anterior and posterior sister lineages in the C. elegans embryo, to calculate correlation of individual embryos' expression data to the average of a control group, and to make box plots of anteriority scores and correlations.

##Installation

Use scp command to download Scripts for Dec 2021 Submission.

```bash
scp -r <username>@gen-murra-004.med.upenn.edu:/gpfs/fs0/l/murr/tools3/scripts_for_Dec_2021_submission <target_directory>
```

##Usage

Run all scripts from directory in which CA data files are located.

image_data_analyzer13.py

	Takes expression data for indicated cell lineages from CA files from directory in which script is run, organizes them into columns by embryo and rows by cell name, and calculates mean expression values for each indicated lineage within each embryo. 

```python <directory_path>/scripts_for_Dec_2021_submission/image_data_analyzer13.py <gene_or_feature_name> <lineage_1> <lineage_2> <negative_control_lineage> <positive_control_lineage> <excluded_generations> <excluded_cell> <minimum_expression_level_cutoff> <treatment_1> ... <treatment_20>
```

	Output is a .csv file with embryos organized by column and cell names organized by row. Individual embryo expression means appear at bottom of spreadsheet. Data from all of CA files in the directory not included in a treatment group are included in a separate group. Treatment groups must include at least 2 CA files.
	

	Arguments

	gene_or_feature_name: Name of gene or genetic feature for which analyzing expression data. Included in output file name as <gene_or_feature_name>_image_analysis.csv.
	lineage_1: First lineage to be analyzed. (eg. ABalaa)
	lineage_2: Second lineage to be analyzed. (eg. ABalap)
	negative_control_lineage: Lineage with no expression (eg. C). The mean expression value from this lineage is subtracted from that of lineage_1 and lineage_2. If no negative control lineage is desired, "none" should be entered as argument.
	positive_control_lineage: THIS ARGUMENT CURRENTLY HAS NO FUNCTIONALITY. Enter "none" as argument.
	excluded_generations: Number of cell generations at top of lineage to exclude from analysis (eg. 2). This permits the exclusion of early cells within a lineage that do not express the fluorescent reporter.
	excluded_cell: Allows the exclusion of a cell from the analysis, the name of which fully includes the name of one of the parent cells of lineage_1 or lineage_2 (eg. EMS). Mainly used to exclude EMS from comparisons that include E or MS.
	minimum_expression_level_cutoff: Minimum expression level value to be used for analysis. (eg. 200) Expression values greater than or equal to the cutoff have the cutoff subtracted from its value. Expression values less than the cutoff are set equal to 0. If no minimum expression level cutoff is desired, "none" should be entered as the argument.
	treatment_1 ... treatment_20: OPTIONAL. Treatments or experimental groups being compared (eg. pop-1i). Should match a unique portion of the data file names for this treatment group. Can include 0 to 20 treatments. Each treatment group must include at least 2 CA files. If all treatment groups have unique identifiers in their file names, it is not necessary include the control group in the treatment list.
	

correlation_analysis.R

	Calculates the pairwise correlation of a set of expression data to a control expression data.

```Rscript <directory_path>/scripts_for_Dec_2021_submission/correlation_analysis.R <input_.csv_file> <type_of_correlation_analysis> <control_expression_column_name>
```

	Output is a .csv file with the pairwise correlation of each embryo's expression data to a control expression data.

	Arguments

	input_.csv_file: .csv file with the expression data of the set of embryos to be analyzed in the format of the output of image_data_analyzer13.py with the single embryo means and group means and standard deviations removed from the bottom of the file. Added to the file is a column with control expression data, which is the within-cell mean of the expression data of the control group (eg. ref-2_promoter).
	type_of_correlation_analysis: Type of correlation analysis that is desired for the comparison (eg. Spearman).
	control_expression_column_name: Name of column containing the control expression data (eg. ref.2_promoter_mean). Write any dashes (-) in column name in input file as dots (.).

	
box_plot_maker_set_y-axis_limits.R

	Plots anteriority scores or correlations in box plots by experimental group.
	
```Rscript <directory_path>/scripts_for_Dec_2021_submission/box_plot_maker_set_y-axis_limits.R <input_.csv_file> <plot_title> <x-axis_label> <y-axis_label> <y-axis_minimum_limit> <y-axis_maximum_limit> <group_1> ... <group_∞>
```

	Output is a box plot of anteriority scores or correlations organized by treatment group.
	
	Arguments
	
	input_.csv_file: .csv file with the anteriority scores or correlations to be plotted.
	plot_title: Title of box plot.
	x-axis_label: Label of x-axis (eg. Experimental_Group).
	y-axis_label: Label of y-axis (eg. Anteriority_Score).
	y-axis_minimum_limit: Minimum value on y-axis.
	y-axis_maximum_limit: Maximum value on y-axis.
	group_1 ... group_∞: Experimental groups for which anteriority scores or correlations are to be plotted.
	
# Support

jrumley@pennmedicine.upenn.edu
jmurr@pennmedicine.upenn.edu

#Authors and acknowledgment

Jonathan D. Rumley, John Isaac Murray

Thanks to BGS Bioinformatics course instructed by Dr. Benjamin Voight, Python bootcamp 2016, EdX R course, and online programming resources. Thanks to Dr. Stephen Philips and others for helpful discussions.