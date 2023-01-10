# Zagrożenia HTTP

## Przygotowanie środowiska do pracy

1. Na początku należy sklonować repozytorium do wybranego przez siebie folderu na dysku:
   `https://github.com/rfmajor/bawim-zagrozenia-http.git`
2. Następnie należy utworzyć nowy projekt w środowisku PyCharm (`File -> New Project`)
   - z listy po lewej stronie trzeba wybrać `Flask`
   - w polu `location` należy wskazać folder zawierający sklonowane repozytorium
3. Po kliknięciu przycisku `Create` trzeba wybrać opcję `Create from existing sources`
4. W prawym górnym rogu aplikacji należy kliknąć przycisk z konfiguracją, następnie `Edit Configurations...`. Powinno pojawić się okienko z konfiguracjami. Po lewej stronie należy kliknąć znak `+` i wybrać z listy opcję `Flask Server`. Następnie należy kliknąć `Apply`

Aplikacja powinna w tym momencie być gotowa do uruchomienia. Tuż po jej starcie będzie dostępna pod adresem `http://127.0.0.1:5000/`.

## Zadania

1. Przejrzyj strukturę bazy danych (plik init.sql) oraz kod aplikacji i spróbuj znaleźć podatność, która pozwoli ci uzyskać prawo do usuwania cudzych postów. 
   - Napisz, w którym miejscu aplikacji występuje ta podatność.
   - Opisz działania, które należało wykonać w celu zrealizowania zadania.
   - Zaproponuj sposób, w który można zapobiec temu atakowi.

2. Wykonaj atak MITM w swojej sieci na udostępnionych maszynach wirtualnych. Przechwyć pliki cookies sesji zalogowanego użytkownika celem dostania się na jego konto.

3. Zmodyfikuj kod funkcji rejestracji, aby odrzucał 20 najbardziej popularnych haseł w 2021 roku. Przykładowa lista haseł: https://nordpass.com/most-common-passwords-list/

# Prezentacja
https://docs.google.com/presentation/d/1VHsevdzyd-CnxhlPBOJbweRi-UJhIw3UJ980ccOon9U/edit?fbclid=IwAR3bi9VFHfHaNWELvhZCXvp0igylMPFZljIRKw52ooFPLpzjIzNvWR7VG1Y#slide=id.g1c9161ba606_0_152
