#!/usr/bin/env python2
from hermes_python.hermes import Hermis

MQTT_IP_ADDR = "localhost"
MQTT_PORT    = 1883
MQTT_ADDR    = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):

	sentence = ''




	hermis.publish_end_session(intent_message.message_id, sentence)

with Hermis(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()