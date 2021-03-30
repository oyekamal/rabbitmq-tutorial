import pika, sys, os
import ast
import base64

class RabbitMqReceiver(object):
    def __init__(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='hello')
        
    # def callback(self,ch, method, properties, body):
    #     print(" [x] Received %r" % body)
    
    def callback(self,ch, method, properties, body):
        # print(" [x] Received %r" % body)
        print(len(body[2:-1]))
        print(body[2:-1])
        print("callback")
        fh = open("imageToSave.png", "wb")
        fh.write(body[2:-1].decode('base64'))
        fh.close() 
        # try:
        #     payload = body.decode('utf-8')
        #     payload = ast.literal_eval(payload)
        #     with open("received.png", "wb") as f:
        #         f.write(payload)
        #         print("working..")
        # except Exception as e:
        #     print(e)
        
        
    def startserver(self):
        self._channel.basic_consume(queue='hello', on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self._channel.start_consuming()
            
        
                            
                                    

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='hello')
# ast.literal_eval(
#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body)

#     channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

if __name__ == '__main__':
    try:
        # main()
        server = RabbitMqReceiver()
        server.startserver()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)