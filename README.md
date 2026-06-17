# RNA-seq FASTQ pipeline

Reproducible Snakemake workflow for processing raw paired-end RNA-seq FASTQ files into gene- and transcript-level count matrices.

This is **Part I** of the project:

1. FASTQ → QC → trimming → alignment/pseudoalignment → count matrices
2. Count matrices → statistics → DEGs → enrichment → figures

## Workflow

```text
raw FASTQ
  ├── FastQC / MultiQC
  ├── fastp trimming
  ├── STAR alignment
  ├── featureCounts gene quantification
  ├── Salmon transcript quantification
  └── final gene/transcript count matrices
```

## Quick start

```bash
mamba env create -f envs/rnaseq.yaml
mamba activate rnaseq
snakemake --cores 12 --use-conda --configfile config/config.yaml
```

## Input naming

```text
data/raw_fastq/{sample}_R1.fastq.gz
data/raw_fastq/{sample}_R2.fastq.gz
```

Generate `config/samples.tsv`:

```bash
python scripts/make_samplesheet_from_fastq.py --fastq-dir data/raw_fastq --out config/samples.tsv
```

## Main outputs

```text
results/qc/multiqc/multiqc_report.html
results/alignment/star/*.sorted.bam
results/counts/gene_counts.tsv
results/salmon/*/quant.sf
```
