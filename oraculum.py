from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
import random
from PyPDF2 import PdfReader

KV = '''
ScreenManager:
    MenuScreen:
    DivinationScreen:
    YesNoScreen:
    WordScreen:

<MenuScreen>:
    name: "menu"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1  # Fundo preto

        MDTopAppBar:
            title: "Oraculum"
            md_bg_color: 0.1, 0.1, 0.1, 1  # Cinza escuro
            specific_text_color: 1, 1, 1, 1  # Texto branco

        Image:
            source: "Corvo.png"
            size_hint_y: None
            height: "250dp"

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "450dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Divinação Completa"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "divination"

            MDRaisedButton:
                text: "Sim ou Não"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "yesno"

            MDRaisedButton:
                text: "Palavras Aleatórias"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "word"

<DivinationScreen>:
    name: "divination"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Divinação Completa"
            md_bg_color: 0.1, 0.1, 0.1, 1
            specific_text_color: 1, 1, 1, 1

        Image:
            source: "Corvo.png"
            size_hint_y: None
            height: "250dp"
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.5
            height: "10dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            MDTextField:
                id: divination_input
                hint_text: "digite sua pergunta aqui"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                mode: "rectangle"
                
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            
                
            MDLabel:
                id: pergunta
                text: "Pergunte algo ao Corvo"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.5
            height: "450dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDRaisedButton:
                text: "Confirmar"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.show_divination_result()

            MDRaisedButton:
                text: "Voltar"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "menu"

<YesNoScreen>:
    name: "yesno"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Sim ou Não"
            md_bg_color: 0.1, 0.1, 0.1, 1
            specific_text_color: 1, 1, 1, 1

        Image:
            source: "Corvo.png"
            size_hint_y: None
            height: "450dp"
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.5
            height: "10dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            MDTextField:
                id: divination_input
                hint_text: "digite sua pergunta aqui"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                mode: "rectangle"
                
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            
                
            MDLabel:
                id: pergunta
                text: "Pergunte algo ao Corvo"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "250dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Perguntar"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.show_yes_no_result()

            MDRaisedButton:
                text: "Voltar"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "menu"

<WordScreen>:
    name: "word"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Palavras Aleatórias"
            md_bg_color: 0.1, 0.1, 0.1, 1
            specific_text_color: 1, 1, 1, 1

        Image:
            source: "Corvo.png"
            size_hint_y: None
            height: "450dp"
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.5
            height: "10dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            MDTextField:
                id: divination_input
                hint_text: "digite sua pergunta aqui"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                mode: "rectangle"
                
            MDLabel:
                id: pergunta
                text: "________________________________________"
                halign: "center"
                color: (1,1,1,1)
                
            
                
            MDLabel:
                id: pergunta
                text: "Pergunte algo ao Corvo"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "250dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Obter Palavras"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.generate_word()

            MDRaisedButton:
                text: "Voltar"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "menu"
'''

class MenuScreen(MDScreen):
    pass

class DivinationScreen(MDScreen):
    pass

class YesNoScreen(MDScreen):
    pass

class WordScreen(MDScreen):
    pass

