# Desafios de Código - Simulando Desafios com IAs Generativas
# 2 / 5 - Avaliando Prompts

# Descrição

Neste desafio, você será solicitado a criar um algoritmo que avalia se um prompt fornecido pelo usuário está adequado. O programa solicitará ao usuário que insira um prompt e, em seguida, verificará se o prompt contém palavras-chave relevantes. As palavras-chave consideradas relevantes serão "inteligência artificial", "sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de tecnologia". Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informará que o prompt está adequado; caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

## Entrada

O usuário será solicitado a inserir um prompt como entrada para o programa.

## Saída

O programa exibirá feedback para o usuário com base na avaliação do prompt inserido. Se o prompt contiver palavras-chave relevantes, o programa informará que o prompt está adequado. Caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
| --- | --- |
| Por favor, explique conceitos de inteligência artificial. | O prompt está adequado. |
| Crie exemplos de conversação. | O prompt está adequado. |
| Qual é a coisa mais bonita do mundo? | O prompt não está adequado. Inclua palavras-chave relevantes. |

## Atenção

Se você não está familiarizado com a linguagem de programação, não se preocupe! Você pode usar uma das seguintes inteligências artificiais para te ajudar a entender o código:

- ChatGPT: [https://chat.openai.com/](https://chat.openai.com/)
- Copilot: [https://copilot.microsoft.com/](https://copilot.microsoft.com/)
- Gemini: [https://gemini.google.com/](https://gemini.google.com/)
- Amazon Q (Para Empresas): [https://aws.amazon.com/pt/q/](https://aws.amazon.com/pt/q/)

Abaixo adicionamos algumas sugestões de uso e prompts para te auxiliar na resolução:

| Sugestões de Uso | Sugestões de Prompts |
| --- | --- |
| Explicação de Conceitos | Pode me explicar o que são estruturas de dados e dar exemplos? |
| Entendimento do Problema | Quais são as restrições ou requisitos específicos que devo considerar neste desafio? |
| Sugestões de Abordagem | Quais são as etapas principais que devo seguir para resolver este desafio? |
| Ajuda na Depuração | Estou recebendo um erro de sintaxe neste trecho de código. O que pode estar errado? |
| Revisão de Algoritmos | Você pode revisar meu algoritmo de ordenação e me dar feedback sobre sua eficiência? |

# SOLUÇÃO COMENTADA:

     #Entrada do usuário
      prompt_usuario = input()
   
     #Função para avaliar se o prompt está adequado
     def avaliar_prompt(prompt):
       #Verifica se o prompt contém palavras-chave relevantes
       palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia" ]
    
    #TODO: Aplique a condição necessária para verificar se o prompt está ou não adequado de acordo com o enunciado
    #Verifica se alguma das palavras-chave está no prompt
    for palavra in palavras_chave:
        if palavra in prompt.lower():
            return "O prompt está adequado."
    
    return "O prompt não está adequado. Inclua palavras-chave relevantes."
    
    #Avaliar o prompt do usuário
    feedback_usuario = avaliar_prompt(prompt_usuario)

    #Exibir feedback
    print(feedback_usuario)
