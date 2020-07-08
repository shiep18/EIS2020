# 引入记录日志的库
import logging
from mcpi.minecraft import Minecraft
mc=Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("HJN")
DOMAIN = "hachina"
ENTITYID = DOMAIN + ".hello_world"
 
# 在python中，__name__代表模块名字
_LOGGER = logging.getLogger(__name__)
 
 
def setup(hass, config):
    """配置文件加载后，setup被系统调用."""
    attr = {"icon": "mdi:lightbulb",
            "friendly_name": "灯",
            "slogon": "灯", }
    hass.states.set(ENTITYID, 'on', attributes=attr)
 
    def change_state(call):
        """change_state函数切换改变实体的状态."""
        # 记录info级别的日志
        _LOGGER.info("hachina's change_state service is called.")
 
        # 切换改变状态值
        if hass.states.get(ENTITYID).state == 'off':
            hass.states.set(ENTITYID, 'on', attributes=attr)
            mc.setBlocks(46,-3,87,116,-3,139,152)
            mc.setBlock(46,-3,87,0)
            mc.setBlock(46,-3,139,0)
            mc.setBlock(116,-3,87,0)
            mc.setBlock(116,-3,139,0)
        else:
            hass.states.set(ENTITYID, 'off', attributes=attr)
            mc.setBlocks(46,-3,87,116,-3,139,155)
 
    # 注册服务hachina.change_state
    hass.services.register(DOMAIN, 'change_state', change_state)
 
    return True
