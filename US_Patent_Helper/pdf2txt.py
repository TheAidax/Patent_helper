from pdfminer.high_level import extract_text, extract_pages

def pulling_Text(parentFilepath,CIPFilepath):
    getParentText = extract_text(parentFilepath)
    getCIPText = extract_text(CIPFilepath)

    parentText = open("parent.txt","w")
    CIPText = open("CIP.txt","w")

    parentText.write(getParentText)
    CIPText.write(getCIPText)

    parentText.close()
    CIPText.close()

pulling_Text("parentMadeSearchable.pdf","child.pdf")