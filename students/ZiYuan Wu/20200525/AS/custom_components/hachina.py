
 
def setup(hass, config):
    """配置文件加载后，setup被系统调用."""
    attr = {"icon": "mdi:yin-yang",
            "friendly_name": "欢迎来到电大",
            "slogon": "积木构建智慧空间！", }
    hass.states.set(DOMAIN+".hello_world","Great！",attributes=attr)
 
    return True