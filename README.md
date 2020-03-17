# COVID-19-Genome-Sequencing-and-Predictions-with-Artificial-Intelligence
# Notice 3/27/2020: This repository is Under Construction

Genome sequencing with deep learning and other artificial intelligence methods.

This code has been successfully implemented with Spyder(Python 3.7) in Windows 10 OS.

The primary goal of this code is to predict the evolution of COVID-19, to aid in treatments and vaccines.

## Instructions

1. Run `Imports_AI_Genome.py` and `Encoding-Genome-Functions.py` for imports and functions. 

2. COVID-19 genome sequences can be downloaded from [Kaggle](https://www.kaggle.com/jamzing/sars-coronavirus-accession/tasks?taskId=458).

3. Parse and convert to string the genome data in `.fasta` files. In this case:
```
# Parse and print genomes and convert to strings
# Human COVID-19
for seq_record in SeqIO.parse('./sars_coronavirus_accession_Kaggle/SARS_CORONAVIRUS_NC_045512_sequence.fasta',"fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    
# Convert sequence to string 
cv19=str(seq_record.seq)

# Bat COVID-19
for seq_record in SeqIO.parse('./sars_coronavirus_accession_Kaggle/BAT_SARS_LIKE_coronavirus_complete_genome_sequence.fasta',"fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    
# Convert sequence to string 
bat19=str(seq_record.seq)
```
### Two ways to encode genome sequences

1. One-hot encode genome string. Non "acgt" bases (n) are 0000.
```
# returns a L x 4 numpy array
one_hot_encoder(string_to_array(cv19))

# Output:
array([[1, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       ...,
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]], dtype=int32)
```

2. Convert sequence (string) to overlapping k-mer words:
```
words=getKmers(cv19,size=6)
sentence = ' '.join(words)

# Print k-mer words:
sentence

# Output
'attaaa ttaaag taaagg aaaggt aaggtt aggttt ggttta gtttat tttata ttatac tatacc atacct 
tacctt accttc ccttcc cttccc ttccca tcccag cccagg ccaggt caggta aggtaa ggtaac gtaaca 
taacaa aacaaa acaaac caaacc aaacca aaccaa accaac ccaacc caacca aaccaa accaac ccaact 
caactt aacttt actttc ctttcg tttcga ttcgat....'
```

### Comparing genomes
### This example: Human COVID-19 vs. Bat COVID-19
Read the Alignment-Hit Table
```
alignHit=pd.read_csv('./sars_coronavirus_accession_Kaggle/MN997409.1-4NY0T82X016-Alignment-HitTable.csv')
alignHit.head()

# Output
   MN997409.1 MN997409.1.1  100.000  29882  ...  1.1  29882.2  0.0  55182
0  MN997409.1   MT020881.1   99.990  29882  ...    1    29882  0.0  55166
1  MN997409.1   MT020880.1   99.990  29882  ...    1    29882  0.0  55166
2  MN997409.1   MN985325.1   99.990  29882  ...    1    29882  0.0  55166
3  MN997409.1   MN975262.1   99.990  29882  ...    1    29882  0.0  55166
4  MN997409.1   LC522974.1   99.993  29878  ...    1    29878  0.0  55164
```

Rename Columns
```
alignHit=alignHit.rename(columns={"MN997409.1": "query acc.ver", "MN997409.1.1": "subject acc.ver",
                            "100.000":"% identity","29882":"alignment length","0":"mismatches",
                            "0.1":"gap opens","1":"q. start","29882.1":"q. end","1.1":"s. start",
                           "29882.2	":"s. end","0.0":"evalue","55182":"bit score"})
```
Put data back in first row
```
alignHit = alignHit.append(pd.Series(['MN997409.1',	'MN997409.1.1',	
                    100.000,	29882,	
                    0,	0.1,	1,	29882.1,	
                    1.1,	29882.2,	0.0,	55182], index=alignHit.columns), ignore_index=True)
```
Describe the data
```
ah=alignHit
ah.describe()

# Output
       % identity  alignment length  ...  evalue    bit score
count  263.000000        263.000000  ...   263.0    263.00000
mean    86.064958      10711.114068  ...     0.0  14240.34981
std      7.609654      10530.955700  ...     0.0  19226.72192
min     77.559000       1603.000000  ...     0.0   1011.00000
25%     80.048000       1925.000000  ...     0.0   2101.00000
50%     82.304000       5417.000000  ...     0.0   3936.00000
75%     90.189000      17716.000000  ...     0.0  15175.00000
max    100.000000      29882.000000  ...     0.0  55182.00000
```
Correlate Human and Bat Virus
```
ah.corr()

# Output
                  % identity  alignment length  ...  evalue  bit score
% identity          1.000000          0.631524  ...     NaN   0.793438
alignment length    0.631524          1.000000  ...     NaN   0.944639
mismatches         -0.453509          0.206680  ...     NaN  -0.125766
gap opens          -0.535174          0.136714  ...     NaN  -0.193213
q. start           -0.052519         -0.560720  ...     NaN  -0.502689
q. end              0.566794          0.355570  ...     NaN   0.367344
s. start           -0.051870         -0.560761  ...     NaN  -0.502181
29882.2             0.569653          0.359521  ...     NaN   0.371660
evalue                   NaN               NaN  ...     NaN        NaN
bit score           0.793438          0.944639  ...     NaN   1.000000
```

## K-Means Clustering and Silhouette Analysis
Run `KmeanuetteIt.py` to use K-Means and Silhouette analysis to measure distance between clusters (Silhouette score) and generate K-Means cluster graphs

## Calculate Cluster Classes with Principal Component Analysis (PCA)
```
covar_matrix = np.matmul(standardized_data.T , standardized_data)
values, vectors = eigh(covar_matrix, eigvals=(9,10))
vectors = vectors.T
new_coordinates = np.matmul(vectors, standardized_data.T)
new_coordinates = np.vstack((new_coordinates)).T
df = pd.DataFrame(data=new_coordinates, columns=("1st_principal", "2nd_principal"))
sns.set()
sns.FacetGrid(df, size=6).map(plt.scatter, '1st_principal', '2nd_principal').add_legend()
plt.title('PCA visualization of sequences')
plt.show()
```


![5 distinct classes of genome sequence clusters found via PCA](https://github.com/MattLondon101/Images/blob/master/pca1.png)








