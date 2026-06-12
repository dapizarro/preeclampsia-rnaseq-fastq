#!/usr/bin/env python3
import argparse, pandas as pd
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('--featurecounts', required=True); p.add_argument('--out', required=True); a=p.parse_args()
fc=pd.read_csv(a.featurecounts, sep='\t', comment='#')
counts=fc.drop(columns=[c for c in ['Chr','Start','End','Strand','Length'] if c in fc.columns]).rename(columns={'Geneid':'gene_id'})
counts.columns=[Path(c).name.replace('.sorted.bam','') if c!='gene_id' else c for c in counts.columns]
counts.to_csv(a.out, sep='\t', index=False)
