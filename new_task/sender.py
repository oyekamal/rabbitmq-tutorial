import pika,sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='amqp://guest:**@localhost:5672//'))
channel = connection.channel()

channel.queue_declare(queue='hello')
message = ' '.join(sys.argv[1:]) or "Hello World!"
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body=message)
print(" [x] Sent %r" % message)
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body=f'{i} message'+"."*i)    
# channel.basic_publish(exchange='', routing_key='hello', body=message)
# print(" [x] Sent 'Hello World!'")
connection.close()