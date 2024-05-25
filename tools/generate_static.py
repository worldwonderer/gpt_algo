import os

from flask import render_template

from api.app import app
from api.models import Problem


def gen():
    output_dir = app.config['STATIC_PAGES_DIR']
    os.makedirs(output_dir, exist_ok=True)

    with app.test_request_context():
        for problem in Problem.objects.all():
            title_slug = problem.title_slug
            try:
                rendered = render_template('detail.html', problem=problem)
                output_path = os.path.join(output_dir, f'{title_slug}.html')

                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(rendered)
            except Exception as e:
                print(f"Error rendering problem with title_slug '{title_slug}': {e}")


if __name__ == '__main__':
    gen()
