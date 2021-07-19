# flask-brq

## Conhecimentos aplicados:
- Python
- Flask-RestX
- SQLAlchemy
- Flask Migrate
- Pandas
- SQLite3

### Primeiro
Instalar as dependências
```bash
pip install -r requirements.txt
```

### Segundo
Criar gerar os arquivos e popular o banco
```bash
python scrip_popular_banco.py
```
Rodar somente na primeira execução. Não fiz travas, pq não tive muito tempo de pensar em todos os cenários de problema que o usuário conseguiria alcançar.
É um problema? Sim. Vou corrigir? Talvez.

### Terceiro
Rodar a aplicaçao
```bash
make run-dev
```

### Extras
Rodando com o Dockerfile
```bash
make build
```
Depois
```bash
make run
```

### Perguntas e respostas
1. É possível encontrar bugs? **R.: Sim**
2. Se encontrei um bug, o que faço? **R.: Sinta-se a vontade para abrir issues.**
3. De 0 a 10, o quanto me diverti e aprendi fazendo esse teste? **R.: 7**
4. O que achei mais fácil? **R.: Preparar os dados com o Pandas, já é algo que faço pra validar base de dados extensas.**
5. O que achei mais difícil? **R.: Popular o banco de dados. Não trabalhei tanto com o SQLAlchemy e tenho certeza que não escolhi a melhor maneira, mas tentei fazer de uma maneira "menos feia", inserindo em bulk.**
6. Onde acho que deixei a desejar? **R.: Nas APIs e documentaçãoes, e não ter feito testes automatizados.**
7. Por quê não escrevi testes? **R.: Tempo mesmo, investi mais tempo garantindo outros pontos e também não consegui me programar de maneira mais eficaz durante o fim de semana.**


