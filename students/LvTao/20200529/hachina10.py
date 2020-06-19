import logging
import serial
import time
serial=serial.Serial('COM10',9600,timeout=0.5)

DOMAIN = "hachina10"
ENTITYID = DOMAIN + ".hello_world"

_LOGGER = logging.getLogger(__name__)
def setup(hass,config):
	attr = {"icon":"mdi:yin-yang",
	"friendly_name":"COM10",
	"slogon":"hello",
	}
	while True:
		time.sleep(0.5)
		data=serial.readline()
		if data != '':
			hass.states.set(ENTITYID,"高兴吗",attributes=attr)
		break;
	def change_state(call):
		_LOGGER.info("hachina's change_state service is called.")
		if hass.states.get(ENTITYID).state == "高兴吗":
			hass.states.set(ENTITYID,"开心",attributes=attr)
		else:
			hass.states.set(ENTITYID,"高兴吗",attributes=attr)
	
	hass.services.register(DOMAIN,"change_state",change_state)
	
	return True
