from pytube import YouTube
from fpdf import FPDF
import requests

class PDFGenerator:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", style='B', size=16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.set_font("Arial", size=12)

    def add_text(self, text):
        self.pdf.multi_cell(0, 10, txt=text)

    def add_image(self, image_path):
        self.pdf.add_page()
        self.pdf.image(image_path, x=10, y=10, w=180)

    def save(self, filename):
        self.pdf.output(filename)

def extract_youtube_info(url):
    try:
        yt = YouTube(url)
        title = yt.title
        description = yt.description
        thumbnail_url = yt.thumbnail_url
        return title, description, thumbnail_url
    except Exception as e:
        print(f"Error while fetching YouTube video: {e}")
        return None, None, None

def main():
    video_url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'  # Substitua pelo URL do vídeo desejado
    pdf_title = "Resumo do Tutorial do YouTube"
    pdf_filename = "Resumo_Tutorial_YouTube.pdf"
    
    # Extrair informações do YouTube
    title, description, thumbnail_url = extract_youtube_info(video_url)
    
    if title is None:
        print("Falha ao extrair informações do vídeo.")
        return

    # Criar o gerador de PDF
    pdf = PDFGenerator(title=pdf_title)

    # Adicionar informações ao PDF
    pdf.add_text(f"Título: {title}")
    pdf.add_text(f"Descrição:\n{description}")

    # Adicionar thumbnail (imagem) ao PDF
    if thumbnail_url:
        # Baixar a thumbnail para salvar como imagem
        thumbnail_path = 'thumbnail.jpg'
        with open(thumbnail_path, 'wb') as f:
            f.write(requests.get(thumbnail_url).content)
        pdf.add_image(thumbnail_path)

    # Salvar o PDF
    pdf.save(pdf_filename)
    print(f"PDF '{pdf_filename}' gerado com sucesso!")

if __name__ == '__main__':
    main()