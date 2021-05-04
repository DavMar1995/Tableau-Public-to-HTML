# MIT License

# Copyright (c) 2021 Lin, You-Jun

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to
# do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from datetime import date
import os


# Choose which kind of method you want to use
DECISION = 1
EXECUTE_OPTIONS = ['FILE_DICT', 'Terminal']
EXECUTE_METHOD = EXECUTE_OPTIONS[DECISION]

FILE_DICT = [
    # For example: create two files
    # File One:
    {
        'name': 'Remote Visitors of Dataportal.asia',
        'title': 'Remote Visitors of Dataportal.asia',
        'code_list': [
            {
                'change_language': True,
                'caption': "",
                'text': "",
                'code': "<div class='tableauPlaceholder' id='viz1601978207478' style='position: relative'><noscript><a href='https:&#47;&#47;aodp.herokuapp.com'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1601978207478');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",
            },
            {
                'change_language': True,
                'caption': "",
                'text': "",
                'code': "<div class='tableauPlaceholder' id='viz1601979795746' style='position: relative'><noscript><a href='https:&#47;&#47;aodp.herokuapp.com'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1601979795746');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
            }
        ],
    },
    # File Two
    {
        'name': 'Remote Visitors of Dataportal.asia (duplicate)',
        'title': 'Remote Visitors of Dataportal.asia (duplicate)',
        'code_list': [
            {
                'change_language': True,
                'caption': "",
                'text': "",
                'code': "<div class='tableauPlaceholder' id='viz1601978207478' style='position: relative'><noscript><a href='https:&#47;&#47;aodp.herokuapp.com'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1601978207478');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",
            },
            {
                'change_language': True,
                'caption': "",
                'text': "",
                'code': "<div class='tableauPlaceholder' id='viz1601979795746' style='position: relative'><noscript><a href='https:&#47;&#47;aodp.herokuapp.com'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;RemoteVisitorsofDataportal_asia&#47;RemoteVisitorsofDataportal_asia2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1601979795746');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
            }
        ],
    },
]


def write_file(file_name, html):
    folder_name = f'html/{date.today().strftime("20%y_%m_%d")}'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    f = open(f'{folder_name}/{file_name}.html', 'w', encoding='utf-8')
    f.write(html)
    f.close()


def create_file(file_dict):
    name = file_dict['name']
    title = file_dict['title']
    code_dict = file_dict['code_list']

    tableau_code = ''
    script = ''

    head = f"""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <title>{title}</title>
    </head>"""

    style = """<style>
        body,
        h1,
        h2,
        h3,
        h4,
        h5 {
            font-family: Microsoft JhengHei;
        }

    </style>"""

    front = f"""<body class="w3-light-grey">
        <div class="w3-content" style="max-width:1400px">
            <header class="w3-container w3-center w3-padding-32">
                <h1><b>{title}</b></h1>
            </header>
            <div class="w3-row">
                <div class="w3-col l12 s12">
    """

    for data in code_dict:
        if data['change_language']:
            data['code'] = data['code'].replace(
                "value='zh-Hant'", "value='en'")
        split_point = data['code'].find('<script')
        tableau_code += f"""
                <div class = "w3-card-4 w3-margin w3-white" >
                    <div class = "w3-container" >
                        <h3 > <b > {data['caption']} </b > </h3 >
                    </div >
                    <div class = "w3-container" >
                        <p > {data['text']}
                        </p >
                    </div >
                    {data['code'][:split_point]}
                </div >
        """
        script += f'{data["code"][split_point:]}'

    end = """
                </div>
            </div>
        </div>
    </body>
    """

    html = head + style + front + tableau_code + end + script + '</html>'

    write_file(name, html)

    print(f'"{name}" has been completed!')


def insert_data():
    print("\nWARNING: if there is already have a same filename as what you type, the file you're going to create will overwrite the existing file.\n")
    name = input('Insert filename: ')
    title = input('Insert title: ')
    code_list = []

    while True:
        code_list.append({
            'change_language': check_input(
                'Need to change to English version or not? \n    Due to the political policy of Tableau, the so called "One-China Policy",\n    both map function and location related data might not work as well.\n    Personally strongly recommend change to English version. \nY/N: '),
            'caption': input('Insert caption (Could be empty): '),
            'text': input('Insert text (Could be empty): \n'),
            'code': input('\nPlease insert embed code from tableau:\n')})
        if not check_input('\nAnother tableau board in this page? (Y/N) : '):
            break

    create_file({
        'name': name,
        'title': title,
        'code_list': code_list,
    })


def check_input(text):
    while True:
        cont = input(text)
        if cont == 'Y' or cont == 'y':
            return True
        elif cont == 'N' or cont == 'n':
            return False


if __name__ == '__main__':
    print(
        f"\nValue of \"DECISION\" is {DECISION}, so will execute in \"{EXECUTE_METHOD}\" mode, which could be changed in Line 24.")
    if EXECUTE_METHOD == EXECUTE_OPTIONS[0]:
        for file in FILE_DICT:
            create_file(file)
    elif EXECUTE_METHOD == EXECUTE_OPTIONS[1]:
        insert_data()
        while True:
            if not check_input("\nIs there another file need to be created? (Y/N) : "):
                break
            insert_data()
    else:
        print(
            f"\nUnexpected value of \"DECISION\", expected 0 or 1, received {DECISION} instead.\nPlease check the value of  \"DECISION\" (Line 24).")