try:
    import pika
    import base64 
except:
    print("modules not install")
    
    
class RabbitMqConfigure(object):
    def __init__(self, queue='hello', host='localhost',routing_key='hello', exchange=''):
        self.host = host
        self.queue = queue
        self.routing_key = routing_key
        self.exchange = exchange
        
class RabbitMq(object):
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel =  self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)
        
    def publish(self, payload={}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routing_key, body=str(payload))
        print("Published.....")
        self._connection.close()

class Image(object):
    __slots__ = ['filename']
    
    def __init__(self, filename):
        self.filename = filename
        
    @property
    def get(self):
        with open(self.filename, 'rb') as f:
            data = f.read()
        return data


if __name__ == "__main__":
    server = RabbitMqConfigure(queue='hello', host='localhost',routing_key='hello', exchange='')
    rabbitmq = RabbitMq(server)
    # image =Image(filename='/home/oye/Documents/rabbitmq_tutorial/class_base_code_send_image/image.png')
    with open("/home/oye/Documents/rabbitmq_tutorial/class_base_code_send_image/image.png", "rb") as image2string: 
        converted_string = base64.b64encode(image2string.read()) 
# print(converted_string) 
    print(len(converted_string))
    rabbitmq.publish(converted_string)
    

# for i in range(10):
#     channel.basic_publish(exchange='', routing_key='hello', body=f'this time  {i}')    
# channel.basic_publish(exchange='', routing_key='hello', body='my name is kamal')
# print(" [x] Sent 'Hello World!'")
# connection.close()