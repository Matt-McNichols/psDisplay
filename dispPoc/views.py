from django.shortcuts import render, get_object_or_404
from dispPoc.models import Text
from dispPoc.forms import TextForm
import os, subprocess
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
customTags = []

def texCompile(Obj):
    inTag   = '~I~{'
    outTag  = '~O~{'
    replTag = '\lstinputlisting{'

    # orginize file paths with their id's
    tempArray = Obj.filePaths.splitlines()
    pathArray = []
    # each line contains an id and a path to a file
    for line in tempArray:
        temp = line.split('::')
        pathArray.append(temp)

    for tag,filePath in pathArray:
        tag = str(tag); filePath = str(filePath);
        # run the files code and store it in an output file
        fileOutput = subprocess.check_output(['python',filePath])

        # make all str replacements
        outLine = outTag + tag + '}'
        outRepl = '\\begin{lstlisting}\n' + fileOutput + '\n\\end{lstlisting}\n'
        print 'outLine',outLine
        print 'outRepl',outRepl
        # replace output tag blocks with file output
        Obj.body=Obj.body.replace(outLine,outRepl)
        # replace input tag with filePath
        Obj.body=Obj.body.replace(tag,filePath)
        # replace input block with lstinputlisting
        Obj.body=Obj.body.replace(inTag,replTag)
    print 'obj.body after str rep: ',Obj.body
    # put blocks together into a file
    fTexName = os.path.join(BASE_DIR,'static/dispPoc/fOut.tex')
    print 'tex file location: ',fTexName
    fTex = open(fTexName,'w')
    fTex.write(Obj.head)
    fTex.write(Obj.body)
    fTex.close()
    # now compile tex file into pdf
    os.chdir('static/dispPoc/');
    os.system('pdflatex fOut.tex')
    os.chdir('../../');
    os.system('pwd')

def index(request):
    Obj = get_object_or_404(Text, name='input')
    form = TextForm(request.POST or None, instance=Obj )
    if form.is_valid():
        form.save(commit=True)
        print 'saving form'
    else:
        print 'error: form is not valid'

    texCompile(Obj)

    return render(request,'dispPoc/index.html',{'form': form})
