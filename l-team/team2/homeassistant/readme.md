# HomeAssistant智能课表
<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>  
<p align="center">
<a href="#"><img alt="Python3" src="https://img.shields.io/badge/Python-3-blue.svg?style=flat-square"></a>
<a href="#"><img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-18.04-orange"></a>
<a href="#"><img alt="HomeAssistant" src="https://img.shields.io/badge/HomeAssistant-0.109.6-blue"></a>
</p> 

## 一、准备材料、环境要求
   
### 1. 一台Ubuntu系统的服务器
   
* 可以到[阿里云](https://developer.aliyun.com/adc/student/)白嫖一台。
* 虚拟机亦可(未实验)。
* Ubuntu版本:18.04。
* 服务器需进行简单部署。
### 2. Windows上部署HomeAssistant
   
* 版本为0.109.6。
  
  
## 二、搭建日历服务器
### 1. 登录服务器
    ssh root@xx.xxx.xx.xxx
    
### 2. 安装next cloud服务
#### 指令：
>apt-get update  
apt-get install snap  
apt-get install snapd  
snap install nextcloud  

### 3. 网站配置
* 给网站指定端口，这里选择80端口  
>snap set nextcloud ports.http=80。  
* 如果是阿里云或腾讯云服务器，需要配置[安全组规则](https://yq.aliyun.com/articles/713259)开放端口，然后重启服务器。  
* 配置完毕后即可通过外网访问服务器端口地址。  
* 第一次访问输入用户名密码创建用户。

### 4. 日历应用安装
* 日历应用到[此处](https://github.com/nextcloud/calendar/releases)下载，目前为2.0.3版本。
* 压缩包放到服务器的`var/snap/nextcloud/21521/nextcloud/extra-apps/`目录下(可用Win-SCP传输文件)。
* 运行`tar -xvf calendar.tar.gz`解压，完成后将压缩包删除。
* 登陆网站，点击用户头像，选择`+应用`,找到calendar应用添加。

## 三、 HomeAssistant配置
* 网站中切换到日历应用界面，点击左下方设置与导入，复制主要的CalDAV地址。
* 在configuration.yaml中添加日历组件([示例](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/configuration.yaml))。
```
    calendar:
  - platform: caldav  
    url: !secret address        # CalDAV地址 
    username: !secret username  # 网站用户名
    password: !secret password  # 网站用户密码
    custom_calendars:
      - name: course               # HA中自定的日历名字
        calendar: class            # next cloud中日历的名字
        search: '.*'               # 寻找匹配的事件名，.*为全部事件
```
* 在automations.yaml中添加自动化([示例](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/automations.yaml))。
```
- id: '1591970192885'
  alias: bell
  description: ''
  trigger: 
    platform: template
    value_template: "{% if is_state_attr('calendar.class_course', 'offset_reached', true) %}true{% endif %}"
  condition: []
  action:
  - data_template:
      entity_id: media_player.kodi
      message: 上课10分钟前提醒。课名{{states.calendar.class_course.attributes.message}}, 地点：{{states.calendar.class_course.attributes.location}}, {{states.calendar.class_course.attributes.description}}
    service: tts.baidu_say
  - data: {}
    entity_id: automation.message
    service: automation.trigger
  initial_state: true
- id: '1591973317613'
  alias: message
  description: ''
  trigger: []
  condition: []
  action:
  - data:
      message: 上课10分钟前提醒。课名：{{states.calendar.class_course.attributes.message}}, 地点：{{states.calendar.class_course.attributes.location}}, {{states.calendar.class_course.attributes.description}}
      target:
      - !secret phonenumber     # 接受短信的电话
    service: notify.my_twilio_sms
```
## 四、 爬取课表
* [table.py](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/table2ics/table.py)中修改学号和密码。
* 运行后自动爬取，完成生成[table.txt](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/table2ics/table.txt)。
* 运行[ics.py](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/table2ics/ics.py)生成[table.ics](https://github.com/shiep18/EIS2020/blob/master/l-team/team2/homeassistant/table2ics/table.ics)。
* 在网站中导入table.ics到目标日历中。
* 启动HomeAssistant。
