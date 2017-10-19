import ccal
import pandas as pd
import numpy as np
from ccal.modalities import differential_gene_expression
from ccal.information.information import compute_information_coefficient
import cuzcatlan as cusca

data_df = pd.read_table("data/BRCA_minimal.gct", header=2, index_col=0)
data_df.drop('Description', axis=1, inplace=True)
temp = open("data/BRCA_minimal.cls")
temp.readline()
temp.readline()
classes = [int(i) for i in temp.readline().strip('\n').split(' ')]
classes = pd.Series(classes)

differential_gene_expression(phenotypes=classes, gene_expression=data_df, output_filename='DE_test',ranking_method=cusca.custom_pearson_corr)