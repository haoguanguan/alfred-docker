# Bookmarks
## 简单介绍
通过alfred+python脚本实现查询chrome书签、自动跳转的功能，<br>
原理很简单：解析存储chrome书签的json文件，通过模糊查询匹配相关网页信息
## 使用介绍
### 方式一：docker+alfred进行快捷操作
    1. 安装docker、alfred
    2. 导入 ./install/bookmarks.alfredworkflow
    3. 确定脚本中的书签的目录是否正确
    4. 简单使用
### 方式二：python+alfred，实现在alfred进行快捷操作
### 方式三：没有alfred，可以通过python脚本调用