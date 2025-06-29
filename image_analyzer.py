
import pytesseract
from PIL import Image

def analyze_image(image: Image.Image) -> str:
    try:
        text = pytesseract.image_to_string(image)
        return text if text else "Mətn tapılmadı."
    except Exception as e:
        return f"Xəta baş verdi: {e}"
