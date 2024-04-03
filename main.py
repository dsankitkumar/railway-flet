import logging
import flet as ft
import os


db=pd.read_csv("stock_price_prediction_data.csv")
stocks_name=db['Stock Name'].str.lower().unique()

def match_strings(input_string, string_list):
    if input_string!="":
        return [s for s in string_list if input_string in s]
    else:
        return

# User interface
def main(page: ft.Page):
    lv = ft.ListView(width=600,height=475,spacing=15)
    def textbox_changed(e):
        if e.control.value!="":
            nm=match_strings(e.control.value.lower(), stocks_name)
            if len(nm)==0:
                lv.controls.clear()
                lv.controls.append(ft.Text(value="This stock not available in you list.",size=17,text_align=ft.TextAlign.CENTER))
                lv.update()
            else:
                lv.controls.clear()
                for item in nm:
                    lv.controls.append(ft.TextButton(item.capitalize(),autofocus=True))
                lv.update()
        else:
            lv.controls.clear()
            lv.update()
    tb = ft.TextField(
        border_radius=30,
        border_width=1,
        text_size=16,
        border_color=ft.colors.GREEN_100,
        focused_border_width=2,
        focused_border_color=ft.colors.GREEN,
        width=600,
        label="Enter stock name....",
        hint_text=random.choice(stocks_name).capitalize(),
        autofocus=True,
        on_change=textbox_changed,
    )

    page.add(tb)
    page.add(lv)


logging.basicConfig(level=logging.INFO)

ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
