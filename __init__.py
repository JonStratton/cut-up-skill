from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import re
from . import brion_pysin_lib

class CutUp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require("CutUp").require("Words"))
    def handle_pysin_brion(self, message):
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['CutUp'], '', utterance)
        cutup = brion_pysin_lib.traditional_cutup( repeat, 'word', 1, 1, 100 )
        self.speak(cutup.strip())

def create_skill():
    return CutUp()

