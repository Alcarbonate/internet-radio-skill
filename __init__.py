from mycroft import MycroftSkill, intent_file_handler


class InternetRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.internet.intent')
    def handle_radio_internet(self, message):
        radio_name = message.data.get('radio_name')

        self.speak_dialog('radio.internet', data={
            'radio_name': radio_name
        })


def create_skill():
    return InternetRadio()

