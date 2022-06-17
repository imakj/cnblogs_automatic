import os
import bean

__file_list = list()


def read_markdown(os_path, p_path):
    """
    遍历博客目录下所有目录
    并且根据目录名问标签 文件名和目录为key 创建文件
    :param os_path: 遍历目录
    :param p_path: 父目录
    :return:
    """
    global __file_list
    try:
        root_path = os.listdir(os_path)
        for path in root_path:
            file_path = os.path.join(os_path, path)
            if os.path.isdir(file_path):
                read_markdown(file_path, path)
            elif os.path.isfile(file_path):
                file_name, file_type = os.path.splitext(path)
                if file_type == '.md' and file_name != 'README':
                    __file_list.append([p_path, file_name, file_path])
    except Exception as e:
        print("获取博客文件失败")
        raise e
    return __file_list


def read_markdown_blog(os_path):
    """
    读取文件列表并且转换成博客园对象
    :param os_path:
    :return:
    """
    print("获取博客文件")
    blog_list = list()
    try:
        read_markdown(os_path, '')
        for file in __file_list:
            description = ''
            with open(file[2], 'r', encoding="utf-8") as f:
                description = f.read()
            if len(description.strip()) > 0:
                blog_list.append(bean.Blog(file[1], description, file[0]))
    except Exception as e:
        print("获取所有博客列表")
        raise e
    return blog_list
