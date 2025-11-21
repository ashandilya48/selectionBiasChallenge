import numpy as np
import matplotlib.pyplot as plt

def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Assemble four panels into a professional-looking statistics meme.

    Args:
        original_img (np.ndarray): Reality image (2D array).
        stipple_img (np.ndarray): Your Model image (2D array).
        block_letter_img (np.ndarray): Selection Bias mask image (2D array).
        masked_stipple_img (np.ndarray): Estimate image (2D array).
        output_path (str): Path to save the final meme PNG.
        dpi (int): Resolution for saving (default 150).
        background_color (str): Background color for figure (default "white").
    """
    # Ensure all images are numpy arrays
    imgs = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]

    # Create figure with 1x4 layout
    fig, axes = plt.subplots(1, 4, figsize=(16, 4), dpi=dpi, facecolor=background_color)

    for ax, img, label in zip(axes, imgs, labels):
        # Show image
        ax.imshow(img, cmap="gray", vmin=0, vmax=1)
        ax.set_title(label, fontsize=12, fontweight="bold", pad=10)
        
        # Remove axis ticks for clean look
        ax.axis("off")
        
        # Add subtle border around each panel
        for spine in ax.spines.values():
            spine.set_edgecolor("black")
            spine.set_linewidth(1)

    # Adjust layout for professional spacing
    plt.tight_layout(pad=2.0, w_pad=2.0, h_pad=0.5)

    # Save as PNG
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight", facecolor=background_color)
    plt.close(fig)
