from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_number
import re
from . import brion_pysin_lib

class CutUp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        if ( not self.settings.get('frag_type') ) or self.settings.get('frag_type') == 'None':
            self.settings['frag_type'] = 'word';
        if ( not self.settings.get('min_chunk') ) or self.settings.get('min_chunk') == 'None':
            self.settings['min_chunk'] = 1
        if ( not self.settings.get('max_chunk') ) or self.settings.get('max_chunk') == 'None':
            self.settings['max_chunk'] = 2
        if ( not self.settings.get('randomness') ) or self.settings.get('randomness') == 'None':
            self.settings['randomness'] = 75

    @intent_handler(IntentBuilder("").require('Set'))
    def handle_pysin_brion_set(self, message):
        possible_setting = message.data.get('Set')
        resp = self.get_response('ask.set.what.value', data={'setting':possible_setting})
        if not resp:
           return
        value = extract_number( resp, ordinals=True ) 
        self.settings[possible_setting] = value
        self.speak( 'set %s to %d' % ( possible_setting, value ) )

    @intent_handler(IntentBuilder("").require("Words"))
    def handle_pysin_brion(self, message):
        utterance = message.data.get('utterance')
        cutup = brion_pysin_lib.traditional_cutup( message.data.get('Words'), self.settings['frag_type'], self.settings['min_chunk'], self.settings['max_chunk'], self.settings['randomness'] )
        self.speak(cutup.strip())

def create_skill():
    return CutUp()

