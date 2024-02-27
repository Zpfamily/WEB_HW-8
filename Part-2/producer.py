import pika
from faker import Faker
from models import Contact
from mongoengine import connect


def generate_fake_contacts(num_contacts):
    fake = Faker()
    contacts = []
    for _ in range(num_contacts):
        name = fake.name()
        email = fake.email()
        contact = Contact(name=name, email=email)
        contacts.append(contact)
    return contacts


def publish_contact_ids():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='contact_ids')

    # Generate fake contacts
    fake_contacts = generate_fake_contacts(10)

    # Save contacts to MongoDB and publish their IDs
    for contact in fake_contacts:
        contact.save()
        channel.basic_publish(exchange='', routing_key='contact_ids', body=str(contact.id))

    connection.close()


if __name__ == '__main__':
    connect(host="mongodb+srv://pkzpfamily:kursorBe09@vassabi.7ihkasp.mongodb.net?retryWrites=true&w=majority&ssl=true")
    Contact.drop_collection()
    publish_contact_ids()

