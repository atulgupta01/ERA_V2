import pickle
import gradio as gr

from train_util import get_stats, merge, encode, decode

with open('model.pkl', 'rb') as handle:
    model = pickle.load(handle)

compiled_pattern = model['compiled_pattern']
merges = model['merges']
vocab = model['vocab']

def generate_tokens(hindi_txt):
  enc_text = encode(hindi_txt, merges, compiled_pattern)
  txt = decode(enc_text, vocab)
  v_mapping = [(str(i),decode([i], vocab)) for i in enc_text]
  enc_text = ', '.join([str(i) for i in enc_text])
  return (enc_text, txt, v_mapping)
  
with gr.Blocks() as demo:
    gr.HTML("<h1 align = 'center'> Token Generation for Hindi Dataset </h1>")

    with gr.Row():
      with gr.Column():
        inputs = [gr.TextArea(label = "Enter initial text to generate tokens in Hindi", lines = 10)]
        generate_btn = gr.Button(value = 'Generate Text')
      with gr.Column():
        enc = gr.Textbox(label = "Encoded Tokens")
        txt = gr.Textbox(label = "Decoded Text from tokens")
        map = gr.Textbox(label = "Mapping of the tokens and respective texts")
        outputs  = [
            enc,
            txt,
            map
            ]
    
    generate_btn.click(fn = generate_tokens, inputs= inputs, outputs = outputs)


if __name__ == '__main__':
    demo.launch() 
