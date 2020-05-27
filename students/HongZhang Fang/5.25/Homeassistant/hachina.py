def setup(hass, config):
    hass.states.set("hachina.hello_world", "太棒了！")
    return True