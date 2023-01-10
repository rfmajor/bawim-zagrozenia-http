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
   
   Pobierz obraz wirtualnej maszyny MITM oraz zaimportuj ją do Virtualbox.
   Będziemy potrzebować trzech urządzeń, dlatego sklonuj istniejącą maszynę dwa razy (`prawy klik -> clone`).
   Maszyny odzwierciedlają serwer, użytkownika oraz intrudera. 
   Następnie dla każdej maszyny wygeneruj nowy MAC Address (`Settings->Network->Advanced->Generate a new random MAC address`)
   Uruchom maszyny, sprawdź czy posiadają swój własny adres IP (komenda `ifconfig`) oraz czy jest możliwa komunikacja między nimi (np poprzez ping).
   Jeżeli tak, to środowisko jest gotowe i poprawnie skonfigurowane.
   
   Na serwerze uruchom terminal i przejdź do katalogu `/app` znajdującego się w folderze domowym.
   Uruchom aplikację poleceniem: `flask run --host=0.0.0.0`.

   Na komputerze klienta możesz teraz odwiedzić stronę wpisując w pasku wyszukiwarki `http://X.X.X.X:5000`, gdzie `X.X.X.X` jest adresem serwera.
   Utwórz nowe konto, zaloguj się oraz dodaj jakiś post. Nie wylogowuj się.

   Czas na przeprowadzenie ataku MITM. Na komputerze intrudera uruchom program `ettercap`. Możesz to zrobić wpisując w terminalu: `sudo ettercap -G` (flaga `-G` otwiera program w trybie graficznym, chociaż możliwe jest również korzystanie z trybu konsolowego).
   Aby znaleźć hosty w naszej sieci, wchodzimy w rozwijany panel po prawej stronie: `Hosts->Hosts list`, a następnie `Hosts->Scan for hosts`.
   Zaznaczamy adres naszego serwera i dodajemy jako Target 1, analogicznie dodajemy użytkownika jako Target 2.
   Następnie w rozwijanym pasku `MITM menu` wybieramy `ARP poisoning` i zaznaczamy tylko opcję `Only poison one-way`. Po zatwierdzeniu tablica ARP naszego servera        zostanie zatruta i ruch kierowany jest przez nasz komputer.
   Przechodzimy do nowego terminala, aby uruchomić program wireshark (`sudo wireshark`).
   Teraz należy wygenerować ruch w sieci, np. na maszynie użytkownika dodajemy post lub przechodzimy między podstronami. Na maszynie intrudera w programie wireshark        powinniśmy zaobserwować przychodzące pakiety. Wybieramy jeden, w którym możemy spodziewać się ciasteczka zawierającego aktywną sesję, np. HTTP FOUND. `Prawy klik -> Follow->TCP Stream`, aby przejrzeć zawartość. Wyszukujemy ciasteczko sesji, które będzie miało postać: `session=value`. 
   Po skopiowaniu klucza przechodzimy do wyszukiwarki, a następnie pod adres serwera. W narzędziu developerskim (`F12`) w zakładce `storage` możemy dodać nowe              ciasteczko do strony. Ustawiamy Name jako `session` oraz znalezione value. Należy pamiętać, aby Path było ustawione na całą stonę czyli `/`.
   Po odświeżeniu strony powinniśmy być zalogowani na koncie użytkownika.


3. Zmodyfikuj kod funkcji rejestracji, aby odrzucał 20 najbardziej popularnych haseł w 2021 roku. Przykładowa lista haseł: https://nordpass.com/most-common-passwords-list/

# Prezentacja
https://docs.google.com/presentation/d/1VHsevdzyd-CnxhlPBOJbweRi-UJhIw3UJ980ccOon9U/edit?fbclid=IwAR3bi9VFHfHaNWELvhZCXvp0igylMPFZljIRKw52ooFPLpzjIzNvWR7VG1Y#slide=id.g1c9161ba606_0_152
