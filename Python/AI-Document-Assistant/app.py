import streamlit as st
from pypdf import PdfReader

st.title("AI Document Assistant")
st.write("Upload a PDF and ask questions about the document.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def find_best_answer(text, question):
    chunks = text.split("\n")
    question_words = question.lower().split()

    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        score = 0
        for word in question_words:
            if word in chunk.lower():
                score += 1

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.success("PDF loaded successfully!")

    st.subheader("Document Preview")
    st.write(text[:2000])

    question = st.text_input("Ask a question about your document")

    if question:
        answer = find_best_answer(text, question)

        if answer:
            st.success("Answer:")
            st.write(answer)
        else:
            st.warning("No relevant answer found.")