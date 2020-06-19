from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button

class Calc_Window(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        Window.size=(300,500)
        
        num_list=[7,8,9,'+',4,5,6,'-',1,2,3,'*','.',0,'(',')','/']
        self.numbers=self.ids.numbers
        
        numc=['C','CA']
        self.numbers=self.ids.numbers
        
        for num in num_list:
            btn=Button(text=str(num),font_size='30px',background_color=(1.0,0.0,0.0,1.0))
            btn.bind(on_release=self.echo_numb)
            self.numbers.add_widget(btn)
        
        for num in numc:
            btn=Button(text=str(num),font_size='30px',background_color=(2.0,2.0,2.0,0.6))
            btn.bind(on_release=self.echo_numb)
            self.numbers.add_widget(btn)
        
        igual=Button(text='=',font_size='30px',background_color=(1.0,2.0,2.0,0.6))
        igual.bind(on_release=self.eval_numb)
        self.numbers.add_widget(igual)
    
    def echo_numb(self,obj):
        inputt=self.ids.inputt
        inputt.text+=obj.text
        
        if obj.text=='CA':
            inputt.text=''
        elif obj.text=='C':
            inputt.text=inputt.text[:-2]
    
    def eval_numb(self,text):
        inputt=self.ids.inputt
        exp=inputt.text
        eva=eval(exp)
        inputt.text=str(eva)
        
                             
class CalcApp(App):
    def build(self):
        return Calc_Window()

if __name__=='__main__':
    CalcApp().run()      