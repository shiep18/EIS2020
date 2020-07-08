from pyecharts.charts import Map,Geo
from pyecharts import options as opts

#将数据处理成列表
def getmaps(proviences, confirmed):
    c_confrimed = confirmed.copy()
    c_confrimed.sort(reverse = True)
    max_value = c_confrimed[0]
    del c_confrimed

    l = [[proviences[i],confirmed[i]] for i in range(len(proviences))]
    china_confirm_map = Map(init_opts=opts.InitOpts(width = "1200px", height="600px"))
    china_confirm_map.set_global_opts(
        title_opts=opts.TitleOpts(title="2019-nCov"),
        visualmap_opts=opts.VisualMapOpts(max_=max_value)  #最大数据范围
    )
    china_confirm_map.add("2019-nCov全国各省感染人数", l, maptype="china")
    return china_confirm_map
