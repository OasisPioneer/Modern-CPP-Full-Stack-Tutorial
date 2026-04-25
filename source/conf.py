# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Modern C++ Full-Stack Tutorial'
copyright = '2026, 龙森'
author = '龙森'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "furo"
html_title = "Modern C++ Full-Stack Tutorial"
html_theme_options = {
    "announcement": "<strong>声明</strong> 本教程并不严谨，如有不足之处欢迎评论指正!",
    "source_repository": "https://github.com/OasisPioneer/Modern-CPP-Full-Stack-Tutorial",
    "source_branch": "main",
    "source_directory": "source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/OasisPioneer/Modern-CPP-Full-Stack-Tutorial",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

html_static_path = ['_static']
html_css_files = [
    'content.css',
]

# -- Options for LaTeX output ------------------------------------------------
latex_additional_files = [
    '_static/Cover.png',
    '_templates/CoverPage.tex.txt',
    '_templates/TitlePage.tex.txt',
]

latex_engine = 'xelatex'
latex_use_xindy = True
latex_toplevel_sectioning = 'part'
latex_table_style = ['booktabs']
latex_elements = {
    'babel': '',
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
% [EN]
\setmainfont{Source Han Sans SC}
\setsansfont{Source Han Sans SC}
\setmonofont{Fira Code}
% [CN]
\setCJKmainfont{Source Han Serif SC}
\setCJKsansfont{Source Han Sans SC}
\setCJKmonofont{Source Han Sans SC}
''',
    'preamble': r'''
\usepackage[UTF8, heading=true, fontset=none]{ctex}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{eso-pic}
\usepackage{indentfirst}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{array}
\usepackage[most]{tcolorbox}

\pagestyle{fancy}

\hypersetup{
    bookmarksnumbered=true,
    bookmarksopen=true,
    bookmarksopenlevel=2,
    colorlinks=true,
    linkcolor=black,
    citecolor=black,
    urlcolor=darkgray
}

\makeatletter   % 自定义页眉与页脚
% 章标题更新 \leftmark 节标题更新 \rightmark
% \renewcommand{\chaptermark}[1]{\markboth{#1}{}}
% \renewcommand{\sectionmark}[1]{\markright{#1}}

\renewcommand{\chaptermark}[1]{%
    \markboth{第\thechapter\ 章\ #1}{}
}
\renewcommand{\sectionmark}[1]{%
    \markright{\thesection\ #1}{}
}

% 自定义 normal 样式：用于文档的普通页面
\fancypagestyle{normal}{
    \fancyhf{}                              % 清除所有默认的页眉页脚设置
    \fancyhead[L]{\nouppercase{\leftmark}}  % 左侧页眉内容
    \fancyhead[C]{\textbf{\@title}}         % 中间页眉内容
    \fancyhead[R]{\nouppercase{\rightmark}} % 右侧页眉内容
    % \fancyfoot[L]{}                       % 左侧页脚内容
    \fancyfoot[C]{\textbf{\thepage}}        % 中间页脚内容
    % \fancyfoot[R]{}                       % 右侧页脚内容
    \renewcommand{\headrulewidth}{0.4pt}    % 设置页眉线的宽度
    \renewcommand{\footrulewidth}{0.4pt}    % 设置页脚线的宽度
}

% 自定义 plain 样式：用于章节的首页（默认不显示页眉，只显示页脚）
\fancypagestyle{plain}{
    \fancyhf{}                              % 清除所有默认设置
    \fancyfoot[C]{\textbf{\thepage}}        % 章节首页通常只显示页码
    \renewcommand{\headrulewidth}{0pt}      % 章节首页通常不显示页眉线
    \renewcommand{\footrulewidth}{0.4pt}    % 章节首页通常不显示页脚线
}
\makeatother

\ctexset{
  contentsname = {目\kern0.8em录},
  part = {
    name = {第, 部分},
    number = \chinese{part},
    format = \centering\bfseries,
    nameformat = \Huge\bfseries\color{gray},
    aftername = {\par\vspace{0em}},
    titleformat = {\fontsize{40pt}{48pt}\selectfont\bfseries},
    pagestyle = empty           % 强制页面不带页码
  },
  chapter = {
    name = {第, 章},
    number = \arabic{chapter},
    fixskip = true,
    format = \huge\bfseries\centering,
    beforeskip = 0pt, 
    afterskip = 15pt,
    % aftertitle = {\par\vspace{-15pt}\rule{\textwidth}{2pt}} 
  },
  section = {
    name = {第, 节},
    number = \arabic{section},
    format = \Large\bfseries,
    afterskip = 0pt,
    % aftertitle = {\par\vspace{-10pt}\rule{15em}{2pt}}
  },
  subsection = {
    % name = {第, 段},
    name = {,},
    % number = \arabic{subsection},
    number = \thesection.\arabic{subsection},
    format = \large\bfseries\noindent\rule[-2pt]{2pt}{1em}\quad,
    beforeskip = 0pt,
    afterskip = 0pt,
    indent = 0pt,
  }
}

% 目录布局
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother

\setlength{\parindent}{2em}         % 首行缩进

\newcolumntype{T}{C}                % 表格居中
''',
    'maketitle': r'''
        \input{CoverPage.tex.txt}
        \input{TitlePage.tex.txt}
''',
    # 'sphinxsetup': 'TitleColor=DarkGoldenrod',
    # 'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    'extraclassoptions': 'openany,oneside',
}

latex_show_urls = 'inline'