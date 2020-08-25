from mycroft import MycroftSkill, intent_file_handler


class Lights(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lights.intent')
    def handle_lights(self, message):
        self.speak_dialog('lights')


def create_skill():
    return Lights()

