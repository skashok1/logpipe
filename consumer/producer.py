from logpipe import Producer
joe = Person.objects.create(first_name='Joe', last_name='Schmoe')
producer = Producer('people', PersonSerializer)
producer.send(joe)