class DivinationApp(MDApp):
    categories = {
        "Lux Element Tarot": [
            "O Vazio", "A Digital", "O DNA", "A Chave", "A Montanha", "O Carro", "A Família", "O Trigo", 
            "O Universo", "O Multiverso", "O Cérebro", "A Tecnologia", "A Inteligência Artificial", "A Prisão",
            "O Lixo", "A Escola", "A Máscara", "A Empresa", "O Templo", "A Ponte", "A Balança", "O Laboratório",
            "O Diamante",
            
            # Símbolos Menores - Ar
            "Lâmpada", "Rede", "Avião", "Algoritmo", "Incenso", "Borboleta", "Realidade Virtual", "Labirinto",
            "Caos", "Espelho", "Relógio", "Sombras",
            
            # Símbolos Menores - Terra
            "Semente", "Broto", "Planta", "Casa", "Terremoto", "Martelo", "Cofre", "Engrenagem", "Planta seca",
            "Empresário", "GPS", "Mendigo",
            
            # Símbolos Menores - Água
            "Lago", "Fonte", "Aliança", "Brinquedo", "Gelo", "Coração", "Submarino", "Pérola", "Lágrima", 
            "Praia", "Navio", "Furacão",
            
            # Símbolos Menores - Fogo
            "Bateria", "Raio", "Forno", "Vela", "Vulcão", "Lareira", "Lanterna", "Sol", "Incêndio", "Estrela",
            "Faísca", "Pimenta"
        ],
        "Lenormand": ["Cavaleiro", "Trevo", "Navio", "Casa", "Árvore", "Nuvens", "Cobra", "Caixão", "Buquê", "Foice", "Chicote", "Corujas (ou Pássaros)", "Criança", "Raposa", "Urso", "Estrelas", "Cegonha", "Cão", "Torre", "Jardim", "Montanha", "Caminhos", "Ratos", "Coração", "Anel", "Livro", "Carta", "Homem", "Mulher", "Lírios", "Sol", "Lua", "Chave", "Peixes", "Âncora", "Cruz"],
        "Marselha": ["O Louco", "O Mago", "A Sacerdotisa", "A Imperatriz", "O Imperador",
                         "O Hierofante", "Os Enamorados", "O Carro", "A Justiça", "O Eremita",
                         "A Roda da Fortuna", "A Força", "O Enforcado", "A Morte", "A Temperança",
                         "O Diabo", "A Torre", "A Estrela", "A Lua", "O Sol", "O Julgamento",
                         "O Mundo", "Ás de Paus", "Dois de Paus", "Três de Paus", "Quatro de Paus",
                         "Cinco de Paus", "Seis de Paus", "Sete de Paus", "Oito de Paus", 
                         "Nove de Paus", "Dez de Paus", "Pajem de Paus", "Cavaleiro de Paus", 
                         "Rainha de Paus", "Rei de Paus", "Ás de Copas", "Dois de Copas", 
                         "Três de Copas", "Quatro de Copas", "Cinco de Copas", "Seis de Copas", 
                         "Sete de Copas", "Oito de Copas", "Nove de Copas", "Dez de Copas", 
                         "Pajem de Copas", "Cavaleiro de Copas", "Rainha de Copas", "Rei de Copas", 
                         "Ás de Espadas", "Dois de Espadas", "Três de Espadas", "Quatro de Espadas", 
                         "Cinco de Espadas", "Seis de Espadas", "Sete de Espadas", "Oito de Espadas", 
                         "Nove de Espadas", "Dez de Espadas", "Pajem de Espadas", "Cavaleiro de Espadas", 
                         "Rainha de Espadas", "Rei de Espadas", "Ás de Ouros", "Dois de Ouros", 
                         "Três de Ouros", "Quatro de Ouros", "Cinco de Ouros", "Seis de Ouros", 
                         "Sete de Ouros", "Oito de Ouros", "Nove de Ouros", "Dez de Ouros", 
                         "Pajem de Ouros", "Cavaleiro de Ouros", "Rainha de Ouros", "Rei de Ouros"],
        "Runa": ["Fehu", "Uruz", "Thurisaz", "Ansuz", "Raidho", "Kenaz", 
                      "Gebo", "Wunjo", "Hagalaz", "Nauthiz", "Isa", "Jera", 
                      "Eihwaz", "Perthro", "Algiz", "Sowilo", "Tiwaz", "Berkano", 
                      "Ehwaz", "Mannaz", "Laguz", "Ingwaz", "Dagaz", "Othala","Fehu invertido", "Uruz invertido", "Thurisaz invertido", "Ansuz invertido", "Raidho invertido", "Kenaz invertido", 
                      "Gebo", "Wunjo", "Hagalaz", "Nauthiz invertido", "Isa", "Jera", 
                      "Eihwaz", "Perthro invertido", "Algiz invertido", "Sowilo", "Tiwaz invertido", "Berkano invertido", 
                      "Ehwaz invertido", "Mannaz invertido", "Laguz invertido", "Ingwaz", "Dagaz", "Othala invertido"],
        "Número": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        "Signo": ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"],
        "Elemento": ["Água", "Terra", "Fogo", "Ar", "Éter"],
        "Cores": ["Preto", "Bramco","Cinza","vermelo","Amarelo","Laranja", "Dourado", "Verde", "Azul Claro", "Azul", "indigo", "Violeta", "Roxo", "Púrpura", "Marrom", "Rosa"]
    }

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(KV)

    def show_divination_result(self):
        results = "\n".join([f"{category}: {random.choice(words)}" for category, words in self.categories.items()])
        self.show_dialog("Resultado da Divinação", results)

    def show_yes_no_result(self):
        answers = ["Sim", "Não", "Talvez", "Tenho Certeza", "Provavelmente Sim", "Provavelmente Não"]
        self.show_dialog("Resposta", random.choice(answers))

    def generate_word(self):
        pdf_files = ["cartas-ciganas-lenormand.pdf","Lux_Element_Tarot_Guia_Informativo.pdf"] #Adicione outros arquivos aqui
        words = self.get_words_from_pdfs(pdf_files)
        if words:
            selected_words = " ".join(random.sample(words, 8))
            self.show_dialog("Palavras Aleatórias", selected_words)
        else:
            self.show_dialog("Erro", "Não foi possível carregar as palavras.")

    def get_words_from_pdfs(self, pdf_files):
        all_words = []
        for filepath in pdf_files:
            try:
                with open(filepath, 'rb') as f:
                    reader = PdfReader(f)
                    text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
                    all_words.extend(text.split())
            except Exception as e:
                print(f"Erro ao ler PDF: {e}")
        return list(set(all_words))

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDRaisedButton(text="Fechar", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

if __name__ == "__main__":
    DivinationApp().run()