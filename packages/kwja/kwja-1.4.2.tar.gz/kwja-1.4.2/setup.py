# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kwja',
 'kwja.callbacks',
 'kwja.cli',
 'kwja.datamodule',
 'kwja.datamodule.datasets',
 'kwja.datamodule.examples',
 'kwja.datamodule.extractors',
 'kwja.evaluators',
 'kwja.models',
 'kwja.models.models',
 'kwja.preprocessors',
 'kwja.utils']

package_data = \
{'': ['*']}

install_requires = \
['hydra-core>=1.2,<2.0',
 'importlib-resources>=5.10,<6.0',
 'jaconv>=0.3,<0.4',
 'jinf>=1.0.4,<2.0.0',
 'omegaconf>=2.1,<3.0',
 'pandas>=1.4,<2.0',
 'pure-cdb>=4.0,<5.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'pytorch-lightning>=1.9.0,<1.10.0',
 'rhoknp>=1.1.0,<1.2.0',
 'rich>=12.4',
 'seqeval>=1.2,<2.0',
 'tokenizers>=0.13.2,<0.14.0',
 'torch>=1.11,<1.13',
 'torchmetrics>=0.10.2,<0.11.0',
 'transformers[sentencepiece]>=4.25.1,<4.26.0',
 'typer>=0.6.1,<0.8.0']

entry_points = \
{'console_scripts': ['kwja = kwja.cli.cli:app']}

setup_kwargs = {
    'name': 'kwja',
    'version': '1.4.2',
    'description': 'A unified language analyzer for Japanese',
    'long_description': '# KWJA: Kyoto-Waseda Japanese Analyzer\n\n[![test](https://github.com/ku-nlp/kwja/actions/workflows/test.yml/badge.svg)](https://github.com/ku-nlp/kwja/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/ku-nlp/kwja/branch/main/graph/badge.svg?token=A9FWWPLITO)](https://codecov.io/gh/ku-nlp/kwja)\n[![PyPI](https://img.shields.io/pypi/v/kwja)](https://pypi.org/project/kwja/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kwja)\n\n[[Paper]](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=220232&item_no=1&page_id=13&block_id=8)\n[[Slides]](https://speakerdeck.com/nobug/kyoto-waseda-japanese-analyzer)\n\nKWJA is a Japanese language analyzer based on pre-trained language models.\nKWJA performs many language analysis tasks, including:\n- Typo correction\n- Tokenization\n- Word normalization\n- Morphological analysis\n- Named entity recognition\n- Word feature tagging\n- Dependency parsing\n- PAS analysis\n- Bridging reference resolution\n- Coreference resolution\n- Discourse relation analysis\n\n## Requirements\n\n- Python: 3.8+\n- Dependencies: See [pyproject.toml](./pyproject.toml).\n\n## Getting Started\n\nInstall KWJA with pip:\n\n```shell\n$ pip install kwja\n```\n\nPerform language analysis with the `kwja` command (the result is in the KNP format):\n\n```shell\n# Analyze a text\n$ kwja --text "KWJAは日本語の統合解析ツールです。汎用言語モデルを利用し、様々な言語解析を統一的な方法で解いています。"\n\n# Analyze a text file and write the result to a file\n$ kwja --file path/to/file.txt > path/to/analyzed.knp\n\n# Analyze texts interactively\n$ kwja\nPlease end your input with a new line and type "EOD"\nKWJAは日本語の統合解析ツールです。汎用言語モデルを利用し、様々な言語解析を統一的な方法で解いています。\nEOD\n```\n\nThe output is in the KNP format, like the following:\n\n```\n# S-ID:202210010000-0-0 kwja:1.0.2\n* 2D\n+ 5D <rel type="=" target="ツール" sid="202210011918-0-0" id="5"/><体言><NE:ARTIFACT:KWJA>\nKWJA ＫWＪＡ KWJA 名詞 6 固有名詞 3 * 0 * 0 <基本句-主辞>\nは は は 助詞 9 副助詞 2 * 0 * 0 "代表表記:は/は" <代表表記:は/は>\n* 2D\n+ 2D <体言>\n日本 にほん 日本 名詞 6 地名 4 * 0 * 0 "代表表記:日本/にほん 地名:国" <代表表記:日本/にほん><地名:国><基本句-主辞>\n+ 4D <体言><係:ノ格>\n語 ご 語 名詞 6 普通名詞 1 * 0 * 0 "代表表記:語/ご 漢字読み:音 カテゴリ:抽象物" <代表表記:語/ご><漢字読み:音><カテゴリ:抽象物><基本句-主辞>\nの の の 助詞 9 接続助詞 3 * 0 * 0 "代表表記:の/の" <代表表記:の/の>\n...\n```\n\nHere are some other options for `kwja` command:\n\n`--model-size`: Model size to be used. Please specify \'tiny\', \'base\' (default) or \'large\'.\n\n`--device`: Device to be used. Please specify \'cpu\' or \'gpu\'.\n\n`--typo-batch-size`: Batch size for typo module.\n\n`--char-batch-size`: Batch size for char module.\n\n`--word-batch-size`: Batch size for word module.\n\n`--tasks`: Tasks to be performed. Please specify \'typo\', \'char\', \'typo,char\', \'char,word\', \'typo,char,word\', \'char,word,word_discourse\' or \'typo,char,word,word_discourse\'.\n  - `typo`: Typo correction\n  - `char`: Tokenization and Word normalization\n  - `word`: Morphological analysis, Named entity recognition, Word feature tagging, Dependency parsing, PAS analysis, Bridging reference resolution, and Coreference resolution\n  - `word_discourse`: Discourse relation analysis\n    - If you need the results of discourse relation analysis, please specify this in addition to `word`.\n\nYou can read a KNP format file with [rhoknp](https://github.com/ku-nlp/rhoknp).\n\n```python\nfrom rhoknp import Document\nwith open("analyzed.knp") as f:\n    parsed_document = Document.from_knp(f.read())\n```\n\nFor more details about KNP format, see [Reference](#reference).\n\n## Usage from Python\n\nMake sure you have `kwja` command in your path:\n\n```shell\n$ which kwja\n/path/to/kwja\n```\n\nInstall [rhoknp](https://github.com/ku-nlp/rhoknp):\n\n```shell\n$ pip install rhoknp\n```\n\nPerform language analysis with the `kwja` instance:\n\n```python\nfrom rhoknp import KWJA\nkwja = KWJA()\nanalyzed_document = kwja.apply(\n    "KWJAは日本語の統合解析ツールです。汎用言語モデルを利用し、様々な言語解析を統一的な方法で解いています。"\n)\n```\n\n## Citation\n\n```bibtex\n@InProceedings{植田2022,\n  author    = {植田 暢大 and 大村 和正 and 児玉 貴志 and 清丸 寛一 and 村脇 有吾 and 河原 大輔 and 黒橋 禎夫},\n  title     = {KWJA：汎用言語モデルに基づく日本語解析器},\n  booktitle = {第253回自然言語処理研究会},\n  year      = {2022},\n  address   = {京都},\n}\n```\n\n## Reference\n\n- [KNP format](http://cr.fvcrc.i.nagoya-u.ac.jp/~sasano/knp/format.html)\n',
    'author': 'Hirokazu Kiyomaru',
    'author_email': 'kiyomaru@i.kyoto-u.ac.jp',
    'maintainer': 'Hirokazu Kiyomaru',
    'maintainer_email': 'kiyomaru@i.kyoto-u.ac.jp',
    'url': 'https://github.com/ku-nlp/kwja',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
