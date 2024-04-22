def difficulty_filter(difficulty):
    mapping = {1: '简单', 2: '中等', 3: '困难'}
    return mapping.get(difficulty, '未知')


def remove_empty_paragraphs(html):
    return html.replace('<p>&nbsp;</p>', '')


def format_code(code):
    return code.replace('\\n', '\n')
