#!/bin/env python
#coding=utf8
import xlwt
import sys

wb=xlwt.Workbook(encoding='utf8')
sh=wb.add_sheet('统计')
#设置边框细黑线
borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
#设置水平居中+垂直居中
alignment = xlwt.Alignment()
alignment.horz = 0x02
alignment.vert = 0x01
#初始化样式
style = xlwt.XFStyle()
style.alignment = alignment
style.borders = borders
sh.write(0,0,'类型',style)
sh.write(0,1,'风险等级',style)
sh.write(0,2,'已消除',style)
sh.write(0,3,'进行中',style)
sh.write(0,4,'待评审',style)
sh.write(0,5,'未开始',style)
sh.write(0,6,'挂起中',style)
sh.write(0,7,'汇总',style)
sh.write(0,8,'消除率',style)
sh.write(0,9,'H2的可控P0P1消除率',style)
sh.write_merge(1,3,0,0,'基础网络',style)
sh.write_merge(4,6,0,0,'数据中心',style)
data=[]
row=0
with open('result.txt','r') as fd:
    for line in fd.readlines():
        data.append(line.strip()) 
if len(data)==8:
    for i in range(0,6):
        row=row+1 
        dd=data[i].split(',') 
        column=0
        for ins_data in dd[1:]:
            column=column+1
            sh.write(row,column,ins_data,style)
    net_p0p1_ratio=data[6].split(',')[1] 
    idc_p0p1_ratio=data[7].split(',')[1] 
    sh.write_merge(1,2,9,9,net_p0p1_ratio,style)
    sh.write(3,9,'N/A',style)
    sh.write_merge(4,5,9,9,idc_p0p1_ratio,style)
    sh.write(6,9,'N/A',style)
else:
    print 'result.txt format error'
    sys.exit(200)
wb.save('系统部.xls')
