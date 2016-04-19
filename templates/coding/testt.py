
views



#code=self.request.Post['code']
    saved=False
    context = RequestContext(request)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # newdoc = Document(docfile = request.FILES['docfile'])
            # newdoc.save()
            # saved=True
            f=open("code.c","w")
            f.write(form.code)
            f.close()
            
            return render(request, 'savee.html')
    else:
        

    # Render list page with the documents and the form
            return render(request, 'save.html')   
    






forms
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        
    )
