#Azure Bot Service

## QnA Maker

### Intro
Usłgua pozwalająca na tworzenie i publikowanie bazy wiedzy ze zdolnościami do przetwarzania języka naturalnego. Baze wiedzy można stworzyć na 2 sposoby:
- wykorzystując REST'owe API
- z pomocą UI, z poziomu QnA Maker portalu

Po stworzeniu zestawu pytań i odpowiedzi należy wytrenować model, po czym można go przetwestować. Na sam koniec trzeba już tylko opublikować model i można zacząć go wykorzystywać w aplikacji.


### Use case'y
Strona FAQ dla nowych studentów wydziału elektrycznego Politechniki Warszawskiej. Strona będzie miała możliwość wyszukiwania pytań z bazy wiedzy. Będzie to o tyle lepsze od standardowego FAQ listą pytań, że nie będzie trzeba wyszukiwać dokładnej treści pytania, które istnieje, a jedynie do wyszukiwarki wystarczy wpisać to jakich informacji potrzebujemy. Pomaga w tym nauczony model, który potrafi przetwarzać język naturalny.


### Pricing
- **Free** -  3 transakcji/s - każdy dokument o rozmiarze do 1 MB; do 100 transakcji na minutę; do 50 000 transakcji na miesiąc - bezpłatne dokumenty zarządzane na miesiąc: 3
- **Standard** - 3 transakcji/s - do 100 transakcji na minutę - €8,433 dla nieograniczonej liczby zarządzanych dokumentów


## Azure Bot Service

### Intro
Usluga zapewniająca framework do tworzenia, publikowania oraz zarządzania botem na Azure. 

Bot można stworzyć na 2 sposobu:
- z poziomu QnA Maker portalu, gdzie mamy możliwość na stworzenie bota dla stworznej już bazy wiedzy
- przy pomocy Microsoft Bot Framework SDK, dzieki czemu mamy możliwość na zmodyfikowanie kodu bota.

Po stworzeniu bota, można zarządzać nim z poziomu portalu Azure, gdzie można:
- rozszerzać funkcjonalności bota dodając własny kod
- przetestować bota w interaktywnym interfejsie do testowania
- skonfigurować logi, anzlizę danych oraz integrację z innymi serwisajmi.

Kiedy bot jest już gotowy można połączyć go z różnymi kanałami komunikacji:
czat na stronie internetowej, email, Microsoft Teams lub inne komunikatory.


### Use case'y
Bot, który udzielający podstawowej pomocy kliento telekomu.


### Pricing
|   | FREE | S1 |
|---|---|---|
| Standard channels | Unlimited messages | 10,000 messages/month |
| Premium channels | Unlimited messages | $0.50 per 1,000 messages |



## Bot Framework Composer

### Intro
Bot Framework Composer to wizualny kreator pozwalający na szybkie i łatwe tworzenie zawansowanych botów do konwersacji bez pisania kodu.

W aplikacji możemy tworzyć zaawansowane workflow, na których oparte będzie działanie bota. Po stworzeniu takiego workflow można je później opublikować do jednego z 2 serwisów Azure Functions lub Azure Web App. 

### Use case'y
Bot pozwalający na umówienie wizyty u lekarza.

### Jak użyć serwisu?
Aby korzystać z Bot Framework Composer należy go na początku zainstalować [LINK](https://aka.ms/bf-composer-download-win).
Dodatkowo wymagane jest zainstalowanie Bot Framework Emulator oraz posiadanie .NET Core SDK 3.1.

Po zainstalowaniu aplikacji możena zacząć tworzenie przebiegów dla bota, a na konću stworzonego bota opublikować.

### Pricing

Usługa darmowa