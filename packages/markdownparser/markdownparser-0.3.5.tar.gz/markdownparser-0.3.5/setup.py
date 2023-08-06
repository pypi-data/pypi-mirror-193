# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markdownparser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'markdownparser',
    'version': '0.3.5',
    'description': '',
    'long_description': '# MarkdownParser\n\nMarkdownParser 是一个 Markdown 语法解析器,用于实现md到html标签的转换\n\n## 安装\n\n```bash\npip install markdownparser\n```\n\n## 快速使用\n\n```python\nimport MarkdownParser\n\nhtml = MarkdownParser.parse(\'# Hello World!\')\nprint(html)\n\n#<div class=\'markdown-body\'><h1>Hello World!</h1></div>\n```\n\n其他接口函数\n\n- `parseFile(file_name:str)->str`: 解析文件\n\n接口类\n\n- `Markdown`\n\n  使用类创建对象后可以利用 `self.preprocess_parser` `self.block_parser` `self.tree_parser` 控制解析过程\n\n  其中Block类属性见[base_class.py](MarkdownParser/base_class.py),可以通过调用block.info()函数查看树的结构\n\n  tree可以通过内部toHTML()方法得到HTML元素\n\n## 测试\n\n您可以使用 `test.py` 测试Markdown解析是否正确\n\n```bash\npython test.py <FILE_NAME>\n\n# python test.py ./testfiles/test1.md\n# python test.py README.md\n```\n\n运行会生成index.html, 使用浏览器打开生成的index.html即可与您的Markdown编辑器的预期渲染结果对比\n\n![20230218202400](https://raw.githubusercontent.com/learner-lu/picbed/master/20230218202400.png)\n\n## 实现思路\n\n[Markdown解析器的代码实现](https://www.bilibili.com/video/BV1LA411X7X3)\n\n您可通过取消 [core.py](./MarkdownParser/core.py) 注释来获取树的结构\n\n```python\ndef parse(self, text: str) -> str:\n\n    # 去除空行/注释/html标签\n    lines = self.preprocess_parser(text)\n    # print(lines)\n    # 逐行解析,得到一颗未优化的树\n    root = self.block_parser(lines)\n    # root.info()\n    # 优化,得到正确的markdown解析树\n    tree = self.tree_parser(root)\n    # tree.info()\n    # 输出到屏幕 / 导出html文件\n    return tree.toHTML()\n```\n\n## 不支持\n\n- 四个空格变为代码段(不想支持)\n- [^1]的引用方式(不想支持)\n- Latex数学公式(不会支持)\n- Setext 形式的标题(不想支持)\n- 上标 / 下标 / 下划线(不想支持)\n- SpecialTextBlock中叠加使用有可能会有bug(没想好怎么支持)\n- TOC与锚点(暂不支持)\n\n  锚点的添加通常和目录的跳转有关,而目录树的生成可以考虑解析tree的根Block的所有子HashHeaderBlock来构建.\n  \n  因为跳转的功能是js实现,锚点id的加入也会影响html结构,所以暂不支持\n\n## 其他特性\n\n- 最外层为div包裹,类名为 `markdown-body`\n- 代码段会根据语言加入一个类名便于后期高亮 `class="language-cpp"`, 未定义语言则为 `language-UNKNOWN`\n- 列表嵌套稍有不同,ul/ol+li完全体\n\n## 相关参考\n\n- [Github Markdown CSS](https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.css)\n- [Mermaid API](https://mermaid.js.org/intro/#mermaid-api)',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luzhixing12345/MarkdownParser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
