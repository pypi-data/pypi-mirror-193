# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sekoia_automation',
 'sekoia_automation.scripts',
 'sekoia_automation.scripts.documentation',
 'sekoia_automation.scripts.new_module.template.{{cookiecutter.module_dir}}',
 'sekoia_automation.scripts.new_module.template.{{cookiecutter.module_dir}}.tests',
 'sekoia_automation.scripts.new_module.template.{{cookiecutter.module_dir}}.{{cookiecutter.module_name.lower().replace(" '
 '", "_")}}_modules']

package_data = \
{'': ['*'],
 'sekoia_automation.scripts': ['new_module/template/*'],
 'sekoia_automation.scripts.documentation': ['templates/*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'boto3>=1.26,<2.0',
 'cookiecutter>=2.1,<3.0',
 'orjson>=3.8,<4.0',
 'pydantic>=1.10,<2.0',
 'python-slugify>=5.0.2,<6.0.0',
 'requests>=2.25,<3.0',
 's3path>=0.4,<0.5',
 'sentry-sdk',
 'tenacity',
 'typer[all]>=0.7,<0.8']

entry_points = \
{'console_scripts': ['sekoia-automation = sekoia_automation.cli:app']}

setup_kwargs = {
    'name': 'sekoia-automation-sdk',
    'version': '1.0',
    'description': 'SDK to create SEKOIA.IO playbook modules',
    'long_description': '# SEKOIA.IO Automation Python SDK\n\nSDK to create SEKOIA.IO playbook modules.\n\nModules can define:\n\n* Triggers: daemons that create events that will start a playbook run\n* Actions: short-lived programs that constitute the main playbook nodes. They take arguments and produce a result.\n\n## Create a trigger\n\nHere is how you could define a very basic trigger:\n\n```python\nfrom sekoia_automation.module import Module\nfrom sekoia_automation.trigger import Trigger\n\n\nclass MyTrigger(Trigger):\n    def run(self):\n        while True:\n            # Do some stuff\n            self.send_event(\'event_name\', {\'somekey\': \'somevalue\'})\n            # Maybe wait some time\n\n\nif __name__ == "__main__":\n    module = Module()\n\n    module.register(MyTrigger)\n    module.run()\n```\n\nYou can access the Trigger\'s configuration with `self.configuration` and the module configuration with `self.module.configuration`.\n\n### Attach files to an event\n\nYou can attach files to an event so that these files are available to the playbook runs.\n\nHere is how you could crete a file that should be available to the playbook run:\n\n```python\nimport os\n\nfrom sekoia_automation import constants\nfrom sekoia_automation.trigger import Trigger\n\n\nclass MyTrigger(Trigger):\n    def run(self):\n        while True:\n            # Create a directory and a file\n            directory_name = "test_dir"\n            dirpath = os.path.join(constants.DATA_STORAGE, directory_name)\n            os.makedirs(dirpath)\n\n            with open(os.path.join(dirpath, "test.txt") "w") as f:\n                f.write("Hello !")\n\n            # Attach the file to the event\n            self.send_event(\'event_name\', {\'file_path\': \'test.txt\'}, directory_name)\n\n            # Maybe wait some time\n```\n\nPlease note that:\n\n* `send_event`\'s third argument should be the path of a directory, relative to `constants.DATA_STORAGE`\n* The directory will be the root of the playbook run\'s storage ("test.txt" will exist, not "test_dir/test.txt")\n* You can ask the SDK to automatically remove the directory after it was copied with `remove_directory=True`\n* You should always do `from sekoia_automation import constants` and use `constants.DATA_STORAGE` so that it is easy to mock\n\nWhen attaching a single file to a playbook run, you can use the `write` function to create the file:\n\n```python\nfrom sekoia_automation.storage import write\nfrom sekoia_automation.trigger import Trigger\n\n\nclass MyTrigger(Trigger):\n    def run(self):\n        while True:\n            # Simple creation of a file\n            filepath = write(\'test.txt\', {\'event\': \'data\'})\n\n            # Attach the file to the event\n            self.send_event(\'event_name\', {\'file_path\': os.path.basename(filepath)},\n                            os.path.dirname(directory_name))\n\n            # Maybe wait some time\n```\n\n### Persisting data to disk\n\nMost of the time, triggers have to maintain some state do to their work properly (such as a cursor).\nIn order to make sure that this data survives a reboot of the Trigger (which can happen with no reason),\nit is useful to persist it to the trigger\'s storage.\n\nWhen the manipulated data is JSON serializable, it is recommended to use the `PersistentJSON` class to do\nso (instead of `shelve`). Used as a context manager, this class will make sure the python dict is properly\nsynchronised:\n\n```python\nfrom sekoia_automation.trigger import Trigger\nfrom sekoia_automation.storage import PersistentJSON\n\n\nclass MyTrigger(Trigger):\n    def run(self):\n        while True:\n            # Read and update state\n            with PersistentJSON(\'cache.json\') as cache:\n        # Use cache as you would use a normal python dict\n```\n\n## Create an action\n\nHere is how you could define a very basic action that simply adds its arguments as result:\n\n```python\nfrom sekoia_automation.module import Module\nfrom sekoia_automation.action import Action\n\n\nclass MyAction(Action):\n    def run(self, arguments):\n        return arguments  # Return value should be a JSON serializable dict\n\n\nif __name__ == "__main__":\n    module = Module()\n\n    module.register(MyAction)\n    module.run()\n```\n\nThere are a few more things you can do within an Action:\n\n* Access the Module\'s configuration with `self.module.configuration`\n* Add log messages with `self.log(\'message\', \'level\')`\n* Activate an output branch with `self.set_output(\'malicious\')` or explicitely disable another with `self.set_output(\'benign\', False)`\n* Raise an error with `self.error(\'error message\')`. Note that raised exceptions that are not catched by your code will be automatically handled by the SDK\n\n### Working with files\n\nActions can read and write files the same way a Trigger can:\n\n```python\nfrom sekoia_automation import constants\n\nfilepath = os.path.join(constants.DATA_STORAGE, "test.txt")\n```\n\nIt is a common pattern to accept JSON arguments values directly or inside a file. The SDK provides an helper to easily read such arguments:\n\n```python\nclass MyAction(Action):\n\n    def run(self, arguments):\n        test = self.json_argument("test", arguments)\n\n        # Do somehting with test\n```\n\nThe value will automatically be fetched from `test` if present, or read from the file at `test_path`.\n\nThe SDK also provides an helper to do the opposite with results:\n\n```python\nclass MyAction(Action):\n\n    def run(self, arguments):\n        return self.json_result("test", {"some": "value"})\n```\n\nThis will create a dict with `test_path` by default or `test` if the last argument was passed directly.\n\n## Same Docker Image for several items\n\nIn most cases, it makes sense to define several triggers and / or actions sharing the same code and the same docker image.\n\nIn this case, here is how you should define the main:\n\n```python\nif __name__ == "__main__":\n    module = Module()\n\n    module.register(Trigger1, "command_trigger1")\n    module.register(Trigger2, "command_trigger2")\n    module.register(Action1, "command_action1")\n    module.register(Action2, "command_action2")\n    module.run()\n```\n\nThe corresponding commands need to be correctly set in the manifests as "docker_parameters".\n\n## Use with Pydantic\n\nIt is recommended to use Pydantic to develop new modules. This should ease development.\n\n### Module Configuration\n\nA pydantic model can be used as `self.module.configuration` by adding type hints:\n\n```python\nclass MyConfigurationModel(BaseModel):\n    field: str\n\nclass MyModule(Module):\n    configuration: MyConfiguration\n\nclass MyAction(Action):\n    module: MyModule\n```\n\n### Triggers\n\nThe Trigger configuration can also be a pydantic model by adding a type hint:\n\n```python\nclass MyTrigger(Trigger):\n    configuration: MyConfigurationModel\n```\n\nYou can also specify the model of created events by setting the `results_model` attribute:\n\n```python\nclass Event(BaseModel):\n    field: str = "value"\n\nclass MyTrigger(Trigger):\n    results_model = Event\n```\n\n### Actions\n\nYou can use a pydantic model as action arguments by adding a type hint:\n\n```python\nclass ActionArguments(BaseModel):\n    field: str = "value"\n\nclass MyAction(Action):\n    def run(self, arguments: ActionArguments):\n        ...\n```\n\nThe model of results can also be specified by setting the `results_model` attribute:\n\n```python\nclass Results(BaseModel):\n    field: str = "value"\n\nclass MyAction(action):\n    results_model = Results\n```\n\n### Automatically generating manifests\n\nWhen using pydantic models to describe configurations, arguments and results, manifests\ncan be automatically generated:\n\n```\n$ poetry run sekoia-automation generate-files\n```\n\nThis will do the following:\n\n* Generate `main.py`\n* Generate a manifest for each action\n* Generate a manifest for each trigger\n* Update the module\'s manifest\n\nFor better results, it is recommended to set the `name` and `description` attributes in Actions\nand Triggers.',
    'author': 'SEKOIA.IO',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://sekoia.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
