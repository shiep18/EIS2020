由于程序的配套文件过大，此处只上传ppt及核心代码。完整程序请在百度云中下载  

.ha替换成C盘中的ha配置文件夹，其中，所有hachina.py之类的文件，涉及到txt存储路径的请改成自己的路径  

在网易云文件夹路径下打开cmd，输入指令node app.js  

在wamp里创建名为expressbos的数据库，然后把expressbos压缩包里的几个sql导入进去 

smart文件夹中，读取txt的路径同样要修改，没有的库请自行pip安装。 
将所有  
mc=minecraft.Minecraft.create('47.100.46.95',4784)  
entityId= mc.getPlayerEntityId("W")
pos=mc.entity.getTilePos(entityId)  
改为  
mc=Minecraft.create()  
pos=mc.player.getTilePos()  

其中使用人脸识别时，要pip install scikit-image，并用pip安装文件夹内的whl包。打开人脸识别文件夹，按照其中readme操作为自己建模。  

启动我的世界要打开minecraft_m3_all\Bukkit\start.bat，然后打开minecraft_m3_all\HMCL-3.2.149.exe。可能游戏会打不开，笔者记不清安装流程了，请自行百度。minecraft_m3_all文件夹内备齐了所需文件。  

打开后选择多人游戏，添加服务器，地址为localhost，能打开即成功。  

最后在数据库，ha，网易云音乐api，start.bat都打开后，进入我的世界，连接服务器，运行smart文件夹中的smartresident.py。  

由于本地搭建服务器，需要多人配合的闯空门功能可能无法正常使用  
