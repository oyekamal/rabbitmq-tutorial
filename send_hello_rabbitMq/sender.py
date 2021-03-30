import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body=f'this time  {i}')    
channel.basic_publish(exchange='', routing_key='hello', body='my name is kamal')
print(" [x] Sent 'Hello World!'")
connection.close()