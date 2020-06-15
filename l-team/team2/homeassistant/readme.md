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
* 配置完毕后即可通过外网访问服务器地址。  
* 第一次访问输入用户名密码创建用户。

### 4. 日历应用安装
* 日历应用到[此处](https://github.com/nextcloud/calendar/releases)下载，目前为2.0.3版本。
* 压缩包放到服务器的`var/snap/nextcloud/21521/nextcloud/extra-apps/`目录下(可用Win-SCP传输文件)。
* 运行`tar -xvf calendar.tar.gz`解压，完成后将压缩包删除。
* 登陆网站，点击用户头像，选择`+应用`,找到calendar应用添加。
