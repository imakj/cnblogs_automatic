import time

import bean
import cnblog
import blog_file

os_path = "D:\\doc\\MakjLearnBlog\\"

def publish_cnblogs():
    """
    发布博客
    :return: 
    """
    # 读取当前目录数据
    blog_list = blog_file.read_markdown_blog(os_path)
    file_map = blog_list_map(blog_list)
    # 读取博客园数据
    cnblog.init_user()
    blog_list = cnblog.get_recent_post()
    cnblog_map = blog_list_map(blog_list)

    for title, blog in file_map.items():
        if title in cnblog_map.keys():
            cb = cnblog_map.get(title)
            print("------------文件存在和博客园都有:%s,%d,%d,%s" %(title , len(cb.get_description().strip()),len(blog.get_description().strip()) , cb.get_description().strip() == blog.get_description().strip()))
        else:
            print("文件存在，博客园没有:"+title)
        time.sleep(3) # 休息三秒 不然引起验证


def blog_list_map(blog_list):
    """
    list转map k title value blog对象
    :param blog_list:
    :return:
    """
    blog_map = dict()
    try:
        if len(blog_list) > 0:
            for blog in blog_list:
                blog_map[blog.get_title()] = blog
    except Exception as e:
        raise e
    return blog_map


if __name__ == '__main__':
    publish_cnblogs()

