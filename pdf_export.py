from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import io

def create_pdf(text_content):
    
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
  
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Muun AI - Etsy SEO Report")
  
    c.setFont("Helvetica", 11)
    y_position = height - 80
    
    lines = text_content.split('\n')
    
    for line in lines:
        
        wrapped_lines = simpleSplit(line, "Helvetica", 11, width - 100)
        
        for wrapped_line in wrapped_lines:
           
            if y_position < 50:
                c.showPage() 
                y_position = height - 50 
                c.setFont("Helvetica", 11) 
            
            c.drawString(50, y_position, wrapped_line)
            y_position -= 14 
            
    c.save()
    buffer.seek(0)
    return buffer