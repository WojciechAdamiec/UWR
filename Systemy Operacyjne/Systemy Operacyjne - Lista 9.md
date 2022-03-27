# Systemy Operacyjne - Lista 9

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 3

### Zadanie 1.
:::info
![](https://i.imgur.com/Dddn2lH.png)
:::

![](https://i.imgur.com/R6hQ8rQ.png)

**Warstwa łącza**:

Warstwa odpowiedzialna za przesłanie pakietu do następnego noda na trasie.

Przykłady protokołów: Ethernet, WiFi

**Warstwa sieciowa**:

Wartstwa odpowiedzialna ze przesyłanie pakietów między komputerami.

Protokół: IP

**Warstwa transportowa**:

Warstwa odpowiedzialna za przesyłanie pakietów między endpointami aplikacji. 

Przykłady protokołów: TCP, UDP

### Zadanie 2.
:::info
![](https://i.imgur.com/HinR0Ks.png)
:::

**UDP**

* Nie ma gwarancji, że pakiet dotrze na miejsce
* Nie ma gwarancji, że pakiety dotrą we właściwej kolejności
* Nie ma gwarancji, że pakiet dotrze do celu tylko raz
* datagram UDP ma ustaloną długość, którą przesyła się razem z danymi
* UDP umożliwia *connectionless service*, To znaczy potrafi np. stworzyć gniazdo i wysłać datagram do danego serwera, a potem natychmiast tym samym gniazdem wysłać inny datagram do innego serwera. Podobnie server UDP może odebrać wiele różnych datagramów na jednym gnieździe, każdy od innego klienta. 

**TCP**

* Protokół polega na połączeniach klient-serwer. Klient TCP łączy się z serwerem, następuje wymiana danych, a następnie połączenie zostaje przerwane.
* TCP zapewnia niezawodność. Gdy wysyła dane na drugi koniec to wymaga odesłania potwierdzenia. Jeśli nie dostanie potwierdzenia pakiet zostaje wysłany ponownie. Jeśli problem będzie się długo powtarzał zakomunikuje porażkę w połączeniu.
* zawiera algorytm do dynamicznego szacowania *round-trip-time*.
* TCP zapewnia poprawne przestawienie kolejności i eliminację zduplikowanych segmentów.
* TCP zapewnia *flow control*.
* full-duplex

**Flow control**:

TPC powiadamia innych ile bajtów danych jest w stanie przyjąć na jeden raz. Idea jest taka, żeby nie dochodziło do przepełnienia bufora. Ta wartość (*window*) zmienia się czasie, gdy dochodzą nowe dane, lub aplikacja czyta z bufora. Gdy bufor się cały zapełni wartość window może być 0, co znaczy, że nie można już przyjąć więcej danych.

---

TCP also sequences the data by associating a sequence number with every byte that it sends. For example, assume an application writes 2,048 bytes to a TCP socket, causing TCP to send two segments, the first containing the data with sequence numbers 1–1,024 and the second containing the data with sequence numbers 1,025–2,048. (A segment is the unit of data that TCP passes to IP.) 

![](https://i.imgur.com/8Y6iaB5.png)
np. Ethernet, telefonia komórkowa

![](https://i.imgur.com/ULUZwKh.png)
np. CB radio, walkie-talkie

### Zadanie 3.
:::info
![](https://i.imgur.com/1TIO2M9.png)
:::

**Komunikacja klient-serwer**

Architektura systemu komputerowego polegająca na podziale zadań: Serwer zapewnia usługi dla klientów, zgłaszających do serwera żądania obsługi (*service request*)

**Gniazdo strumieniowe**

Gniazda oparte na połączeniach, umożliwiają sekwencyjny przepływ danych z gwarancją dostarczenia pakietu i zachowania kolejności.

Stream sockets
Connection-oriented sockets, which use Transmission Control Protocol (TCP), Stream Control Transmission Protocol (SCTP) or Datagram Congestion Control Protocol (DCCP). A stream socket provides a sequenced and unique flow of error-free data without record boundaries, with well-defined mechanisms for creating and destroying connections and reporting errors. A stream socket transmits data reliably, in order, and with out-of-band capabilities. On the Internet, stream sockets are typically implemented using TCP so that applications can run across any networks using TCP/IP protocol.

![](https://i.imgur.com/iujmObg.png)

![](https://i.imgur.com/VnCJDW4.png)
![](https://i.imgur.com/sZe2S21.png)
![](https://i.imgur.com/rUAnBnC.png)
![](https://i.imgur.com/uVIuGUE.png)
![](https://i.imgur.com/y0PWaHo.png)
![](https://i.imgur.com/ryBpMNr.png)

![](https://i.imgur.com/JVm3ID3.png)

`int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen)` wykorzystywane jest do zaakceptowania połączenia z gniazdem o danym `sockfd`. Wypełnia ono adres gniazda klienta `*addr` i zwraca podłączony deskryptor, który może być wykorzystany do komunikacji z klientem, używając uniksowych operacji I/O. Gniazdo przekazywane do `accept()` jest związane z serwerem, a zwracane z klientem.

![](https://i.imgur.com/Qo0YYDZ.png)

### Zadanie 4.
:::info
![](https://i.imgur.com/D6db6hz.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/Sa4BVoP.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/Xlzyc8h.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/Fwm0L45.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/cZdg8WU.png)
:::

### Zadanie 9.
:::info
![](https://i.imgur.com/QBQ8OqE.png)
:::