# -*- coding: utf-8 -*-
import datetime
import re

from pyecharts import options as opts
from pyecharts.charts import Line


def get_list(date):
    return datetime.datetime.strptime(date[0], "%Y.%m.%d").timestamp()


def readFile(file):
    f = open(file, 'r', encoding="utf-8")
    list_ = []
    for i in f.readlines():
        itemArray = i.strip().rstrip().strip("\n").strip("\u3000\u3000").split("|")
        itemArrayReplace = []
        for y in itemArray:
            price = re.search("\d+(\.)?(\d)+(\.)?(\d)+", y)
            if price:
                itemArrayReplace.append(price.group())
        list_.append(itemArrayReplace)
    f.close()
    list_.sort(key=lambda x: get_list(x), reverse=False)
    return list_


if __name__ == '__main__':
    list_ = readFile('result/price.txt')
    日期 = []
    南昌 = []
    宜春 = []
    九江 = []
    德安 = []
    for item in list_:
        日期.append(item[0])
        南昌.append(item[1])
        宜春.append([item[2]])
        九江.append(item[3])
        德安.append(item[4])
    bar = (
        Line(init_opts=opts.InitOpts(width="3200px", height="800px"))
        .add_xaxis(日期)
        .add_yaxis("南昌", 南昌, is_clip=False)
        .add_yaxis("宜春", 宜春, is_clip=False)
        .add_yaxis("九江", 九江, is_clip=False)
        .add_yaxis("德安", 德安, is_clip=False)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2021年江西鸡蛋价格", subtitle="数据来源:www.feedtrade.com.cn"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False)
        )
    )
    bar.render()

