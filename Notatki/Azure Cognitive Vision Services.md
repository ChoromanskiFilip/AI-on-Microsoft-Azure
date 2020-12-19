# Azure Cognitive Vision Services

## Face API

### Intro
Usługa zapewnia algorytm, udostępniony za pośrednictwem RESTowego web serwisu. Algorytm pozwala na wykrywanie, analizowanie oraz rozpoznawanie twarzy. Serwis pozwala na sprawdzanie podobieństwa twarzy i wyznaczanie cech dla danej twarzy (wiek, płeć, intensywność uśmiechu, zarost, poza, emocje). Face API potrafi również grupować ludzi o podobnych twarzach do tych samych kategorii.

Face API używa sztucznej inteligencji do:
- wykrywania aktywności ludzi na zdjęciach
- dopasowywania twarzy do tych istniejących w bazie danych
- wyznaczania położenia twarzy na zdjęciu i zwracania koordynat
- analizowania i wykrywania twarzy w wideo

### Use case'y
- System autoryzujący wejście do pomieszczenia na podstawie wyglądu twarzy.
- Algorytm porównujący twarze - nie trzeba wtedy przejmować się segmentacją obrazy i wykrywaniem położenia twarzy.
- Przymierzalnia czapek - Face API pozwala na wyciagniecie twarzy z obrazu, nastepnie można obslużyć nałożenie czapki na twarz.


### Pricing
- **Free** - 20 transakcji/min - dla *Face Detection*, *Face Verification*, *Face Identification*, *Face Grouping*, *Similar Face Search*: 50 000 darmowych transakcji na miesiąc

- **Standard** - 10 transakcji/s 
    - dla *Face Detection*, *Face Verification*, *Face Identification*, *Face Grouping*, *Similar Face Search*:
        - 0-1M transakcji - $1 za 1,000 transakcji
        - 1M-5M transakcji - $0.80 za 1,000 transakcji
        - 5M-100M transakcji - $0.60 za 1,000 transakcji
        - 100M+ transakcji - $0.40 za 1,000 transakcji

    - dla *Face Storage*:
        - $0.01 za 1,000 twarzy na miesiąc


## Computer Vision API

### Intro
Usluga dostarcza algorytmy służące do przetwarzania obrazów oraz zwraca informacje, które można z nich wyczytać. Przykładowo można sprawdzić czy zawartość obrazka jest odpowiednia dla dzieci. Serwis ma również takie funkcje jak: kategoryzowanie zawartości zdjęć, opisywanie zdjęć za pomocą pełnych zdań w języku Angielskim.

Aby skorzystać z usługi należy stworzyć serwis za pośrednictwem [Portal Azure](porta.azure.com), wygenerować klucz i wysłać zapytanie do jednego z endpointów. 

### Use case'y
- Analiza filmów i wykrywanie otoczenia.
- Rozpoznawanie nazw budynków na zdjęciach.
- Digitalizacja dokumentów 

### Pricing
- **Free** - 20 transakcji/min - 5,000 transakcji na miesiąc za darmo

- **S1** - 10 transakcji/s 
    - dla *Face*, *GetThumbnail*, *Color*, *Image Type*, *GetAreaOfInterest*:
        - 0-1M transakcji - $1 za 1,000 transakcji
        - 1M-5M transakcji - $0.80 za 1,000 transakcji
        - 5M-10M transakcji - $0.65 za 1,000 transakcji
        - 10M-100M transakcji - $0.65 za 1,000 transakcji
        - 100M+ transakcji - $0.65 za 1,000 transakcji

    - dla *OCR*, *Adult*, *Celebrity*, *Landmark*, *Detect, Objects*, *Brand*:
        - 0-1M transakcji - $1.50 za 1,000 transakcji
        - 1M-5M transakcji - $1 za 1,000 transakcji
        - 5M-10M transakcji - $0.65 za 1,000 transakcji
        - 10M-100M transakcji - $0.65 za 1,000 transakcji
        - 100M+ transakcji - $0.65 za 1,000 transakcji

    - dla *Describe+*, *Read*:
        - $2.50 za 1,000 transakcji 

    - dla *Spatial analysis*:
        - Darmowe podczas preview


## Custom Vision

### Intro
Usługa ***Custom Vision*** pozwala na stworznie niestandardowego modelu do klasyfikacji zdjęć, który trzeba nauczyć na podstawie zetkietowanych zdjęć, które dostarczymy. 


### Use case'y
- Rozpoznawanie rasy psa ze zdjęcia.


### Pricing
- **Free** - 2 transakcji/s:
    - *Upload, trenowanie i wyliczanie predykcji*:
        - 5,000 obrazów w zbiorze treningowym za darmo na projekt
        - 10,000 predykcji na miesiąc za darmo
    - limity: 
        - *Do 2 projektów*
        - *Do 1 godziny trenowania modelu na miesiąc*

- **Standard** - 10 transakcji/s: 
    - *Transakcje upload'u oraz wyliczania predykcji* - $2 za 1,000 transakcji
    - *Trenowanie* - $20 za godzine obliczeń
    - *Przechowywanie obrazów* (każdy obraz do 6 MB) - $0.70 za 1,000 obrazów


## Video Indexer

### Intro
Azure Video Indexer to usługa pozwalająca na wydobywanie informacji z plików multimedialnych. Używa ona modeli uczenia maszynowego, które mogą być dostosowywane do własnych potrzeb. Informacje jakie możemy wykryć przy pomocy tego serwisu to między innymi:
- identyfikowanie twarzy,
- rozpoznawanie tekstu,
- etykietowanie obiektów,
- segmentacja.

Dodatkowe informacje możemy wydobyć ze ścieżki audio, takie jak:
- transkrypcja,
- detekcja emocji.

### Use case'y
- Tworzenie napisów do filmów.
- Zczytywanie numerów rejestracyjnych z monitoringu ulicznego.

### Pricing
- **Free** 
    - do 10 godzin darmowego indeksowania wideo dla użytkowników korzystających ze stronyc internetowej 
    - do 40 godzin dla użytkowników korzystających z API

- **Standard** 
    - Audio/Video Analysis - 0.035$ za minutę
    - Encoding 
        - Standard - 0.015$ za minutę
        - Premium - 0.015$ za minutę
    - Streming 
        - Standard - 2.15$ za dzień
        - Premium - 4.64$ za dzień
