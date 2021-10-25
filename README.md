<h1>
    <center>
    Statistikuks kujunemine
    </center>
    <center>
    <span style="font-size:20px">
    <br>Meelis Utt
    </span>
    </center>
</h1>

---

## Kava

* Kes ma olen ja miks ma siin olen
* Hea tuju dieet ehk mis kasu või kus ma kasutan matemaatikat ja matemaatilist statistikat
    * Tuttav kontseptsioon
    * Andmetest lugeda välja päeva kulgu, ilma et ma teaks õppusest midagi
    * codewars näide w/ Go and python
* Minu aeg Tartu Ülikoolis
    * baka
        * koolitöö ja -elu
        * töö
    * magister
        * koolielu ja -töö
        * huvid (OpSys, madalama taseme programmeerimiskeeled)
        * töö


* soovitused
    * koos õppimine: esiteks toredam, teiseks kergem ja väiksem stress õppimisel
    * täiendavad huvid
    * konspektid: video obsidianist
    * tööriistad/programmeerimiskeeled/mõttemaailm/(täiendavad)ained, mis tuleb kasuks
* Kokkuvõte

---

<table>
<tr>
<th> Kes ma olen </th>
<th> Miks ma siin olen </th>
</tr>
<tr>
<td>

* 2016-2019 Matemaatilise statistika bakalaureus
* 2019-2021 Actuarial and financial engineering
    * (Kindlustus- ja finanstmatemaatika)

Lisaks

* 2018-04-09 - 2018-05-20   erialane praktika KVÜÕA RAK
* 2018-08-17 - 2018-12-31   HeiVäl Consulting: andmeanalüütik
* 2019-06-01 - 2021-03-14   Resta: analüütik/arendaja/andmetehnik
* 2021-03-14 - ...          Omniva: andmeanalüütik/andmetehnik
</td>
<td>

* Sest Mare kutsus mind
* Võimalus anda konteksti ja soovitusi uutele õppijatele
* Võimalus saada ise uusi kogemusi ja õppida
* Peamine eesmärk on anda konteksti
    * õpitule
    * järgnevale 3-5+ aastale

</td>
</tr>
</table>

---

<!-- TODO: -->
## Hea tuju dieet ehk mis kasu või kus ma kasutan matemaatikat ja matemaatilist statistikat

<!-- TODO: -->

### Tuttav kontseptsioon

Näide Omnivast.

Olgu meil

* teenindusjuhtumi avamise ja sulgemise aeg
* vastutava meeskonna tööajad (ajas muutuvad)

Vaja

* leida teenindusjuhtumile kulunud reaalne tööaeg
* (ilma loogilise muutuseta) implementeerida R'i kood SQL'i

Näide meeskondade tööaja tabelist

| Meeskond | Nädalapäev | Töötunde | Kehtiv kuni |
|--------- | ---------- | -------- | ----------- |
| paki     | 1          | 8        | 2050-01-01  |
| paki     | 2          | 8        | 2050-01-01  |
| paki     | 3          | 4        | 2050-01-01  |
| paki     | 4          | 4        | 2050-01-01  |
| paki     | 5          | 8        | 2050-01-01  |
| paki     | 6          | 4        | 2050-01-01  |
| paki     | 7          | 4        | 2050-01-01  |
| paki     | 2          | 6        | 2021-09-23  |
| paki     | 2          | 4        | 2021-09-29  |
| paki     | 2          | 3        | 2021-10-25  |
| paki     | 5          | 8        | 2021-09-24  |
| paki     | 6          | 5        | 2021-09-06  |
| paki     | 7          | 7        | 2021-09-13  |


Teenindusjuhtum
* avati 2021-08-29
* suleti 2021-10-26

Üldine loogika:
* simuleerime teenindusjuhtumi kulgu päeva kaupa

```
2021-08-29
2021-08-30
2021-09-01
...
2021-10-26
```

* simuleeritud aja ning tööaegade tabeli ühendamisel loome eeldused selleks, et leida iga päeva reaalse tööaja

Probleem:
* teisipäeva (nädalapäev = 2), reede, laupäeva ja pühapäeva kohta tekib mitu rida, kuidas me teame milline on õige.

Lahendus:
* Meil oleks vaja võtta vastava kuupäeva kohta väikseima `Kehtiv kuni` väärtusega meeskonna töötundidega rida.
* Probleem:
    * Sellise kohmaka definitsiooniga on keeruline töötada, kui peas peab andmete kulgu visualiseerima
    * Kas meil on mingi tuttav mõiste, mis võtab lahenduse sisu kokku?
* Lahendus:
  * Tegemist on ju supreemumiga
  * See on tuttav kontseptsioon ning seetõttu on sellega lihtsam töötada


**Aga kas oleks ka lihtsamalt saanud?**


### Andmetest lugeda välja päeva kulgu, ilma et ma teaks õppusest midagi

### codewars näide w/ Go and python

[naide3](https://github.com/moledoc/statistikuks_kujunemine/tree/main/codewars_example)

---

<!-- TODO: -->
## Minu aeg Tartu Ülikoolis
### baka
#### koolitöö ja -elu
#### töö
### magister
#### koolielu ja -töö
#### huvid (OpSys, madalama taseme programmeerimiskeeled)
#### töö
---

<!-- TODO: -->
## soovitused
### koos õppimine: esiteks toredam, teiseks kergem ja väiksem stress õppimisel
### täiendavad huvid
### konspektid: video obsidianist
### tööriistad/programmeerimiskeeled/mõttemaailm/(täiendavad)ained, mis tuleb kasuks
---

<!-- TODO: -->
## Kokkuvõte