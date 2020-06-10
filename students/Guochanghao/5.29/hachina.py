DOMAIN = "hachina"
def setup(hass, config):
    attr = {"icon": "mdi:yin-yang",
            "friendly_name": "LED灯",
            "slogon": "积木构建智慧空间！"}
    hass.states.set("hachina.hello_world", "太棒了！", attributes=attr)
    return True