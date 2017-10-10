from PyPDF2 import PdfFileWriter
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait

output = PdfFileWriter()

packet = StringIO.StringIO()
cv=canvas.Canvas(packet, pagesize=(8.5 * inch, 11 * inch))
cv.drawString(0, 500, "Hello World!")
cv.circle(50, 250, 20, stroke=1, fill=0)
cv.save()

packet.seek(0)


with open("1.pdf", "wb") as fp:
	fp.write(packet.getvalue())
