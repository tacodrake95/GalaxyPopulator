import math

numArms = 3
incPerCyc = 0.5
spirSeverity = 1
numSystems = 200
minStars = 0
maxStars = 1
minStarSize = 0.25
maxStarSize = 2.5
minStarTemp = 50
maxStarTemp = 200
minStarDist = 5
maxStarDist = 1000
minPlanets = 2
maxPlanets = 5
minPlanetG = 50
maxPlanetG = 150
minPlanetAtm = 10
maxPlanetAtm = 200
maxPlanetDistance = 200
minPlanetTheta = 0
maxPlanetTheta = 360
minPlanetRotPer = 1000
maxPlanetRotPer = 100000
minPlanetSea = 32
maxPlanetSea = 96
minMoons = 1
maxMoons = 3
minMoonAtm = 0
maxMoonAtm = 100
minMoonTheta = 0
maxMoonTheta = 360
minMoonRotPer = 1000
maxMoonRotPer = 100000
minMoonSea = 32
maxMoonSea = 96
blackHolePct = 1
ringsPct = 1
solDist = .25
#starSpread = 2
rescaleFactor = 1
starSpread = (maxStarDist * rescaleFactor) / (numSystems * incPerCyc)

starNames = """Acamar
Achernar
Achird
Acrab
Acrux
Acubens
Adhafera
Adhara
Adhil
Ain
Ainalrami
Aladfar
Albaldah
Albali
Albireo
Alchiba
Alcor
Alcyone
Aldebaran
Alderamin
Aldhanab
Aldhibah
Aldulfin
Alfirk
Algedi
Algenib
Algieba
Algol
Algorab
Alhena
Alioth
Aljanah
Alkaid
Alkalurops
Alkaphrah
Alkarab
Alkes
Almaaz
Almach
Alnair
Alnasl
Alnilam
Alnitak
Alniyat
Alphard
Alphecca
Alpheratz
Alpherg
Alrakis
Alrescha
Alruba
Alsafi
Alsciaukat
Alsephina
Alshain
Alshat
Altair
Altais
Alterf
Aludra
Alula
Alula
Alya
Alzirr
Ancha
Angetenar
Ankaa
Anser
Antares
Arcturus
Arkab
Arkab
Arneb
Ascella
Asellus
Asellus
Ashlesha
Aspidiske
Asterope
Athebyne
Atik
Atlas
Atria
Avior
Azelfafage
Azha
Azmidi
Barnard's
Baten
Beemim
Beid
Bellatrix
Betelgeuse
Bharani
Biham
Botein
Brachium
Bunda
Canopus
Capella
Caph
Castor
Castula
Cebalrai
Celaeno
Cervantes
Chalawan
Chamukuy
Chara
Chertan
Copernicus
Cor
Cujam
Cursa
Dabih
Dalim
Deneb
Deneb
Denebola
Diadem
Diphda
Dschubba
Dubhe
Dziban
Edasich
Electra
Elgafar
Elkurud
Elnath
Eltanin
Enif
Errai
Fafnir
Fang
Fawaris
Felis
Fomalhaut
Fulu
Fumalsamakah
Furud
Fuyue
Gacrux
Giausar
Gienah
Ginan
Gomeisa
Grumium
Gudja
Guniibuu
Hadar
Haedus
Hamal
Hassaleh
Hatysa
Helvetios
Heze
Homam
Iklil
Imai
Intercrus
Izar
Jabbah
Jishui
Kaffaljidhma
Kang
Kaus
Kaus
Kaus
Keid
Khambalia
Kitalpha
Kochab
Kornephoros
Kraz
Kurhah
Larawag
La
Lesath
Libertas
Lich
Lilii
Maasym
Mahasim
Maia
Marfik
Markab
Markeb
Marsic
Matar
Mebsuta
Megrez
Meissa
Mekbuda
Meleph
Menkalinan
Menkar
Menkent
Menkib
Merak
Merga
Meridiana
Merope
Mesarthim
Miaplacidus
Mimosa
Minchir
Minelauva
Mintaka
Mira
Mirach
Miram
Mirfak
Mirzam
Misam
Mizar
Mothallah
Muliphein
Muphrid
Muscida
Musica
Nahn
Naos
Nashira
Nekkar
Nembus
Nihal
Nunki
Nusakan
Ogma
Okab
Paikauhale
Peacock
Phact
Phecda
Pherkad
Piautos
Pipirima
Pleione
Polaris
Polaris
Polis
Pollux
Porrima
Praecipua
Prima
Procyon
Propus
Proxima
Ran
Rasalas
Rasalgethi
Rasalhague
Rastaban
Regulus
Revati
Rigel
Rigil
Rotanev
Ruchbah
Rukbat
Sabik
Saclateni
Sadachbia
Sadalbari
Sadalmelik
Sadalsuud
Sadr
Saiph
Salm
Sargas
Sarin
Sceptrum
Scheat
Schedar
Secunda
Segin
Seginus
Sham
Shaula
Sheliak
Sheratan
Sirius
Situla
Skat
Spica
Sualocin
Subra
Suhail
Sulafat
Syrma
Tabit
Taiyangshou
Taiyi
Talitha
Tania
Tania
Tarazed
Tarf
Taygeta
Tegmine
Tejat
Terebellum
Theemin
Thuban
Tiaki
Tianguan
Tianyi
Titawin
Toliman
Tonatiuh
Torcular
Tureis
Ukdah
Unukalhai
Unurgunite
Vega
Veritate
Vindemiatrix
Wasat
Wazn
Wezen
Wurren
Xamidimura
Xuange
Yed
Yed
Yildun
Zaniah
Zaurak
Zavijava
Zhang
Zibal
Zosma
Zubenelgenubi
Zubenelhakrabi
Zubeneschamali"""
starList = starNames.split("\n")
# From https://www.fantasynamegenerators.com/planet_names.php
planetNames = """Nimuria
Dundunope
Maccora
Xolromia
Xeorilia
Miutis
Chiceter
Sogaruta
Gippe JUHV
Dreron 5O5P
Kenvoapra
Yanzauliv
Piborth
Rinzillon
Kaibos
Evis
Mikater
Deenerth
Crurn 4
Chuna 596
Innulia
Heseonides
Unilia
Revurn
Gunov
Taegantu
Bikatania
Cruirus
Stroth OLY
Thao 9P4O
Xilristea
Pogrinus
Cosides
Zulrorth
Mioturn
Xitov
Gruteliv
Nuonov
Grosie K7C
Drarvis ZEDB
Ephionov
Vimuinus
Edrosie
Cobrosie
Nonov
Voitania
Phapucarro
Crehecury
Trora 1YUC
Myke 4A4
Sodraonope
Demiotania
Linnoth
Kunninda
Enerth
Beonov
Gnatitune
Gnugoclite
Sichi XH0
Ladus Y5X3
Kithonia
Gegnazuno
Bagnara
Onkyria
Tostea
Gatis
Deigawa
Minaruta
Borth 0N
Grolla ZNX
Bivustea
Ponrueliv
Ecromia
Echillon
Honerth
Orilia
Gnazaturn
Zilacury
Griea 92S1
Crorix ANV
Ceccivis
Delrinov
Nuthonoe
Utrao
Giocarro
Tunides
Gucuhines
Streebos
Grilles UF5
Zoria 3K
Vonviuhines
Ichainus
Thundone
Cezars
Revis
Eonope
Vakunides
Strichonope
Niri 5X8Y
Lypso BZW
Duvuiyama
Themenia
Mizora
Ustrarth
Atania
Peawei
Vusomia
Broliria
Brone 7UH
Broria SI5I
Hucoinus
Allialara
Vilnion
Selnion
Sailea
Eothea
Chelitov
Phiucarro
Grolla G6Q
Grurn 87V
Pinnegantu
Bennatania
Binyke
Punrerth
Huyama
Guarus
Phavinus
Pheticarro
Dragua K4
Moria 81L
Litruazuno
Ullaonerth
Xonzippe
Hogniri
Ranov
Menope
Leotera
Dikarus
Theshan UOC
Meshan ERQ
Bigiatania
Hebbeunerth
Ibilia
Kenvonoe
Gonope
Chenia
Brothonov
Virogawa
Drerth 156
Striuq 1F5Y
Banrucury
Tholmobos
Balmonoe
Pechippe
Molara
Kalea
Zocanov
Gudogawa
Cronoe G5
Cyke XOGC
Tibroliv
Odicury
Cebbars
Kignone
Daotania
Zairia
Thabicury
Malitune
Gnade LNZJ
Cosie AL
Thognastea
Etheoter
Tanzuna
Dosion
Peizuno
Hotune
Siithea
Llozerus
Zarvis 62
Cromia 2B4
Ecaenus
Zadauvis
Rogerth
Nelyria
Layama
Cutov
Crerozuno
Grochehiri
Nippe V1Y
Sars 30
Helaotania
Obicury
Endomia
Vodyke
Mogawa
Natune
Greoter
Chadinope
Chorth F6
Drerth 31N1
Lenveoliv
Endirus
Nicrilia
Sogreshan
Viegantu
Ruter
Zagetov
Stricuter
Gillon SS9
Gade P80
Cecraecury
Celviunus
Iphion
Hellorth
Yourilia
Patania
Gnugitera
Chehogawa
Phadus 0JL
Moth PO9
Thundoalia
Thastroanerth
Uneshan
Vamorth
Pulara
Meirus
Noitania
Stripitera
Llion T72
Dyria AMQ
Ponvania
Anvapra
Eccilia
Nagnonoe
Tueclite
Nihiri
Bodiliv
Novocury
Gnilles 14Y
Bryke Y3
Sastrulea
Hibohines
Cimeshan
Holluna
Ouhines
Eicarro
Nochacury
Bruvocarro
Badus 5VL
Thars 1CC
Ophuethea
Bondaiter
Tacuna
Ulradus
Sothea
Noathea
Lusilia
Melulara
Chiuq 4FW
Zides 6YQ6
Endoter
Godrihiri
Hetrippe
Golomia
Siania
Loacarro
Phihicarro
Dralogantu
Crides 18J
Theon S3O
Obbiocury
Chebbiliv
Binragua
Colrade
Ciathea
Chephus
Druducury
Baogawa
Droth 6Z7J
Dade 817J
Nibbauhiri
Nebriuliv
Penkadus
Ocillon
Vagawa
Coatis
Griyiphus
Chaestea
Crone 2DW8
Llao AO9G
Sabbuenides
Abbuenus
Cacruna
Uccarvis
Gaunerth
Pibos
Bikarilia
Gneerus
Stryria 7QW
Trarvis OO2
Relmeuwei
Muzeotov
Cagagua
Xallore
Iagantu
Hegantu
Gniluthea
Sotinus
Crara XKZ
Brorix B1F
Vomarilia
Yanatania
Sachillon
Bilmiri
Uerilia
Xivis
Chobostea
Trudutov
Deon GFK7
Thara 9XG
Chasonides
Kinarus
Elvosie
Haphoth
Thunerth
Lanus
Brocutov
Dusarilia
Phyke MGUE
Crypso 1O6T
Cingaopra
Lelleturn
Bedoth
Hubade
Nemia
Ritania
Phoozuno
Niconope
Veon 4C6O
Drion ET0
Alleatov
Ochater
Olrora
Kastrolla
Mueter
Naigawa
Vepatania
Brugurus
Croria E8
Stronoe 6GB6
Kunvozuno
Tadrizuno
Sulore
Tobbiuq
Baclite
Chonia
Gnacanerth
Cresotis
Greshan BSF
Norix AKZ
Magrewei
Linvaoturn
Lustrilles
Pesides
Lioyama
Meyama
Veicarro
Dreozuno
Trade J4
Cuna 9B9
Retriuria
Xunoagawa
Ulrillon
Xotrade
Alea
Veoruta
Strienus
Brokuturn
Vides 2479
Grarth 9BQ
Hithiyama
Yucaoria
Menurn
Xitherth
Cutera
Nagantu
Cehanus
Grusinus
Stryria EXQ
Thilia V44
Ognualiv
Rusinov
Cilvilles
Logadus
Oter
Aonia
Droawei
Stroketer
Thorix 87K
Llorth 7F
Lathaigantu
Dachecarro
Lunkeon
Yindarvis
Mianope
Vuithea
Bukutania
Pholapra
Lomia A849
Lleon 63
Sabbuithea
Dogroanus
Daphilia
Ninzov
Saurus
Unus
Merezuno
Groolara
Chars 81
Thorth FG
Cogranov
Zitrenus
Ogosie
Gitragua
Betov
Rounus
Gnievis
Gemistea
Bruna 82EU
Vuna 33
Yinvohiri
Gubaothea
Potrov
Culrade
Veurus
Bocarro
Minuliv
Gelavis
Dryria D9
Bonoe 75H
Envayama
Mivoupra
Zestriuq
Udonoe
Arilia
Zienus
Negehiri
Cimaclite
Gippe 2T65
Crinda WV
Echiezuno
Anvoter
Thenzov
Cobrorix
Dubos
Toazuno
Grexilia
Nazanope
Phara 0P
Vion 4FL5
Ungietov
Hedoania
Almillon
Teniri
Piter
Leiria
Zoolia
Nuogantu
Varvis 2V7
Madus KXK
Pucenus
Talvaemia
Dinrarth
Imurn
Panov
Sawei
Bodunides
Becanus
Strars INO
Chov 57GA
Obreugantu
Kachicarro
Ucides
Yanvarvis
Yeoclite
Guliv
Phusoliv
Gnipurilia
Sov 2CI
Gniuq P0O5
Ucroter
Rulnaupra
Ugrypso
Thibrion
Muria
Kamia
Letharia
Strabenov
Phides LZV
Briuq K7J2
Yiloclite
Laccuestea
Ulnorix
Yevagua
Yevis
Unia
Sutehines
Leutera
Grao W62P
Phora G48W
Ubaruta
Kunzaria
Sagniea
Zibbadus
Moucarro
Zauria
Maduclite
Luhinus
Michi 4
Strillon PUX4
Nubrenus
Unnanus
Kibbeon
Hilolla
Yevis
Mavis
Bisihines
Suitania
Grolla Q7G
Greon SMU6
Pandoaruta
Xindezuno
Kogreron
Nulvars
Ievis
Ruyama
Milopra
Zeuhiri
Chonoe BNK7
Greshan 747H
Halmaphus
Catrierilia
Almorth
Pagagua
Hienia
Camia
Gnagarus
Dunuphus
Sinda 722
Thilles CK60
Vacciethea
Accahines
Necrion
Sunniri
Nebos
Suinope
Llechetune
Lluanus
Drolla 94U
Zade 17
Xondouwei
Xagreogawa
Tidarvis
Gendilia
Xeliv
Mitune
Chusemia
Malemia
Chonoe 
Druna 45H
Ledirus
Obbetov
Abbides
Raccapus
Kiliv
Vatis
Chevezuno
Phezocury
Leron XLD
Cyke NAV
Yicceamia
Vudater
Nuzagua
Yudeon
Yulia
Boulia
Phuzirilia
Stresunides
Magua 1Z
Cichi XS50
Becupra
Yobonus
Telvara
Kadion
Roinope
Aeclite
Strayeturn
Druhustea
Gadus 7
Llapus 61D8
Zalmucarro
Huseirus
Noccomia
Lopheon
Hater
Awei
Llucumia
Dethohiri
Milia ZVS
Grora 2VKC"""
planetList = planetNames.split("\n")