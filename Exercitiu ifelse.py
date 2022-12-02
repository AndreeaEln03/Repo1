# pentru un bacomat verificam userul si parola.Userl are 2 incercari atat pentru username cat si pentru parola
# userul doreste sa scoata o anumita suma de bani acesta avand un sold curent.suma dorita trebuie sa fie mai mica sau egaladecat soldul cutent
# daca se introduce o suma mai mare poate sa reincerce sau nu.La a doua incercare iese din program

expected_user = 'Liviu'
expected_pass = '2222'
sold = 3000.50
username =input('Indroduceti numele:')
if username == expected_user:
    print('User corect')
else:
    print('User incorect, incercati din nou')
    username = input('Indroduceti user:')
    assert username == expected_user, 'User incorect .O zi frumoasa'
    print('User corect')

parola = input('Introdu parola:')
if parola == expected_pass:
    print('parola corecta')
else:
    print('Parola inccorecta, Incearca din nou')
    parola =input('Indrodu parola')
    assert _ parola== expected_pass, 'Parola gresita ,O zi frumoasa!'
    print('parola corecta')

suma =float(input('Introdu suma dorita:'))
if suma <= sold
    print('Ridicati suma')

else:
    print('suma dorita este prea mare ,sold insuficient!')
    reincercare =input('Doriti sa incercati din nou? Da/Nu:')
    if reincercare == Da
        suma =float(input('Introdu suma dorita:'))
        assert suma <= sold, 'Suma introdusa este prea mare '
        print('Ridicati banii')
 elif 


