## How to download their datasets

```python
import pandas as pd 
data_name = 'ToyotaCorolla'
df = pd.read_csv(f'{data_name}.csv')
compression_opts = dict(method='zip',
                        archive_name=f'{data_name}.csv')  
df.to_csv(f'{data_name}.zip', index=False,
          compression=compression_opts) 
```