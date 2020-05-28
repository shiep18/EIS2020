import logging
DOMAIN = "hachina3"
ENTITYID = DOMAIN + ".hello_world"

_LOGGER = logging.getLogger(__name__)

def setup(hass,config):
    attr = {"icon": "mdi:yin-yang",
            "friendly_name":"迎接新世界",
            "slogon": "积木构建智慧空间！"}
    hass.states.set(DOMAIN+".hello_world","太棒了!",attributes=attr)

    def change_state(call):
        _LOGGER.info("hachina's change_state service is called.")

        if hass.states.get(ENTITYID).state=='ON':
            hass.states.set(ENTITYID,'OFF',attributes=attr)
        else:
            hass.states.set(ENTITYID,'ON',attributes=attr)

    hass.services.register(DOMAIN,'change_state',change_state)
    return True
