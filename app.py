import os
import gradio as gr
from pdf2image import convert_from_path

def save_images_from_pdf(pdf_file):
    save_dir = "./imgs"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    filename = os.path.splitext(os.path.basename(pdf_file.name))[0]

    images = convert_from_path(pdf_file.name)
    
    for i, image in enumerate(images):
        image_path = os.path.join(save_dir, f"{filename}_{i}.png")
        image.save(image_path, "PNG")
    
    return [os.path.join(save_dir, f"{filename}_{i}.png") for i in range(len(images))]

# Gradio interface
iface = gr.Interface(
    fn=save_images_from_pdf,
    inputs=gr.File(type="filepath", label="Upload PDF"),
    outputs=gr.Gallery(label="Converted Images"),
    title="PDF to Image Converter",
    description="Upload a PDF file and convert each page into an image. Images are saved in the 'imgs' directory."
)

if __name__ == "__main__":
    iface.launch()
    print("App launched successfully!")
