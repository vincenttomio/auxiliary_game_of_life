# Auxiliares para o Jogo da Vida Reverso

Este repositório contém scripts auxiliares desenvolvidos para apoiar a implementação do projeto [Jogo da Vida Reverso](https://github.com/vincenttomio/ia_jogo_da_vida/tree/main). Esses scripts foram utilizados para criar entradas, calcular a próxima geração em uma matriz de acordo com as regras de Conway, e analisar a proporção de células vivas e mortas.

## Descrição dos Arquivos

1. **`entrada.py`**
   - Função: Gera uma matriz inicial de entrada para o Jogo da Vida.
   - Utilização: Facilita a criação de entradas para testes e simulações do jogo.

2. **`prox.py`**
   - Função: Calcula o próximo estado de uma matriz usando as regras do Jogo da Vida de Conway.
   - Utilização: Permite verificar como uma configuração inicial evoluirá com base nas regras do jogo.

3. **`conta_zero.py`**
   - Função: Analisa uma matriz do Jogo da Vida e retorna a porcentagem de células vivas e mortas.
   - Utilização: Auxilia no cálculo de métricas para avaliar os estados gerados.

## Contexto do Projeto

Os scripts neste repositório foram usados como ferramentas complementares para o desenvolvimento do projeto "Jogo da Vida Reverso", cujo objetivo é implementar um programa que recebe como entrada um estado do Jogo da Vida em uma matriz e retorna um estado imediatamente anterior que minimiza o número de células vivas.

Mais detalhes sobre o projeto principal estão disponíveis no repositório [Jogo da Vida Reverso](https://github.com/vincenttomio/ia_jogo_da_vida/tree/main).

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/auxiliary_game_of_life.git
   ```

2. Navegue para o diretório clonado:
   ```bash
   cd auxiliary_game_of_life
   ```

3. Execute os scripts conforme necessário, por exemplo:
   - Gerar uma matriz de entrada:
     ```bash
     python entrada.py
     ```
   - Calcular o próximo estado:
     ```bash
     python prox.py
     ```
   - Analisar porcentagem de células vivas e mortas:
     ```bash
     python conta_zero.py
     ```



---

**Nota:** Estes scripts foram desenvolvidos para fins educacionais e experimentais no contexto do projeto citado. Não são otimizados para produção.

🎓 **Autor:** Vincent Tomio

📫 Entre em contato: [seu-email](mailto:vvsbt20@inf.ufpr.br)
