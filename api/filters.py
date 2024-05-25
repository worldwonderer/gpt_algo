from bs4 import BeautifulSoup


def difficulty_filter(difficulty):
    mapping = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
    return mapping.get(difficulty, '未知')


def remove_empty_paragraphs(html):
    return html.replace('<p>&nbsp;</p>', '')


def format_code(code):
    return code.replace('\\n', '\n')


def clean_remote_html(html_content):
    html_content = html_content.replace('<p><br></p>', '').replace('\\"', '"').strip('"')
    soup = BeautifulSoup(html_content, 'html.parser')
    # 遍历所有后代节点
    for tag in soup.find_all(True):  # True 表示匹配所有标签
        if 'style' in tag.attrs:
            del tag.attrs['style']
        if tag.name.startswith('h') and tag.name[1:].isdigit():
            print(tag.name)
            level = int(tag.name[1:])
            if level > 1:
                tag.name = f'h{level + 1}'
    return str(soup)
