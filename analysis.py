# analysis.py — DataPulse analysis
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import glob

print('DataPulse Analysis')
print('=' * 35)

files = glob.glob('data/*.csv') + glob.glob('data/*.xlsx')
print(f'Found files: {files}')

for f in files:
    print(f'\n--- {f} ---')
    if f.endswith('.csv'):
        df = pd.read_csv(f)
    else:
        df = pd.read_excel(f)
    
    print(f'Shape: {df.shape[0]} rows, {df.shape[1]} columns')
    print('Columns:', list(df.columns))
    print(df.head(3).to_string())
    print('\nSummary:')
    print(df.describe(include='all').to_string())
    
    out = Path('outputs') / (Path(f).stem + '_summary.csv')
    df.describe(include='all').to_csv(out)
    print(f'Saved: {out}')

    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        plt.figure()
        df[num_cols[0]].hist()
        plt.title(f'{Path(f).stem} - {num_cols[0]} distribution')
        plt.xlabel(num_cols[0])
        plt.ylabel('Count')
        chart = Path('outputs') / (Path(f).stem + '_chart.png')
        plt.savefig(chart)
        plt.close()
        print(f'Saved chart: {chart}')

print('\n' + '=' * 35)
print('Analysis complete!')