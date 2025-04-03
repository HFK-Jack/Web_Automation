# 使用说明

## Python 第三方库

- 解决环境使用pip安装报错的问题（报错Could not fetch URL https://pypi.org/simple/tensorflow/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url:）
  ```
  pip install package_name -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

  可替换用的镜像源
    1)http://mirrors.aliyun.com/pypi/simple/ 阿里云
    2)https://pypi.mirrors.ustc.edu.cn/simple/ 中国科技大学
    3)http://pypi.douban.com/simple/ 豆瓣
    4)https://pypi.tuna.tsinghua.edu.cn/simple/ 清华大学
    5)http://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
  ```
- pycharm修改永久镜像源方法
  https://www.johngo689.com/19235/
  
    
- 自动生成依赖包文件
  ```
  pip freeze > xxx.txt
  ```
  
- 批量安装第三方依赖包
  ```
  pip3 install -r xxx.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
 
  ```
  
## Pytest
- 断言：pytest 里面断言实际上就是 python 里面的 assert 断言方法，常用的有以下几种
  - assert xxx    ：判断 xxx 为真
  - assert not xx ：判断 xx 不为真
  - assert a in b ：判断 b 包含 a
  - assert a == b ：判断 a 等于 b
  - assert a != b ：判断 a 不等于 b



## 易发生错误-解决方案
- 使用.gitignore后，设置的内容不生效
  - 1.输入命令清除缓存：git rm -r --cached .idea 【想清啥就把.idea换成啥就好了】
  - 2.如远程仓库已经有不想提交的代码，需要删除掉
  
- 安装opencv-python报ERROR: Could not build wheels for opencv-python, which is required to install pyproject.toml-based projects
  - mac版本10.13 python3.7 安装对应版本 opencv-python-4.5.1.48


## github仓库版本
git version 2.43.0.windows.1

