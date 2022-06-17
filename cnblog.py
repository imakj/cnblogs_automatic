#! /usr/bin/env python
# coding=utf-8

"""
xmlrpc api：https://rpc.cnblogs.com/metaweblog/makj
"""

import xmlrpc.client as xmlrpclib
import json
from bean import Blog

# 博客配置路径(config path)
__cfg_path = "userinfo.json"
title2id = {}
# 全局登录配置
__url, __appkey, __blogid, __user, __passwd = None, None, None, None, None
__server, __mwb = None, None



def init_user():
    """
    登录 并且获取系统信息
    :return:
    """
    try:
        global __url, __appkey, __blogid, __user, __passwd, __server, __mwb
        with open(__cfg_path, "r", encoding="utf-8") as f:
            print("加载用户文件:%s" %__cfg_path)
            cfg = json.load(f)
            __url = cfg["url"]
            __appkey = cfg["appkey"]
            __blogid = cfg["blogid"]
            __user = cfg["usr"]
            __passwd = cfg["passwd"]
            __server = xmlrpclib.ServerProxy(cfg["url"])
            __mwb = __server.metaWeblog
            print("加载成功 全局初始化完成:%s" % __cfg_path)
    except Exception as e:
        print("初始化用户信息错误")
        raise e

def get_categories():
    """
    获取所有标签信息 只获取随笔标签
    :return: 随笔所有分类集合
    """
    cg_list = list()  # 随笔list集合
    try:
        if __mwb is not None:
            categroy_list = __mwb.getCategories(__blogid, __user, __passwd)
            for cg in categroy_list:
                if cg["title"].startswith("[随笔分类]"):
                    cg_list.add(get_categories_value(cg["title"]))
    except Exception as e:
        print("获取所有标签信息错误")
        raise e
    return cg_list


def get_categories_value(categories_title):
    """
    转换标签
    :param categories_title:
    :return:
    """
    try:
        if categories_title != '':
            return categories_title[6:]
    except Exception as e:
        print("转换标签错误")
        raise e
    return None


def new_category(title):
    """
    创建标签
    :param title:  标签名字
    :return: True False
    """
    try:
        if __server is not None:
            title_value = title
            category = dict(name=title_value, parent_id=-1)
            rec_id = __server.wp.newCategory(__blogid, __user, __passwd, category)
            if rec_id > 0:
                print("创建标签成功:%s:%d" %(title_value, rec_id))
                return True
    except Exception as e:
        print("创建随笔分类错误")
        raise e
    return False


def get_recent_post():
    """
    获取所有博客列表
    :return: 博客集合
    """
    blog_list = list()
    try:
        if __mwb is not None:
            recent_post = __mwb.getRecentPosts(__blogid, __user, __passwd, 99999)
            count = len(recent_post)
            print("查询到总是%d"%count)
            if count > 0:
                for rp in recent_post:
                    bl_categories = set()
                    if 'categories' in rp.keys():
                        for c in rp['categories']:
                            bl_categories.add(c)
                    bl = Blog(rp['title'], rp['description'], bl_categories, rp['dateCreated'])
                    blog_list.append(bl)
            return blog_list
    except Exception as e:
        print("获取所有博客列表")
        raise e
    return blog_list


def new_post(blog):
    """
    发布新的blog
    :param blog:
    :return:
    """
    try:
        if blog is not None:
            post = dict(title=blog.get_title(), description=blog.get_description(), categories=blog.get_categories())
            rec = __mwb.newPost(__blogid, __user, __passwd, post, True)
            if len(rec.strip()) > 0:
                blog.set_blog_id(rec.strip())
                return True
    except Exception as e:
        print("获取所有博客列表")
        raise e
    return False


def edit_post(blog):
    """
    修改的blog
    :param blog:
    :return:
    """
    try:
        if blog is not None:
            post = dict(title=blog.get_title(), description=blog.get_description(), categories=blog.get_categories())
            rec = __mwb.editPost(blog.get_blog_id(), __user, __passwd, post, True)
            return rec
    except Exception as e:
        print("获取所有博客列表")
        raise e
    return False


if __name__ == '__main__':
    # b1s = set()
    # b1s.add('123')
    # b1 = Blog('123', '123', b1s)
    # b2s = set()
    # b2s.add('456')
    # b2 = Blog('456', '456', b2s)
    # print(b1.get_title(),b1.get_description(),b1.get_categories())
    # print(b2.get_title(),b2.get_description(),b2.get_categories())
    b1s = set()
    b1s.add('k3s')
    b = Blog('测试', '测试', list(b1s))
    init_user()
    # new_post(b)
    b.set_blog_id("16380236")
    print(b.get_blog_id())
    # 16380236
    edit_post(b)
    # new_category(b)
    # get_recent_post()
    # cg_list = getCategories()
    # print(cg_list)
    # print(newCategory("test3"))
    # get_cfg()
    # getCategories()
    # newCategory("testssss2")

    # {
    #     'description': '[随笔分类]docker',
    #     'htmlUrl': '',
    #     'rssUrl': '',
    #     'title': '[随笔分类]docker',
    #     'categoryid': '2171239'
    # }
    # suibitype_list = ['test']
    # post = dict(description="测试啊21", title="测试2", categories=suibitype_list)
    # newPost(blogid,usr,passwd,post,True)

