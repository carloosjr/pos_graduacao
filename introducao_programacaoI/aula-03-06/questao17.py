# Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame
# este dicionário de glossário.

# a. Pense em cinco palavras relacionadas à programação que você conhece. Use estas palavras como chaves em seu
# glossário e armazene seus significados como valores.

# b. Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo:
# você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma
# linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
# para inserir uma linha em branco entre cada palavra-significado em sua saída.

# c. Sugestões de termos: Algoritmos, Python, Web Scraping, Lógica de Programação, Google Colab, Visual Studio Code

glossario = {
     'Algoritmos': 'São sequências de instruções lógicas e precisas que resolvem um problema específico. Em programação, um algoritmo é uma série de passos bem definidos que um computador segue para realizar uma tarefa.',
     
     'Python': 'É uma linguagem de programação popular e de alto nível, conhecida por sua sintaxe clara e legível. Python é amplamente utilizado em uma variedade de domínios, desde o desenvolvimento de aplicativos web de análise até de dados e inteligência artificial.',
     
     'Web Scraping': 'É a técnica de captura automática de dados de sites da web. Usando web scraping, é possível extrair informações de uma página da web de forma estruturada, geralmente convertendo-as em um formato como CSV ou JSON.',
         
     'Lógica de Programação': 'É o conjunto de regras e princípios usados ​​para projetar algoritmos e resolver problemas usando programação. A lógica de programação envolve a compreensão de estruturas de controle, como condicionais e loops, e a habilidade de criar sequências lógicas de instruções para alcançar um objetivo.',
         
     'Google Colab': 'É um serviço gratuito baseado na nuvem oferecido pelo Google. Ele fornece um ambiente de notebook interativo que permite escrever e executar o código Python diretamente no navegador, sem a necessidade de configurar um ambiente local. ',
         
     'Visual Studio Code': 'É um editor de código-fonte gratuito e altamente popular, desenvolvido pela Microsoft. Ele suporta várias linguagens'    
 }

for i in glossario:
    print(f'{i.upper()}: \n\t{glossario[i]}')