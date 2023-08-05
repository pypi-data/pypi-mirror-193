# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zamm',
 'zamm.actions',
 'zamm.actions.edit_file',
 'zamm.actions.note',
 'zamm.actions.use_terminal',
 'zamm.agents',
 'zamm.agents.tools',
 'zamm.chains',
 'zamm.chains.general',
 'zamm.chains.general.choice',
 'zamm.llms',
 'zamm.prompts']

package_data = \
{'': ['*'], 'zamm': ['resources/*', 'resources/tutorials/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'langchain-visualizer>=0.0.10,<0.0.11',
 'openai>=0.26.4,<0.27.0',
 'pexpect>=4.8.0,<5.0.0',
 'pyyaml>=6.0,<7.0',
 'simple-term-menu>=1.6.1,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'ulid>=1.1,<2.0',
 'vcr-langchain>=0.0.13,<0.0.14']

entry_points = \
{'console_scripts': ['zamm = zamm.cli:app']}

setup_kwargs = {
    'name': 'zamm',
    'version': '0.0.1',
    'description': 'General automation driver',
    'long_description': '# ZAMM\n\nTeach GPT how to do something, and have it do it for you afterwards. This is good for boring but straightforward tasks that you haven\'t gotten around to writing a proper script to automate.\n\nWe are entering a time when our target audiences may include machines as well as humans. As such, this tool will generate tutorials that you can edit to make pleasant for both humans and LLMs alike to read.\n\n**This is an experimental tool, and has only been run on WSL Ubuntu so far.** It seems to work ok on the specific examples below. YMMV. Please feel free to add issues or PRs.\n\n## Quickstart\n\nTeach GPT to do something:\n\n```bash\nzamm teach\n```\n\nYou will be roleplaying the LLM. Sessions are recorded in case a crash happens, or if you want to change something up. On Linux, sessions are saved to `~/.local/share/zamm/sessions/`. To continue from a previous session, run:\n\n```bash\nzamm teach --session-recording <path-to-recording>\n```\n\nOnce a session finishes, you can use the newly generated tutorial file to do something. For example, to run the recording I made at [zamm/resources/tutorials/hello.md](zamm/resources/tutorials/hello.md):\n\n```bash\nzamm execute --task \'Write a script goodbye.sh that prints out "Goodbye world". Execute it.\' --documentation zamm/resources/tutorials/hello.md\n```\n\n**Note that GPT successfully generalizes from the tutorial to code in a completely different language based just on the difference in filenames.** Imagine having to manually add that feature to a script!\n\n### Free-styling\n\nYou can also simply tell the LLM to do something without teaching it to do so beforehand. However, this is a lot more brittle. An example of a free-style command that works:\n\n```bash\nzamm execute --task \'Write a script hello.py that prints out "Hello world". Execute it.\'\n```\n',
    'author': 'Amos Jun-yeung Ng',
    'author_email': 'me@amos.ng',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
