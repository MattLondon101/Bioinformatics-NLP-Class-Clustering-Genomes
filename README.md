# COVID-19-Genome-Sequencing-and-Predictions-with-Artificial-Intelligence
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

4. One-hot encode genome string. Non "acgt" bases (n) are 0000.
```
# returns a L x 4 numpy array
one_hot_encoder(string_to_array(cv19))
```
```
# Data will print as array
array([[1, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 0, 1],
       ...,
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]], dtype=int32)
```


