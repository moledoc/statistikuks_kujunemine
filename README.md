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

* Haridustee/töö ja miks ma siin olen
* Hea tuju dieet ehk miks matemaatika/statistika
* Minu aeg Tartu Ülikoolis retrospektiivselt
    * Tuttav kontseptsioon
    * Bakalaureus
        * Mis aineid ma siis võtsin?
    * Magister
* Soovitused

Kas on küsimusi, enne kui alustan?
* Võite küsida kohe, kui mõni küsimus tekib.

---

<table>
<tr>
<th> Haridustee/töö </th>
<th> Miks ma siin olen </th>
</tr>
<tr>
<td>

* 2016-2019 Matemaatilise statistika bakalaureus
* 2019-2021 Actuarial and financial engineering
    * (Kindlustus- ja finanstmatemaatika)
    * AFE (KFM)

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
    * õpitule/õppeainetel
    * järgnevale 3-5+ aastale

</td>
</tr>
</table>


**Disclaimer**: räägin enda kogemustest ja mõtetest ehk ilmselgelt info on kallutatud. Te ei pruugi sama arvata või samadest asjadest huvitatud olla ja see ok. Ka see loob teile konteksti.

---

## Hea tuju dieet ehk miks matemaatika/statistika

Ruttan veidi ette, aga:
* suure tõenäosusega hakkate koodi kirjutama
  * (kuigi mitte päris sellist nagu "tavalised" programmeerijad).
* Ebaefektiivne kood võib töö ära teha küll, aga see võib uusi probleeme tekitada.

Järgnev näide ei ole töös ette tulnud, kuid tuli ennast täiendades ette.

