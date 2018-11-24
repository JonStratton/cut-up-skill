from mycroft import MycroftSkill, intent_file_handler


class CutUp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('up.cut.intent')
    def handle_up_cut(self, message):
        self.speak_dialog('up.cut')


def create_skill():
    return CutUp()

