# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_lightgbm', 'neptune_lightgbm.impl']

package_data = \
{'': ['*']}

install_requires = \
['graphviz', 'lightgbm', 'matplotlib', 'neptune-client>=0.16.17', 'scikit-plot']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 'dev': ['pre-commit', 'pytest>=5.0', 'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'neptune-lightgbm',
    'version': '1.0.0',
    'description': 'Neptune.ai LightGBM integration library',
    'long_description': '# Neptune + LightGBM Integration\n\nExperiment tracking, model registry, data versioning, and live model monitoring for LightGBM trained models.\n\n## What will you get with this integration?\n\n* Log, display, organize, and compare ML experiments in a single place\n* Version, store, manage, and query trained models, and model building metadata\n* Record and monitor model training, evaluation, or production runs live\n\n## What will be logged to Neptune?\n\n* training and validation metrics,\n* parameters,\n* feature names, num_features, and num_rows for the train set,\n* hardware consumption (CPU, GPU, memory),\n* stdout and stderr logs,\n* training code and git commit information.\n* [other metadata](https://docs.neptune.ai/you-should-know/what-can-you-log-and-display)\n\n![image](https://user-images.githubusercontent.com/97611089/160637021-6d324be7-00f0-4b89-bffd-ae937f6802b4.png)\n*Example dashboard with train-valid metrics and selected parameters*\n\n\n## Resources\n\n* [Documentation](https://docs.neptune.ai/integrations-and-supported-tools/model-training/lightgbm)\n* [Code example on GitHub](https://github.com/neptune-ai/examples/blob/main/integrations-and-supported-tools/lightgbm/scripts/Neptune_LightGBM_train_summary.py)\n* [Example of a run logged in the Neptune app](https://app.neptune.ai/o/common/org/lightgbm-integration/e/LGBM-86/dashboard/train-cls-summary-6c07f9e0-36ca-4432-9530-7fd3457220b6)\n* [Run example in Google Colab](https://colab.research.google.com/github/neptune-ai/examples/blob/main/integrations-and-supported-tools/lightgbm/notebooks/Neptune_LightGBM.ipynb)\n\n## Example\n\n```python\n# On the command line:\npip install neptune-client lightgbm neptune-lightgbm\n```\n```python\n# In Python:\nimport lightgbm as lgb\nimport neptune.new as neptune\nfrom neptune.new.integrations.lightgbm import NeptuneCallback\n\n# Start a run\nrun = neptune.init_run(\n    project="common/lightgbm-integration",\n    api_token=neptune.ANONYMOUS_API_TOKEN,\n)\n\n# Create a NeptuneCallback instance\nneptune_callback = NeptuneCallback(run=run)\n\n# Prepare datasets\n...\nlgb_train = lgb.Dataset(X_train, y_train)\n\n# Define model parameters\nparams = {\n    "boosting_type": "gbdt",\n    "objective": "multiclass",\n    "num_class": 10,\n    ...\n}\n\n# Train the model\ngbm = lgb.train(\n    params,\n    lgb_train,\n    callbacks=[neptune_callback],\n)\n```\n\n## Support\n\nIf you got stuck or simply want to talk to us, here are your options:\n\n* Check our [FAQ page](https://docs.neptune.ai/getting-started/getting-help#frequently-asked-questions)\n* You can submit bug reports, feature requests, or contributions directly to the repository.\n* Chat! When in the Neptune application click on the blue message icon in the bottom-right corner and send a message. A real person will talk to you ASAP (typically very ASAP),\n* You can just shoot us an email at support@neptune.ai\n',
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
