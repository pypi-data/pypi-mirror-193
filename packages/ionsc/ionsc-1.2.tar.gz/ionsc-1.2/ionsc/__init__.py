def iDecrypt(ini):
    inicio = ini
    start = 0
    grp = inicio[start] + inicio[start+1] + inicio[start+2];
    grp1 = len(inicio)/3
    final = ""

    for i in range(int(grp1)):
        if grp == '3a.':
            final+='a';
        elif grp == '6a.':
            final+='b';
        elif grp == '9a.':
            final+='c';
        elif grp == '3b.':
            final+='d'
        elif grp == '6b.':
            final+='e'
        elif grp == '9b.':
            final+='f'
        elif grp == '3c.':
            final+='g'
        elif grp == '6c.':
            final+='h'
        elif grp == '9c.':
            final+='i'
        elif grp == '3d.':
            final+='j'
        elif grp == '6d.':
            final+='k'
        elif grp == '9d.':
            final+='l'
        elif grp == '3e.':
            final+='m'
        elif grp == '6e.':
            final+='n'
        elif grp == '9e.':
            final+='o'
        elif grp == '3f.':
            final+='p'
        elif grp == '6f.':
            final+='q'
        elif grp == '9f.':
            final+='r'
        elif grp == '3g.':
            final+='s'
        elif grp == '6g.':
            final+='t'
        elif grp == '9g.':
            final+='u'
        elif grp == '3h.':
            final+='v'
        elif grp == '6h.':
            final+='w'
        elif grp == '9h.':
            final+='x'
        elif grp == '3i.':
            final+='y'
        elif grp == '6i.':
            final+='z'
        elif grp == '9i.':
            final+='A'
        elif grp == '3j.':
            final+='B'
        elif grp == '6j.':
            final+='C'
        elif grp == '9j.':
            final+='D'
        elif grp == '3k.':
            final+='E'
        elif grp == '6k.':
            final+='F'
        elif grp == '9k.':
            final+='G'
        elif grp == '3l.':
            final+='H'
        elif grp == '6l.':
            final+='I'
        elif grp == '9l.':
            final+='J'
        elif grp == '3m.':
            final+='K'
        elif grp == '6m.':
            final+='L'
        elif grp == '9m.':
            final+='M'
        elif grp == '3n.':
            final+='N'
        elif grp == '6n.':
            final+='O'
        elif grp == '9n.':
            final+='P'
        elif grp == '3o.':
            final+='Q'
        elif grp == '6o.':
            final+='R'
        elif grp == '9o.':
            final+='S'
        elif grp == '3p.':
            final+='T'
        elif grp == '6p.':
            final+='U'
        elif grp == '9p.':
            final+='V'
        elif grp == '3q.':
            final+='W'
        elif grp == '6q.':
            final+='X'
        elif grp == '9q.':
            final+='Y'
        elif grp == '3r.':
            final+='Z'
        elif grp == '6r.':
            final+='.'
        elif grp == '9r.':
            final+='!'
        elif grp == '3s.':
            final+='?'
        elif grp == '6s.':
            final+='#'
        elif grp == '9s.':
            final+='@'
        elif grp == '3t.':
            final+="'"
        elif grp == '6t.':
            final+='"'
        elif grp == '9t.':
            final+=':'
        elif grp == '3u.':
            final+=';'
        elif grp == '6u.':
            final+=','
        elif grp == '9u.':
            final+='('
        elif grp == '3v.':
            final+=')'
        elif grp == '6v.':
            final+='['
        elif grp == '9v.':
            final+=']'
        elif grp == '3w.':
            final+='{'
        elif grp == '6w.':
            final+='}'
        elif grp == '9w.':
            final+='0'
        elif grp == '3x.':
            final+='1'
        elif grp == '6x.':
            final+='2'
        elif grp == '9x.':
            final+='3'
        elif grp == '3y.':
            final+='4'
        elif grp == '6y.':
            final+='5'
        elif grp == '9y.':
            final+='6'
        elif grp == '3z.':
            final+='7'
        elif grp == '6z.':
            final+='8'
        elif grp == '9z.':
            final+='9'
        elif grp == '30.':
            final+='+'
        elif grp == '60.':
            final+='-'
        elif grp == '90.':
            final+='/'
        elif grp == '31.':
            final+='\\'
        elif grp == '61.':
            final+='='
        elif grp == '91.':
            final+='>'
        elif grp == '32.':
            final+='<'
        elif grp == '62.':
            final+='*'
        elif grp == '92.':
            final+='$'
        elif grp == '33.':
            final+='%'
        elif grp == '63.':
            final+='&'
        elif grp == '.-.':
            final+=' '
        else:
            final+='�'

        start+=3
        
        return final

