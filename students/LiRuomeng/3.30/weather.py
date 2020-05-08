import urllib.request
import gzip
import json
import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
print('------天气查询------')
def get_weather_data() :
    city_name = input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    #需要输入城市名 urllib.parse解析成各个组件
    weather_data = urllib.request.urlopen(url1).read()
    #读取网页数据 这里读取的数据是经过gzip压缩的
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #解压网页数据
    weather_dict = json.loads(weather_data)
    #将json数据转换为dict数据
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data
    #将json数据转换为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        temp = int(weather_dict.get('data').get('wendu'))
        gewei = temp%10
        shiwei = temp//10
        print(gewei,shiwei)
        for i in range(gewei):
            mc.setBlock(pos.x-2, pos.y + i, pos.z, 213)#213是豹纹
        for i in range(shiwei):
            mc.setBlock(pos.x-3, pos.y + i, pos.z, 213)
     
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
        print('*******************************')
show_weather(get_weather_data())


