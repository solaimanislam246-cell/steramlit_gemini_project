import streamlit as st
from api_calling import note_generate,audio_generate,quiz_generate
from PIL import Image

 

#tile part
st.title("Note Summary & Quiz Generator", anchor=None)
st.markdown("Upload upto 3 images of your notes to Generate a summary and quiz.")
st.divider()



#sidebar part
with st.sidebar:
    st.header("Control panel")

    #image upload
    images=st.file_uploader("upload your notes",
                     type =['jpg', 'jpeg', 'png'],
                     accept_multiple_files=True
                     )
    
    pil_images = []

    for img in images:
     pil_img = Image.open(img)
     pil_images.append(pil_img)


    if images:
        if len(images)>3:
            st.error ("Please upload upto 3 images")
        else:
          col = st.columns(len(images))

          st.subheader("Uploaded Images")

        for i, image in enumerate(images):
             with col[i]:
                 st.image(image)

                
 #difficulty
    selected_box = st.selectbox(
        "Select the difficulty level for the quiz",
        ("Easy", "Medium", "Hard"),
        index  = None
    )
    pressed =  st.button("Click", type = "primary")


# slove problem
if pressed:
    if not images:
        st.error("You must upload at least one image")
    if not selected_box:
       st.error("You must select a difficulty level")


    if images and selected_box:
           #note
        with st.container(border = True):
         st. subheader("Your Notes")

         with st.spinner("AI is generating your notes..."):
            generate_notes = note_generate(pil_images) # this part will be replaced by API
            st.markdown(generate_notes )


           # audio transcript
        with st.container(border = True):
         st.subheader("Audio Transcript")
         with st.spinner("AI is generating your Audio..."):
            
            #clear markdown
            generate_notes = note_generate.replace("*","") 
            generate_notes = note_generate.replace("#","")
            generate_notes = note_generate.replace("-","")
            
            audio_buffer = audio_generate(generate_notes)
            st.audio(audio_buffer, format="audio/mp3")# this part will be replaced by API



           #quiz
        with st.container(border = True):
         st.subheader("Quiz")
         with st.spinner("AI is generating your Quiz..."): 
            quizes = quiz_generate(pil_images,selected_box)
            st.markdown(f"Quiz {selected_box}")# this part will be replaced by API

     

