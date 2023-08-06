# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jupyter2hashnode']

package_data = \
{'': ['*'],
 'jupyter2hashnode': ['examples/*', 'nbconvert/templates/hashnode/*']}

install_requires = \
['Pillow>=9.4.0,<10.0.0',
 'nbconvert>=7.2.9,<8.0.0',
 'python-dotenv>=0.21.1,<0.22.0',
 'requests>=2.28.2,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0']

extras_require = \
{':extra == "docs"': ['Sphinx>=6.1.3,<7.0.0',
                      'sphinx-rtd-theme>=1.2.0,<2.0.0',
                      'nbsphinx>=0.8.12,<0.9.0']}

entry_points = \
{'console_scripts': ['rick-portal-gun = jupyter2hashnode.cli:app']}

setup_kwargs = {
    'name': 'jupyter2hashnode',
    'version': '0.1.31',
    'description': 'Export from jupyter notebook into hashnode blog articles',
    'long_description': '[![PyPI version](https://badge.fury.io/py/jupyter2hashnode.svg)](https://badge.fury.io/py/jupyter2hashnode)\n\nJupyter2Hashnode is a useful tool for converting Jupyter Notebooks into Hashnode stories by simplifying the process of compressing images, uploading images, and publishing the story article.\n\n[See the full documentation here](https://jupyter2hashnode.readthedocs.io/en/latest/)\n\n# How to install\n```console\n    $ pip install jupyter2hashnode\n```\n\n\n# Using as a command line tool\n\nIf jwt, token, publication_id arguments not passed then will use environment variables HASHNODE_JWT, HASHNODE_TOKEN, HASHNODE_PUBLICATION_ID. \n\nNotes:\n\nTo obtain JWT: Open https://hashnode.com, account must be logged in, open DevTools of chrome browser (F12), go to Application tab, go to Cookies, find and copy value of "jwt" cookie (245 characters)\n\nTo obtain Hashnode API token: Open https://hashnode.com/settings/developer, click on "Generate New Token" button or use the existing one\n\nTo obtain Publication ID: Go to https://hashnode.com/settings/blogs, click "Dashboard" of the blog you want to upload to, copy the ID, e.g. https://hashnode.com/<id>/dashboard\n\n**Usage**:\n\n```console\n    $ jupyter2hashnode [OPTIONS] NOTEBOOK_PATH [OUTPUT_PATH]\n```\n\n**Arguments**:\n\n* `NOTEBOOK_PATH`: notebook file name or complete path  [required]\n* `[OUTPUT_PATH]`: output folder name or complete output path where the files will be written to, if none creates output folder with the same name as the notebook file name\n\n**Options**:\n\n* `-j, --jwt TEXT`: JWT token for authentication at https://hashnode.com/api/upload-image.\n* `-t, --token TEXT`: Token for authentication at https://api.hashnode.com  mutation createPublicationStory endpoint\n* `-p, --publication TEXT`: ID of the Hashnode publication e.g. https://hashnode.com/<id>/dashboard\n* `--title TEXT`: Article title  [required]\n* `--hide-from-feed / --no-hide-from-feed`: Hide this article from Hashnode and display it only on your blog  [default: True]\n* `--delete-files / --no-delete-files`: Delete all files after creating the publication story  [default: True]\n* `--upload / --no-upload`: Upload the publication story to the Hashnode server  [default: True]\n* `-v, --version`: Show the application\'s version and exit.\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n\n# Using as a library\n\nclass Jupyter2Hashnode\n\nNotes:\n- To obtain JWT\n    1. Open https://hashnode.com, account must be logged in\n    2. Open DevTools of chrome browser (F12)\n    3. Go to Application tab\n    4. Go to Cookies\n    5. Find and copy value of "jwt" cookie (245 characters)\n- To obtain Hashnode API token\n    1. Open https://hashnode.com/settings/developer\n    2. Click on "Generate New Token" button or use the existing one\n- To obtain Publication ID\n    1. Go to https://hashnode.com/settings/blogs\n    2. Click on "Dashboard" button of the blog you want to upload to\n    3. Copy ID from the URL, e.g. https://hashnode.com/<id>/dashboard\n- \n\nAttributes:\n\n    HASHNODE_JWT (str): JWT token for authentication at Hashnode image uploader, https://hashnode.com/api/upload-image.\n    HASHNODE_TOKEN (str): Token for authentication with the Hashnode server, to use https://api.hashnode.com\n                                mutation createPublicationStory endpoint\n    HASHNODE_PUBLICATION_ID (str): ID of the Hashnode publication e.g. https://hashnode.com/<id>/dashboard\n        \nMethods:\n\n    create_publication_story(title:str, notebook_path: str, output_path:Optional[str]=None, \n                                delete_files:bool=True, upload:bool=True):\n        This function is used to create a publication story on the Hashnode blog platform by \n        converting a Jupyter Notebook to a markdown file, compressing images, uploading images\n        to the Hashnode server, and replacing image URLs in the markdown file.\n\n        Parameters:\n            title (str): Title of the publication story.\n            notebook_path (str): Path to the Jupyter Notebook file.\n            hide_from_feed (bool): Hide this article from Hashnode and display it only on your blog, Default is True.\n            output_path (str, optional): Path to the output directory. Default is None.\n            delete_files (bool, optional): Boolean value indicating whether to delete all files after \n                                            creating the publication story. Default is True.\n            upload (bool, optional): Boolean value indicating whether to upload the publication story\n                                        to the Hashnode server. Default is True.\n\n        Returns:\n            None\n\n\n\n    \n**Usage**:\n\n```python\n    from jupyter2hashnode import Jupyter2Hashnode\n        \n    j2h = Jupyter2Hashnode(jwt, token, publication_id)\n    j2h.create_publication_story(title, notebook_path, hide_from_feed, output_path, delete_files, upload)\n```',
    'author': 'Tiago Patricio Santos',
    'author_email': 'tiagopatriciosantos@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tiagopatriciosantos/jupyter2hashnode',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
