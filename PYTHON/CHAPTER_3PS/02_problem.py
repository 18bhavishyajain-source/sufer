letter = ''' Dear <|name|>,
you are selected !
<|Date|>'''

print(letter.replace("<|name|>", "Chiku").replace("<|Date|>", "26 07 2009"))