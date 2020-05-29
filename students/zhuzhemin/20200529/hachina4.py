
"""
文件名 hachina4.py.
 
演示程序，注册一个服务.
"""
 
# 引入记录日志的库
import logging
 
DOMAIN = "hachina4"
ENTITYID = DOMAIN + ".hello_world"
 
# 在python中，__name__代表模块名字
_LOGGER = logging.getLogger(__name__)
 
 
def setup(hass, config):
    """配置文件加载后，setup被系统调用."""
    attr = {"icon": "mdi:yin-yang",
            "friendly_name": "DOOR!",
            "slogon": "DOOR！", }
    hass.states.set(ENTITYID, 'LOCKED', attributes=attr)
 
    def change_state(call):
        """change_state函数切换改变实体的状态."""
        # 记录info级别的日志
        _LOGGER.info("hachina's change_state service is called.")
        f = open(r"C:\Apache24\htdocs\index2.html",'r')
        a = f.readline()
        # 切换改变状态值
        if hass.states.get(ENTITYID).state == 'LOCKED':
            if a=="2":
                hass.states.set(ENTITYID, 'CLOSED', attributes=attr)
            elif a=="3":
                hass.states.set(ENTITYID, 'OPEN', attributes=attr)
        elif hass.states.get(ENTITYID).state == 'CLOSED':
            if a=="1":
                hass.states.set(ENTITYID, 'LOCKED', attributes=attr)
            elif a=="3":
                hass.states.set(ENTITYID, 'OPEN', attributes=attr)
        elif hass.states.get(ENTITYID).state == 'OPEN':
            if a=="1":
                hass.states.set(ENTITYID, 'LOCKED', attributes=attr)
            elif a=="2":
                hass.states.set(ENTITYID, 'CLOSED', attributes=attr)
 
    # 注册服务hachina.change_state
    hass.services.register(DOMAIN, 'change_state', change_state)
    return True


