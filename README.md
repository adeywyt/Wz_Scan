# Wz_Scan
<h4>作者：adey</h4>
<h4>年龄：14岁</h4>
<h4>简介：是一名初中学生.</h4>
<br>

# 子域名收集工具
<h4>使用Python编写的子域名收集工具</h4>
<h4>使用requests库，sys库，time库开发的</h4>
<br>

# Python编写子域名扫描工具思路：

<h4>[1]首先有个子域名的字典.</h4>
<h4>[2]然后读取子域名字典.</h4>
<h4>[3]将字典与url进行拼接</h4>
<h4>[4]进行get请求</h4>
<h4>[5]判断Http状态码是否是200.</h4>
<br>

# 子域名收集的使用
扫描https协议的网站
```
python Wz_Scan.py https xx.com      
```
扫描http协议的网站
```
python Wz_Scan.py http xx.com        
```

# 实例图片：
![Snipaste_2022-08-26_16-36-07](https://user-images.githubusercontent.com/108849049/186860229-800307e1-8634-42ae-b503-d67512ec604d.png)

# 总结：
Wz_Scan工具的使用方法就是如此简单.代码比较水.