[Näide: populatsiooni kasv](https://github.com/moledoc/statistikuks_kujunemine/tree/main/population_growth)

See on lihtne näide, kus näeme kuidas matemaatika/statistika teadmisi kasutades on võimalik programmi efektiivsust oluliselt tõsta.

---

## Minu aeg Tartu Ülikoolis retrospektiivselt

Esiteks mõttetera:
* mõelge ainetest ja teadmistest kui tööriistadest:
  * teil ei pea iga tööriist kaasas olema; paljude tööriistade puhul on oluline oskus seda kasutada ja ära tunda kus seda kasutada saab (nt populatsiooni kasvu näide).
  * Ja kui teil peaks mingit tööriista vaja minema (ja seda ei pruugi üldse ette näha), siis on teil see kohe/lühikese ajaga võimalik kasutusele võtta.

Miks selline mõttetera/miks ma sellega alustasin?
* Mõne aine puhul võib teil tekkida küsimsed:
  * Miks ma seda õpin?
  * Kus ma seda kasutan?
  * Mis kasu mul sellest on?
* Iga teadmise kohta ei oska ma veel näidet tuua, aga mõne kohta küll. Toon ühe näite.

---

### Tuttav kontseptsioon

Olgu meil

* teenindusjuhtumi avamise ja sulgemise aeg
* vastutava meeskonna tööajad (ajas muutuvad)

Vaja

* leida teenindusjuhtumile kulunud reaalne tööaeg

Piirangud
* olemasolevat loogikat ei tohi muuta
* lahendus on tarvilik teha SQL'is

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

* simuleeritud aja ning tööaegade tabeli ühendamisel loome eeldused selleks, et leida iga päeva reaalse tööaja.

Probleem:
* teisipäeva (nädalapäev = 2), reede, laupäeva ja pühapäeva kohta tekib tööaja ja simuleeritud päevad kohta mitu rida
  * Kuidas me teame milline on õige?

Lahendus:
* Meil oleks vaja võtta vastava kuupäeva kohta väikseima `Kehtiv kuni` väärtusega meeskonna töötundidega rida.
* Probleem:
    * Sellise kohmaka definitsiooniga on keeruline töötada, kui peas peab andmete kulgu visualiseerima
    * Kas meil on mingi tuttav mõiste, mis võtab lahenduse sisu kokku?
* Lahendus:
  * Tegemist on ju supreemumiga
  * See on tuttav kontseptsioon ning seetõttu on sellega lihtsam töötada


Ma ei oodanud leida supreemumi kontseptsiooni mitte-matemaatilises töös, aga
* selles oli äratundmise rõõm;
* lihtsustas minu tööd: lihtsustas mõttetööd ja lahenduse idee edasiandmist;
    * kuigi ma ei kasutanud kogu teadmist supreemumi kohta, teadmised ja kogemused selle kontseptsiooniga olid väärtuslikud.

**Aga kas seda kõike oleks ka lihtsamalt saanud, kui me oleks võinud loogikat muuta?**

---

Järgmine mõttetera:
* selleks, et selgelt infot/ideid/kontseptsioone edasi anda, peab teemat palju kõrgemal tasemel tundma, kui seda on konkreetne info/idee/kontseptsioon.

Küllaltki loogiline mõttetera, aga vahepeal on kõige raskem lihtsaid asju märgata.

Miks see on oluline?
* Olles tulevased analüütikud, siis enda mõtete, ideede, leidude jm selge edasiandmine on oluline oskus.
* Eriti kuna annate infot edasi inimestele, kes on matemaatikast ja/või arvutitest väga kauged.

Aga nüüd, kuidas minust ikkagi statistik kujunes (kuigi mu ametinimetus seda ei kajasta, hetkel)?

### Bakalaureus

Soovitaksin keskenduda koolile, vähemalt esimese 1.5a jooksul.

Kui tunnete, et jaksate rohkem aineid võtta (nagu varasematest loengutest kuuldud), siis tehke seda. Mina ei teinud.

#### **Mis aineid ma siis võtsin?**

<table>
<tr>
<th> Sügis </th>
<th> Kevad </th>
</tr>
<tr>
<td>

* analüütline geomeetria
* kõrgem matemaatika I
* matemaatiline maailmapilt
* matemaatilise teksti küljendamine
* programeerimine
* sissejuhatus matemaatilise statistika erialasse


</td>
<td>

* algebra I
* andmeanalüüs I
* erialane inglise k
* kõrgem matemaatika II
* objekt-orienteeritud programmeerimine (OOP)
* tõenäosusteooria ja matemaatiline statistika

</td>
</tr>
<td>

* algoritmid ja andmestruktuurid
* infoturve
* lähis-ida kultuurilugu
* matemaatiline analüüs III
* sissejuhatus finantsmatemaatikasse
* statistika tarkvara R
* tõenäosusteooria ja matemaatiline statistika II

</td>
<td>

* andmeanalüüs II
* andmebaasid
* andmeturve
* militaartehnoloogiad
* monte carlo meetodid
* numbrilised meetodid
* valikuuringute teooria I

</td>
</tr>
<td>

* jaapani kultuur ja ühiskond
* katseplaneerimise teooria
* kõne ning hääle tervishoid
* mitteparameetriline statistika
* populatsioonigeneetika
* tarkvaratehnika
* turu-uuringud

</td>
<td>

* eesti keel (bakalaureusetöö jaoks)
* juhuslikud protsessid
* kvalitatiivsete andmete analüüs
* maatriksid statistikas
* statistiline andmeteadus ja visualiseerimine

</td>
</tr>
</table>


Teise aasta lõpus/suvi vastu kolmandat/kolmanda esimene pool on hea aeg erialaseks tööks:
* juba oskate midagi
* veidi rohkem aega (võib-olla)

Võimalus ka isiklike projektidega alustada
* hea CV jaoks
* enda oskuste arendamisteks ja õpitu rakendamiseks

### Magister

Miks 'Kindlustus- ja finantsmatemaatika'?
* Olin kahevahel: 'Kindlustus- ja finantsmatemaatika' ja 'Arvutiteadusete magister koos andmeteaduse suunamooduliga'
* Valisin KFM, kuna leidsin, et seda on mõistlikum õppida:
  * seda on raskem iseseisvalt õppida
  * leidsin, et see annab mulle rohkem lisandväärtust

Mis siis magistris sai?
* Sain matemaatilise ülevaate kindlustusest ja finantsmatemaatikast.
* Aga mul hakkas tekkima suurem huvi ka arvutiteaduse suunas: madalama taseme programmeerimiskeeled, operatsioonisüsteemid jms,
    * võtsin vastavaid vabaaineid
    * õppisin kooli kõrvalt
* See tähendab, et magistri jooksul sain arendada interdistsiplinaarseid oskusi.
* Eriti kuna käisin ka osakoormusega tööl:
  * 3p nädalas oli kool ja 2p oli jäetud vabaks, et saaks tööl käia.


<table>
<tr>
<th> Sügis </th>
<th> Kevad </th>
</tr>
<tr>
<td>

* distributions in financial mathematics
* life insurance mathematics I
* machine learning
* mathematical statistics I
* non-life insurance mathematics
* risk theory
* simulation methods in financial mathematics
* stochastic models
* time series analysis


</td>
<td>

* C++
* computational finance
* general linear models
* life insurance mathematics II
* martingales
* models in financial mathematics
* operatsioonisüsteemid

</td>
</tr>
<td>

* data engineering
* parallel computing
* professional practice
* (funktsionaalsed) programeerimiskeeled

</td>
</tr>
</table>


Hakkasin tegema isiklike projekte: https://github.com/moledoc
* selleks, et omandada uusi oskusi
* näidata olemasolevaid oskusi
  * hakkab tekkima portfoolio, mida CV's välja tuua


Milliseid projekte tegin
* Programmeerimisprojektid
  * suures osas peate nkn koodi kirjutama hakkama; oskus hästi programmeerida või jälgida häid tavasid tõstab teie väärtust
  * Oskus kasutada _git_'i või muud versioonihaldus programmi.
  * Hea koht kus alustada, on teha midagi, mida te tunnete, et teil vaja oleks; Minu puhul näiteks [kulude jälgimise programm](https://github.com/moledoc/depr_showcase/tree/master/expenses-rshiny)
* Operatsioonisüsteemid
  * \*Unix tüüpi operatsioonisüsteemidega tutvumine
    * _linux_
    * \*BSD
  * Paljud andmebaasid on ülesse seatud _linux_'is, mistõttu baasteadmisi omada on hea
  * suurema võimsusega arvutusserverid kasutavad tihtipeale _linux_'it (kasvõi TÜ enda HPC keskus)
* Kui oleks jõudnud, siis ka andmeteaduse projekte
  * vaadake nt kaggle.com, datacamp.com ringi (ülikooli kaudu võib saada tasuta kursusi)

---

## Soovitused

* Koos õppimine
    * muudab õppimise meeldivamaks
    * on kergem ja vähendab stressi (nt kui millegiga kinni või ei saa mingist teemast aru)
    * tekitab meeldejäävaid olukordi
        * aeg ülikoolis võiks olla ka positiivselt meeldejääv
    * loob ühtsustunnet ja sõprust
* täiendavad huvid
    * isiklikud projektid
    * täiesti muu/uue teemaga kurssi viimine = interdistsiplinaarsed oskused
* Mis minumeelest (sest minul on) tuleb kasuks
    * _git_'i tundmine
    * baasteadmised _linux_'is
    * programmeerimise head tavad
    * oskus kirjutada dokumentatsiooni (koodile, raportile, mudelile jm lahendusele)
    * oskus muuta kood loetavaks (_refactoring_)
    * oskus optimeerida koodi
* omandada oskus/julgus küsida küsimusi

Tagasi vaadates, mida ma tahan, et ma oleks osanud/teinud:
* [Parem konspekteerimine](https://www.youtube.com/watch?v=MYJsGksojms&list=WL&index=29&t=42s)
    *  Ei pea seda tööriista kasutama, on palju erinevaid võimalusi
        * vimwiki (norra keel)
        * Rmarkdown (magistritöö)
---