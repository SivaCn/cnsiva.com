
import os

BLOGS_DIR_NAME = 'blogs'
MAIN_LEVEL_DIR = 'cnsiva'


class Blog(object):
    def __init__(self):
        self.left_nav_template_level_0 = """
            <li>
                <label for="%(dir_name_joined)s">
                    <img src="folder.png" height="20" width="20">
                    &nbsp;
                    %(dir_name)s
                </label>
                <input type="checkbox" id="%(dir_name_joined)s" />
                <ol>
                    %(articles_template)s
                </ol>
            </li>
            """

        self.left_nav_template_level_1 = """
            <li class="file">
                &nbsp;&nbsp;&nbsp;
                %(article_name)s
            </li>"""

    def format_nav_window(self):
        pass

    def format_arrticle_window(self):
        pass

    def format_tree_list(self, tree_data_as_dict):

        content = ''
        content += """<ol class="tree">"""
        for _category, _articles in tree_data_as_dict.items():
            articles = list()
            _category_name = os.path.split(_category)[-1]

            for _each_article in _articles:
                _article_path = os.path.join(_category, _each_article)
                if os.path.isfile(_article_path):
                    articles.append(self.left_nav_template_level_1 % {'article_name': _each_article})

            content += self.left_nav_template_level_0 % {'articles_template': ''.join(articles),
                                                         'dir_name_joined': _category_name,
                                                         'dir_name': _category_name}
        content += """</ol>"""

        content = """
            <div class="row">
                <div class="four columns outlined">""" + content + """</div></div>"""
 
        return content

    def get_articles_by_category(self, blog_type):
        pwd = os.getcwd()
        blog_base_path = os.path.join(pwd, MAIN_LEVEL_DIR, BLOGS_DIR_NAME)
        current_blog_path = os.path.join(blog_base_path, blog_type)

        if blog_type not in ('python'):
            raise Exception("Not a Valid Blog type.")

        _all_dirs = [os.path.join(current_blog_path, item)
                     for item in os.listdir(current_blog_path)]

        _file_system = dict()

        for each_dir in _all_dirs:
            if os.path.isdir(each_dir):
                _file_system[each_dir] = os.listdir(each_dir)

        return self.format_tree_list(_file_system)


class PythonBlog(Blog):
    def get_page_content(self):
        return self.get_articles_by_category(blog_type='python')
