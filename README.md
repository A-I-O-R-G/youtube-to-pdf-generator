
# Documentação Detalhada

## 1. Introdução
Este software permite extrair informações de vídeos do YouTube, como título, descrição e miniatura, e organiza essas informações em um arquivo PDF. Utiliza a biblioteca `pytube` para acessar as informações do YouTube e `FPDF` para a criação do PDF.

## 2. Instalação
Para instalar as bibliotecas necessárias, utilize o seguinte comando:
```bash
pip install pytube fpdf requests
```

## 3. Uso
- Altere a variável `video_url` para o URL do vídeo do YouTube que você deseja processar.
- Execute o script. O PDF resultante será salvo como `Resumo_Tutorial_YouTube.pdf`.

Exemplo de como rodar o script:
```bash
python script.py
```

## 4. Referência de API
- **PDFGenerator**: Classe responsável pela criação de PDFs.
  - `__init__(self, title)`: Inicializa o PDF com um título.
  - `add_text(self, text)`: Adiciona texto ao PDF.
  - `add_image(self, image_path)`: Adiciona uma imagem ao PDF.
  - `save(self, filename)`: Salva o PDF com o nome especificado.

- `extract_youtube_info(url)`: Extrai informações de um vídeo do YouTube.
  - Parâmetro: `url` (str): URL do vídeo do YouTube.
  - Retorna uma tupla contendo o título, descrição e URL da miniatura.

## 5. Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer fork do repositório e enviar suas melhorias.

## 6. Licença
Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais informações.