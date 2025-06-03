Minhas alterações
principal.py
1 - Alterado o lugar do comando limp("cls") para dentro do While
2 - Acrescentada a opção 6 - Raiz - para solicitar o segundo valor
3 - Inicializada as variáveis valor1 e valor2 para evitar erro caso o segundo valor não seja solicitado.
4 - Alterado o nome da variável resutado para resultado
5 - Retirada a opção 10 do menu (interface) - se é secreto não pode aparecer
6 - Criado um dicionário para deixar a mensagem do resultado mais amigável
7 - Inserido comando para salvar o histórico

operacoes.py
1 - retirado o teste de opção de saída selecionada que já é testado no principal.py

interface.py
1 - Retirada a opção 10 do menu
2 - Alterado o nome de Soma para Adição, seguindo o padrão das outras operações

historico.py
1 - Inserida a funçao arquivo para checar se existe ou não
2 - Criada a função salvar_historico que não existia

Outros
1 - Criado o arquivo game_cobrinha.py para completar o jogo
2 - Ajustado posicionamento das mensagens finais do jogo
3 - Eliminado o comando quit para não encerrar a calculadora
