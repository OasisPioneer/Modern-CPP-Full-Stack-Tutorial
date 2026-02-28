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
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

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
latex_elements = {
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
\setCJKmainfont{Source Han Sans SC}
\setCJKsansfont{Source Han Sans SC}
\setCJKmonofont{Source Han Sans SC}
''',
    'preamble': r'''
\usepackage[UTF8, heading=true, fontset=none]{ctex}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{eso-pic}

\definecolor{ChapterColorScheme}{RGB}{24, 112, 125}
\definecolor{SectionColorScheme}{RGB}{98, 137, 196}
\definecolor{SubsectionColorScheme}{RGB}{88, 161, 174}

\setlength{\parindent}{2em}
\usepackage{indentfirst}

\ctexset{
  contentsname = {目录},
  part = {
    name = {第, 部分},
    number = \chinese{part},
    pagestyle = empty           % 强制页面不带页码
  },
  chapter = {
    name = {第, 章},
    number = \arabic{chapter},
    fixskip = true,
    format = \Huge\bfseries\color{ChapterColorScheme}\centering,
    beforeskip = 0pt, 
    afterskip = 15pt,
    aftertitle = {\par\vspace{-15pt}\rule{\textwidth}{2pt}} 
  },
  section = {
    name = {第, 节},
    number = \arabic{section},
    format = \Large\bfseries\color{SectionColorScheme}\centering,
    afterskip = 0pt,
    aftertitle = {\par\vspace{-10pt}\rule{15em}{2pt}}
  },
  subsection = {
    name = {第, 段},
    number = \arabic{subsection},
    format = \Large\bfseries\color{SubsectionColorScheme}\noindent\rule[-2pt]{4pt}{1em}\quad,
    afterskip = 0pt,
    indent = 0pt,
  }
}

\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother
''',
    'maketitle': r'''
        \input{CoverPage.tex.txt}
        \input{TitlePage.tex.txt}
''',
    'sphinxsetup': 'TitleColor=DarkGoldenrod',
    # 'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
    'extraclassoptions': 'openany,oneside',
}

latex_show_urls = 'footnote'