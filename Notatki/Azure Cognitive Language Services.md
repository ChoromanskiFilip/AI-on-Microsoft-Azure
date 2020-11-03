# Azure Cognitive Language Services

Cognitive Language Services mogą służyć do analizy tekstu, odgadywania zamiarów, wykrywania treści dla dorosłych oraz przetwarzania języka naturalnego.

## Azure Content Moderator

### Intro


Serwis ten pozwala na automatyczne nadzorowanie zawartości obrazów, tekstu oraz wideo.

#### Główne funkcje:

- **Wykrywanie wulgaryzmów**

	API pozwalające na wykrywanie wulgaryzmów w tekście. Przyjmuje na wejście tekst, a zwraca liste wulgaryzmów występujących w tekście wraz z miejscem, w którym występuje.

- **Klasyfikacja** tekstu do niżej opisanych kategorii

	API przyjmujące na wejścje tekst, a zwracające wynik określający prawdopodobieństwo przypisania do każdej z niżej wymienionych kategorii (wartosc z przedziału 0-1).

	- ***Category 1***: Potencjalna obecność języka, który w pewnych sytuacjach może zostać uznany za jednoznacznie seksualny lub dla dorosłych.
	- ***Category 2***: Potencjalna obecność języka, który w niektórych przypadkach może być uznany za dwuznaczny lub dojrzałysituations.
	- ***Category 3***: Potencjalna obecność języka, który może zostać uznany za obraźliwy w pewnych sytuacjach.

- **Wykrywanie danych osobowych**
	
	API pozwalajace na wykrywanie danych osobowych, takich jak:
	- Adres eamail
	- Adres pocztowy w USA
	- Adres IP
	- Numer telefonu w USA
	- Numer telefonu w Wielkiej Brytanii
	- Numer ubezpieczenia
	API przyjmuje na wejściu tekst, a zwraca obiekt JSON z wystąpieniami różnego typu danych osobowych, pogrupowanych po typie.

### Use case'y

Przykładowo można użyć tego serwisu do filtrowania wpisów na forum. W bardzo prosty sposób pozwoli to nam na wprowadzenie filtru wulgaryzmów oraz treści nieodpowiednich lub dyskryminujących. Dodatkowo możemy zapobiec przechowywaniu wrażliwych danych osobowych przypadkowo wprowadzonych przez użytkowników forum.

### Jak użyć serwisu?
1. Wejść na strone [Azure portal](portal.azure.com).
2. Stworzyć nowy zasób *Content Moderator*
3. Będąc w widoku stworzonego zasobu, z panelu po lewej stronie wybrać *Keys and Endpoints* i skopiować jeden z kluczy.
4. Teraz mozna korzystać z zasobu wysyłając zapytania do API na adres o podanej strukturze:
`https://{endpoint}/contentmoderator/moderate/v1.0/ProcessText/Screen[?autocorrect][&PII][&listId][&classify][&language]`

