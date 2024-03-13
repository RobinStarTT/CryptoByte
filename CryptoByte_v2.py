# Função para criptografar/descriptografar usando a Cifra de César
def caesar(data, key, mode):
    # Alfabeto utilizado na cifra
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            # Calcula o novo índice para criptografar/descriptografar
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            # Garante que o novo índice esteja dentro do tamanho do alfabeto
            new_index = new_index % len(alphabet)
            # Adiciona a letra correspondente ao novo índice à nova mensagem
            new_data += alphabet[new_index:new_index+1]
    return new_data

# Constantes para indicar o modo de criptografar/descriptografar
MODE_ENCRYPT = 1
MODE_DECRYPT = 0

# Introdução ao programa
print("CryptoByte, o software ideal para quem quer criptografar e descriptografar informações de forma rápida, simples e segura.")
print("\n")

# Menu principal
comando0 = int(input("Digite 1 para utilizar a criptografia simétrica mais simples, 2 para utilizar a criptografia simétrica mais complexa (requer biblioteca) ou 3 para ler os termos de uso e política de privacidade: "))

# Opção 1: Criptografia Simples
if comando0 == 1:
    print("\n")
    comando1 = int(input("Digite 1 para criptografar, 0 para descriptografar ou 2 para conhecer essa versão do CryptoByte: "))

    if comando1 == 1:
        print("\n")
        msg = input("Digite a mensagem a ser criptografada: ")
        key = int(input("Digite a chave (numérica) que irá permitir a descriptografia da mensagem: "))
        ciphered = caesar(msg, key, MODE_ENCRYPT)
        print("\n")
        print("O código criptografado é: {}".format(ciphered))
        arquivo = open('ArqC - código e chave.txt', 'w')
        arquivo.write("O código gerado é: {} \n".format(ciphered))
        arquivo.write("A chave é: {} \n".format(key))
        arquivo.close()
        print("\n")
        comando2 = int(input("Gostaria de descriptografar a mensagem (1 para SIM ou 0 para NÃO)? "))
        print("\n")

        if comando2 == 1:
            msg1 = input("Digite o código gerado ao criptografar a mensagem: ")
            key1 = int(input("Digite a chave cadastrada ao criptografar a mensagem: "))
            cyphered = caesar(msg1, key1, MODE_DECRYPT)
            print("\n")
            print("A mensagem criptografada foi: {}".format(cyphered))
            arquivo = open('ArqC - mensagem descriptografada.txt', 'w')
            arquivo.write("A mensagem criptografada foi: {} \n".format(cyphered))
            arquivo.close()
            print("\n")
            print("Fim da criptografia.")
            input()

        elif comando2 == 0:
            print("A mensagem não será descriptografada.")
            input()

    elif comando1 == 0:
        msg1 = input("Digite o código gerado ao criptografar a mensagem: ")
        key1 = int(input("Digite a chave cadastrada ao criptografar a mensagem: "))
        cyphered = caesar(msg1, key1, MODE_DECRYPT)
        print("\n")
        print("A mensagem criptografada foi: {}".format(cyphered))
        arquivo = open('ArqC - mensagem descriptografada.txt', 'w')
        arquivo.write("A mensagem criptografada foi: {} \n".format(cyphered))
        arquivo.close()
        print("\n")
        print("Fim da criptografia.")
        input()

    elif comando1 == 2:
        print("\n")
        print("Nessa versão do CryptoByte, o programa utiliza a Cifra de César. Reinicie o software e faça os testes.")
        input()

    else:
        print("\n")
        print("Fim do programa.")
        input()

# Opção 2: Criptografia Complexa
elif comando0 == 2:
    print("\n")
    comando = int(input("Digite 1 para criptografar, 0 para descriptografar ou 2 para conhecer essa versão do CryptoByte: "))

    from cryptography.fernet import Fernet, MultiFernet

    if comando == 1: 
        key1 = Fernet.generate_key().decode("utf-8")
        key2 = Fernet.generate_key().decode("utf-8")
        key3 = Fernet.generate_key().decode("utf-8")
        k1 = Fernet(key1)
        k2 = Fernet(key2)
        k3 = Fernet(key3)
        f = MultiFernet([k1, k2, k3])
        print("\n")
        mensagem = input("Digite a mensagem a ser criptografada: ")
        codec = bytes(mensagem, "utf-8")
        print("\n")
        token = f.encrypt(codec).decode("utf-8")
        print("O código criptografado é: {}".format(token))
        print("\n")
        print("Para descriptografar a mensagem use as seguintes chaves de segurança: \n Chave 1: {} \n Chave 2: {} \n Chave 3: {}".format(key1, key2, key3))
        arquivo = open('ArqF - códigos e chaves.txt', 'w')
        arquivo.write("O código gerado é: {} \n".format(token))
        arquivo.write("A chave 1 é: {} \n".format(key1))
        arquivo.write("A chave 2 é: {} \n".format(key2))
        arquivo.write("A chave 3 é: {} \n".format(key3))
        arquivo.close()
        print("\n")
        comando5 = int(input("Gostaria de descriptografar a mensagem (1 para SIM ou 0 para NÃO)? "))

        if comando5 == 1:
            print("\n")
            codigo = input("Digite o código gerado ao criptografar a mensagem: ")
            print("\n")
            key1 = input("Digite a chave 1 gerada ao criptografar a mensagem: ")
            k1 = Fernet(key1)
            key2 = input("Digite a chave 2 gerada ao criptografar a mensagem: ")
            k2 = Fernet(key2)
            key3 = input("Digite a chave 3 gerada ao criptografar a mensagem: ")
            k3 = Fernet(key3)
            f2 = MultiFernet([k1, k2, k3])
            rotated = f2.rotate(codigo)
            drs = f2.decrypt(rotated)
            traduzir = (drs).decode("utf-8")
            print("\n")
            print("A mensagem criptografada foi: {}".format(traduzir))
            print("\n")
            arquivo = open('ArqF - mensagem descriptografada.txt', 'w')
            arquivo.write("A mensagem criptografada foi: {} \n".format(traduzir))
            arquivo.close()
            print("Fim da criptografia.")
            input()

        elif comando5 == 0:
            print("\n")
            print("A mensagem não será descriptografada.")
            input()

    elif comando == 0:
        print("\n")
        codigo = input("Digite o código gerado ao criptografar a mensagem: ")
        print("\n")
        key1 = input("Digite a chave 1 gerada ao criptografar a mensagem: ")
        k1 = Fernet(key1)
        key2 = input("Digite a chave 2 gerada ao criptografar a mensagem: ")
        k2 = Fernet(key2)
        key3 = input("Digite a chave 3 gerada ao criptografar a mensagem: ")
        k3 = Fernet(key3)
        f2 = MultiFernet([k1, k2, k3])
        rotated = f2.rotate(codigo)
        tomato = f2.decrypt(rotated)
        traduzir = (tomato).decode("utf-8")
        print("\n") 
        print("A mensagem criptografada foi: {}".format(traduzir))
        print("\n")
        arquivo = open('ArqF - mensagem descriptografada.txt', 'w')
        arquivo.write("A mensagem criptografada foi: {} \n".format(traduzir))
        arquivo.close()
        print("Fim da criptografia.")
        input()

    elif comando == 2:
        print("\n")
        print("Nessa versão do CrpytoByte, o programa utiliza a biblioteca Cryptography. Reinicie o software e faça os testes.")
        input()

    else:
        print("\n")
        print("Fim do programa.")
        input()

# Opção 3: Termos de Uso e Política de Privacidade
elif comando0 == 3:
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
    input()


print('Test for commit')