# Zagrożenia HTTP

## Przygotowanie środowiska do pracy
 
W terminalu swojego IDE (zalecamy PyCharm, ale może być dowolne) wpisz kolejno:
- `python -m venv venv`
- `./venv/Scripts/activate`
Spowoduje to uruchomienie potrzebnego środowiska wirtualnego. Następnie:
- pip3 install flask
- pip3 install app
- pip3 install –upgrade flask
 
Następnie należy wybrać interpreter pythona z oznaczeniem venv.
Projekt powinien być gotowy do uruchomienia.

## Zadania

1. Przejrzyj strukturę bazy danych (plik init.sql) oraz kod aplikacji i spróbuj znaleźć podatność, która pozwoli ci uzyskać prawo do usuwania cudzych postów. 
  - Napisz, w którym miejscu aplikacji występuje ta podatność.
  - Opisz działania, które należało wykonać w celu zrealizowania zadania.
  - Zaproponuj sposób, w który można zapobiec temu atakowi.

2. Wykonaj atak MITM w swojej sieci na udostępnionych maszynach wirtualnych. Przechwyć pliki cookies sesji zalogowanego użytkownika celem dostania się na jego konto.

3. Zmodyfikuj kod funkcji rejestracji, aby odrzucał 20 najbardziej popularnych haseł w 2021 roku. Przykładowa lista haseł: https://nordpass.com/most-common-passwords-list/

# Prezentacja
https://docs.google.com/presentation/d/1VHsevdzyd-CnxhlPBOJbweRi-UJhIw3UJ980ccOon9U/edit?fbclid=IwAR3bi9VFHfHaNWELvhZCXvp0igylMPFZljIRKw52ooFPLpzjIzNvWR7VG1Y#slide=id.g1c9161ba606_0_152
