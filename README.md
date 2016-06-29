## Earlham Institute scripts

###### agp2fa.py

Concatenate in a fasta file.
Inputs: fasta_file, agp_file.

###### bfr.py

Calculate BFR (Bulk Frequency Ratio) from a vcf file produced by freebayes.
--filter takes a list of samples and calculate BFR only if at least one of them has a different genotype from the others.


Usage:

```
Calculate BFR

positional arguments:
  vcf                   vcf file

optional arguments:
  -h, --help            show this help message and exit
  --mindp MINDP         DP minimum treshold
  -t TRAIT [TRAIT ...], --trait TRAIT [TRAIT ...]
                        trait samples
  -b BASE [BASE ...], --base BASE [BASE ...]
                        base samples
  --field FIELD         SNP index numerator/ default=AO
  -f FILTER [FILTER ...], --filter FILTER [FILTER ...]
                        filter for different GT
```
