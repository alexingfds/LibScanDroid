for elem in arraysource:
    if(elem[0] == 'app3'):
        app.append(librsansdoublon.index(elem[len(elem) - 1]))
    print()

print(app)
dictindice =dict()
dictindice['appt'] = app
print(dictindice)
print(dictindice.get('appt'))
if(7 in dictindice.get('appt')):
    print('yes')