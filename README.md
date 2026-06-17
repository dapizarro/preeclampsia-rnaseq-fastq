# RNA-seq FASTQ Pipeline

Reproducible Snakemake workflow for processing raw paired-end RNA-seq data from FASTQ files to gene- and transcript-level count matrices.

This repository represents **Part I** of a modular two-stage RNA-seq analysis framework:

### Part I — FASTQ Processing *(this repository)*

Raw FASTQ → quality control → trimming → alignment/pseudoalignment → count matrices

### Part II — Statistical Analysis *(under development)*

Count matrices → normalization → differential expression → functional enrichment → visualization and reporting

---

## Workflow Overview

```text
Raw FASTQ
    │
    ├── FastQC / MultiQC
    │       └── sequencing quality assessment
    │
    ├── fastp
    │       └── adapter removal and quality trimming
    │
    ├── STAR
    │       └── genome alignment
    │
    ├── featureCounts
    │       └── gene-level quantification
    │
    ├── Salmon
    │       └── transcript-level quantification
    │
    └── Count matrices
            ├── gene counts
            └── transcript abundances
```

---

## Quick Start

Create the Conda environment:

```bash
mamba env create -f envs/rnaseq.yaml
mamba activate preeclampsia-rnaseq
```

Run the workflow:

```bash
snakemake --cores 12 --use-conda --configfile config/config.yaml
```

---

## Input Data

Expected FASTQ naming convention:

```text
data/raw_fastq/
├── sample01_R1.fastq.gz
├── sample01_R2.fastq.gz
├── sample02_R1.fastq.gz
└── sample02_R2.fastq.gz
```

Generate the sample sheet automatically:

```bash
python scripts/make_samplesheet_from_fastq.py \
    --fastq-dir data/raw_fastq \
    --out config/samples.tsv
```

---

## Main Outputs

```text
results/
├── qc/
│   └── multiqc/multiqc_report.html
├── alignment/
│   └── star/*.sorted.bam
├── counts/
│   └── gene_counts.tsv
└── salmon/
    └── */quant.sf
```

---

## Project Status

🚧 **Active Development**

The FASTQ-to-counts workflow is fully functional and can be used for RNA-seq preprocessing and quantification.

A companion repository focused on downstream statistical analyses is currently under development and will include:

* differential expression analysis
* pathway and enrichment analyses
* publication-ready visualizations
* automated reporting

---

## Development Roadmap

### Implemented

* [x] FASTQ quality control (FastQC)
* [x] MultiQC reporting
* [x] Adapter and quality trimming (fastp)
* [x] STAR genome alignment
* [x] featureCounts gene quantification
* [x] Salmon transcript quantification
* [x] Gene-level count matrices
* [x] Transcript abundance estimates

### Planned

* [ ] Differential expression analysis
* [ ] Functional enrichment analysis
* [ ] Publication-ready figures
* [ ] Automated HTML/RMarkdown reports

---

## Citation

If you use this workflow in your research, please cite DOI: Zenodo. https://doi.org/10.5281/zenodo.20702759
# RNA-seq FASTQ Pipeline

Reproducible Snakemake workflow for processing raw paired-end RNA-seq data from FASTQ files to gene- and transcript-level count matrices.

This repository represents **Part I** of a modular two-stage RNA-seq analysis framework:

### Part I — FASTQ Processing *(this repository)*

Raw FASTQ → quality control → trimming → alignment/pseudoalignment → count matrices

### Part II — Statistical Analysis *(under development)*

Count matrices → normalization → differential expression → functional enrichment → visualization and reporting

---

## Workflow Overview

```text
Raw FASTQ
    │
    ├── FastQC / MultiQC
    │       └── sequencing quality assessment
    │
    ├── fastp
    │       └── adapter removal and quality trimming
    │
    ├── STAR
    │       └── genome alignment
    │
    ├── featureCounts
    │       └── gene-level quantification
    │
    ├── Salmon
    │       └── transcript-level quantification
    │
    └── Count matrices
            ├── gene counts
            └── transcript abundances
```

---

## Quick Start

Create the Conda environment:

```bash
mamba env create -f envs/rnaseq.yaml
mamba activate preeclampsia-rnaseq
```

Run the workflow:

```bash
snakemake --cores 12 --use-conda --configfile config/config.yaml
```

---

## Input Data

Expected FASTQ naming convention:

```text
data/raw_fastq/
├── sample01_R1.fastq.gz
├── sample01_R2.fastq.gz
├── sample02_R1.fastq.gz
└── sample02_R2.fastq.gz
```

Generate the sample sheet automatically:

```bash
python scripts/make_samplesheet_from_fastq.py \
    --fastq-dir data/raw_fastq \
    --out config/samples.tsv
```

---

## Main Outputs

```text
results/
├── qc/
│   └── multiqc/multiqc_report.html
├── alignment/
│   └── star/*.sorted.bam
├── counts/
│   └── gene_counts.tsv
└── salmon/
    └── */quant.sf
```

---

## Project Status

🚧 **Active Development**

The FASTQ-to-counts workflow is fully functional and can be used for RNA-seq preprocessing and quantification.

A companion repository focused on downstream statistical analyses is currently under development and will include:

* differential expression analysis
* pathway and enrichment analyses
* publication-ready visualizations
* automated reporting

---

## Development Roadmap

### Implemented

* [x] FASTQ quality control (FastQC)
* [x] MultiQC reporting
* [x] Adapter and quality trimming (fastp)
* [x] STAR genome alignment
* [x] featureCounts gene quantification
* [x] Salmon transcript quantification
* [x] Gene-level count matrices
* [x] Transcript abundance estimates

### Planned

* [ ] Differential expression analysis
* [ ] Functional enrichment analysis
* [ ] Publication-ready figures
* [ ] Automated HTML/RMarkdown reports

---

## Citation

If you use this workflow in your research, please cite DOI: Zenodo. https://doi.org/10.5281/zenodo.20702759
