class Blog(object):

    # 博客id
    __blog_id = ''

    # 标题
    __title = ''

    # 内容
    __description = ''

    # 标签列表
    __categories = set()

    # 创建时间
    __data_create = None

    # 文章标记用于区分文章是否更新
    __mark = ''

    def __init__(self):
        """
        创建 初始化列表
        """
        __categories = list()

    def __init__(self, title, description, categories, data_create=None):
        if title is not None and description is not None:
            self.__title = title
            self.__description = description
            self.__categories = categories
            self.__data_create = data_create

    def get_blog_id(self):
        return self.__blog_id

    def set_blog_id(self, blog_id):
        self.__blog_id = blog_id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_categories(self):
        return self.__categories

    def get_data_create(self):
        return self.__data_create
