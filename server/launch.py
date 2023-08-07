import numpy as np
import gradio as gr

from fastapi import FastAPI

from app.generator import generate

"""
iface = gr.Interface(fn=generate,
                     inputs=[
                         gr.components.Slider(minimum=1, maximum=98, step=1, label="Min", value=1),
                         gr.components.Slider(minimum=2, maximum=99, step=1, label="Max", value=12),
                         gr.components.Checkbox(label="Only Lower Case", value=False),
                         gr.components.Checkbox(label="Use Digits", value=True),
                         gr.components.Checkbox(label="Use Punctuation", value=True),
                         gr.components.Checkbox(label="First Number", value=False)
                     ],
                     outputs=gr.components.Textbox())

iface.launch(server_name="127.0.0.1", server_port=8090, show_api=True, debug=True)
"""
application = FastAPI()


@application.post("/generate")
def _generate(min: int = 1, max: int = 99,
              only_lower_case: bool = False, used_digits: bool = True,
              used_punctuation: bool = True, first_number: bool = False):
    result = generate(min=min, max=max, only_lower_case=only_lower_case,
                      used_digits=used_digits, used_punctuation=used_punctuation,
                      first_number=first_number)
    return result


@application.get("/")
def home():
    return """
                <h1 style='text-align:center;'>Password Generator</h1>
                """
