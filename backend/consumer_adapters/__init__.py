from .ConstantValueConsumerAdapter import ConstantValueConsumerAdapter
from .ModbusConsumerAdapter import ModbusConsumerAdapter
from .FakeControllableConsumerAdapter import FakeControllableConsumerAdapter
from .VzugHomeConsumerAdapter import VzugHomeConsumerAdapter
from .SGReadyConsumerAdapter import SGReadyConsumerAdapter
from .InfluxDbConsumerAdapter import InfluxDbConsumerAdapter

CONSUMER_TYPE_MAPPING = {
    'constant': ConstantValueConsumerAdapter,
    'modbus': ModbusConsumerAdapter,
    'vzugHome': VzugHomeConsumerAdapter,
    'fakeControllable': FakeControllableConsumerAdapter,
    'sgReady': SGReadyConsumerAdapter,
    'influxDb': InfluxDbConsumerAdapter
}
