### Assignment 20

## Link to the [App](https://huggingface.co/spaces/samatul/ERA_V2_S20)

<img src="https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_20/App.jpg" alt="Gradio App" width="700" height="350">

## Details

* Selected language **Hindi** for generating the text. The sample hindi can be written using followng [link](https://www.quillpad.in/editor.html). This site converts english to hindi.
* Downloaded one novel by renown author **Mushi Premchand** from this [site](https://archive.org/details/booksbylanguage_hindi?tab=collection&query=munshi)
* The regex used is standard for devanagri lipi _(r""" ?\p{Devanagari}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")_
* Used **5000** tokens and It worked well for most of the tokens.
* Some interesting tokens generated -
  - **'326', ' में'** - Very frequent token
  - **'364', ' भी'** - Very frequent token
  - **'286', ' ज'** - Very frequent token and only one character but it also got converted to ('1889', ' समाज')
  - **'653', ' बहुत'** - frequent token
  - **'1729', ' साहित्य'** - Repeated token and generated earlier
  - **'3616', 'प्रेमचंद'** - Token id suggests later than 1729 but repeated in the novel (Name of Author)
  - **'280', ' ।'** - Hindi fullstop
* It also has certain limitations
  -  '827', ' मि�' (Not able to decode for the token)
  -  '182', '�' (Not able to decode for the token)
  -  **But this did not impact the overall conversion**


## Files
1. Training Log in the [Jupyter notebook](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_20/S_19_train.ipynb)
2. App Development log in [Jupyter notebook](https://github.com/atulgupta01/ERA_V2/blob/main/Assignment_20/app.py)

