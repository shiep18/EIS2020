import logging

DOMAIN = "hachina"
ENTITYID = DOMAIN + ".hello_world"

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    attr = {"icon": "mdi:yin-yang",
            "frendly_name": "欢迎来到电大！",
            "slogon": "积木构建智慧空间！"}
    hass.states.set(ENTITYID, "Perfect！",attributes=attr)

    def change_state(call):
        """change_state函数切换改变实体的状态."""
        # 记录info级别的日志
        _LOGGER.info("hachina's change_state service is called.")
 
        # 切换改变状态值
        if hass.states.get(ENTITYID).state == 'Perfect！':
            hass.states.set(ENTITYID, 'bad', attributes=attr)
        else:
            hass.states.set(ENTITYID, 'Perfect！', attributes=attr)
    
    # 注册服务hachina.change_state
    hass.services.register(DOMAIN, 'change_state', change_state)
    
    return True

