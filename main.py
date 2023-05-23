from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
 
class Root(BoxLayout):
    def count_up(self):
        self.ids.label1.value += 1
 
    def count_reset(self):
        self.ids.label1.value = 0
 
class MyApp(App):
    title = 'My Application'
 
 
if __name__ == '__main__':
    MyApp().run()