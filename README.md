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








