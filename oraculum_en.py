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
                text: "Complete Divination"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "divination"

            MDRaisedButton:
                text: "Yes or Not"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "yesno"

            MDRaisedButton:
                text: "Random Words"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "word"

<DivinationScreen>:
    name: "divination"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Complete Divination"
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
                hint_text: "write your question here"
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
                text: "Ask the Crow something"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.5
            height: "450dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            MDRaisedButton:
                text: "Confirm"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.show_divination_result()

            MDRaisedButton:
                text: "Back"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "menu"

<YesNoScreen>:
    name: "yesno"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Yes or Not"
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
                hint_text: "write your question here"
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
                text: "Ask the Crow something"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "250dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Confirm"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.show_yes_no_result()

            MDRaisedButton:
                text: "Back"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "menu"

<WordScreen>:
    name: "word"
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0, 0, 1

        MDTopAppBar:
            title: "Random Words"
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
                hint_text: "write your question here"
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
                text: "Ask the Crow something"
                halign: "center"
                color: (1,1,1,1)

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "250dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "Get Words"
                size_hint_x: 0.7
                pos_hint: {"center_x": 0.5}
                on_release: app.generate_word()

            MDRaisedButton:
                text: "Back"
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
            "The Void", "The Fingerprint", "The DNA", "The Key", "The Mountain", "The Car", "The Family", "The Wheat", 
            "The Universe", "The Multiverse", "The Brain", "Technology", "Artificial Intelligence", "The Prison",
            "The Trash", "The School", "The Mask", "The Company", "The Temple", "The Bridge", "The Balance", "The Laboratory",
            "The Diamond",
            
            # Minor Symbols - Air
            "Lamp", "Network", "Airplane", "Algorithm", "Incense", "Butterfly", "Virtual Reality", "Labyrinth",
            "Chaos", "Mirror", "Clock", "Shadows",
            
            # Minor Symbols - Earth
            "Seed", "Sprout", "Plant", "House", "Earthquake", "Hammer", "Safe", "Gear", "Dry Plant",
            "Businessman", "GPS", "Beggar",
            
            # Minor Symbols - Water
            "Lake", "Fountain", "Alliance", "Toy", "Ice", "Heart", "Submarine", "Pearl", "Tear", 
            "Beach", "Ship", "Hurricane",
            
            # Minor Symbols - Fire
            "Battery", "Lightning", "Oven", "Candle", "Volcano", "Fireplace", "Lantern", "Sun", "Fire", "Star",
            "Spark", "Pepper"
        ],
        "Lenormand": ["Rider", "Clover", "Ship", "House", "Tree", "Clouds", "Snake", "Coffin", "Bouquet", "Scythe", "Whip", "Owls (or Birds)", "Child", "Fox", "Bear", "Stars", "Stork", "Dog", "Tower", "Garden", "Mountain", "Paths", "Rats", "Heart", "Ring", "Book", "Letter", "Man", "Woman", "Lilies", "Sun", "Moon", "Key", "Fish", "Anchor", "Cross"],
        "Marseille": ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
                         "The Hierophant", "The Lovers", "The Chariot", "Justice", "The Hermit",
                         "Wheel of Fortune", "Strength", "The Hanged Man", "Death", "Temperance",
                         "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgment",
                         "The World", "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands",
                         "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", 
                         "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", 
                         "Queen of Wands", "King of Wands", "Ace of Cups", "Two of Cups", 
                         "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", 
                         "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", 
                         "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups", 
                         "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", 
                         "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", 
                         "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", 
                         "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles", 
                         "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", 
                         "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", 
                         "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"],
        "Rune": ["Fehu", "Uruz", "Thurisaz", "Ansuz", "Raidho", "Kenaz", 
                      "Gebo", "Wunjo", "Hagalaz", "Nauthiz", "Isa", "Jera", 
                      "Eihwaz", "Perthro", "Algiz", "Sowilo", "Tiwaz", "Berkano", 
                      "Ehwaz", "Mannaz", "Laguz", "Ingwaz", "Dagaz", "Othala","Fehu inverted", "Uruz inverted", "Thurisaz inverted", "Ansuz inverted", "Raidho inverted", "Kenaz inverted", 
                      "Gebo", "Wunjo", "Hagalaz", "Nauthiz inverted", "Isa", "Jera", 
                      "Eihwaz", "Perthro inverted", "Algiz inverted", "Sowilo", "Tiwaz inverted", "Berkano inverted", 
                      "Ehwaz inverted", "Mannaz inverted", "Laguz inverted", "Ingwaz", "Dagaz", "Othala inverted"],
        "Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        "Sign": ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "Element": ["Water", "Earth", "Fire", "Air", "Ether"],
        "Colors": ["Black", "White","Gray","Red","Yellow","Orange", "Gold", "Green", "Light Blue", "Blue", "Indigo", "Violet", "Purple", "Crimson", "Brown", "Pink"]
    }

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(KV)

    def show_divination_result(self):
        results = "\n".join([f"{category}: {random.choice(words)}" for category, words in self.categories.items()])
        self.show_dialog("Divination Result", results)

    def show_yes_no_result(self):
        answers = ["Yes", "No", "Maybe", "I'm Sure", "Probably Yes", "Probably No"]
        self.show_dialog("Answer", random.choice(answers))

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
            buttons=[MDRaisedButton(text="Close", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

if __name__ == "__main__":
    DivinationApp().run()