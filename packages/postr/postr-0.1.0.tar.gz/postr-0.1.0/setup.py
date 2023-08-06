# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['postr', 'postr.model', 'postr.relay']

package_data = \
{'': ['*']}

install_requires = \
['coincurve>=18.0.0,<19.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'rel>=0.4.7,<0.5.0',
 'socketify>=0.0.5,<0.0.6',
 'websocket-client>=1.4.2,<2.0.0',
 'websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'postr',
    'version': '0.1.0',
    'description': 'Small python nostr client',
    'long_description': '# Postr\nSmall python nostr client library for Python 3.10+\n\n## Installation \n```\npip install postr\n```\n\n## Example\n\n```python\nimport asyncio\nimport postr\n\nasync def controller():\n    user = postr.User()\n    hub = postr.RelayHub()\n    damus = await hub.connect("wss://relay.damus.io")\n    wellorder = await hub.connect("wss://nostr-verified.wellorder.net")\n\n\n    hub.publish(\n        postr.RequestMessage(\n            subscription_id="ABC",\n            filters=postr.Filter(kinds=postr.SetMetadata),\n        )\n    )\n    # \n    hub.publish(\n        postr.EventMessage(event=user.sign(postr.TextNote(content="Hello there!")))\n    )\n\n    # parse messages as they are received\n    while True:\n        match message := await hub.messages.get():\n            case postr.SubscriptionResponse(event=postr.TextNote()):\n                event = message.event\n                log.info(f"TextNote {event.content}")\n            case postr.SubscriptionResponse(event=postr.RecommendServer()):\n                event = message.event\n                known = set(map(lambda x: x.relay, hub.connections))\n                if event.url not in known:\n                    log.info(f"Connecting to \'{event.url}\'")\n                    socket = await hub.connect(event.url)\n            case postr.SubscriptionResponse(event=postr.SetMetadata()):\n                event = message.event\n                log.info(f"Set Metadata: {event.content}")\n            case postr.SubscriptionResponse():\n                event = message.event\n                log.info(f"unknown kind {event.kind}")\n            case postr.EndOfStoredEventsResponse():\n                log.info("Closing subscription at end of stored events")\n                hub.publish(\n                    postr.CloseMessage(subscription_id=message.subscription_id),\n                    connection=message.relay,\n                )\n            case _:\n                log.info("Received something else")\n\n\nif __name__ == "__main__":\n    logging.basicConfig(level=logging.INFO)\n```',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
