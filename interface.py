import PySimpleGUI as sg
from selenium import webdriver
import time

sg.ChangeLookAndFeel("SystemDefault")

WIN_W = 50
WIN_H = 10
bot: dict = {'size': (28, 1)} # define o tamanho do botão

layout = [
    [sg.Text("Contato 01", size=(10, 1)),
     sg.In(key="c1")],
    [sg.Text("Contato 02", size=(10, 1)),
     sg.In(key="c2")],
    # [sg.Text("Contato 03", size=(10, 1)),
    #  sg.In(key="c3")],
    # [sg.Text("Contato 04", size=(10, 1)),
    #  sg.In(key="c4")],
    # [sg.Text("Contato 05", size=(10, 1)),
    #  sg.In(key="c5")],
    # [sg.Text("Contato 06", size=(10, 1)),
    #  sg.In(key="c6")],
    # [sg.Text("Contato 07", size=(10, 1)),
    #  sg.In(key="c7")],
    # [sg.Text("Contato 08", size=(10, 1)),
    #  sg.In(key="c8")],
    # [sg.Text("Contato 09", size=(10, 1)),
    #  sg.In(key="c9")],
    # [sg.Text("Contato 10", size=(10, 1)),
    #  sg.In(key="c10")],
    [sg.Multiline(font=("Consolas", 12), text_color="black", size=(WIN_W, WIN_H), key="msg")],
    [sg.Button('Enviar', **bot), sg.Button('Sair', **bot)]

]

window = sg.Window(
    "Conexão com WhatsApp",
    layout=layout,
    margins=(0, 0), #marcar como comentario quando usar o Stretch
    #resizable=True,
    return_keyboard_events=False,
    icon=r'C:\Users\charli.castelli\Downloads\whats_icon.ico',
    finalize=True

)
#window.read()

def exibir_finalizacao():
    sg.PopupOK(
        """Finalizado com sucesso!!!"""
    )

while True:
    event, values = window.read()
    if event in (None, 'Sair'):
        break


    #print("Dados digitados", values)
    class WhatsappBot:
        def __init__(self):
            self.mensagem = values["msg"]
            self.grupos = [values["c1"],
                           values["c2"],
                           # values["c3"],
                           # values["c4"],
                           # values["c5"],
                           # values["c6"],
                           # values["c7"],
                           # values["c8"],
                           # values["c9"],
                           # values["c10"]
                           ]
            options = webdriver.ChromeOptions()
            options.add_argument('lang=pt-br')
            self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

        def EnviarMensagens(self):
            self.driver.get('https://web.whatsapp.com/')
            time.sleep(20)

            for contatos in self.grupos:
                nova_conversa = self.driver.find_element_by_xpath("//span[@data-icon='chat']")
                time.sleep(2)
                nova_conversa.click()
                grupo = self.driver.find_element_by_xpath(f"//span[@title='{contatos}']")
                time.sleep(2)
                grupo.click()
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                time.sleep(2)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                # time.sleep(5)
                # botão_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']") # Não usei o botão enviar pq recuperei algo digitado na interface grafica e não um texto digitado direto no codigo
                # time.sleep(3)
                # botão_enviar.click()
                time.sleep(3)


    bot = WhatsappBot()
    bot.EnviarMensagens()




window.close()


# Codigos abaixo eu estava tentando enviar um anexo
                # attachment_box = self.driver.find_element_by_xpath('//span[@data-icon="clip"]')
                # time.sleep(2)
                # attachment_box.click()
                # time.sleep(3)
                # image_box = self.driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                # time.sleep(3)
                # image_box.send_keys(self.mensagem)