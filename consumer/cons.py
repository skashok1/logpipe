consumer = Consumer('people', consumer_timeout_ms=1000)
consumer.register(PersonSerializer)
consumer.run()

# Watch for messages and block forever
# consumer = Consumer('people')
# consumer.register(PersonSerializer)
#consumer.run()