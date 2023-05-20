<h1 align="center">Análise Perfil Instagram - BBB</h1>
<h4 align="justify">Projeto visa construir uma base de dados extraindo dados do Instagram de perfis dos participante do BBB 23. O código será automatizado para todos os dias buscar dados e gerar um arquivo texto, gráfico e xlsx. </h4>
<h4> É disponibilizado via REST Api, desenvolvido com Flask com rotas para trazer o números de todos inscritos e bem como trazer o histório de inscrito geral e pessoal. </h4>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

## 🖥️ Tecnologías Utilizadas:

- Python 3.9</br>
- Flask </br>
- Pandas </br>
- Instaloader </br>
- BeautifulSoup </br>

## 📌 Rotas da API:
 API hospedada no [Render](http://render.com/) gratuitamente, por essa razão, a primeira vez para acessar a API demorá cerca de 30s a 60s. 
 <p>A base de dados não está sendo mais atualizada diariamente devido o fim do BBB</p>
 <p> Em geral a a API retorna dados dos brothers como nome, imagem, username do instagram e quantidade de seguidores, o status se está ainda no programa, quem é lider, mostro e paredão </p>

    - Retorna dados de todos o participantes
    https://instabrothers-bbb-api.onrender.com/brothers

    - Retornar dados dos participantes ordenado por quem está ganhando mais seguidores
    https://instabrothers-bbb-api.onrender.com/brother/compare-followers

    - Retorna detalhado por data quantos seguidores possuia o participante passado por parâmetro
    https://instabrothers-bbb-api.onrender.com/brother/{NomeParticipante}
    
    - Retorna ranking dos participantes que possuem mais seguidores
    https://instabrothers-bbb-api.onrender.com/ranking
    
    - Retorna noticias relacionado ao BBB com base no site NoticiasdaTv do Uol
    https://instabrothers-bbb-api.onrender.com/news


## :hammer: Funcionalidades do projeto

- `Gerar DataFrame`: busca perfil dos participantes do BBB 23


