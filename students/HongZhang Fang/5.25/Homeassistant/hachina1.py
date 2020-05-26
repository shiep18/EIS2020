DOMAIN = "hachina"
def setup(hass,config):
    attr={"icon": "mdi:yin-yang",
          "friendly_name": "上海电力大学",
          "slogon": "积木构建智慧空间!"}
    hass.states.set(DOMAIN+".hello_world","fantastic",attributes=attr)
    return True      