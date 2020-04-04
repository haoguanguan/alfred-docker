# Bookmarks
## 简单介绍
通过alfred+python脚本实现查询chrome书签、自动跳转的功能，
原理很简单：解析存储chrome书签的json文件，通过模糊查询匹配相关网页信息
## 使用介绍
### 方式一：没有python环境，docker+alfred进行快捷操作
### 方式二：python+alfred，实现在alfred进行快捷操作
### 方式三：没有alfred，可以通过python脚本调用
    1. 修改 ./src/bookmark.py:109 为 自己浏览器存储书签的目录
    2. 安装py27环境
    3. 运行示例