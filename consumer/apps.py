from django.apps import AppConfig
from logpipe import Consumer, register_consumer

class ConsumerConfig(AppConfig):
    name = 'consumer'

@register_consumer
def build_person_consumer():
    consumer = Consumer('people')
    consumer.register(PersonSerializer)
    return consumer
