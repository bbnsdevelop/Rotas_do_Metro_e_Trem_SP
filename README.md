# Trabalho de conclusão do curso de Ciências da computação - Rotas das linhas metropolitana de São Paulo
Este trabalho tem como objetivo apresentar para o usuário, qual a rota mais rápida para navegar nos trens e metrô de Saão Paulo.
Utilizaremos os dados do GeoSampa para analisar os dados, usaremos a IA AIMA para solucionar nosso Problema e por fim, também usaremos os algoritmos A-Estrela e busca Gulosa. 


# API
Ultilizaremos a API GeoSampa para consultar as linhas metropolitana do estado de São Paulo, e com bases nessas informações nossa IA irá definir uma melhor rota a ser tomada.

# O que é o GeoSampa?
GeoSampa não é apenas um site
Infraestrutura de dados espaciais <----
Bancos de dados PostGis, GeoServer(s), Servidor de Arquivos, ETL (Extract, Transfer, Load)
Softwares Livres (Decreto Nº 58.447 de 1º de outubro de 2018)
Equipe de pessoas GeoInfo e Intersecretarial
Mais recentemente: Amazon OpenData (LiDAR 3D recente) e GitHub
Estabelecido em Decreto
Decreto 57.770, de 03 de julho de 2017
Estabelece O Sistema de Informações Geográficas do Município de São Paulo – SIG-SP
IMDE - Infra-estrutura Municipal de Dados Espaciais
SIG-SP é um sistema aberto, integrador, dinâmico e permanente, em constante adequação à realidade urbana e à evolução das ferramentas tecnológicas.

```
from IPython.display import IFrame
IFrame("http://wms.geosampa.prefeitura.sp.gov.br/geoserver/web/", width=950, height=600)
```

