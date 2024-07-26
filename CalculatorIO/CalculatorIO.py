"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State): 
    Input: str = ""
    Output: int = 0
    oCalc: str = ""

    def numInput(self, num1):
        if self.Output != 0:
            self.clear            
        self.Input += str(num1)
        #if self.firstNum != 0:
            #self.secondNum = num1
        #else:
            #self.firstNum = num1    
        print(self.Input)
    def operator(self, oCalc):        
        if oCalc not in self.Input:
            self.Input += oCalc
            self.oCalc = oCalc
        else:
            pass                                  
        print(self.Input)
    def out(self):
        strPart = self.Input.rpartition(f"{self.oCalc}")
        if strPart[1] == "+":
            self.Output = float(strPart[0])+float(strPart[2])
            self.Input = str(self.Output)
        elif strPart[1] == "-":
            self.Output = float(strPart[0])-float(strPart[2])
            self.Input = str(self.Output)
        elif strPart[1] == "x":
            self.Output = float(strPart[0])*float(strPart[2])
            self.Input = str(self.Output)
        elif strPart[1] == "/":
            self.Output = float(strPart[0])/float(strPart[2])
            self.Input = str(self.Output)   
        else:
            pass             
        print(strPart,self.Output)   
    def clear(self):
        self.Input = ""   
        self.Output = 0
        self.oCalc = ""
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(  
        rx.text_area(
            value=f"{State.Input}",
            #disabled=True,
        ),
        rx.button(
            '=',
            on_click=State.out,
        ),
        rx.button(
            'Clear',
            on_click=State.clear,
        ),
        rx.button(
            'x',
            on_click=State.operator("x"),
        ),
        rx.button(
            '+',
            on_click=State.operator("+"),
        ),
        rx.button(
            '-',
            on_click=State.operator("-"),
        ),
        rx.button(
            '/',
            on_click=State.operator("/"),
        ),
        rx.grid(
            rx.foreach(
                rx.Var.range(9),
                lambda i: rx.button(f"{i + 1}", on_click=State.numInput(i+1),height="10vh"),
            ),
            gap="1rem",
            grid_template_columns=[
                "1fr",
                "repeat(2, 1fr)",
                "repeat(2, 1fr)",
                "repeat(3, 1fr)",
            ],
            width="100%",
        ),
        # rx.flex(
        #     rx.foreach(
        #         rx.Var.range(10),
        #         lambda i: rx.card(f"Card {i + 1}", width="16%"),
        #     ),
        #     justify="between",
        #     direction="row",
        #     spacing="4",
        #     width="100%",    
        #     height="20vh",
        #     margin_top="16px",
        #     align='start',
        #     wrap="wrap-reverse",            
        # ),                                      
    )


app = rx.App()
app.add_page(index)

