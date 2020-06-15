import qrcode

'''
qrcode.make(str):str为二维码包含的文字信息,也可以是网页链接，返回二维码对象
qrcode.save(str):将二维码以str为名保存到本地目录（注意文件的扩展名）
qrcode.show()：运行时展示二维码图案
'''
#创建包含信息的二维码对象
img = qrcode.make("2020littleteam4_new")
#二维码保存
img.save('verify_new.png')
#展示二维码
img.show()
