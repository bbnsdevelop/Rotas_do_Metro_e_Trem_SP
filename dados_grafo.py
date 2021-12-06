
def carrega_grafo(grafo):

  ####################################################################
  ## Inicializando o grafos com os dados das linhas da CPTM e Metrô ##
  ####################################################################

  #linha 1 
  grafo.connect("Tucuruvi","Parada Inglesa", distance = 5)
  grafo.connect("Parada Inglesa","Jardim São Paulo", distance = 5)
  grafo.connect("Jardim São Paulo","Santana", distance = 4)
  grafo.connect("Santana","Carandiru", distance = 6)
  grafo.connect("Carandiru","Portuguesa - Tiete", distance = 6)
  grafo.connect("Portuguesa - Tiete","Armênia", distance = 3)
  grafo.connect("Armênia","Tiradentes", distance = 5)
  grafo.connect("Tiradentes","Luz", distance = 4)
  grafo.connect("Luz","São Bento", distance = 2)
  grafo.connect("São Bento","Sé", distance = 3)
  grafo.connect("Sé","Liberdade", distance = 5)
  grafo.connect("Liberdade","São Joaquim", distance = 3)
  grafo.connect("São Joaquim","Vergueiro", distance = 2)
  grafo.connect("Vergueiro","Paraíso", distance = 2)
  grafo.connect("Paraíso","Ana Rosa", distance = 2)
  grafo.connect("Ana Rosa","Vila Mariana", distance = 4)
  grafo.connect("Vila Mariana","Santa Cruz", distance = 5)
  grafo.connect("Santa Cruz","Praça da Árvore", distance = 4)
  grafo.connect("Praça da Árvore","Saúde", distance = 2)
  grafo.connect("Saúde","São Judas", distance = 3)
  grafo.connect("São Judas","Conceição", distance = 2)
  grafo.connect("Conceição","Jabaquara", distance = 4)
                                
  grafo.locations["Tucuruvi"] = (-23.480333456649916, -46.60351088289334)
  grafo.locations["Parada Inglesa"] = (-23.486873804965725, -46.60875620008528)
  grafo.locations["Jardim São Paulo"] = (-23.492129251613274, -46.616684959606054)
  grafo.locations["Santana"] = (-23.50237403107141, -46.624807474948575)
  grafo.locations["Carandiru"] = (-23.508962056800602, -46.62484044241358)
  grafo.locations["Portuguesa - Tiete"] = (-23.515870777674298, -46.62514032892046)
  grafo.locations["Armênia"] = (-23.52534593962692, -46.62931073076998)
  grafo.locations["Tiradentes"] = (-23.53068449767632, -46.632463415427104)
  grafo.locations["Luz"] = (-23.536247886741588, -46.63421705777678)
  grafo.locations["São Bento"] = (-23.541947886741588, -46.63421705777678)

    

  grafo.locations["Sé"] = (-23.5492908,-46.6334714)
  grafo.locations["Liberdade"] = (-23.555208470969735, -46.63552418474166)
  grafo.locations["São Joaquim"] = (-23.561626525412485, -46.638586371248216)
  grafo.locations["Vergueiro"] = (-23.568865305663707, -46.63994300736535)
  grafo.locations["Paraíso"] = (-23.575133660727808, -46.640308938606694)
  grafo.locations["Ana Rosa"] = (-23.58156515481154, -46.63862477590406)
  grafo.locations["Vila Mariana"] = (-23.589504691944157, -46.6345929925378)
  grafo.locations["Santa Cruz"] = (-23.598741545921634, -46.63685130149925)
  grafo.locations["Praça da Árvore"] = (-23.610502977722085, -46.63803787064281)
  grafo.locations["Saúde"] = (-23.618627803869444, -46.63933926905802)
  grafo.locations["São Judas"] = (-23.62565332652243, -46.64089584367209)
  grafo.locations["Conceição"] = (-23.635203224778255, -46.64107446700202)
  grafo.locations["Jabaquara"] = (-23.646131568126386, -46.640449285418185)

  grafo.linha["1"] = ["Tucuruvi", "Parada Inglesa", "Jardim São Paulo", "Santana", "Carandiru", "Portuguesa - Tiete", "Armênia", "Tiradentes",
                    "Luz", "São Bento", "Sé", "Liberdade", "São Joaquim", "Vergueiro", "Paraíso", "Ana Rosa", "Vila Mariana", "Santa Cruz",
                    "Praça da Árvore", "Saúde", "São Judas", "Conceição", "Jabaquara"] 

  #grafo.metro = [lista de todas as estacoes]
  #grafo.cptm = [lista de todas as estacoes]

  #linha 2 
  grafo.connect("Vila Madalena","Sumaré", distance = 4)
  grafo.connect("Sumaré","Clinicas", distance = 3)
  grafo.connect("Clinicas","Consolação", distance = 2)
  grafo.connect("Consolação","Trianon - Masp", distance = 4)
  grafo.connect("Trianon - Masp","Brigadeiro", distance = 3)
  grafo.connect("Brigadeiro","Paraíso", distance = 3)
  grafo.connect("Paraíso","Ana Rosa", distance = 2)
  grafo.connect("Ana Rosa","Chácara Klabin", distance = 5)
  grafo.connect("Chácara Klabin","Santos-Imigrantes", distance = 5)
  grafo.connect("Santos-Imigrantes","Alto do Ipiranga", distance = 4)
  grafo.connect("Alto do Ipiranga","Sacomã", distance = 4)
  grafo.connect("Sacomã","Tamanduateí", distance = 3)
  grafo.connect("Tamanduateí","Vila Prudente", distance = 2)

  grafo.locations["Vila Madalena"] = (-23.546361645456575, -46.69015454463203)
  grafo.locations["Sumaré"] = (-23.550758050329577, -46.67785929880772)
  grafo.locations["Clinicas"] = (-23.55431834209947, -46.67098211482033)
  grafo.locations["Consolação"] = (-23.55777035615408, -46.66068243213432)
  grafo.locations["Trianon - Masp"] = (-23.563695610390113, -46.65398763924175)
  grafo.locations["Brigadeiro"] = (-23.56886339405256, -46.647410862017104)
  grafo.locations["Paraíso"] = (-23.575127399636393, -46.64025472830635)
  grafo.locations["Ana Rosa"] = (-23.581489435327168, -46.638666860544326)
  grafo.locations["Chácara Klabin"] = (-23.592691005436482, -46.630466499295565)
  grafo.locations["Santos-Imigrantes"] = (-23.59594143783894, -46.62088463468468)
  grafo.locations["Alto do Ipiranga"] = (-23.60192763496051, -46.61250209774301)
  grafo.locations["Sacomã"] = (-23.60299155938876, -46.60269057397356)
  grafo.locations["Tamanduateí"] = (-23.593357467599997, -46.58995728354701)
  grafo.locations["Vila Prudente"] = (-23.584330710490008, -46.58191923452355)

  grafo.linha["2"] = ["Vila Madalena", "Sumaré", "Clinicas", "Consolação", "Trianon - Masp", "Brigadeiro", "Paraíso",
                      "Ana Rosa", "Chácara Klabin", "Santos-Imigrantes", "Alto do Ipiranga", "Sacomã", "Tamanduateí", "Vila Prudente"] 


  #Linha 3
  grafo.connect("Corinthians - Itaquera","Arthur Alvim", distance = 6)
  grafo.connect("Arthur Alvim","Patriarca - Vila Ré", distance = 5)
  grafo.connect("Patriarca - Vila Ré","Guilhermina Esperança", distance = 5)
  grafo.connect("Guilhermina Esperança","Vila Matilde", distance = 3)
  grafo.connect("Vila Matilde","Penha", distance = 4)
  grafo.connect("Penha","Carrão", distance = 4)
  grafo.connect("Carrão","Tatuapé", distance = 3)
  grafo.connect("Tatuapé","Belém", distance = 6)
  grafo.connect("Belém","Bresser - Mooca", distance = 4)
  grafo.connect("Bresser - Mooca","Brás", distance = 3)
  grafo.connect("Brás","Pedro II", distance = 3)
  grafo.connect("Pedro II","Sé", distance = 4)
  grafo.connect("Sé","Anhangabaú", distance = 4)
  grafo.connect("Anhangabaú","República", distance = 2)
  grafo.connect("República","Santa Cecilia", distance = 2)
  grafo.connect("Santa Cecilia","Marechal Deodoro", distance = 2)
  grafo.connect("Marechal Deodoro","Palmeiras - Barra Funda", distance = 4)

  grafo.locations["Corinthians - Itaquera"] = (-23.542186366042127, -46.470935444505486)
  grafo.locations["Arthur Alvim"] = (-23.54049909138366, -46.484107109260485)
  grafo.locations["Patriarca - Vila Ré"] = (-23.531066066750277, -46.50147709504839)
  grafo.locations["Guilhermina Esperança"] = (-23.529295454991576, -46.516626211426875)
  grafo.locations["Vila Matilde"] = (-23.5318234878959, -46.53092775002239)
  grafo.locations["Penha"] = (-23.533505537380528, -46.54255780841295)
  grafo.locations["Carrão"] = (-23.537804010537346, -46.56410131088682)
  grafo.locations["Tatuapé"] = (-23.54022368423034, -46.576600404965056)
  grafo.locations["Belém"] = (-23.54276134293046, -46.58952865247439)
  grafo.locations["Bresser - Mooca"] = (-23.546331686801924, -46.60727414726818)
  grafo.locations["Brás"] = (-23.547816842612416, -46.61584648736085)
  grafo.locations["Pedro II"] = (-23.549606875658412, -46.625974508335325)
  #grafo.locations["Sé"] = (-23.6069, -46.6305)
  grafo.locations["Anhangabaú"] = (-23.54779717179493, -46.63892421356816)
  grafo.locations["República"] = (-23.543931796884525, -46.6424432718236)
  grafo.locations["Santa Cecilia"] = (-23.539151557827907, -46.649266811456435)
  grafo.locations["Marechal Deodoro"] = (-23.533879323176535, -46.656358572072634)
  grafo.locations["Palmeiras - Barra Funda"] = (-23.525232794460198, -46.66685137383305)

  grafo.linha["3"] = ["Corinthians - Itaquera", "Arthur Alvim", "Patriarca - Vila Ré", "Guilhermina Esperança", "Vila Matilde", "Penha",
                      "Carrão", "Tatuapé", "Belém", "Bresser - Mooca", "Brás", "Pedro II", "Sé", "Anhangabaú", "República", "Santa Cecilia", 
                      "Marechal Deodoro", "Palmeiras - Barra Funda"] 



  #Linha 4 
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("São Paulo - Morumbi", "Butantã", distance = 2) 
  grafo.connect("Butantã", "Pinheiros", distance = 4) 
  grafo.connect("Pinheiros", "Faria Lima", distance = 4)
  grafo.connect("Faria Lima", "Fradique Coutinho", distance = 1) 
  grafo.connect("Fradique Coutinho", "Oscar Freire", distance = 3) 
  grafo.connect("Oscar Freire", "Paulista", distance = 2) 
  grafo.connect("Paulista", "Higienópolis - Mackenzie", distance = 2) 
  grafo.connect("Higienópolis - Mackenzie", "República", distance = 2) 
  grafo.connect("República", "Luz", distance = 2) 


  grafo.locations["São Paulo - Morumbi"] = (-23.585904735942258, -46.72320241005245)
  grafo.locations["Butantã"] = (-23.57179687035862, -46.70812250633363)
  grafo.locations["Pinheiros"] = (-23.56744050505374, -46.70197488314512)
  grafo.locations["Faria Lima"] = (-23.567529010525025, -46.69330598385903)
  grafo.locations["Fradique Coutinho"] = (-23.56619158813438, -46.68426157491871)
  grafo.locations["Oscar Freire"] = (-23.56086143124611, -46.672073617186385)
  grafo.locations["Paulista"] = (-23.555117994347576, -46.66183830756984)
  grafo.locations["Higienópolis - Mackenzie"] = (-23.5488923759976, -46.652225270369804)
  grafo.locations["República"] = (-23.54401396032517, -46.64259077577914)
  grafo.locations["Luz"] = (-23.536410746104455, -46.63422228342527)

  grafo.linha["4"] = ["São Paulo - Morumbi", "Butantã", "Pinheiros", "Faria Lima", "Fradique Coutinho", "Oscar Freire", "Paulista",
            "Higienópolis - Mackenzie", "República", "Luz"]



  #linha 5 Lilas
  ###########################
  #Ajustar o grafo
  #############################
  grafo.connect("Capão Redondo", "Campo Limpo" , distance = 5) 
  grafo.connect("Campo Limpo", "Vila das Belezas", distance = 3) 
  grafo.connect("Vila das Belezas", "Giovanni Gronchi", distance = 5) 
  grafo.connect("Giovanni Gronchi", "Santo Amaro", distance = 5) 
  grafo.connect("Santo Amaro", "Largo Treze", distance = 5)
  grafo.connect("Largo Treze", "Adolfo Pinheiro", distance = 2) 
  grafo.connect("Adolfo Pinheiro", "Alto da Boa Vista", distance = 2) 
  grafo.connect("Alto da Boa Vista", "Borba Gato", distance = 2) 
  grafo.connect("Borba Gato", "Brooklin", distance = 1) 
  grafo.connect("Brooklin", "Campo Belo", distance = 2) 
  grafo.connect("Campo Belo", "Eucaliptos", distance = 3) 
  grafo.connect("Eucaliptos", "Moema", distance = 2) 
  grafo.connect("Moema", "AACD-Servidor", distance = 2) 
  grafo.connect("AACD-Servidor", "Hospital São Paulo", distance = 1) 
  grafo.connect("Hospital São Paulo","Santa Cruz", distance = 2) 
  grafo.connect("Santa Cruz", "Chácara Klabin", distance = 2)


  grafo.locations["Capão Redondo"] = (-23.65918752466623, -46.76811505976349)
  grafo.locations["Campo Limpo"] = (-23.648377632276855, -46.75395728675275)
  grafo.locations["Vila das Belezas"] = (-23.64024019717143, -46.74566526651029)
  grafo.locations["Giovanni Gronchi"] = (-23.64392774265444, -46.73408664819389)
  grafo.locations["Santo Amaro"] = (-23.655749394693096, -46.72165956911321)
  grafo.locations["Largo Treze"] = (-23.654070071510183, -46.70868758801579)
  grafo.locations["Adolfo Pinheiro"] = (-23.650014664524978, -46.70431769620912)
  grafo.locations["Alto da Boa Vista"] = (-23.64143488274559, -46.69904628939343)
  grafo.locations["Borba Gato"] = (-23.633380923838732, -46.69281621106696)
  grafo.locations["Brooklin"] = (-23.6262919778308, -46.68792914865306)
  grafo.locations["Campo Belo"] = (-23.6184784101085, -46.68209286720453)
  grafo.locations["Eucaliptos"] = (-23.6096455959843, -46.66838248650728)
  grafo.locations["Moema"] = (-23.603531990859636, -46.661779247435454)
  grafo.locations["AACD-Servidor"] = (-23.59715702320318, -46.65220355526584)
  grafo.locations["Hospital São Paulo"] = (-23.598323262616255, -46.64558563990558)
  grafo.locations["Santa Cruz"] = (-23.598890315897965, -46.63690965067398)
  grafo.locations["Chácara Klabin"] = (-23.592773379685937, -46.63053217875713)


  grafo.linha["5"] = ["Capão Redondo", "Campo Limpo", "Vila das Belezas", "Giovanni Gronchi", "Santo Amaro", "Largo Treze", "Adolfo Pinheiro",
            "Alto da Boa Vista", "Borba Gato", "Brooklin", "Campo Belo", "Eucaliptos", "Moema", "AACD-Servidor", "Hospital São Paulo",
            "Santa Cruz", "Chácara Klabin"]


  ###########################
  #linha 7 Ruby
  ###########################


  grafo.connect("Jundiaí", "Várzea Paulista", distance = 8) 
  grafo.connect("Várzea Paulista", "Campo Limpo Paulista", distance = 8)
  grafo.connect("Campo Limpo Paulista", "Botujuru", distance = 5)
  grafo.connect("Botujuru", "Francisco Morato", distance = 10)
  grafo.connect("Francisco Morato", "Baltazar Fidélis", distance = 4)
  grafo.connect("Baltazar Fidélis", "Caieiras", distance = 9)
  grafo.connect("Caieiras", "Perus", distance = 5)
  grafo.connect("Perus", "Vila Aurora", distance = 5)
  grafo.connect("Vila Aurora", "Jaraguá", distance = 3)
  grafo.connect("Jaraguá", "Vila Clarice", distance = 3)
  grafo.connect("Vila Clarice", "Pirituba", distance = 5)
  grafo.connect("Pirituba", "Piqueri", distance = 3)
  grafo.connect("Piqueri", "Lapa", distance = 3)
  grafo.connect("Lapa", "Água Branca", distance = 3)
  grafo.connect("Água Branca", "Palmeiras - Barra Funda", distance = 3)
  grafo.connect("Palmeiras - Barra Funda", "Luz", distance = 4)
  grafo.connect("Luz", "Brás", distance = 15)



  grafo.locations["Jundiaí"] = (-23.195174700949323, -46.872428130630475)
  grafo.locations["Várzea Paulista"] = (-23.20877127882304, -46.82905848319274)
  grafo.locations["Campo Limpo Paulista"] = (-23.206165986762393, -46.7859442560159)
  grafo.locations["Botujuru"] = (-23.23598696588493, -46.76742383998185)
  grafo.locations["Francisco Morato"] = (-23.28240615864155, -46.74221329433402)
  grafo.locations["Baltazar Fidélis"] = (-23.309844812565167, -46.72380655802352)
  grafo.locations["Caieiras"] = (-23.366068941562244, -46.75154216580921)
  grafo.locations["Perus"] = (-23.404944322361754, -46.75340351625121)
  grafo.locations["Vila Aurora"] = (-23.437428618825972, -46.74686557347242)
  grafo.locations["Jaraguá"] = (-23.455065258881373, -46.738473802517674)
  grafo.locations["Vila Clarice"] = (-23.46996234733515, -46.743956458691535)
  grafo.locations["Pirituba"] = (-23.48781890111371, -46.72608243774128)
  grafo.locations["Piqueri"] = (-23.503834247838483, -46.714732329292715)
  grafo.locations["Lapa"] = (-23.51741281910782, -46.70340326459982)
  grafo.locations["Água Branca"] = (-23.52118059918351, -46.68832925006749)
  grafo.locations["Palmeiras - Barra Funda"] = (-23.525340175558533, -46.667363808961426)
  grafo.locations["Luz"] = (-23.534940012079623, -46.635219692740364)
  grafo.locations["Brás"] = (-23.544842522522742, -46.61611675125584)

  grafo.linha["7"] = ["Jundiaí", "Várzea Paulista", "Campo Limpo Paulista", "Botujuru", "Francisco Morato", "Baltazar Fidélis", "Caieiras", "Perus",
          "Vila Aurora", "Jaraguá", "Vila Clarice", "Pirituba", "Piqueri", "Lapa", "Água Branca", "Palmeiras - Barra Funda", "Luz", "Brás"]



  #linha 8 Diamante
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Júlio Prestes", "Palmeiras - Barra Funda", distance = 5)
  grafo.connect("Palmeiras - Barra Funda", "Lapa", distance = 5)
  grafo.connect("Lapa","Domingos de Moraes", distance = 6)
  grafo.connect("Domingos de Moraes", "Imperatriz Leopoldina", distance = 4)
  grafo.connect("Imperatriz Leopoldina", "Presidente Altino", distance = 3)
  grafo.connect("Presidente Altino","Osasco", distance = 3)
  grafo.connect("Osasco", "Comandante Sampaio", distance = 5)
  grafo.connect("Comandante Sampaio", "Quitaúna", distance = 4)
  grafo.connect("Quitaúna","General Miguel Costa", distance = 4)
  grafo.connect("General Miguel Costa", "Carapicuiba", distance = 3)
  grafo.connect("Carapicuiba", "Santa Terezinha", distance = 5)
  grafo.connect("Santa Terezinha", "Antonio João", distance = 6)
  grafo.connect("Antonio João", "Barueri", distance = 3)
  grafo.connect("Barueri", "Jardim Belval", distance = 2)
  grafo.connect("Jardim Belval", "Jaredim Silveira", distance = 4)
  grafo.connect("Jaredim Silveira", "Jandira", distance = 5)
  grafo.connect("Jandira", "Sagrado Coração", distance = 4)
  grafo.connect("Sagrado Coração", "Engenheiro Cardoso", distance = 3)
  grafo.connect("Engenheiro Cardoso", "Itapevi", distance = 3)
  grafo.connect("Itapevi", "Santa Rita", distance = 4)
  grafo.connect("Santa Rita", "Amador Bueno", distance = 5)



  grafo.locations["Júlio Prestes"] = (-23.53406756808327, -46.64078948864577)
  grafo.locations["Palmeiras - Barra Funda"] = (-23.52542769536095, -46.66732681711201)
  grafo.locations["Lapa"] = (-23.520043901148142, -46.69843263323359)
  grafo.locations["Domingos de Moraes"] = (-23.51912469480943, -46.72279312737115)
  grafo.locations["Imperatriz Leopoldina"] = (-23.52375800880584, -46.73863165009942)
  grafo.locations["Presidente Altino"] = (-23.531318524131283, -46.761901671398014)
  grafo.locations["Osasco"] = (-23.527738788830945, -46.777300490808635)
  grafo.locations["Comandante Sampaio"] = (-23.525361790758527, -46.79413611694181)
  grafo.locations["Quitaúna"] = (-23.522726995800646, -46.80759837085408)
  grafo.locations["General Miguel Costa"] = (-23.523471617108584, -46.81618797595051)
  grafo.locations["Carapicuiba"] = (-23.518717423965043, -46.83583474562942)
  grafo.locations["Santa Terezinha"] = (-23.516426185193307, -46.84857859617537)
  grafo.locations["Antonio João"] = (-23.517256763802514, -46.85851130328215)
  grafo.locations["Barueri"] = (-23.512931969347928, -46.87631521216463)
  grafo.locations["Jardim Belval"] = (-23.514535883246506, -46.89149538705589)
  grafo.locations["Jaredim Silveira"] = (-23.523299781772177, -46.894056651139856)
  grafo.locations["Jandira"] = (-23.527767427146586, -46.9042080026877)
  grafo.locations["Sagrado Coração"] = (-23.5290275047863, -46.914859113175126)
  grafo.locations["Engenheiro Cardoso"] = (-23.535069982192017, -46.929383354561146)
  grafo.locations["Itapevi"] = (-23.54563649135988, -46.93547416552864)
  grafo.locations["Santa Rita"] = (-23.544949264630738, -46.94853036540057)
  grafo.locations["Amador Bueno"] = (-23.53057394718201, -46.98429435777471)

  grafo.linha["8"] = ["Júlio Prestes", "Palmeiras - Barra Funda", "Lapa", "Domingos de Moraes", "Imperatriz Leopoldina", "Presidente Altino", "Osasco", "Comandante Sampaio",
            "Quitaúna", "General Miguel Costa", "Carapicuiba", "Santa Terezinha", "Antonio João", "Barueri", "Jardim Belval", "Jaredim Silveira", "Jandira",
                      "Sagrado Coração", "Engenheiro Cardoso", "Itapevi", "Santa Rita", "Amador Bueno"] 


  # linha 9 Esmeralda
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Mendes - Vila Natal", "Grajaú", distance = 3)
  grafo.connect("Grajaú", "Primavera-Interlagos", distance = 5)
  grafo.connect("Primavera-Interlagos", "Autódromo", distance = 2)
  grafo.connect("Autódromo", "Jurubatuba", distance = 2)
  grafo.connect("Jurubatuba", "Socorro", distance = 4)
  grafo.connect("Socorro", "Santo Amaro", distance = 3)
  grafo.connect("Santo Amaro", "João Dias", distance = 5)
  grafo.connect("João Dias", "Granja Julieta", distance = 6)
  grafo.connect("Granja Julieta", "Morumbi", distance = 4)
  grafo.connect("Morumbi", "Berrini", distance = 3)
  grafo.connect("Berrini", "Vila Olímpia", distance = 4)
  grafo.connect("Vila Olímpia", "Cidade Jardim", distance = 3)
  grafo.connect("Cidade Jardim", "Hebraica-Rebouças", distance = 3)
  grafo.connect("Hebraica-Rebouças", "Pinheiros", distance = 2)
  grafo.connect("Pinheiros", "Cidade Universitária", distance = 4)
  grafo.connect("Cidade Universitária", "Villa Lobos-Jaquaré", distance = 5)
  grafo.connect("Villa Lobos-Jaquaré", "Ceasa", distance = 2)
  grafo.connect("Ceasa", "Presidente Altino", distance = 4)
  grafo.connect("Presidente Altino", "Osasco", distance = 5)



  grafo.locations["Mendes - Vila Natal"] = (-23.75371024593318, -46.708792379365825)
  grafo.locations["Grajaú"] = (-23.736511736376748, -46.69854085511842)
  grafo.locations["Primavera-Interlagos"] = (-23.722826435234026, -46.69605569556504)
  grafo.locations["Autódromo"] = (-23.70612912257775, -46.6910471432227)
  grafo.locations["Jurubatuba"] = (-23.677280094017625, -46.704428771611354)
  grafo.locations["Socorro"] = (-23.66369363614629, -46.71238128216632)
  grafo.locations["Santo Amaro"] = (-23.65630453143889, -46.72086905785274)
  grafo.locations["João Dias"] = (-23.640427330175022, -46.72297453681926)
  grafo.locations["Granja Julieta"] = (-23.62737444809375, -46.71463704236138)
  grafo.locations["Morumbi"] = (-23.621979996636156, -46.70259357679431)
  grafo.locations["Berrini"] = (-23.605059594443265, -46.69678212675197)
  grafo.locations["Vila Olímpia"] = (-23.59374307592157, -46.694488133331525)
  grafo.locations["Cidade Jardim"] = (-23.585403963743904, -46.6932646701707)
  grafo.locations["Hebraica-Rebouças"] = (-23.572999430150144, -46.699764318213504)
  grafo.locations["Pinheiros"] = (-23.567392476851648, -46.702708276474716)
  grafo.locations["Cidade Universitária"] = (-23.557089075965543, -46.713337112733775)
  grafo.locations["Villa Lobos-Jaquaré"] = (-23.54597872157314, -46.734403619080894)
  grafo.locations["Ceasa"] = (-23.537356159130418, -46.74338842671072)
  grafo.locations["Presidente Altino"] = (-23.531291985989878, -46.764569632720175)
  grafo.locations["Osasco"] = (-23.527961829824672, -46.777033663681685)


  grafo.linha["9"] = ["Mendes - Vila Natal", "Grajaú", "Primavera-Interlagos", "Autódromo", "Jurubatuba", "Socorro", "Santo Amaro", "João Dias", "Granja Julieta",
            "Morumbi", "Berrini", "Vila Olímpia", "Cidade Jardim", "Hebraica-Rebouças", "Pinheiros", "Cidade Universitária", "Villa Lobos-Jaquaré", "Ceasa",
                      "Presidente Altino", "Osasco"]


  
  #linha 10 Turquesa 
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Rio Grande Da Serra", "Ribeirão Pires", distance = 4)
  grafo.connect("Ribeirão Pires", "Guapituba", distance = 3)
  grafo.connect("Guapituba", "Mauá", distance = 4)
  grafo.connect("Mauá", "Capuava", distance = 5)
  grafo.connect("Capuava", "Prefeito Celso Daniel Santo André", distance = 5)
  grafo.connect("Prefeito Celso Daniel Santo André", "Prefeito Saladino", distance = 4)
  grafo.connect("Prefeito Saladino", "Utinga", distance = 4)
  grafo.connect("Utinga", "São Caetano do Sul - Prefeito Walter Braido", distance = 6)
  grafo.connect("São Caetano do Sul - Prefeito Walter Braido", "Tamanduateí", distance = 6)
  grafo.connect("Tamanduateí", "Ipiranga", distance = 4)
  grafo.connect("Ipiranga", "Juventus - Mooca", distance = 4)
  grafo.connect("Juventus - Mooca", "Brás", distance = 6)



  grafo.locations["Rio Grande Da Serra"] = (-23.743189833098363, -46.3917094735514)
  grafo.locations["Ribeirão Pires"] = (-23.71371761482574, -46.414650517752925)
  grafo.locations["Guapituba"] = (-23.692123628693018, -46.4486811526855)
  grafo.locations["Mauá"] = (-23.66838649157275, -46.46137910635298)
  grafo.locations["Capuava"] = (-23.658291207421442, -46.48985732472124)
  grafo.locations["Prefeito Celso Daniel Santo André"] = (-23.652214643277116, -46.52803210497991)
  grafo.locations["Prefeito Saladino"] = (-23.63829930003603, -46.5362094275908)
  grafo.locations["Utinga"] = (-23.626110885496402, -46.544135976376985)
  grafo.locations["São Caetano do Sul - Prefeito Walter Braido"] = (-23.610075764028696, -46.570040083086546)
  grafo.locations["Tamanduateí"] = (-23.59262775621162, -46.5893987014031)
  grafo.locations["Ipiranga"] = (-23.58242760264616, -46.596467232008635)
  grafo.locations["Juventus - Mooca"] = (-23.558032478426597, -46.60816702091861)
  grafo.locations["Brás"] = (-23.544910384518754, -46.61626167981548)


  grafo.linha["10"] = ["Rio Grande Da Serra", "Ribeirão Pires", "Guapituba", "Mauá", "Capuava", "Prefeito Celso Daniel Santo André", "Prefeito Saladino",
            "Utinga", "São Caetano do Sul - Prefeito Walter Braido", "Tamanduateí", "Ipiranga", "Juventus - Mooca", "Brás"] 




  #Linha 11 
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Luz", "Brás", distance = 4)
  grafo.connect("Brás", "Tatuapé", distance = 5)
  grafo.connect("Tatuapé","Itaquera", distance = 12)
  grafo.connect("Itaquera", "Dom Bosco", distance = 4)
  grafo.connect("Dom Bosco", "José Bonifácio", distance = 3)
  grafo.connect("José Bonifácio","Guaianases", distance = 3)
  grafo.connect("Guaianases", "Antônio Gianetti Neto", distance = 4)
  grafo.connect("Antônio Gianetti Neto", "Ferraz de Vasconcelos", distance = 4)
  grafo.connect("Ferraz de Vasconcelos","Poá", distance = 4)
  grafo.connect("Poá", "Calmon Viana", distance = 2)
  grafo.connect("Calmon Viana", "Suzano", distance = 4)
  grafo.connect("Suzano", "Jundiapeba", distance = 7)
  grafo.connect("Jundiapeba", "Brás Cubas", distance = 5)
  grafo.connect("Brás Cubas", "Mogi das Cruzes", distance = 5)
  grafo.connect("Mogi das Cruzes", "Estudantes", distance = 3)


  grafo.locations["Luz"] = (-23.53397772240847, -46.63535221818501)
  grafo.locations["Brás"] = (-23.54489066427105, -46.61647320795409)
  grafo.locations["Tatuapé"] = (-23.540065228997243, -46.57652962908655)
  grafo.locations["Itaquera"] = (-23.54213678302639, -46.47104518675703)
  grafo.locations["Dom Bosco"] = (-23.54164883906437, -46.44812310209778)
  grafo.locations["José Bonifácio"] = (-23.538927199337365, -46.43167821559208)
  grafo.locations["Guaianases"] = (-23.542115996393246, -46.41554697326241)
  grafo.locations["Antônio Gianetti Neto"] = (-23.554164416217272, -46.38363564442716)
  grafo.locations["Ferraz de Vasconcelos"] = (-23.540632445512102, -46.368208544427375)
  grafo.locations["Poá"] = (-23.52525465409641, -46.34360500209793)
  grafo.locations["Calmon Viana"] = (-23.525204454032828, -46.33332027510901)
  grafo.locations["Suzano"] = (-23.533880073532885, -46.307994632779454)
  grafo.locations["Jundiapeba"] = (-23.542731834150434, -46.25804051559219)
  grafo.locations["Brás Cubas"] = (-23.536103986504855, -46.22526351743856)
  grafo.locations["Mogi das Cruzes"] = (-23.521024536515444, -46.196779459768536)
  grafo.locations["Estudantes"] = (-23.515169803448757, -46.184026373262995)


  grafo.linha["11"] = ["Luz", "Brás", "Tatuapé", "Itaquera", "Dom Bosco", "José Bonifácio", "Guaianases", "Antônio Gianetti Neto",
            "Ferraz de Vasconcelos", "Poá", "Calmon Viana", "Suzano", "Jundiapeba", "Brás Cubas", "Mogi das Cruzes", "Estudantes"]

  #Linha 12
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Brás", "Tatuapé", distance = 6)
  grafo.connect("Tatuapé", "Engenheiro Goulart", distance = 14)
  grafo.connect("Engenheiro Goulart", "USP Leste", distance = 3)
  grafo.connect("USP Leste", "Comendador Ermelino", distance = 5)
  grafo.connect("Comendador Ermelino", "São Miguel Paulista", distance = 7)
  grafo.connect("São Miguel Paulista", "Jardim Helena-Vila Mara", distance = 3)
  grafo.connect("Jardim Helena-Vila Mara", "Itaim Paulista", distance = 3)
  grafo.connect("Itaim Paulista", "Jardim Romano", distance = 3)
  grafo.connect("Jardim Romano", "Engenheiro Manoel Feio", distance = 3)
  grafo.connect("Engenheiro Manoel Feio", "Itaquaquecetuba", distance = 4)
  grafo.connect("Itaquaquecetuba", "Aracaré", distance = 4)
  grafo.connect("Aracaré", "Calmon Viana", distance = 4)


  grafo.locations["Brás"] = (-23.54489066427105, -46.61647320795409)
  grafo.locations["Tatuapé"] = (-23.540065228997243, -46.57652962908655)
  grafo.locations["Engenheiro Goulart"] = (-23.49801471078125, -46.51975277326335)
  grafo.locations["USP Leste"] = (-23.485322703076754, -46.5013334462745)
  grafo.locations["Comendador Ermelino"] = (-23.484932462824318, -46.4823367020988)
  grafo.locations["São Miguel Paulista"] = (-23.49038063044894, -46.443702002098696)
  grafo.locations["Jardim Helena-Vila Mara"] = (-23.492534833503054, -46.42113121743935)
  grafo.locations["Itaim Paulista"] = (-23.4938040141751, -46.40206327326347)
  grafo.locations["Jardim Romano"] = (-23.484678081678428, -46.38555301559313)
  grafo.locations["Engenheiro Manoel Feio"] = (-23.479080852302033, -46.36733614627488)
  grafo.locations["Itaquaquecetuba"] = (-23.485418863477456, -46.348569103945074)
  grafo.locations["Aracaré"] = (-23.499652843595996, -46.339033786757724)
  grafo.locations["Calmon Viana"] = (-23.525204454032828, -46.33332027510901)


  grafo.linha["12"] = ["Brás", "Tatuapé", "Engenheiro Goulart", "USP Leste", "Comendador Ermelino", "São Miguel Paulista", "Jardim Helena-Vila Mara", "Itaim Paulista", "Jardim Romano",
            "Engenheiro Manoel Feio", "Itaquaquecetuba", "Aracaré", "Calmon Viana"] 

  #Linha 13
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("Engenheiro Goulart", "Guarulhos Cecap", distance = 10)
  grafo.connect("Guarulhos Cecap", "Aeroporto de Guarulhos", distance = 3)

  grafo.locations["Engenheiro Goulart"] = (-23.49801471078125, -46.51975277326335)
  grafo.locations["Guarulhos Cecap"] = (-23.461511513613107, -46.4974875891592)
  grafo.locations["Aeroporto de Guarulhos"] = (-23.433280213296698, -46.49381650209965)


  grafo.linha["13"] = ["Engenheiro Goulart", "Guarulhos Cecap", "Aeroporto de Guarulhos"] 



  #Linha 15 
  ###########################
  #Ajustar o grafo
  #############################

  grafo.connect("São Mateus", "Fazenda da Juta", distance = 6)
  grafo.connect("Fazenda da Juta", "Sapopemba", distance = 4)
  grafo.connect("Sapopemba", "Jardim Planalto", distance = 5)
  grafo.connect("Jardim Planalto", "Vila União", distance = 3)
  grafo.connect("Vila União", "Vila Tolstói", distance = 4)
  grafo.connect("Vila Tolstói", "Camilo Haddad", distance = 2)
  grafo.connect("Camilo Haddad", "São Lucas", distance = 3)
  grafo.connect("São Lucas", "Oratório", distance = 3)
  grafo.connect("Oratório", "Vila Prudente", distance = 2)



  grafo.locations["São Mateus"] = (-23.6126262,-46.4781011)
  grafo.locations["Fazenda da Juta"] = (-23.6236, -46.4939)
  grafo.locations["Sapopemba"] = (-23.612, -46.4873)
  grafo.locations["Jardim Planalto"] = (-23.6062, -46.5078)
  grafo.locations["Vila União"] = (-23.603, -46.5156)
  grafo.locations["Vila Tolstói"] = (-23.6008, -46.5272)
  grafo.locations["Camilo Haddad"] = (-23.5954, -46.5376)
  grafo.locations["São Lucas"] = (-23.5889, -46.5446)
  grafo.locations["Oratório"] = (-23.5822, -46.5618)
  grafo.locations["Vila Prudente"] = (-23.5844, -46.5819)


  grafo.linha["15"] = ["São Mateus", "Fazenda da Juta", "Sapopemba", "Jardim Planalto", "Vila União", "Vila Tolstói",
            "Camilo Haddad", "São Lucas", "Oratório", "Vila Prudente"]
  return  grafo
