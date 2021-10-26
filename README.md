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


**Disclaimer**: räägin enda kogemustest ja mõtetest ehk ilmselgelt info on kallutatud. Te ei pruugi sama arvata või samadest asjadest huvitatud olla ja see ok. See on osa konteksti loomisest - nüüd teate, et see ei huvita vms.

---

## Hea tuju dieet ehk miks matemaatika/statistika

Ruttan veidi ette, aga:
* suure tõenäosusega hakkate koodi kirjutama
  * (kuigi mitte päris sellist nagu "tavalised" programmeerijad).
* Ebaefektiivne kood võib töö ära teha küll, aga see võib uusi probleeme tekitada.

Järgnev näide ei ole tööst võetud, kuid tuli mul ennast täiendades ette.

See on lihtne näide, kus näeme kuidas matemaatika/statistika teadmisi kasutades on võimalik programmi efektiivsust oluliselt tõsta.

[Näide: populatsiooni kasv](https://github.com/moledoc/statistikuks_kujunemine/tree/main/codewars_example)



<!-- ### Andmetest lugeda välja päeva kulgu, ilma et ma teaks õppusest midagi -->
<!-- TODO: -->
<!-- [naide2](https://github.com/moledoc/statistikuks_kujunemine/tree/main/oppus) -->

---

<!-- TODO: -->

## Minu aeg Tartu Ülikoolis retrospektiivselt

Esiteks

Mõttetera:
* mõelge ainetest ja teadmistest kui tööriistadest:
  * teil ei pea iga tööriist kaasas olema, paljude puhul on oluline oskus seda kasutada ja ära tunda (nt populatsiooni kasvu näide).
  * ja kui teil peaks tööriista vaja minema (ja seda ei pruugi üldse ette näha), siis teil on see kohe/lühikese ajaga võimalik kasutusele võtta.

Miks selline mõttetera/miks ma sellega alustasin?
* Mõne aine puhul võib teil tekkida küsimsed:
  * Miks ma seda õpin?
  * Kus ma seda kasutan?
  * Mis kasu mul sellest on?
* Iga teadmise kohta ei oska ma veel näidet tuua, aga mõne kohta küll.

---

### Tuttav kontseptsioon

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

**Aga kas seda kõike oleks ka lihtsamalt saanud?**


Ma ei oodanud leida supreemumi kontseptsiooni, aga
* selles oli äratundmise rõõm;
* lihtsustas minu tööd: lihtsustas mõttetööd ja lahenduse idee edasiandmist;
    * kuigi ma ei kasutanud kogu teadmist supreemumi kohta.

---

Järgmine mõttetera:
* selleks, et selgelt infot/ideid/kontseptsioone edasi anda, peate teemat palju kõrgemal tasemel tundma, kui seda on konkreetne info/idee/kontseptsioon.

Küllaltki loogiline mõttetera, aga vahepeal on kõige raskem lihtsaid asju märgata.

Miks see on oluline?
* Olles tulevased analüütikud, siis enda mõtete, ideede, leidude jm selge edasiandmine on oluline oskus.
* Eriti kuna annate infot edasi inimestele, kes on matemaatikast ja/või arvutitest väga kauged.

Aga nüüd, kuidas minust ikkagi statistik kujunes (kuigi mu ametinimetus seda ei kajasta, hetkel)?

### Bakalaureus




<!-- Hakkan nimetama aineid, teadmisi, ideid jm mida olen kasutanud.

Kui on küsimusi mingi aine, teadmise vms kohta, et kus seda kasutada, siis julgelt märku anda.


* IT-suunamoodul
  * andmebaasid
    * SQL
  * programmeerimise põhikontseptsioonid
    * python - laialt kasutusel data science, analysis, ML
* mõtlemise arendamine ning ideede ja konseptsioonide omandamine: jäägi arvutamisel algebra jäägiklassid mõtteviis -->


Soovitaksin keskenduda koolile, vähemalt esimese 1.5h jooksul.

Kui tunnete, et jaksate rohkem aineid võtta (nagu varasematest loengutest kuuldud), siis tehke seda. Mina ei teinud.

Teise aasta lõpus, suvi vastu kolmandat, kolmanda esimene pool on hea aeg erialaseks tööks.
* juba oskate midagi
* veidi rohkem aega (võib-olla)

Võimalus ka isiklike projektidega alustada
* hea CV jaoks
* enda oskuste arendamisteks ja õpitu rakendamiseks

### Magister

Miks 'Kindlustus- ja finantsmatemaatika'?
* Olin kahevahel: 'Kindlustus- ja finantsmatemaatika' ja 'Arvutiteadusete magister koos andmeteaduse suunamooduliga'
* Valisin AFE (Actuarial and Finanfial Engineering), kuna leidsin, et seda on mõistlikum õppida:
  * seda on raskem iseseisvalt õppida;
  * leidsin, et see annab mulle rohkem lisandväärtust.

Mis siis sai?
* Sain matemaatilise ülevaate kindlustusest ja finantsmatemaatikast.
* Aga mul hakkas tekkima suurem huvi ka arvutiteaduse suunas: madalama taseme programmeerimiskeeled, operatsioonisüsteemid jms,
    * seda ma õppisin kooli kõrval.
* See tähendab, et magistri jooksul sain arendada interdistsiplinaarseid oskusi.
* Eriti kuna käisin ka osakoormusega ka tööl:
  * 3p nädalas oli kool ja 2p oli jäetud vabaks, et saaks tööl käia.


Hakkasin tegema isiklike projekte
* Õpid uusi teadmisi.
* Saad CV's neid näidata ehk tekitad endale portfooliot.

Milliseid projekte tegin
* Programmeerimisprojektid
  * Suures osas peate nkn koodi kirjutama hakkma, oskus hästi programmeerida või jälgida häid tavasid tõstab teie väärtust
  * Oskus kasutada _giti_ või muud versioonihaldus programmi.
  * Näiteks kulude programm r-shiny'ga
* Operatsioonisüsteemid
  * Paljud andmebaasid asuvad linuxis, mistõttu baasteadmisi omada on hea.
* Kui oleks jõudnud, siis ka andmeteaduse projekte
  * vaadake nt kaggle.com ringi

---


## Soovitused

* Koos õppimine muudab
    * õppimise meeldivamaks
    * kergem ja vähendab stressi
    * tekitab meeldejäävaid olukordi
        * aeg ülikoolis võiks olla ka positiivselt meeldejääv
    * ühtsustunne ja sõprus
* täiendavad huvid
    * isiklikud projektid
    * täiesti muu teemaga kurssi viimine
    * interdistsiplinaarsed oskused
* tööriistad/programmeerimiskeeled/mõttemaailm/(täiendavad)ained, mis tuleb kasuks
    * git
    * linux
    * oskus jälgida, et kood oleks loetav ja efektiivne ning dokumenteeritud

Mida ma ise oleks tahtnud veel teha
* [Parem konspekteerimine](https://www.youtube.com/watch?v=MYJsGksojms&list=WL&index=29&t=42s)
    *  Ei pea seda tööriista kasutama, on palju erinevaid võimalusi
        * vimwiki (norra keel)
        * Rmarkdown (magistritöö)
---
