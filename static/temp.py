
    # put blocks together into a file
    fTexName = os.path.join(BASE_DIR,'static/dispPoc/fOut.tex')
    print 'tex file location: ',fTexName
    fTex = open(fTexName,'w')
    fTex.write(headObj.data)
    fTex.write(bodyObj.data)
    fTex.close()