def iEncrypt(ini):
    inicial = ini
    final = ""
    for i in inicial:
        if i == 'a':
            final+='3a.'
        elif i == 'b':
            final+='6a.'
        elif i == 'c':
            final+='9a.'
        elif i == 'd':
            final+='3b.'
        elif i == 'e':
            final+='6b.'
        elif i == 'f':
            final+='9b.'
        elif i == 'g':
            final+='3c.'
        elif i == 'h':
            final+='6c.'
        elif i == 'i':
            final+='9c.'
        elif i == 'j':
            final+='3d.'
        elif i == 'k':
            final+='6d.'
        elif i == 'l':
            final+='9d.'
        elif i == 'm':
            final+='3e.'
        elif i == 'n':
            final+='6e.'
        elif i == 'o':
            final+='9e.'
        elif i == 'p':
            final+='3f.'
        elif i == 'q':
            final+='6f.'
        elif i == 'r':
            final+='9f.'
        elif i == 's':
            final+='3g.'
        elif i == 't':
            final+='6g.'
        elif i == 'u':
            final+='9g.'
        elif i == 'v':
            final+='3h.'
        elif i == 'w':
            final+='6h.'
        elif i == 'x':
            final+='9h.'
        elif i == 'y':
            final+='3i.'
        elif i == 'z':
            final+='6i.'
        elif i == 'A':
            final+='9i.'
        elif i == 'B':
            final+='3j.'
        elif i == 'C':
            final+='6j.'
        elif i == 'D':
            final+='9j.'
        elif i == 'E':
            final+='3k.'
        elif i == 'F':
            final+='6k.'
        elif i == 'G':
            final+='9k.'
        elif i == 'H':
            final+='3l.'
        elif i == 'I':
            final+='6l.'
        elif i == 'J':
            final+='9l.'
        elif i == 'K':
            final+='3m.'
        elif i == 'L':
            final+='6m.'
        elif i == 'M':
            final+='9m.'
        elif i == 'N':
            final+='3n.'
        elif i == 'O':
            final+='6n.'
        elif i == 'P':
            final+='9n.'
        elif i == 'Q':
            final+='3o.'
        elif i == 'R':
            final+='6o.'
        elif i == 'S':
            final+='9o.'
        elif i == 'T':
            final+='3p.'
        elif i == 'U':
            final+='6p.'
        elif i == 'V':
            final+='9p.'
        elif i == 'W':
            final+='3q.'
        elif i == 'X':
            final+='6q.'
        elif i == 'Y':
            final+='9q.'
        elif i == 'Z':
            final+='3r.'
        elif i == '.':
            final+='6r.'
        elif i == '!':
            final+='9r.'
        elif i == '?':
            final+='3s.'
        elif i == '#':
            final+='6s.'
        elif i == '@':
            final+='9s.'
        elif i == "'":
            final+='3t.'
        elif i == '"':
            final+='6t.'
        elif i == ':':
            final+='9t.'
        elif i == ';':
            final+='3u.'
        elif i == ',':
            final+='6u.'
        elif i == '(':
            final+='9u.'
        elif i == ')':
            final+='3v.'
        elif i == '[':
            final+='6v.'
        elif i == ']':
            final+='9v.'
        elif i == '{':
            final+='3w.'
        elif i == '}':
            final+='6w.'
        elif i == '0':
            final+='9w.'
        elif i == '1':
            final+='3x.'
        elif i == '2':
            final+='6x.'
        elif i == '3':
            final+='9x.'
        elif i == '4':
            final+='3y.'
        elif i == '5':
            final+='6y.'
        elif i == '6':
            final+='9y.'
        elif i == '7':
            final+='3z.'
        elif i == '8':
            final+='6z.'
        elif i == '9':
            final+='9z.'
        elif i == '+':
            final+='30.'
        elif i == '-':
            final+='60.'
        elif i == '/':
            final+='90.'
        elif i == '\\':
            final+='31.'
        elif i == '=':
            final+='61.'
        elif i == '>':
            final+='91.'
        elif i == '<':
            final+='32.'
        elif i == '*':
            final+='62.'
        elif i == '$':
            final+='92.'
        elif i == '%':
            final+='33.'
        elif i == '&':
            final+='63.'
        elif i == ' ':
            final+='.-.'
        else:
            final+='.?.'
    return final

def multiEncrypt(text, layers):
    a = text
    for i in range(layers):
        a = iEncrypt(a)
    
def multiDecrypt(text, layers):
    a = text
    for i in range(layers):
        a = iDecrypt(a);
