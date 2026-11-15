# Nähdään elokuvissa -sivusto

Status 15.11.2026:

-Sivustosta vasta käyttäjän luonti ja kirjautuminen luotu, sekin erittäin vahvasti esimerkin mukaisesti
-Tietokannan taulut luova create-db.sql kirjoitettu. Tietokannan ei haluta luovan uutta katsomiskertaa (sivuston perustietue), ellei katsomiskertaan ole jo luontihetkellä liitettynä ainakin kaksi osallistujaa. Sitä varten tekoäly ohjeisti luomaan härpäkkeen, jonka vuoksi katsomiskerran luontitransaktiossa pitää luoda myös kahden käyttäjän rivit Seeings -tauluun. En ole vielä testannut tätä härpäkettä, mutta ainakaan Sqlite ei herjaa tauluja luodessa. Taidan tietää, miten härpäkettä voi tehdä siistimmäksi: ehkä Seeingsin pääavain voi olla event_id:n ja user_id:n yhdistelmä. Mutta testataan ensin, ymmärsinkö tekoälyn oikein / toimiiko härpäke tällaisenaan.


**Kurssin tietokannat ja web-ohjelmointi kurssityö**

Sovelluksessa käyttäjät pystyvät merkitsemään, milloin ja missä ovat katsoneet elokuvia muiden käyttäjien kanssa. Katsomiskertaan kirjataan aika ja paikka (esim. "Tennispalatsi 3"). Katsomiskertaan merkitään myös keiden käyttäjien kanssa elokuva on nähty. Tämä on pakollinen tieto, eli palveluun kirjataan vain yhdessä muiden käyttäjien kanssa katsottuja elokuvia. Duplikaattitapahtumaa ei voi lisätä, eli tapahtuman täytyy erota muista ainakin elokuvan, ajan, tai paikan suhteen.

Käyttäjä voi lisätä katsomiskertaan myös avainsanoja elokuvan genreen ja tapahtuman luonteeseen liittyen. Omat avainsanojen lisäykset voi peruuttaa.

Käyttäjä voi kommentoida katsomiskertoja. Omia kommentteja voi muokata ja poistaa.

Käyttäjä voi lisätä itsensä johonkin katsomiskertaan, jos on sattunut samaan näytökseen.

Koska katsomiskerrat ovat yhteisiä, niin niitä ei voi poistaa tai muokata miten sattuu. Kaikki alunperin tapahtumaan merkityt käyttäjät (mukaanlukien lisääjä) saa puolen tunnin ajan muokata tapahtumaa tai poistaa sen kokonaan. Muutoin käyttäjät voivat poistaa ainoastaan itsensä tapahtumasta. Kun viimeinen käyttäjä poistaa itsensä, myös katsomiskerta tuhoutuu.

Katsomiskertoja voi selata ja hakea sijainnin, osallistujien, elokuvan, tägien, ja/tai kommenttien sisällön perusteella.

Käyttäjäsivulla näkee käyttäjästä tilastoja ja näyttökerrat joihin on merkittynä ja kommentit.
<br><br>

**Muista:**

Sovelluksen käyttöliittymän ja README.md-tiedoston kieli voi olla suomi, ruotsi tai englanti. Sovelluksen teknisen toteutuksen (koodi, tietokanta, commit-viestit) kielen tulee olla englanti.
<br><br>

**Ohjeet sovelluksen kokeiluun omalla koneella:**
<br>

Sovellus käyttää tietokantana SQLite3:ea. Sen tulee olla asennettuna, tällä tai vastaavalla komennolla:
```
sudo dnf install sqlite3
```
<br>

Kun SQLite3 on asennettuna, luodaan tietokanta seuraavalla komennolla:
```
sqlite3 database.db < create-db.sql
```
<br>

Ohjelman ajamiseen suositellaan virtuaaliympäristöä, joka luodaan seuraavasti:
```
python3 -m venv venv
```
<br>

Virtuaaliympäristö käynnistetään seuraavasti:
```
source venv/bin/activate
```
<br>

Seuraavalla komennolla poistutaan virtuaaliympäristöstä:
```
deactivate
```
<br>

Sovellus käyttää Flaskia, joka asennetaan virtuaaliympäristössä seuraavasti:
```
pip install flask
```
<br>

Sovellus käynnistetään komennolla
```
flask run
```
