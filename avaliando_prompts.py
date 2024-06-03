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