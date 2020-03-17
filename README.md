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
# Parse and print genome
for seq_record in SeqIO.parse('./sars_coronavirus_accession_Kaggle/SARS_CORONAVIRUS_NC_045512_sequence.fasta',"fasta"):
    print(seq_record.id)
    print(seq_record.seq)
```
```
# Convert sequence to string 
cv19=str(seq_record.seq)
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








