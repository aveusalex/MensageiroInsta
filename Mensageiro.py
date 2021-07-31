from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date
from pytz import timezone
import time
import random
import os


arquivo = "tudoju.txt"
arq = os.getcwd().split("\\")[0] + "\\BOT_insta\\bases\\" + arquivo

with open("E:\\BOT_insta\\Mensageiro\\frases.txt") as texto:
    frases = [frase for frase in texto]


def remove_repetidos(diretorio):
    listinha = []
    with open(diretorio, "r") as f:
        A = f.read()
        A = A.split("!")
        for i in A:
            if i not in listinha:
                listinha.append(i)

    return listinha


def digite_como_pessoa(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        time.sleep(random.randint(1, 5) / 15)


def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    dias = int(value / (24 * 3600))

    valorH = value - (dias * 24 * 3600)
    horas = int(valorH / 3600)

    valorM = valorH - (horas * 3600)
    minutos = int(valorM / 60)

    valorS = valorM - (minutos * 60)
    segundos = int(valorS)

    return f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos."


def main(usuario, pasword, link, frase_antes, shut):
    try:
        data = f"{date.today().day}/{date.today().month}/{date.today().year}"
        hora_inicio = datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%H:%M:%S")
        qtsjafoi = 0
        Fim = False
        er = 0
        bloqueados = 0
        # insira a base de dados em useerss
        pessoas = remove_repetidos(arq)
        # onde iniciar a lista?
        with open("E:\\BOT_insta\\parada.txt") as ultimo:
            ini = ultimo.readline()

        if ini == 'Cabou':
            beg = 0
        else:
            beg = pessoas.index(ini)
        beg1 = beg
        root = str(os.getcwd().split("\\")[0])
        driver = webdriver.Firefox(executable_path=f"{root}\\BOT_insta\\geckodriver\\geckodriver.exe")
        driver.get(link)
        time.sleep(5)
        driver.find_element_by_xpath("//input[@name='username']").click()
        login = driver.find_element_by_xpath("//input[@name='username']")
        login.clear()
        # usuario de login
        digite_como_pessoa(usuario, login)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='password']").click()
        senha = driver.find_element_by_xpath("//input[@name='password']")
        senha.clear()
        # senha de login
        digite_como_pessoa(pasword, senha)
        time.sleep(2)
        senha.send_keys(Keys.RETURN)
        time.sleep(6)
        for i in range(2):
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
                time.sleep(3)
            except:
                pass

        while not Fim:
            i = pessoas[beg][1:]

            try:
                pesq = driver.find_element_by_xpath('//span[@class="TqC_a"]')
                pesq.click()
                time.sleep(2)
                pesq = driver.find_element_by_xpath('//input[@class="XTCLo x3qfX focus-visible"]')
                digite_como_pessoa(f"{i}", pesq)
                ultimo_marcado = i
                time.sleep(random.randint(9, 10))
                s = 0
                while s < 4:
                    try:
                        pesq.send_keys(Keys.RETURN)
                        time.sleep(4)
                    except:
                        pass
                    s += 1
                try:
                    driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]").click()
                    time.sleep(random.randint(4, 6))
                except:
                    pass
                driver.find_element_by_xpath("//button[contains(text(), 'Enviar mensagem')]").click()
                time.sleep(random.randint(5, 6))
                try:
                    driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
                    time.sleep(3)
                except:
                    pass
                chat = driver.find_element_by_xpath("//textarea")
                chat.click()
                chat.clear()
                time.sleep(5)
                digite_como_pessoa(frase_antes[random.randint(0, len(frase_antes))], chat)  # Mayra
                qtsjafoi += 1
                time.sleep(random.randint(5, 7))
                chat.send_keys(Keys.RETURN)
                time.sleep(random.randint(30, 45))
                print(f"{qtsjafoi} : @{i}")
                er = 0
                driver.back()
                time.sleep(2)
                driver.back()
                time.sleep(5)
                beg += 1

                if beg == len(pessoas) - beg1:
                    with open("E:\\BOT_insta\\parada.txt", "w") as ultimo:
                        ultimo.write("Cabou")

                    Fim = True

            except:
                print(f"@{i} é fechado")
                bloqueados += 1
                er += 1
                beg += 1
                driver.back()
                time.sleep(5)
                time.sleep(10)
                if er == 10:
                    with open("E:\\BOT_insta\\parada.txt", "w") as ultimo:
                        ultimo.write("@" + i)

                    Fim = True

        hora_fim = datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%H:%M:%S")

        hora_seg_inicio = hora_inicio.split(":")
        hora_seg_fim = hora_fim.split(":")
        contar = 0

        for parte in hora_seg_inicio:
            if contar == 0:
                segundos_inicio = int(parte) * 3600
                contar += 1
            elif contar == 1:
                segundos_inicio += int(parte) * 60
                contar += 1
            elif contar == 2:
                segundos_inicio += int(parte)
                contar += 1

        contar = 0

        for parte in hora_seg_fim:
            if contar == 0:
                segundos_fim = int(parte) * 3600
                contar += 1
            elif contar == 1:
                segundos_fim += int(parte) * 60
                contar += 1
            elif contar == 2:
                segundos_fim += int(parte)
                contar += 1

        data_fim = f"{date.today().day}/{date.today().month}/{date.today().year}"
        dias = int(data_fim.split("/")[0]) - int(data.split('/')[0])
        if segundos_fim >= segundos_inicio:
            duracao = segundos_fim - segundos_inicio
            if dias > 0:
                duracao += dias * 3600 * 24
        elif segundos_fim < segundos_inicio:
            duracao = (segundos_fim) + ((24 * 3600) - segundos_inicio)
            if dias > 1:
                duracao += (dias - 1) * 3600 * 24
        duracao = stopWatch(duracao)

        with open("E:\\BOT_insta\\relatorios\\relatorio.txt", "a+") as info:
            info.write(
                f"No dia {data}, houveram {qtsjafoi} comentários no sorteio {link} na conta de @{usuario}. {bloqueados} contas fechadas. Início: {hora_inicio} - {data}. Fim: {hora_fim} - {data_fim}. Duração: {duracao}. Último marcado: {ultimo_marcado}. Base de dados: {arq}\n\n")

        if shut == True:
            os.system('shutdown -s')

    except:
        hora_fim = datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%H:%M:%S")

        hora_seg_inicio = hora_inicio.split(":")
        hora_seg_fim = hora_fim.split(":")
        contar = 0

        for parte in hora_seg_inicio:
            if contar == 0:
                segundos_inicio = int(parte) * 3600
                contar += 1
            elif contar == 1:
                segundos_inicio += int(parte) * 60
                contar += 1
            elif contar == 2:
                segundos_inicio += int(parte)
                contar += 1

        contar = 0

        for parte in hora_seg_fim:
            if contar == 0:
                segundos_fim = int(parte) * 3600
                contar += 1
            elif contar == 1:
                segundos_fim += int(parte) * 60
                contar += 1
            elif contar == 2:
                segundos_fim += int(parte)
                contar += 1

        data_fim = f"{date.today().day}/{date.today().month}/{date.today().year}"
        dias = int(data_fim.split("/")[0]) - int(data.split('/')[0])
        if segundos_fim >= segundos_inicio:
            duracao = segundos_fim - segundos_inicio
            if dias > 0:
                duracao += dias * 3600 * 24
        elif segundos_fim < segundos_inicio:
            duracao = (segundos_fim) + ((24 * 3600) - segundos_inicio)
            if dias > 1:
                duracao += (dias - 1) * 3600 * 24
        duracao = stopWatch(duracao)

        with open("E:\\BOT_insta\\relatorios\\relatorio.txt", "a+") as info:
            info.write(
                f"No dia {data}, houveram {qtsjafoi} comentários no sorteio {link} na conta de @{usuario}. {bloqueados} contas fechadas. Início: {hora_inicio} - {data}. Fim: {hora_fim} - {data_fim}. Duração: {duracao}. Último marcado: {ultimo_marcado}. Base de dados: {arq}\n\n")


if __name__ == '__main__':
    with open("E:\\BOT_insta\\login.txt") as login:
        lista = [line for line in login]

    main(lista[0], lista[1], "https://www.instagram.com/", frases, False)
