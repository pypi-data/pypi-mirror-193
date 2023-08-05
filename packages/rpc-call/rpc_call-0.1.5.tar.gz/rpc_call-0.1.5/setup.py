# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpc_call']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=8.3.0,<9.0.0',
 'loguru>=0.6.0,<0.7.0',
 'orjson>=3.8.5,<4.0.0',
 'pika>=1.3.1,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'simplejson>=3.18.1,<4.0.0']

entry_points = \
{'console_scripts': ['client = tests.simple_client:run',
                     'server = tests.simple_server:run']}

setup_kwargs = {
    'name': 'rpc-call',
    'version': '0.1.5',
    'description': '',
    'long_description': '> **Note:**\n> The main idea of the project is based on RabbitMQ RPC, so RabbitMQ must be installed. Please keep it mind.\n\n### Get started\n\n#### *Simple RPC client using FastAPI*\n#### **`client.py`**\n\n```python\nimport asyncio\nfrom fastapi import FastAPI, Depends, status\nfrom rpc_call.async_client import RPCClient\nfrom rpc_call.types import Task, TaskResult\n\napp = FastAPI()\n\nasync def rpc_connection() -> RPCClient:\n    return await RPCClient(\n        amqp_dsn = "amqp://<client>:<passwd>@<host>:<port>/<vhost>",\n        queue_name = "<RabbitMQQueueName>"\n    ).connect()\n\n@app.post("/RPCEndpoint", response_model=TaskResult)\nasync def read_users(task: Task, rpc_conn: RPCClient = Depends(rpc_connection)) -> TaskResult:\n    task_result = await rpc_conn.call(task)\n    return task_result\n```\n```bash\n$ uvicorn client:app --host 0.0.0.0 --port 8000 --reload\n```\n\n#### *Simple RPC server*\n\n#### **`server.py`**\n\n```python\nfrom rpc_call.server import RPCServer\n\nclass CallbackHandler:\n    def test_func(self, arg: str) -> str:\n        return f"test_func(\'{arg}\') call result"\n\nif __name__ == "__main__":\n    RPCServer(\n        amqp_dsn = "amqp://<client>:<passwd>@<host>:<port>/<vhost>",\n        queue_name = "<RabbitMQQueueName>",\n        callback_handler = CallbackHandler\n    )\n```\n```shell\n$ python server.py\n```\n\n### Usage\n\n```bash\ncurl -X \'POST\' \\\n  \'http://127.0.0.1:8000/RPCEndpoint\' \\\n  -H \'accept: application/json\' \\\n  -H \'Content-Type: application/json\' \\\n  -d \'{\n  "procedure": "test_func",\n  "kwargs": {"arg": "Hello world!"}\n}\'\n```\nAnd the response will be:\n```json\n{\n  "status_code": 200,\n  "result": {\n    "test_func": "test_func(\'Hello world!\') call result"\n  }\n}\n```\n\n---\nSo now, with this elegant and simple library, you can call your code remotely! 👏\nGood luck! 😉\n\n\n',
    'author': 'Artyom Syssolov',
    'author_email': 'artyom.syssolov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
