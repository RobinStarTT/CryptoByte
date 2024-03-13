print("CryptoByte, o software ideal para quem quer criptografar e descriptografar informações de forma rápida, simples e segura.")#introdução ao programa
print("\n")
comando0 = int(input("Digite 1 para utilizar a criptografia simétrica mais simples, 2 para utilizar a criptografia simétrica mais complexa (requer biblioteca) ou 3 para ler os termos de uso e política de privacidade: "))

MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

if comando0 == 1:
    
    print("\n")
    comando1 = int(input("Digite 1 para criptografar, 0 para descriptografar ou 2 para conhecer essa versão do CryptoByte: "))

    if comando1 == 1:
        print("\n")
        msg = str(input("Digite a mensagem a ser criptografada: "))
        key = int(input("Digite a chave (numérica) que irá permitir a descriptografia da mensagem: "))
        ciphered = caesar(msg, key, MODE_ENCRYPT )
        print("\n")
        print("O código criptografado é: {}".format(ciphered))

        arquivo = open('ArqC - código e chave.txt','w')
        arquivo.write("O código gerado é: {} \n".format(ciphered))
        arquivo.write("A chave é: {} \n".format(key))
        arquivo.close()
        print("\n")
        comando2 = int(input("Gostaria de descriptografar a mensagem (1 para SIM ou 0 para NÃO)? "))
        print("\n")
        if comando2 == 1:
            msg1 = str(input("Digite o código gerado ao criptografar a mensagem: "))
            key1 = int(input("Digite a chave cadastrada ao criptografar a mensagem: "))
            cyphered = caesar(msg1, key1, MODE_DECRYPT)
            print("\n")
            print("A mensagem criptografada foi: {}".format(cyphered))
            arquivo = open('ArqC - mensagem descriptografada.txt','w')
            arquivo.write("A mensagem criptografada foi: {} \n".format(cyphered))
            arquivo.close()
            print("\n")
            print("Fim da criptografia.")


        if comando2 == 0:
            print("A mensagem não será descriptografada.")


    if comando1 == 0:
        print("\n")
        msg1 = str(input("Digite o código gerado ao criptografar a mensagem: "))
        key1 = int(input("Digite a chave cadastrada ao criptografar a mensagem: "))
        cyphered = caesar(msg1, key1, MODE_DECRYPT)
        print("\n")
        print("A mensagem criptografada foi: {}".format(cyphered))
        arquivo = open('ArqC - mensagem descriptografada.txt','w')
        arquivo.write("A mensagem criptografada foi: {} \n".format(cyphered))
        arquivo.close()
        print("\n")
        print("Fim da criptografia.")

    if comando1 == 2:
        print("\n")
        print("Nessa versão do CryptoByte, o programa utiliza a Crifa de César. É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Para codificar uma mensagem basta digitar seu conteúdo, cadastrar uma chave numérica e guardar o código gerado. Já para descriptografar, é necessário estar com o código gerado e a chave cadastrada. Reinicie o software e faça os testes.")
    else:
        print("\n")
        print("Fim do programa.")


