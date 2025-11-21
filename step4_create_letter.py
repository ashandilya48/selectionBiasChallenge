import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_block_letter_A(height: int, width: int, letter: str = "A", font_size_ratio: float = 0.9) -> np.ndarray:
    """
    Generate a block letter image as a numpy array.
    
    Args:
        height (int): Height of the output image.
        width (int): Width of the output image.
        letter (str): The letter to render (default "A").
        font_size_ratio (float): Ratio of font size relative to image height.
    
    Returns:
        np.ndarray: 2D array (height × width) with values in [0, 1].
                    Background = 1.0 (white), Letter = 0.0 (black).
    """
    # Create a white background image
    img = Image.new("L", (width, height), color=255)  # "L" = grayscale
    
    # Try to load a bold system font
    possible_fonts = [
        "arialbd.ttf",        # Arial Bold
        "DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf"
    ]
    
    font = None
    font_size = int(height * font_size_ratio)
    for font_path in possible_fonts:
        try:
            font = ImageFont.truetype(font_path, font_size)
            break
        except IOError:
            continue
    
    # Fallback to default PIL font if none found
    if font is None:
        font = ImageFont.load_default()
    
    draw = ImageDraw.Draw(img)
    
    # Get text size and position for centering
    text_bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Draw the letter in black
    draw.text(position, letter, font=font, fill=0)
    
    # Convert to numpy array, normalize to [0,1]
    arr = np.array(img, dtype=np.float32) / 255.0
    
    return arr

# Example usage: Generate block letter "A" with dimensions 250x375
#block_A = create_block_letter_A(250, 375, letter="A")

#print(block_A.shape)  # (250, 375)