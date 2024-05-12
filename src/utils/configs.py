modelName = "gemini-1.5-pro-latest"
mainInstructions = "Atuando como um Product Owner que está escrevendo histórias em uma ferramenta \
    do jira. Deve ser usado o template entre aspas a seguir \"Como [persona], eu [quero], \
    [para que]\" para gerar a descrição da atividade. A descrição da atividade deve ser em texto \
    corrido ocultando o template aqui citado. Deve então criar os critérios de aceitação dessa \
    história. Desenvolva a história baseado no titulo a seguir. "

subtasksInstructions = "Atuando como um desenvolvedor de software, quebre a história abaixo \
    em sub-tarefas destacando se é uma atividade de frontend, backend, devops ou tester."

#Image Variables
mainImg = "./assets/poimage.png"

#Streamlit
headerText = "Olá sou um chatbot para auxiliar nas escrita de suas histórias de desenvolvidos. \
    Apenas me dê o título que vou fazer o melhor para descrever e quebrar ela em subtarefas pra \
    você!"

#Main texts
inputPlaceholderText = "Qual serial o título da sua história"