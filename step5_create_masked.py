import numpy as np

def create_masked_stipple(stipple_img: np.ndarray, mask_img: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Apply a block letter mask to a stippled image.
    
    Args:
        stipple_img (np.ndarray): 2D numpy array of stippled image values in [0, 1].
        mask_img (np.ndarray): 2D numpy array of mask values in [0, 1].
        threshold (float): Threshold to determine mask area (default 0.5).
    
    Returns:
        np.ndarray: 2D numpy array with stipples removed where mask is dark.
    """
    # Ensure input shapes match
    if stipple_img.shape != mask_img.shape:
        raise ValueError("stipple_img and mask_img must have the same shape")
    
    # Create boolean mask: True where mask is dark (below threshold)
    mask_dark = mask_img < threshold
    
    # Apply mask: remove stipples (set to white=1.0) where mask is dark
    masked_stipple = np.where(mask_dark, 1.0, stipple_img)
    
    return masked_stipple
