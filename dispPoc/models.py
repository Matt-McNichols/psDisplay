from __future__ import unicode_literals

from django.db import models

# write the latex file header
header= '''
\\documentclass{report}
\\usepackage{geometry}
\\usepackage[dvipsnames]{xcolor}
\\usepackage{hyperref}
\\usepackage{graphicx}
\\usepackage{float}
\\usepackage{amsmath}
\\usepackage{subcaption}
\\usepackage{caption}
\\usepackage{mathtools}
\\usepackage{listings}

\\graphicspath{ {images/}}
\\hypersetup{
colorlinks=true,
linktoc=all,
linkcolor=blue!60,
}
\\geometry{legalpaper, portrait, margin=0.5in}
\\lstdefinestyle{custom}{
  basicstyle=\\small\\ttfamily,
  columns=flexible,
  breaklines=true,
  frame=single,
  language=Python ,
  keepspaces=true,
  backgroundcolor=\\color{gray!20},
  keywordstyle=\\bfseries\\color{purple!70!black},
  identifierstyle=\\color{black},
  stringstyle=\\color{orange},
  commentstyle=\\color{green!40!black}
}

\\lstset{style=custom}

\\title{Default Title}
\\author{Matt McNichols}
\\date{\\today}

\\DeclarePairedDelimiter\\floor{\\lfloor}{\\rfloor}
'''

# Create your models here.
class Text(models.Model):
    name = models.CharField(max_length=10)
    head = models.TextField(default=header)
    body = models.TextField(null=True)
    filePaths = models.TextField(null=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
