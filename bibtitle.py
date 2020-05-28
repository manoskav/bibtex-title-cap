import os, sys, re

bibname = sys.argv[1]
assert os.path.exists(bibname), "File does not exist."
assert bibname[-3:] == "bib", "Bibtex file must have .bib extension."

with open(bibname, 'r') as file:
    lines = file.readlines()

#  Regular expression to catch the "title" bibtex tag
pattern = r'(^(\s)*)(title)(\s)*(=)(\s)*{(?P<title>.*)}(\s)*(,?)((\s)*$)'
regex = re.compile(pattern, flags=re.IGNORECASE)

for i in range(len(lines)):

    line = lines[i]
    
    hastitle = regex.search(line)

    if hastitle is not None:

        tmptitle = hastitle.group('title')

        lentitle = len(tmptitle)
        j = 0

        while j < lentitle:

            char = tmptitle[j]
                
            if char.isupper():
                if j > 0:
                    prechar = tmptitle[j-1]
                else:
                    prechar = ''

                if j < lentitle-1:
                    postchar = tmptitle[j+1]
                else:
                    postchar = ''

                if not (prechar == "{" and postchar == "}"):
                    tmptitle = "".join(
                            [tmptitle[:j], "{"+char+"}", tmptitle[j+1:]])
                    j += 2

            j += 1
            lentitle = len(tmptitle)

        start, end = hastitle.span('title')
        lines[i] = "".join([line[0:start], tmptitle, line[end:]])

with open(bibname[:-4]+"-new"+".bib", 'w') as file:
    file.writelines(lines)
