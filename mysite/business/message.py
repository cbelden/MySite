from flask.ext.mail import Message
from mysite import mail, app


def send_email(form):
    # Get form info
    boss_name = form['name']
    boss_email = form['email']
    company = form['company']
    words_of_wisdom = form['message']
    phone_num = form['number']

    # Get my info
    my_email = app.config['MAIL_USERNAME']

    # Compose message - to myself
    title = 'Contact from MySite - %s' % boss_name
    msg_to_me = Message(title, sender=my_email, recipients=[my_email])
    msg_to_me.body = """
    From: %s
    Company: %s
    Phone: %s

    Message:
    %s
    """ % (boss_name, company, phone_num, words_of_wisdom)

    # Compose Message - thank you
    msg_to_boss = Message('calbelden.com - Thank you!', sender=my_email, recipients=[boss_email])
    msg_to_boss.body = """
    Thank you %s for your message, I will respond shortly!

    Best,
    Cal
    """ % boss_name.split(' ')[0].capitalize()

    # Send messages
    mail.send(msg_to_me)
    mail.send(msg_to_boss)
