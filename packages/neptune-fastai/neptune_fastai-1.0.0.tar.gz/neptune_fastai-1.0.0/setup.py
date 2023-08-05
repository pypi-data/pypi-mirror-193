# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_fastai', 'neptune_fastai.impl']

package_data = \
{'': ['*']}

install_requires = \
['fastai>=2.4', 'neptune-client>=0.16.17']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 'dev': ['pre-commit',
         'pytest>=5.0',
         'pytest-tap==3.2',
         'pytest-cov==2.10.1',
         'pytest-xdist==2.2.0']}

setup_kwargs = {
    'name': 'neptune-fastai',
    'version': '1.0.0',
    'description': 'Neptune.ai fast.ai integration library',
    'long_description': '# Neptune + Fastai Integration\n\nExperiment tracking, model registry, data versioning, and live model monitoring for fastai trained models.\n\n## What will you get with this integration?\n\n* Log, display, organize, and compare ML experiments in a single place\n* Version, store, manage, and query trained models, and model building metadata\n* Record and monitor model training, evaluation, or production runs live\n\n## What will be logged to Neptune?\n\n* Hyper-parameters\n* Losses & metrics\n* Training code (Python scripts or Jupyter notebooks) and git information\n* Dataset version\n* Model Configuration, architecture, and weights\n* [other metadata](https://docs.neptune.ai/you-should-know/what-can-you-log-and-display)\n\n![image](https://user-images.githubusercontent.com/97611089/160639808-bd381089-66c8-4ed5-a895-0c018b378e0a.png)\n*Example dashboard with train-valid metrics and selected parameters*\n\n\n## Resources\n\n* [Documentation](https://docs.neptune.ai/integrations-and-supported-tools/model-training/fastai)\n* [Code example on GitHub](https://github.com/neptune-ai/examples/tree/main/integrations-and-supported-tools/fastai/scripts)\n* [Example dashboard in the Neptune app](https://app.neptune.ai/o/common/org/fastai-integration/e/FAS-61/dashboard/fastai-dashboard-1f456716-f509-4432-b8b3-a7f5242703b6)\n* [Run example in Google Colab](https://colab.research.google.com/github/neptune-ai/examples/blob/main/integrations-and-supported-tools/fastai/notebooks/Neptune_fastai.ipynb)\n\n## Example\n\n```python\n# On the command line:\npip install fastai neptune-client[fastai]\n```\n```python\n# In Python:\nimport neptune.new as neptune\n\n# Start a run\nrun = neptune.init_run(project="common/fastai-integration",\n                       api_token=neptune.ANONYMOUS_API_TOKEN,\n                       source_files=["*.py"])\n\n# Log a single training phase\nlearn = learner(...)\nlearn.fit(..., cbs = NeptuneCallback(run=run))\n\n# Log all training phases of the learner\nlearn = cnn_learner(..., cbs=NeptuneCallback(run=run))\nlearn.fit(...)\nlearn.fit(...)\n\n# Stop the run\nrun.stop()\n```\n\n## Support\n\nIf you got stuck or simply want to talk to us, here are your options:\n\n* Check our [FAQ page](https://docs.neptune.ai/getting-started/getting-help#frequently-asked-questions)\n* You can submit bug reports, feature requests, or contributions directly to the repository.\n* Chat! When in the Neptune application click on the blue message icon in the bottom-right corner and send a message. A real person will talk to you ASAP (typically very ASAP),\n* You can just shoot us an email at support@neptune.ai\n',
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
