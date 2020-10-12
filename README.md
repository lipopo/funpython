# funpython

## 说明

用于构建一些突发奇想的工具和一些有趣的脚本工具，消遣时光。

## 安装
```bash
    python setup.py install
```
## apaint工具
### 简介
将图像转换为字符散点图。
### 效果
原图

![template_img](https://github.com/lipopo/funpython/blob/develop/templates/template_img.png)

转换成

![template_translate](https://github.com/lipopo/funpython/blob/develop/templates/template_translate.png)

### 使用方式
安装funypython后，默认会自动安装a_paint工具

使用过程：
```bash
paint_img paint -col 100 -row 100 -E [img_path]
```

-E是加密操作，如果不使用加密则把-E去除。
解密操作如下
```bash
paint_img decode-paint [file_path]
```

具体用法参照命令的help

## code_dot工具

### 简介

故名思意，及时根据给定图像，给出点行

### 效果


### 使用方式

安装funypython后，默认会安装code_dot工具

```
code_dot -i Acca
```
