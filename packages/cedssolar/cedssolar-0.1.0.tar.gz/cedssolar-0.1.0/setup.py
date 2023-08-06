# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cedssolar',
 'cedssolar.CHS',
 'cedssolar.dataIngestion',
 'cedssolar.gridSearch',
 'cedssolar.location',
 'cedssolar.raksha',
 'cedssolar.soda']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=2.0.4,<3.0.0',
 'matplotlib>=3.7.0,<4.0.0',
 'multiprocess>=0.70.14,<0.71.0',
 'nbformat>=4.2.0,<5.0.0',
 'nrel-pysam==3.0.0',
 'numpy>=1.24.2,<2.0.0',
 'pandas-dataclasses>=0.11.0,<0.12.0',
 'pandas>=1.5.3,<2.0.0',
 'plotly>=5.13.0,<6.0.0',
 'psycopg2>=2.9.5,<3.0.0',
 'pvlib>=0.9.4,<0.10.0',
 'pydantic>=1.10.5,<2.0.0',
 'python-dotenv>=0.21.1,<0.22.0',
 'pytz>=2022.7.1,<2023.0.0',
 'scikit-learn>=1.2.1,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'cedssolar',
    'version': '0.1.0',
    'description': 'A python package to differentially privately infer solar metadata information',
    'long_description': '## CEDS Solar\n\nA Differential Private Solar Metadata inference package.\n\n## Installation\n\nInstall the package using the following command:\n\n```\npip install git+https://github.com/lbnl-cybersecurity/CEDSSolar.git\npip install git+https://github.com/fmfn/BayesianOptimization\n```\n\n## Usage\n\nThe package may be used as follows:\n\n- Import packages:\n\n```python\nfrom CEDSSolar.gridSearch.GridSearchKevala import SolarPVMetaData\nfrom CEDSSolar.gridSearch import fit\nfrom CEDSSolar.gridSearch.fit import Fit\nfrom CEDSSolar.gridSearch.results import aggregate_across_months, filter_grid_search_results\nfrom CEDSSolar.gridSearch.plot import plot_grid_search_results, plotly_final\nfrom CEDSSolar.gridSearch.query import get_data\n\nimport pandas as pd\nimport numpy as np\nfrom bayes_opt import SequentialDomainReductionTransformer\nimport sqlalchemy\nimport json\nimport plotly.express as px\nimport pytz\nfrom dotenv import dotenv_values\n```\n\n- Initialize database connection:\n\n```python\nconfig = dotenv_values("../.env")\nengine = sqlalchemy.create_engine(\n    f\'postgresql://{config["USERNAME"]}:{config["PASSWORD"]}@{config["HOSTNAME"]}:{config["PORT"]}/{config["DB_NAME"]}\'\n)\n```\n\n- Ingest relevant solar generation data:\n\n```python\nsystem_id, year = \'824950\', \'2016\'\ndf, lat, lon, info = get_data(engine, system_id, year)\ntrue_fit = Fit(json.loads(info)["azimuth"], 90)\n```\n\n- Initialize the SolarPVMetaData class:\n\n```python\nsmd = SolarPVMetaData(df.copy(), lat=lat, lon=lon, year=year)\n```\n\n- Perform a smart grid search:\n\n```python\nyearly_results_list = smd.smart_grid_search(\n    top_percent_to_retain_per_month=0.1, rmse_filtered=False\n)\n```\n\n- Plot the results:\n\n```python\nplotly_final(\n    yearly_results_list,\n    true_fit,\n    [\n        fit.best_fit(yearly_results_list[0]),\n        fit.best_fit(yearly_results_list[1]),\n    ],\n    "count",\n)\n```\n\n![me](README.png)\n\n- Alternatively, to perform inference via DP Bayesian Optimization:\n\n```python\n\nbayes_results = smd.bayesian_search(\n    (0, 360),\n    (0, 90),\n    dict(bounds_transformer=SequentialDomainReductionTransformer()),\n    dict(init_points=10, n_iter=80),\n)\nyearly_results = (\n    pd.concat(\n        [\n            pd.DataFrame(pd.DataFrame(bayes_results.res).params.tolist()),\n            pd.DataFrame(bayes_results.res).target,\n        ],\n        axis=1,\n    )\n    .set_index(["surface_azimuth", "surface_tilt"])\n    .rename(columns={"target": "count"})\n)\nplotly_final(\n    [yearly_results], true_fit, [fit.best_fit(yearly_results)], "count", -1, -3\n)\n```\n',
    'author': 'Nikhil Ravi',
    'author_email': 'nr337@cornell.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