Wiecej informacji o API [tutaj](https://westus.dev.cognitive.microsoft.com/docs/services/57cf753a3f9b070c105bd2c1/operations/57cf753a3f9b070868a1f66f)
### Pricing
`Na dzień 3 listopad 2020.`

Istnieja 2 rodzaje planów:
1. Free	- 1 transakacja na sekunde - 5,000 darmowych transakcji na miesiąc

2. Standard - 10 transakcji na sekunde - w zależności od liczby transakcji: 
	- 0-1M transakcji - $1 za 1,000 transakcji
	- 1M-5M transakcji - $0.75 za 1,000 transakcji
	- 5M-10M transakcji - $0.60 za 1,000 transakcji
	- 10M+ transakcji - $0.40 za 1,000 transakcji


## Language Understanding Intelligent Service (LUIS)
LUIS to usługa wchodząca w skład Azure Cognitive Services, która zapewnia API pozwalające na wykrywanie znaczenia oraz istotnych informacji z tekstu.

### Intro
LUIS analizuje tekst wykorzystując 3 główne aspekty:

- Utterances (*Wypowiedź*): Wypowiedź czyli dane tekst wprowadzany przez użytkownika, który musi zostać zinterpretowany.
- Intents (*Intencje*): Intencja reprezentuje zadanie lub akcje, którą użytkownik chce wykonać. Jej zamiar wyrażony jest w wypowiedzi.
- Entities (*Encje*): Encje reprezentują słowa lub frazy zawarte w wypowiedzi, którą chcemy wyodrębnić.


### Use case'y

Przykładowym wykorzystaniem może być wyszukiwarka pozwalająca na odnajdowanie w dokumentach informacji na podstawie kontekstu i znaczenia, a nie tak jak zwykle ma to miejsce słów kluczowych. 

### Jak użyć serwisu?
1. Wejść na strone [Azure portal](portal.azure.com).
2. Stworzyć nowy zasób *Language Understanding* (type LUIS in search)
3. Za pośrednictwem jednego z poniższych linków nalzeży stworzyć nową aplikacje:
	- North America: [https://www.luis.ai/](https://www.luis.ai/)
	- Europe: [https://eu.luis.ai/](https://eu.luis.ai/)
	- Australia: [https://au.luis.ai/](https://au.luis.ai/)
4. W stworzonej aplikacji, stworzyć baze danych składającą się z Intencji oraz Encji.
5. Wytrenować model LUIS.
6. Stworzyć endpoint dzięki któremu będzie można korzystać z usługi LUIS w aplikacji.

### Pricing
`Na dzień 3 listopad 2020.`

Istnieja 2 rodzaje planów:
1. Free - 5 transakacji na sekunde - 10,000 darmowych transakcji na miesiąc - tylko przetwarzanie tekstu

2. Standard - 50 transakacji na sekunde :
	- przetwarzanie tekstu - $1.50 za 1,000 transakcji
	- przetwarzanie mowy - $5.50 za 1,000 transakcji



## Text Analytics API


### Intro
Text Analytics API jest to usługa, która pomaga na wydobyć informacje z tekstu. Pozwala on na zidentyfikowanie języka używanego przez użytkownika, wykrycie sentymentu jakim charakteryzuje się tekst, wyodrębnienie kluczowych fraz oraz zidentyfikowanie dobrze znanych encji.

Przykładowo korzystając z wykrywania sentymentu, w odpowiedzi dostajemy wartość z przedziału 0-1, gdzie wartości bliżej zera świadczą o negatywnym sentymencie, a bliżej 1 o pozytywnym.

### Use case'y
Automatyczne badanie ankiet przeprowadzanych pod koniec każdego semestru na uczelni. Dzięki temu moglibyśmy uzyskać obiektywny wskażnik mówiący nam o ogólnym zadowoleniu wśród studentów.

### Jak użyć serwisu?
1. Wejść na strone [Azure portal](portal.azure.com).
2. Stworzyć nowy zasób *Text Analytics* 
3. Będąc w widoku stworzonego zasobu, z panelu po lewej stronie wybrać *Keys* i skopiować jeden z kluczy.
4. Następnie za pośrednictwem strony:
https://[location].dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0
Możemy użyć jednej z dostępnych metod i wysłać zapytanie.


### Pricing
`Na dzień 3 listopad 2020.`

Istnieja 7 rodzaji planów:
1. **Free** - 5,000 darmowych transakcji na miesiąc
2. **Standard**: 
	- 0-500,000 rekordów - $2 za 1,000 rekordów
	- 0.5M-2.5M rekordów - $1 za 1,000 rekordów
	- 2.5M-10.0M rekordów - $0.50 za 1,000 rekordów
	- 10M+ rekordów - $0.25 za 1,000 rekordów
3. **S0 - $74.71/miesiąc** - Do 25,000 transakcji na miesiąc - Średnio: $3 za 1,000 transakcji
4. **S1 - $249.86/miesiąc** - Do 100,000 transakcji na miesiąc - Średnio: $2.50 za 1,000 transakcji
5. **S2 - $999.75/miesiąc** - Do 500,000 transakcji na miesiąc - Średnio: $2 za 1,000 transakcji
6. **S3 - $2,499.84/miesiąc** - Do 2,500,000 transakcji na miesiąc - Średnio: $1 za 1,000 transakcji
7. **S4 - $4,999.99/miesiąc** - Do 10,000,000 transakcji na miesiąc - Średnio: $0.50 za 1,000 transakcji