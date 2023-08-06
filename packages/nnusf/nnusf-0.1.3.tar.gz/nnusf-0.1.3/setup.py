# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nnusf',
 'nnusf.cli',
 'nnusf.data',
 'nnusf.export_lhapdf',
 'nnusf.plot',
 'nnusf.reports',
 'nnusf.scripts',
 'nnusf.sffit',
 'nnusf.theory',
 'nnusf.theory.bodek_yang',
 'nnusf.theory.data_vs_theory',
 'nnusf.theory.highq',
 'nnusf.theory.yadknots']

package_data = \
{'': ['*'], 'nnusf.reports': ['assets/*'], 'nnusf.theory': ['assets/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'SQLAlchemy>=1.4.39,<2.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'banana-hep>=0.6.6,<0.7.0',
 'click>=8.1.3,<9.0.0',
 'greenlet>=1.1.2,<2.0.0',
 'h5py>=3.7.0,<4.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'pandas>=1.4.2,<2.0.0',
 'particle>=0.21.2,<0.22.0',
 'pendulum>=2.1.2,<3.0.0',
 'pineappl>=0.5.0,<0.6.0',
 'pygit2>=1.10.1,<2.0.0',
 'pylint>=2.14.4,<3.0.0',
 'pytzdata>=2020.1,<2021.0',
 'rich>=12.5.1,<13.0.0',
 'scipy>=1.8.1,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'setuptools>=65.5.1,<66.0.0',
 'tensorflow<2.9.10',
 'termcolor==1.1.0',
 'yadism>=0.12.3,<0.13.0']

entry_points = \
{'console_scripts': ['nnu = nnusf.cli:command']}

setup_kwargs = {
    'name': 'nnusf',
    'version': '0.1.3',
    'description': 'Predictions for all-energy neutrino structure functions',
    'long_description': '<h1 align="center">NNSFν</h1>\n<p align="center">\n  <a href="https://zenodo.org/account/settings/github/repository/NNPDF/nnusf#"><img alt="Zenodo" src="https://zenodo.org/badge/DOI/10.5281/zenodo.7657132 .svg"></a>\n  <a href="https://arxiv.org/abs/2302.08527"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2302.08527-b31b1b?labelColor=222222"></a>\n  <img alt="Docs" src="https://assets.readthedocs.org/static/projects/badges/passing-flat.svg">\n  <a href="https://pypi.org/project/nnusf/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nnusf"/></a>\n  <img alt="Status" src="https://www.repostatus.org/badges/latest/active.svg">\n  <img alt="License" src="https://img.shields.io/badge/License-GPL3-blue.svg">\n</p>\n\n<p align="justify">\n  <b>NNSFν</b> is a python module that provides predictions for neutrino structure functions. \n  It relies on <a href="https://github.com/N3PDF/yadism">YADISM</a> for the large-Q region \n  while the low-Q regime is modelled in terms of a Neural Network (NN). The NNSFν \n  determination is also made available in terms of fast interpolation\n  <a href="https://lhapdf.hepforge.org/">LHAPDF</a> grids that can be accessed through an independent\n  driver code and directly interfaced to the <a href="http://www.genie-mc.org/">GENIE</a> Monte Carlo\n  neutrino event generators.\n</p>\n\n\n# Quick links\n\n- [Installation instructions](https://nnpdf.github.io/nnusf/quickstart/installation.html)\n- [Tutorials](https://nnpdf.github.io/nnusf/tutorials/datasets.html)\n- [Delivery & Usage](https://nnpdf.github.io/nnusf/delivery/lhapdf.html)\n\n# Citation\n\nTo refer to NNSFν in a scientific publication, please use the following:\n```bibtex\n@article{Candido:2023utz,\n    author = "Candido, Alessandro and Garcia, Alfonso and Magni, Giacomo and Rabemananjara, Tanjona and Rojo, Juan and Stegeman, Roy",\n    title = "{Neutrino Structure Functions from GeV to EeV Energies}",\n    eprint = "2302.08527",\n    archivePrefix = "arXiv",\n    primaryClass = "hep-ph",\n    reportNumber = "Nikhef 2022-014, Edinburgh 2022/27, TIF-UNIMI-2023-5",\n    month = "2",\n    year = "2023"\n}\n```\nAnd if NNSFν proved to be useful in your work, consider also to reference the codes:\n```bibtex\n@misc{https://doi.org/10.5281/zenodo.7657132,\n  doi = {10.5281/ZENODO.7657132},\n  url = {https://zenodo.org/record/7657132},\n  author = "Candido, Alessandro and Garcia, Alfonso and Magni, Giacomo and Rabemananjara, Tanjona and Rojo, Juan and Stegeman, Roy",\n   title = "{Neutrino Structure Functions from GeV to EeV Energies}",\n  publisher = {Zenodo},\n  year = {2023},\n  copyright = {Open Access}\n}\n```\n',
    'author': 'Alessandro Candido',
    'author_email': 'candido.ale@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NNPDF/nnusf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
