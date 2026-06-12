#!/usr/bin/env python3
import argparse
from pathlib import Path
import pandas as pd
p=argparse.ArgumentParser()
p.add_argument('--fastq-dir', required=True); p.add_argument('--out', required=True)
a=p.parse_args()
rows=[]
for r1 in sorted(Path(a.fastq_dir).glob('*_R1*.fastq.gz')):
    r2 = r1.with_name(r1.name.replace('_R1','_R2'))
    if r2.exists():
        rows.append({'sample':r1.name.split('_R1')[0], 'fastq_1':str(r1), 'fastq_2':str(r2)})
if not rows: raise SystemExit('No paired FASTQ files found')
pd.DataFrame(rows).to_csv(a.out, sep='\t', index=False)
