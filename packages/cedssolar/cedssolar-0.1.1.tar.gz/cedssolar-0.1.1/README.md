## CEDS Solar

A Differential Private Solar Metadata inference package.

## Installation

Install the package using the following command:

```
pip install git+https://github.com/lbnl-cybersecurity/CEDSSolar.git
pip install git+https://github.com/fmfn/BayesianOptimization
```

## Usage

The package may be used as follows:

- Import packages:

```python
from CEDSSolar.gridSearch.GridSearchKevala import SolarPVMetaData
from CEDSSolar.gridSearch import fit
from CEDSSolar.gridSearch.fit import Fit
from CEDSSolar.gridSearch.results import aggregate_across_months, filter_grid_search_results
from CEDSSolar.gridSearch.plot import plot_grid_search_results, plotly_final
from CEDSSolar.gridSearch.query import get_data

import pandas as pd
import numpy as np
from bayes_opt import SequentialDomainReductionTransformer
import sqlalchemy
import json
import plotly.express as px
import pytz
from dotenv import dotenv_values
```

- Initialize database connection:

```python
config = dotenv_values("../.env")
engine = sqlalchemy.create_engine(
    f'postgresql://{config["USERNAME"]}:{config["PASSWORD"]}@{config["HOSTNAME"]}:{config["PORT"]}/{config["DB_NAME"]}'
)
```

- Ingest relevant solar generation data:

```python
system_id, year = '824950', '2016'
df, lat, lon, info = get_data(engine, system_id, year)
true_fit = Fit(json.loads(info)["azimuth"], 90)
```

- Initialize the SolarPVMetaData class:

```python
smd = SolarPVMetaData(df.copy(), lat=lat, lon=lon, year=year)
```

- Perform a smart grid search:

```python
yearly_results_list = smd.smart_grid_search(
    top_percent_to_retain_per_month=0.1, rmse_filtered=False
)
```

- Plot the results:

```python
plotly_final(
    yearly_results_list,
    true_fit,
    [
        fit.best_fit(yearly_results_list[0]),
        fit.best_fit(yearly_results_list[1]),
    ],
    "count",
)
```

![me](README.png)

- Alternatively, to perform inference via DP Bayesian Optimization:

```python

bayes_results = smd.bayesian_search(
    (0, 360),
    (0, 90),
    dict(bounds_transformer=SequentialDomainReductionTransformer()),
    dict(init_points=10, n_iter=80),
)
yearly_results = (
    pd.concat(
        [
            pd.DataFrame(pd.DataFrame(bayes_results.res).params.tolist()),
            pd.DataFrame(bayes_results.res).target,
        ],
        axis=1,
    )
    .set_index(["surface_azimuth", "surface_tilt"])
    .rename(columns={"target": "count"})
)
plotly_final(
    [yearly_results], true_fit, [fit.best_fit(yearly_results)], "count", -1, -3
)
```
