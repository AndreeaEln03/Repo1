lista_goala=1
dict_gol = {}

#declara si initializam un dict
note_elevi ={'Alex': 10 , 'Ela': 9,'Ana': 10}

#adaugam elemente
note_elevi['Sebi' ] = 7

#printam dictul
print(note_elevi)

#aflam note
print(note_elevi['Alex'])
print(note_elevi.get('Alex'))

#actualizam valori
note_elevi['Sebi'] = 10

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop('Alex')
note_elevi.get('Alex', 'numai avem acest elev')
print(note_elevi)

#returnare keys
print(note_elevi.keys())