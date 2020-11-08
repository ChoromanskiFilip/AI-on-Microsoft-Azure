# Azure Cognitive Speech Services

## Speech-to-Text

### Intro
Funkcja serwisu Cognitive Speech Services - Speech-to-Text - pozwala na dokonywanie transkrypcji strumienia audio. W aplikacji wykorzystujący ten serwis możemy wyświetlać tekst powstaly z transkrypcji oraz traktować go jako dane przekazane przez użytkownika.

#### Główne możliwości:
- tłumaczenie prezentacji na żywo
- tłumaczenie konwersacji
- automatyczna obsługa klienta
- tworzenie podpisów pod filmami lub plikami audio
- interakcje przy pomocy sztuczej inteligencji w różnych językach

### Use case'y
Automatyczne tworzenie napisów pod filmami na platformie streamingowej.

### Jak użyć serwisu?
1. Wejść na strone [Azure portal](portal.azure.com).
2. Stworzyć nowy zasób *Speech*
3. Będąc w widoku stworzonego zasobu, z panelu po lewej stronie wybrać *Keys and Endpoints* i skopiować jeden z kluczy.
4. Teraz mozna korzystać z zasobu wysyłając zapytania do API przy pomocy gotowych bibliotek w Pythonie lub C#.


### Pricing
- **Free** - 1 zapytanie jednocześnie:
	- ***Standard*** - 5 godzin audio za darmo na miesiąc
	- ***Custom*** - 5 godzin audio za darmo na miesiąc; Endpoint hosting: 1 darmowy model za darmo na miesiąc
	- ***Conversation transcription multi-channel audio*** - godzin audio za darmo na miesiąc

- **Standard** - 20 zapytań jednocześnie:
	- ***Standard*** - $1.28 za godzine audio
	- ***Custom*** - $1.792 za godzine audio; Endpoint hosting: $1.6517 za model za godzine
	- ***Conversation transcription multi-channel audio*** - $2.69 per za godzine audio


## Text-to-Speech

### Intro
Text-to-Speech to inaczej syntezator mowy. Działa on podobnie jak inne tego programy: czyli podajemy jakiś tekst, który ma zostać przeczytany przez automat, a na wyjściu otszymujemy strumień audio. Do wyboru mamy kilka głosów.

Do wyboru mamy 2 rodzaje głosów:
- **Standard** - natualnie brzmiące głosy, zrozumiałe dla słuchacza
- **Neural** - głosy dodatowo wzmocnione siecią głębokiego uczenia, które dodają umiejętności ukazywania stresu oraz intonacji do wymawianego tekstu

### Use case'y
Wtyczka do przeglądarki pozwalająca na odczytywanie artykułów ze stron internetowych.


### Jak użyć serwisu?
Tak samo jak dla Speech-to-Text - wykorzystujemy inne funkcje / klasy z biliotek dla C# lub Python.


### Pricing
- **Free** - 1 zapytanie jednocześnie:
	- ***Standard*** - 5 milinów znaków na miesiąc za darmo 
	- ***Neural*** - pół miliona znaków na miesiąc za darmo 
	- ***Custom*** - 5 milinów znaków na miesiąc za darmo; Endpoint hosting: 1 darmowy model za darmo na miesiąc

- **Standard** - 20 zapytań jednocześnie:
	- ***Standard*** - $5.12 za 1 milion znaków
	- ***Neural*** - $20.48 za 1 milion znaków; Tworzenie długich audio: $128 za 1 milion znaków
	- ***Custom*** - $7.68 za 1 milion znaków; Endpoint hosting: $0.0688 za model za godzine
	- ***Custom Neural*** - $30.72 za 1 milion znaków; Endpoint hosting: $5.17 za model za godzine; Tworzenie długich audio: $128 za 1 milion znaków


## Speech translation

### Intro
Serwis pozwalający na tłumaczenie w czasie rzeczywistym wypowiadanych fraz i natymiastowe odczytywanie przetłumaczonych wypowiedzi. Serwis pozwala na tłumaczenia w różnych językach oraz automatyczne wykrywanie języka w jakim otrzymuje audio.


### Use case'y
Robot witający gości w hotelu oraz udzielający informacji gościom w różnych językach.


### Jak użyć serwisu?
Tak samo jak dla Speech-to-Text - wykorzystujemy inne funkcje / klasy z biliotek dla C# lub Python.


### Pricing
- **Free** - 1 zapytanie jednocześnie - 5 godzin audio za darmo na miesiąc

- **Standard** - 20 zapytań jednocześnie - $3.20 za godzinę audio