# Plotagem das linhas e estações metrô
![image](https://user-images.githubusercontent.com/36892558/145660651-97b68ac8-9ee5-47b3-9efc-11c6e5fcf2a7.png)

![image](https://user-images.githubusercontent.com/36892558/145660658-0eb0cddb-f975-48cd-9ed4-398da73e8518.png)

```
msp_linhas

lmt_empres	lmt_nome	lmt_linha	geometry
0	METRO	AZUL	1	LINESTRING (336347.634 7402505.900, 336236.084...
1	METRO	LILAS	5	LINESTRING (319728.880 7382422.010, 319870.607...
2	METRO	VERMELHA	3	LINESTRING (329805.473 7397314.933, 329892.801...
3	METRO	PRATA	15	LINESTRING (349391.385 7387987.827, 349196.481...
4	METRO	VERDE	2	LINESTRING (327451.814 7395020.984, 327563.894...
5	VIAQUATRO	AMARELA	4	LINESTRING (333193.209 7396221.222, 333147.548...

```


# Plotagem das linhas e estações trem
![image](https://user-images.githubusercontent.com/36892558/145660662-517f3a0c-0fc3-43b3-b768-18f93b293d94.png)


![image](https://user-images.githubusercontent.com/36892558/145660668-4899066d-34f5-4411-a8f8-c8c5e2d8afb0.png)


```
trem_linhas

ltr_numero	ltr_empres	ltr_nome	geometry
0	13	CPTM	JADE	LINESTRING (344212.277 7400379.429, 344235.200...
1	13	CPTM	JADE	LINESTRING (344762.782 7400564.924, 344769.279...
2	13	CPTM	JADE	LINESTRING (344673.476 7400514.990, 344686.490...
3	9	CPTM	ESMERALDA	LINESTRING (318956.336 7396814.286, 319008.122...
4	9	CPTM	ESMERALDA	LINESTRING (318956.336 7396814.286, 318979.453...
5	9	CPTM	ESMERALDA	LINESTRING (326980.186 7379832.304, 326989.444...
6	9	CPTM	ESMERALDA	LINESTRING (318748.108 7396977.637, 318801.857...
7	9	CPTM	ESMERALDA	LINESTRING (326306.607 7380757.824, 326314.105...
8	9	CPTM	ESMERALDA	LINESTRING (326306.607 7380757.824, 326311.003...
9	8	CPTM	DIAMANTE	LINESTRING (332532.439 7396605.883, 332487.009...
10	8	CPTM	DIAMANTE	LINESTRING (332539.013 7396610.414, 332493.998...
11	10	CPTM	TURQUESA	LINESTRING (333103.262 7396319.342, 333289.875...
12	10	CPTM	TURQUESA	LINESTRING (344732.767 7383142.844, 344800.492...
13	10	CPTM	TURQUESA	LINESTRING (333104.119 7396323.216, 333291.018...
14	10	CPTM	TURQUESA	LINESTRING (333107.031 7396336.378, 333277.564...
15	12	CPTM	SAFIRA	LINESTRING (356557.146 7401117.470, 356557.299...
16	12	CPTM	SAFIRA	LINESTRING (356557.146 7401117.470, 356578.435...
17	12	CPTM	SAFIRA	LINESTRING (356556.817 7401124.159, 356558.689...
18	12	CPTM	SAFIRA	LINESTRING (335022.662 7395309.113, 335107.969...
19	12	CPTM	SAFIRA	LINESTRING (357207.308 7401168.719, 357312.900...
20	12	CPTM	SAFIRA	LINESTRING (357212.464 7401173.680, 357177.463...
21	12	CPTM	SAFIRA	LINESTRING (357212.464 7401173.680, 357255.944...
22	12	CPTM	SAFIRA	LINESTRING (335037.357 7395317.883, 335118.796...
23	7	CPTM	RUBI	LINESTRING (332488.423 7396741.171, 332481.138...
24	7	CPTM	RUBI	LINESTRING (332488.423 7396741.171, 332482.505...
25	7	CPTM	RUBI	LINESTRING (333107.895 7396340.287, 333083.539...
26	7	CPTM	RUBI	LINESTRING (333103.262 7396319.342, 333078.447...
27	7	CPTM	RUBI	LINESTRING (328909.577 7397439.890, 328890.263...
28	7	CPTM	RUBI	LINESTRING (331051.744 7397167.405, 331039.426...
29	7	CPTM	RUBI	LINESTRING (323329.960 7401796.955, 323273.341...
30	7	CPTM	RUBI	LINESTRING (321173.428 7415050.508, 321204.438...
31	7	CPTM	RUBI	LINESTRING (321173.428 7415050.508, 321202.003...
32	7	CPTM	RUBI	LINESTRING (321910.685 7416041.001, 321997.834...
33	7	CPTM	RUBI	LINESTRING (324009.436 7401193.647, 324001.059...
34	7	CPTM	RUBI	LINESTRING (324009.436 7401193.647, 323992.360...
35	7	CPTM	RUBI	LINESTRING (322415.272 7405092.025, 322401.144...
36	7	CPTM	RUBI	LINESTRING (322415.272 7405092.025, 322408.283...
37	7	CPTM	RUBI	LINESTRING (333104.119 7396323.216, 333079.357...
38	7	CPTM	RUBI	LINESTRING (317214.135 7432658.472, 317211.801...
39	7	CPTM	RUBI	LINESTRING (317214.135 7432658.472, 317196.707...
40	7	CPTM	RUBI	LINESTRING (315667.577 7432651.557, 315557.446...
41	7	CPTM	RUBI	LINESTRING (333107.031 7396336.378, 333082.581...
42	13	CPTM	JADE	LINESTRING (344214.316 7400383.594, 344233.463...
43	11	CPTM	CORAL	LINESTRING (333107.895 7396340.287, 333246.019...
44	11	CPTM	CORAL	LINESTRING (333107.031 7396336.378, 333277.564...

```




# Grafo linha metropolitana de São Paulo
![image](https://user-images.githubusercontent.com/36892558/145660698-9f634e27-a8f0-4e97-8470-f98b6b163b5f.png)



```
tempo = 0
estacoes = []
for node_caminho in node.path():
  print("Estação: "+node_caminho.state)
  estacoes.append(node_caminho.state)
  tempo = node_caminho.path_cost
  
```
# Descrição do percurso:
```
Estação: Jundiaí
Estação: Várzea Paulista
Estação: Campo Limpo Paulista
Estação: Botujuru
Estação: Francisco Morato
Estação: Baltazar Fidélis
Estação: Caieiras
Estação: Perus
Estação: Vila Aurora
Estação: Jaraguá
Estação: Vila Clarice
Estação: Pirituba
Estação: Piqueri
Estação: Lapa
Estação: Palmeiras - Barra Funda
Estação: Luz
Estação: Brás
Estação: Juventus - Mooca
Estação: Ipiranga
Estação: Tamanduateí
Estação: São Caetano do Sul - Prefeito Walter Braido
Estação: Utinga
Estação: Prefeito Saladino
Estação: Prefeito Celso Daniel Santo André
Estação: Capuava
Estação: Mauá
Estação: Guapituba
Estação: Ribeirão Pires
Estação: Rio Grande Da Serra
```

# IA com algoritimo A* e busca gulosa - para direcionar o melhor percurso
![image](https://user-images.githubusercontent.com/36892558/145660724-28e32912-dc49-4c72-ae42-9c869cc67300.png)


