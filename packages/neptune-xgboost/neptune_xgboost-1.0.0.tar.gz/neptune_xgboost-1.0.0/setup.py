# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_xgboost', 'neptune_xgboost.impl']

package_data = \
{'': ['*']}

install_requires = \
['graphviz', 'matplotlib', 'neptune-client>=0.16.17', 'xgboost>=1.3.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 'dev': ['pre-commit', 'pytest>=5.0', 'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'neptune-xgboost',
    'version': '1.0.0',
    'description': 'Neptune.ai XGBoost integration library',
    'long_description': '# Neptune + XGBoost Integration\n\nExperiment tracking, model registry, data versioning, and live model monitoring for XGBoost trained models.\n\n## What will you get with this integration?\n\n* Log, display, organize, and compare ML experiments in a single place\n* Version, store, manage, and query trained models, and model building metadata\n* Record and monitor model training, evaluation, or production runs live\n\n## What will be logged to Neptune?\n\n* metrics,\n* parameters,\n* learning rate,\n* pickled model,\n* visualizations (feature importance chart and tree visualizations),\n* hardware consumption (CPU, GPU, Memory),\n* stdout and stderr logs, and\n* training code and git commit information\n* [other metadata](https://docs.neptune.ai/you-should-know/what-can-you-log-and-display)\n\n![image](https://user-images.githubusercontent.com/97611089/160614588-5d839a11-e2f9-4eed-a3d1-39314ebdb1ea.png)\n*Example dashboard with train-valid metrics and selected parameters*\n\n\n## Resources\n\n* [Documentation](https://docs.neptune.ai/integrations-and-supported-tools/model-training/xgboost)\n* [Code example on GitHub](https://github.com/neptune-ai/examples/blob/main/integrations-and-supported-tools/xgboost/scripts/Neptune_XGBoost_train.py)\n* [Example of a run logged in the Neptune app](https://app.neptune.ai/o/common/org/xgboost-integration/e/XGBOOST-84/dashboard/train-e395296a-4f3d-4a58-ab88-6ef06bbac657)\n* [Run example in Google Colab](https://colab.research.google.com/github/neptune-ai/examples/blob/main/integrations-and-supported-tools/xgboost/notebooks/Neptune_XGBoost.ipynb)\n\n## Example\n\n```python\n# On the command line:\npip install neptune-client xgboost>=1.3.0 neptune-xgboost\n```\n```python\n# In Python:\nimport neptune.new as neptune\nimport xgboost as xgb\nfrom neptune.new.integrations.xgboost import NeptuneCallback\n\n# Start a run\nrun = neptune.init_run(\n    project="common/xgboost-integration",\n    api_token=neptune.ANONYMOUS_API_TOKEN,\n)\n\n# Create a NeptuneCallback instance\nneptune_callback = NeptuneCallback(run=run, log_tree=[0, 1, 2, 3])\n\n# Prepare datasets\n...\ndata_train = xgb.DMatrix(X_train, label=y_train)\n\n# Define model parameters\nmodel_params = {\n    "eta": 0.7,\n    "gamma": 0.001,\n    "max_depth": 9,\n    ...\n}\n\n# Train the model and log metadata to the run in Neptune\nxgb.train(\n    params=model_params,\n    dtrain=data_train,\n    callbacks=[neptune_callback],\n)\n```\n\n## Support\n\nIf you got stuck or simply want to talk to us, here are your options:\n\n* Check our [FAQ page](https://docs.neptune.ai/getting-started/getting-help#frequently-asked-questions)\n* You can submit bug reports, feature requests, or contributions directly to the repository.\n* Chat! When in the Neptune application click on the blue message icon in the bottom-right corner and send a message. A real person will talk to you ASAP (typically very ASAP),\n* You can just shoot us an email at support@neptune.ai\n',
    'author': 'neptune.ai',
    'author_email': 'contact@neptune.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://neptune.ai/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
