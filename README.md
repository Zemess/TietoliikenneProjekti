# Tietoliikenteen sovellusprojekti 2024
## Tomi Ahola ja Samuli Hyötylä
### Viikko 1 (Aloitus)
#### **Tehty:**
- Katsoimme SDLC-videot: *Software Development Lifecycle in 9 minutes* ja *An Entire Software Development Life Cycle by Forrest Knight*.  
- Perehdyimme SDLC-vaiheisiin ja opimme niiden vaiheet: suunnittelu, analysointi, suunnittelu (design), toteutus (implementation), testaus, käyttöönotto ja ylläpito.   
- Loimme kahden hengen ryhmälle yksityisen GitHub-repositorion ja projektin käyttäen Kanban-templatea.   
- Lisäsimme repositoryn web-osoitteen projektin palautukseen.
- Tutustuimme markdown-kuvauskieleen ja tutkimme esimerkkejä, kuten Teemun *demoproject*-repositorya.  
- Kirjoitimme repositoryyn kuvaustiedoston (readme.md) käyttäen markdownia.  
- Otimme käyttöön Kanban-taulun GitHub-projektihallintaa varten ja lisäsimme tauluun sarakkeet (Backlog, To Do, In Progress, Review/Test, Done).  
- Määrittelimme tehtäviä, kuten SDLC-videoiden katsominen, README-tiedoston kirjoittaminen, arkkitehtuurikuvan luominen ja Linux-tehtävien suorittaminen.  
- Selailemme oppaan *A Field Guide to Scrum Events* ja suoritimme Scrum-testin Moodlessa.  
- Asensimme nRF5340 Development Kit -työkalut ja valmistauduimme alustakehitykseen.  
- Loimme paikallisen testailu-branchin kloonatun repositoryn alle.
- Tarkistimme GitHubissa, että testailu-branch näkyy oikein.  
- Piirsimme arkkitehtuurikaavion projektin eri komponenttien ja tiedonsiirtoyhteyksien kuvaamiseksi.
- Lisäsimme karkean version arkkitehtuurikuvasta projektin readme.md-tiedostoon.

![Arkkitehtuuri.png Icon](https://github.com/Zemess/TietoliikenneProjekti/blob/main/Arkkitehtuuri.png)
- Katselimme Twitch-striimejä koodaajilta.
- Otimme käyttöön oman Linux-palvelimen ja testasimme SSH-yhteyttä palvelimelle.  
- Vaihdoimme Linux-palvelimen käyttäjän salasanan komennolla `passwd`.  
### Viikko 2 (kiihtyvyysanturin dataa (x,y,z) BLE yhteyden yli puhelimeen)
#### **Tehty:**
Katsoimme Karin videon tavoitteista, jonka jälkeen latasimme ja testasimme Karin koodipohjan "WorkingADCSolution" ja saimme sen toimimaan nrf laitteellamme.
Tämän jälkeen aloimme työstää BLE osuutta koodista. Menimme nordic academyn sivuille ja aloimme työstää koodia pala palalta.
Kun koodi oli valmis, testasimme senkin toiminnallisuuden ja aloimme tämän jälkeen työstämään Karin koodin toiminallisuutta BLE koodipohjaan.
Teimme kytkennät NRF laitteelle ja testasimme yhdistetyn koodin, jonka totesimme pitkän taistelun jälkeen toimivaksi.
### Viikko 3 (Serverien hallinta)
#### **Tehty:**
Aloitimme viikon omien servujen käyttöönotolla. Asensimme Netfiler palomuurit, jonka jälkeen aloimme työstämään MySQL tietokantaa serverien sisälle.
MySQL testattiin ja toettiin toimivaksi. Latasimme winSCP ja wireshark ohjelmat, jonka lisäksi asensimme Apache web palvelimen ja PHP:n servuillemme.
Ohessa teimme raspille Python-ohjelman nanolla.

![nano.kuva.png](https://github.com/Zemess/TietoliikenneProjekti/blob/main/nano.kuva.png)
##### **Häiriöt/ongelmat:**
Ongelmana tällä viikolla oli Raspin haluamattomuus yhdistää servereille ollenkaan, mutta saimme dataa muualta joten ongelma selvisi.
### Viikko 4 (Pikkutehtäviä/kiinniottoa)
#### **Tehty:**
Tämä viikko oli kiinniottoa suurilta osin.
Teimme pieniä korjailuja viikon 2 koodiin ja yritimme saada Raspin toimimaan serveriemme kanssa.
Tehtäviä emme ennättäneet tekemään tällä viikolla, mutta teimme töitä senkin edestä.
### Viikko 5 (Kmeans)
#### **Tehty:**
Aloimme tekemään annetusta sensoridatasta opetusalgoritmiä K-means luokittelijalle, jonka olisi tarkoitus mitatun datan perustella oppia laskemaan keskipiste suuntadatasta.

![Kmeans.kuva.png](https://github.com/Zemess/TietoliikenneProjekti/blob/main/Kmeans.kuva.png)
Keskipisteet printattiin 3d-malliin joka näytti tältä:

![3d.PNG](https://github.com/Zemess/TietoliikenneProjekti/blob/main/3d.PNG)
Tämä tallennettiin keskipiste.h tiedostoksi seuraavaa vaihetta varten.
### Viikko 6 (Confusion)
#### **Tehty:**
Otimme Karin valmiin Confusion/adc pohjan käyttöön johon lisäsimme oman keskipiste.h tiedoston. Täydensimme confusion.c tiedostoon puuttuvat koodit ja latasimme sen NRF-laitteelle.
Latauksen jälkeen nappi 3 antoi yhden suunta-arvon, nappi 4 antoi suunta-arvoa, nappi 2 näytti sen hetkisen taulun arvot ja nappi 1 nollasi taulun "reset".

![confusion.kuva.png](https://github.com/Zemess/TietoliikenneProjekti/blob/main/confusion.kuva.png)

### Viikko 7 (tehtävien viimeistely/Posteri)
#### **Tehty:**
Teimme ReadME.md, kanbanin ja kaikki muut kirjoitusta vailla olleet tehtävät loppuun.
Saimme posterin valmiiksi ja palautukseen.
Kaikki tehtävät on nyt tehty ja loman viettoon.
