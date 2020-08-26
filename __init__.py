from mycroft import MycroftSkill, intent_handler
import requests

class Lights(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)


	def initialize(self):
		self.register_entity_file('state.entity')
		self.register_entity_file('num.entity')

	@intent_handler('lights.intent')
	def handle_lights(self, message):
		state = message.data.get('state')
		num = message.data.get('num')

		if(num == 'one'):
			num = '1'
		if(num == 'two'):
			num = '2'

		if( num is None or int(num) == 1):
			if(state is None):
				self.log.info("toggle light one")
				toggle_request('1')
				#toggle light one
			else:
				self.log.info("switch light one " + state)
				light_request(state, '1') 
				#turn light one {state}

		if( num is None or int(num) == 2):
			if(state is None):
				toggle_request('2')
				self.log.info("toggle light two")
				#toggle light two
			else:
				light_request(state, '2')
				self.log.info("switch light two " + state)
				#turn light two {state}

		self.speak_dialog('lights.dialog')


def create_skill():
	return Lights()

def light_request(state, light):
	r = requests.post('http://localhost/lights?light={}&state={}'.format(light, state))
	return r

def toggle_request(light):
	r = requests.post('http://localhost/lights/toggle?light={}'.format(light))
	return r
