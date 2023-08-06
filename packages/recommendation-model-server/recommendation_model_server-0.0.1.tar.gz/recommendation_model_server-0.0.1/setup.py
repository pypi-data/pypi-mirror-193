# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['recommendation_model_server']

package_data = \
{'': ['*']}

install_requires = \
['autoflake>=2.0.1,<3.0.0',
 'coverage>=7.1.0,<8.0.0',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.92.0,<0.93.0',
 'httpx>=0.23.3,<0.24.0',
 'ipykernel>=6.21.2,<7.0.0',
 'joblib>=1.2.0,<2.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'lightgbm>=3.3.5,<4.0.0',
 'mypy>=1.0.1,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'polars>=0.16.6,<0.17.0',
 'pre-commit>=3.0.4,<4.0.0',
 'pyarrow>=11.0.0,<12.0.0',
 'pyupgrade>=3.3.1,<4.0.0',
 'twine>=4.0.2,<5.0.0',
 'types-requests>=2.28.11.14,<3.0.0.0',
 'uvicorn>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'recommendation-model-server',
    'version': '0.0.1',
    'description': 'A real-time inference server',
    'long_description': '# model server\n```mermaid\n---\ntitle: REST-inference service\n---\nclassDiagram\n    note "100 requests per second"\n\n    class VenueRating{\n    """\n    Represents the predicted ranking of a venue.\n\n    Attributes:\n    -----------\n    venue_id : int The ID of the venue being rated.\n    q80_predicted_rank : float\n        The predicted ranking of the venue,\n        as a 80-quantile of predicted rating\n        for venue across available sessions\n    """\n    venue_id: int\n    q80_predicted_rank: float\n    }\n    class TrainingPipeline{\n      str pre-trained-model-file: stored with mlflow in gcs bucket\n    }\n\n    class InferenceFeatures{\n    venue_id: int\n    conversions_per_impression: float\n    price_range: int\n    rating: float\n    popularity: float\n    retention_rate: float\n    session_id_hashed: int\n    position_in_list: int\n    is_from_order_again: int\n    is_recommended: int\n    }\n    class FastAPIEndpoint{\n      def predict_ratings(): Callabe\n    }\n\n    class Model_Instance{\n        joblib.load(model_artifact_bucket)\n        str model_artifact_bucket - variable\n        str rank_column - fixed for the model\n        str group_column - fixed for the model\n    }\n    TrainingPipeline --|> Model_Instance\n    InferenceFeatures --|> FastAPIEndpoint\n    Model_Instance --|> FastAPIEndpoint\n    FastAPIEndpoint --|> VenueRating\n\n```\n\n[![PyPI](https://img.shields.io/pypi/v/model-server?style=flat-square)](https://pypi.python.org/pypi/model-server/)\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/model-server?style=flat-square)](https://pypi.python.org/pypi/model-server/)\n\n[![PyPI - License](https://img.shields.io/pypi/l/model-server?style=flat-square)](https://pypi.python.org/pypi/model-server/)\n\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://ra312.github.io/model-server](https://ra312.github.io/model-server)\n**Training Source Code**: [https://github.com/ra312/personalization](https://github.com/ra312/personalization)\n**Source Code**: [https://github.com/ra312/model-server](https://github.com/ra312/model-server)\n**PyPI**: [https://pypi.org/project/model-server/](https://pypi.org/project/model-server/)\n\n---\n\nA model server  for almost realtime inference\n\n## Installation\n\n```sh\npip install model-server\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.8.1+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/ra312/model-server/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/ra312/model-server/releases) and publish it. When\n a release is published, it\'ll trigger [release](https://github.com/ra312/model-server/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n',
    'author': 'Rauan Akylzhanov',
    'author_email': 'akylzhanov.r@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