if comando0 == 2:
    print("\n")
    comando = int(input("Digite 1 para criptografar, 0 para descriptografar ou 2 para conhecer essa versão do CryptoByte: ")) #ações que o usuário pode tomar
    from cryptography.fernet import Fernet, MultiFernet

    if comando == 1: 

        key1 = Fernet.generate_key().decode("utf-8") #criação de uma chave Fernet e posterior decodificação usando o padrão binário de comprimento variável
        key2 = Fernet.generate_key().decode("utf-8")
        key3 = Fernet.generate_key().decode("utf-8")

        k1 = Fernet(key1) #segunda codificação da chave gerada 
        k2 = Fernet(key2)
        k3 = Fernet(key3)

        f = MultiFernet([k1, k2, k3]) #cria uma relação entre as chaves geradas para que elas funcionem em conjunto
        print("\n")
        mensagem = str(input("Digite a mensagem a ser criptografada: ")) #o usuário entra com a informação que ele precisa criptografar
        codec = bytes(mensagem,"utf-8") #codificação da mensagem do tipo string em bytes usando o padrão UTF-8
        print("\n")
        token = f.encrypt(codec).decode("utf-8") #encriptando a mensagem que já havia sido criptografada de string para bytes, só que dessa vez usando a biblioteca, e após isso decriptando o código gerado usando o padrão UTF-8
        print("O código criptografado é: {}".format(token)) #impressão do código criptografado
        print("\n")
        print ("Para descriptografar a mensagem use as seguintes chaves de segurança: \n Chave 1: {} \n Chave 2: {} \n Chave 3: {}".format(key1, key2, key3)) #impressão das chaves geradas
    
        arquivo = open('ArqF - códigos e chaves.txt','w')
        arquivo.write("O código gerado é: {} \n".format(token))
        arquivo.write("A chave 1 é: {} \n".format(key1))
        arquivo.write("A chave 2 é: {} \n".format(key2))
        arquivo.write("A chave 3 é: {} \n".format(key3))
        arquivo.close()
        print("\n")
        comando5 = int(input("Gostaria de descriptografar a mensagem (1 para SIM ou 0 para NÃO)? ")) #ações que o usuário pode tomar
        if comando5 == 1:
            print("\n")
            codigo = str(input("Digite o código gerado ao criptografar a mensagem: ")) #para descriptografar, o usuário precisa fornecer o código gerado ao criptografar a mensagem
            print("\n")
            key1 = str(input("Digite a chave 1 gerada ao criptografar a mensagem: ")) #chave gerada ao criptografar
            k1 = Fernet(key1) #a chave digitada passa pelo padrão Fernet de criptografia

            key2 = str(input("Digite a chave 2 gerada ao criptografar a mensagem: "))
            k2 = Fernet(key2)

            key3 = str(input("Digite a chave 3 gerada ao criptografar a mensagem: "))
            k3 = Fernet(key3)

            f2 = MultiFernet([k1, k2, k3]) #verificação da veracidade das chaves e se elas compartilham do mesmo código

            rotated = f2.rotate(codigo) #o código inserido é criptografado novamente, isso preserva informações do dado criptografado (data/hora)
            drs = f2.decrypt(rotated) #decriptação do código (parte 01)

            traduzir = (drs).decode("utf-8") #decriptação do código (parte 02)
            print("\n")
            print("A mensagem criptografada foi: {}".format(traduzir))
            print("\n")
            arquivo = open('ArqF - mensagem descriptografada.txt','w')
            arquivo.write("A mensagem criptografada foi: {} \n".format(traduzir))
            arquivo.close()
            print("Fim da criptografia.")


        if comando5 == 0:
            print("\n")
            print("A mensagem não será descriptografada.")


    if comando == 0:
        print("\n")
        codigo = str(input("Digite o código gerado ao criptografar a mensagem: "))
        print("\n")
        key1 = str(input("Digite a chave 1 gerada ao criptografar a mensagem: "))
        k1 = Fernet(key1)

        key2 = str(input("Digite a chave 2 gerada ao criptografar a mensagem: "))
        k2 = Fernet(key2)

        key3 = str(input("Digite a chave 3 gerada ao criptografar a mensagem: "))
        k3 = Fernet(key3)

        f2 = MultiFernet([k1, k2, k3]) 

        rotated = f2.rotate(codigo)
        tomato = f2.decrypt(rotated)

        traduzir = (tomato).decode("utf-8")
        print("\n")
        print("A mensagem criptografada foi: {}".format(traduzir))
        print("\n")
        arquivo = open('ArqF - mensagem descriptografada.txt','w')
        arquivo.write("A mensagem criptografada foi: {} \n".format(traduzir))
        arquivo.close()
        print("Fim da criptografia.")


    
    if comando == 2:
        print("\n")
        print("Nessa versão do CrpytoByte, o programa utiliza a biblioteca Cryptography. Ela é especializada em criptografia de informações e é desenvolvida especificamente para a linguagem de programação Python. Inclui processos de baixo, médio e alto níveis de complexidade. Alguns dos métodos utilizados nas criptografias são: cifras simétricas, resumos das mensagens e funções para a derivação das chaves geradas. O app CryptoByte garante a criptografia de ponta à ponta dos seus dados de forma intuitiva e confiável. Reinicie o software e faça os testes.")

    else:
        print("\n")
        print("Fim do programa.")


if comando0 == 3:
    print("\n")
    print("Os seguintes termos de uso e política de privacidade garantem tanto ao usuário, quanto ao aplicativo, direitos e deveres ao executarem qualquer ação juntos:")
    print("\n")
    print("Política Privacidade:")
    print("A sua privacidade é importante para nós. É política do CryptoByte respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar no app CryptoByte. Solicitamos informações pessoais apenas quando realmente precisamos delas para lhe fornecer um serviço. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento. Também informamos por que estamos coletando e como será usado. Apenas retemos as informações coletadas pelo tempo necessário para fornecer o serviço solicitado. Quando armazenamos dados, protegemos dentro de meios comercialmente aceitáveis para evitar perdas e roubos, bem como acesso, divulgação, cópia, uso ou modificação não autorizados. Não compartilhamos informações de identificação pessoal publicamente ou com terceiros, exceto quando exigido por lei. Você é livre para recusar a nossa solicitação de informações pessoais, entendendo que talvez não possamos fornecer alguns dos serviços desejados. Se você tiver alguma dúvida sobre como lidamos com dados do usuário e informações pessoais, entre em contacto conosco.")
    print("\n")
    print("Política de Uso")
    print("Ao fazer uso do software, o usuário está ciente de que o aplicativo utiliza bibliotecas em sua composição para o seu melhor funcionamento, sendo esse fato acordado entre ambas as partes. ")
    print("\n")
    print("O que são bibliotecas?")
    print("As bibliotecas Python são um conjunto de módulos e funções úteis que reduzem o uso de código no programa. São mais de 137 mil bibliotecas Python que facilitam a programação dos desenvolvedores, com diversas finalidades. Por meio delas, é possível fazer tratamento de dados Python. Há, também, bibliotecas Python data science, bibliotecas Python para automação, dentre outras.")
    print("\n")
    print("Compromisso do usuário:")
    print("O usuário se compromete a fazer uso adequado dos conteúdos e da informação que o CryptoByte oferece no aplicativo e com caráter enunciativo, mas não limitativo:")
    print("A Não se envolver em atividades que sejam ilegais ou contrárias à boa fé a à ordem pública;")
    print("B Não difundir propaganda ou conteúdo de natureza racista, xenofóbica, ou azar, qualquer tipo de pornografia ilegal, de apologia ao terrorismo ou contra os direitos humanos;")
    print("C Não causar danos aos sistemas físicos (hardwares) e lógicos (softwares) do CryptoByte, de seus fornecedores ou terceiros, para introduzir ou disseminar vírus informáticos ou quaisquer outros sistemas de hardware ou software que sejam capazes de causar danos anteriormente mencionados.")