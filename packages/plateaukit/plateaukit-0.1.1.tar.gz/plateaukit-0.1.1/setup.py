# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plateaukit',
 'plateaukit.download',
 'plateaukit.extractors',
 'plateaukit.generators']

package_data = \
{'': ['*']}

install_requires = \
['aiomultiprocess>=0.9.0,<0.10.0',
 'bidict>=0.22.1,<0.23.0',
 'cjio[reproject]>=0.8.0,<0.9.0',
 'click>=8.1.3,<9.0.0',
 'geojson>=2.5.0,<3.0.0',
 'geopandas>=0.12.2,<0.13.0',
 'joblib>=1.2.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'lxml>=4.9.2,<5.0.0',
 'numpy<1.24',
 'prettytable>=3.6.0,<4.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pyogrio>=0.5.1,<0.6.0',
 'pyproj>=3.4.1,<4.0.0',
 'quantized-mesh-encoder>=0.4.3,<0.5.0',
 'requests>=2.28.2,<3.0.0',
 'tortoise-orm>=0.19.2,<0.20.0',
 'tqdm>=4.64.1,<5.0.0',
 'xdg>=5.1.1,<6.0.0',
 'xmltodict>=0.13.0,<0.14.0']

entry_points = \
{'console_scripts': ['plateaukit = plateaukit.cli:cli']}

setup_kwargs = {
    'name': 'plateaukit',
    'version': '0.1.1',
    'description': '',
    'long_description': '# PlateauKit\n\n> Python library and converter for 3D city models by MLIT Project PLATEAU\n\n国土交通省PLATEAU 3D都市モデルのPythonライブラリおよび変換ツール (WIP)\n\n## 特徴 Features\n\n- [x] PLATEAUデータセットのインストール・管理\n- [x] 並列処理でのデータ変換\n- [x] citygml-tools / citygml4j (Java) に依存せずCityJSONを生成 (一部)\n- [ ] JupyterLab / Jupyer Notebookでの3D都市モデル表示 (LOD1/2)\n\n## PlateauKitのインストール Install\n\n```sh\npip install plateaukit\n```\n\n## コマンドライン Command-line\n\n### PLATEAUデータをインストール/アンインストール\n\n#### 利用可能な都市モデルの一覧を表示\n\n```sh\nplateaukit install --list\n```\n\n#### 都市モデルをダウンロード・インストール\n\n```sh\n# (方法1) 東京都23区のデータをダウンロードして追加\nplateaukit install plateau-tokyo23ku\n\n# (方法2) 事前にダウンロード済みの東京都23区のデータを追加 (CityGML)\nplateaukit install plateau-tokyo23ku --local ./13100_tokyo23-ku_2020_citygml_3_2_op/ --format citygml\n```\n\n```sh\n# 追加済みのデータの一覧を表示\nplateaukit list\n```\n\n#### 都市モデルをアンインストール\n\n```sh\n# 東京都23区のデータをアンインストール\nplateaukit uninstall plateau-tokyo23ku\n```\n\n### PLATEAU CityGMLからCityJSON/GeoJSONを生成\n\n```sh\n# 建造物 (bldg) データからLOD0/1相当のGeoJSONを生成\nplateaukit generate-geojson --dataset plateau-tokyo23ku -t bldg /tmp/tokyo23ku-bldg.json\n```\n\n```sh\n# 建造物 (bldg) データからLOD0/1/2相当のCityJSONを生成 (データセット指定未対応、ファイル単位)\nplateaukit generate-cityjson ./udx/bldg/53395548_bldg_6697_2_op.gml /tmp/53395548_bldg_6697_2_op.cityjson\n```\n\n### PLATEAU CityGMLから属性情報を抽出\n\n> TODO: ドキュメントの整備\n\n## ライブラリ Library\n\n> TODO: ドキュメントの整備\n\n## ロードマップ Roadmap\n\n- [ ] ドキュメントの整備\n- [ ] データセットの軽量版のバンドルを提供\n- [ ] ファイル分割の平均化\n- [ ] テストの作成\n\n## その他のツール・ライブラリ Alternatives\n\n- [plateaupy](https://github.com/AcculusSasao/plateaupy)\n  - [rhenerose/plateaupy](https://github.com/rhenerose/plateaupy)\n- [raokiey/plateau-geo-tools](https://github.com/raokiey/plateau-geo-tools)\n',
    'author': 'Kentaro Ozeki',
    'author_email': '32771324+ozekik@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
