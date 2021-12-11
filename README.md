# geosampa
dados do geosampa


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


from IPython.display import IFrame
IFrame("http://wms.geosampa.prefeitura.sp.gov.br/geoserver/web/", width=950, height=600)

# Plotagem das linhas e estações metrô
![image](https://user-images.githubusercontent.com/36892558/145660651-97b68ac8-9ee5-47b3-9efc-11c6e5fcf2a7.png)

![image](https://user-images.githubusercontent.com/36892558/145660658-0eb0cddb-f975-48cd-9ed4-398da73e8518.png)


# Plotagem das linhas e estações trem
![image](https://user-images.githubusercontent.com/36892558/145660662-517f3a0c-0fc3-43b3-b768-18f93b293d94.png)


![image](https://user-images.githubusercontent.com/36892558/145660668-4899066d-34f5-4411-a8f8-c8c5e2d8afb0.png)


# Grafo linha metropolitana de São Paulo
![image](https://user-images.githubusercontent.com/36892558/145660698-9f634e27-a8f0-4e97-8470-f98b6b163b5f.png)




# IA com algoritimo A* e busca gulosa - para direcionar o melhor percurso
![image](https://user-images.githubusercontent.com/36892558/145660724-28e32912-dc49-4c72-ae42-9c869cc67300.png)


