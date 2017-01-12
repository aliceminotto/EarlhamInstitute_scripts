## Earlham Institute scripts

_also known as "requests from people and/or super easy scrits that will make my life easier"_

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

###### rm_jobs.sh

Simple bash script to remove all Agave API jobs with a certain status (e.g. FAILED or FINISHED). Required to have the CyVerse CLI installed to work.

Usage:
```
rm_jobs.sh <STATUS>
```

###### rmi_docker.sh

Simple bash script to remove all dangling images with linked containers.
