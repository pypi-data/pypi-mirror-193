# 简介

本python包用于机器学习课程使用，方便大家调用一些通用功能，如下载课程演示用数据集等。将会根据课程内容和需要进行更新。

## 主要功能

### 查询可下载数据集名称

- 函数名: mllesson.datasets.getnames
- 无参数

### 调取数据集名称与文件名字典

- 函数名: mllesson.datasets.getdict
- 无参数
- 下载数据集时会被mllesson.datasets.getdataset调用

### 下载数据集

- 函数名: mllesson.datasets.getdataset
- 参数name: 可使用mllesson.datasets.getnames函数查询
- 参数filedir: 数据集下载路径，默认为`'./'`

### 调用serverless服务器iris数据集预测结果

- 函数名: mllesson.api.iris
- 参数k1: 花萼长度
- 参数k2: 花萼宽度
- 参数k3: 花瓣长度
- 参数k4: 花瓣宽度

