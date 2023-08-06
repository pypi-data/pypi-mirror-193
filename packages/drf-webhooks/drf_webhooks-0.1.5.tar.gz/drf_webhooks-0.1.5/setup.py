# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_webhooks', 'drf_webhooks.tests', 'drf_webhooks.tests.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1,<5.0',
 'celery>=5.2,<6.0',
 'djangorestframework-xml>=2.0,<3.0',
 'djangorestframework>=3.14,<4.0',
 'httpx>=0.23,<0.24',
 'inflection>=0.5,<0.6',
 'pendulum>=2.1,<3.0',
 'pytimeparse>=1.1,<2.0',
 'xmltodict>=0.13,<0.14']

setup_kwargs = {
    'name': 'drf-webhooks',
    'version': '0.1.5',
    'description': 'Setup webhooks using existing DRF Serializers',
    'long_description': '# Django Rest Framework - Webhooks\n**Configurable webhooks based on DRF Serializers**\n\n## Goals:\n- [x] Use existing DRF Serializers from REST API to serialize data in webhooks\n    - [x] Consistent data formatting\n    - [x] Reusable OpenAPI schemas\n- [x] Configurable webhooks that simply work *(by way of django signals magic)* without the developer having to keep track of where to trigger them\n    - [x] Still allow for "manual" triggering of webhooks\n        - This is useful because signals aren\'t always triggered.\n        - For example: `QuerySet.update` does not trigger signals\n- [x] Disable webhooks using context managers\n    - This can be useful when syncing large chunks of data\n    - or with a duplex sync (when two systems sync with each other) to avoid endless loops\n- [x] **Webhook Signal Session**\n    - [x] A context manager gathers all models signals and at the end of the session only triggers the resulting webhooks\n        - [x] If a model instance is both `created` and `deleted` within the session, then no webhook is sent for that model instance\n        - [x] If a model instance is `created` and then also `updated` within the session, then a `created` event is sent with the data from the last `updated` signal. Only one webhook even is sent\n        - [x] If a models instance is `updated` multiple times within the session, then only one webhook event is sent.\n    - [x] Middleware wraps each request in **Webhook Signal Session** context\n        - **NOTE:** The developer will have to call the context manager in code that runs outside of requests (for example in celery tasks) manually\n- [ ] Automatically determine which nested models need to be monitored for changes. Currently this must be done by setting `signal_model_instance_base_getters`\n\n\n## Example:\n\n```python\nfrom auth.models import User\nfrom core.models import Address, Landlord, RentalUnit, Tenant\nfrom drf_webhooks.utils import ModelSerializerWebhook\n\n\nclass DepositSerializerWebhook(ModelSerializerWebhook):\n    serializer_class = DepositSerializer\n    base_name = \'core.deposit\'\n\n    @staticmethod\n    def get_address_instance_base(address):\n        tenants = address.tenant_set.all()\n        for tenant in tenants:\n            yield from tenant.deposits.all()\n\n        unit = getattr(address, "unit", None)\n        if unit:\n            yield from address.unit.deposits.all()\n\n    # Monitor changes to data in nested serializers:\n    signal_model_instance_base_getters = {\n        Tenant: lambda x: x.deposits.all(),\n        User: lambda x: x.tenant.deposits.all(),\n        RentalUnit: lambda x: x.deposits.all(),\n        Address: get_address_instance_base,\n        Landlord: lambda x: [],  # Not important for this hook\n    }\n\n...\n\nclass DepositSerializer(serializers.ModelSerializer):\n    tenant = TenantSerializer(read_only=True)\n    landlord = LandlordSerializer(read_only=True)\n    unit = RentalUnitSerializer(read_only=True)\n\n    class Meta:\n        model = Deposit\n        fields = [\n            \'id\',\n            \'created\',\n            \'tenant\',\n            \'landlord\',\n            \'unit\',\n            \'date_from\',\n            \'date_to\',\n            \'security_deposit_amount\',\n            \'last_months_rent_amount\',\n            \'fee_rate\',\n            \'fee_amount\',\n            \'status\',\n            \'initiator\',\n        ]\n\n...\n```\n',
    'author': 'Arnar Yngvason',
    'author_email': 'arnar@reon.is',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/demux/drf-webhooks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
