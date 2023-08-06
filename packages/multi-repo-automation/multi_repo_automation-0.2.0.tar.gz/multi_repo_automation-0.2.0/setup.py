# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multi_repo_automation']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML', 'identify', 'requests', 'ruamel.yaml']

extras_require = \
{'update-stabilization-branches': ['c2cciutils']}

setup_kwargs = {
    'name': 'multi-repo-automation',
    'version': '0.2.0',
    'description': 'Library for automation updates on multiple repositories.',
    'long_description': '# Multi repo automation\n\n## Config\n\nCreate a file with something like this:\n\n```yaml\n- dir: /home/user/src/myrepo\n  name: user/myrepo\n  types: [\'javascript\', \'python\', \'docker\']\n  master_branch: master\n  stabilization_branches: [1.0, 1.1]\n  folders_to_clean: []\n```\n\n## Utilities\n\n```python\nimport multi_repo_automation as mra\n\n# Test if a file exists\nif mra.run(["git", "ls-files", "**/*.txt"], stdout=subprocess.PIPE).stdout.strip() != "":\n  print("Found")\n# Get all YAML files:\nmra.all_filenames_identify("yaml")\n# Test if a file exists and contains a text\nif mra.git_grep(file, r"\\<text\\>"]):\n  print("Found")\n# Edit a file in vscode\nmra.edit("file")\n```\n\n## Genenric run\n\n```python\n#!/usr/bin/env python3\nimport multi_repo_automation as mra\n\n\ndef _do() -> None:\n    # Do something\n    pass\n\nif __name__ == "__main__":\n    mra.main(_do)\n```\n\nIn the \\_do function do the changes you want in your repo.\n\nUse the `--help` option to see the available options.\n\n## To update all the master branches write a script like\n\n```python\n#!/usr/bin/env python3\nimport multi_repo_automation as mra\n\ndef _do() -> None:\n    # Do something\n    pass\n\nif __name__ == "__main__":\n    mra.main(\n        _do,\n        os.path.join(os.path.dirname(__file__), "repo.yaml"),\n        "/home/sbrunner/bin/firefox/firefox",\n        config={\n            "pull_request_branch": "branch_name",\n            "pull_request_title": "Commit/Pull request message",\n            "pull_request_body": "Optional body",\n        },\n    )\n```\n\n## To update all the stabilization branches write a script like\n\n```python\n#!/usr/bin/env python3\nimport multi_repo_automation as mra\n\ndef _do() -> None:\n    # Do something\n    pass\n\nif __name__ == "__main__":\n    mra.main(\n        _do,\n        os.path.join(os.path.dirname(__file__), "repo.yaml"),\n        "/home/sbrunner/bin/firefox/firefox",\n        config={\n            "pull_request_on_stabilization_branches": True,\n            "pull_request_branch_prefix": "prefix",\n            "pull_request_title": "Commit/Pull request message",\n            "pull_request_body": "Optional body",\n        },\n    )\n```\n\n## Configuration\n\nThe configuration is a YAML file `~/.config/multi-repo-automation.yaml` with the following options:\n\n`repos_filename`: the filename of the files with the repositories definitions, default is `repos.yaml`.\n`browser`: the browser to use to open the pull requests, default is `xdg-open`.\n',
    'author': 'Stéphane Brunner',
    'author_email': 'stephane.brunner@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sbrunner/multi-repo-automation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
