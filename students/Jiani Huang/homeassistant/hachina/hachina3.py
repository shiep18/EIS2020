DOMAIN = "hachina"
def setup(hass, config):
    attr = {"icon": "mdi:yin-yang",
            "friendly_name": "迎接新世界",
            "slogon": "积木构建智慧空间！"}
    hass.states.set(DOMAIN+".hello_world", "on", attributes=attr)
    return True
