import pika
from models import Contact
from mongoengine import connect


def send_email(contact_id):
    # Це функція-заглушка, яка імітує відправку електронного листа
    print(f"Відправлено листа до контакту з ID: {contact_id}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact:
        print(f"Processing contact {contact_id}")
        send_email(contact_id)
        contact.message_sent = True
        contact.save()
        print(f"Email sent for contact {contact_id}")
    else:
        print(f"Contact with id {contact_id} not found")


def consume_contact_ids():
    # Підключаємося до RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='contact_ids')
    channel.basic_consume(queue='contact_ids', on_message_callback=callback, auto_ack=True)
    print(' [*] Очікування повідомлень. Щоб вийти, натисніть CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    connect(host="mongodb+srv://pkzpfamily:kursorBe09@vassabi.7ihkasp.mongodb.net?retryWrites=true&w=majority&ssl=true")
    consume_contact_ids()
