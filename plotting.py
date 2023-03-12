import os
import matplotlib.pyplot as plt
from IPython.display import HTML

def center_fig(fig, name):
    """Saves the current figure into an image and center-display
    """
    # Save the plot as a PNG file
    folder = 'figures'
    ext = '.png'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if name[-4:] == ext:
        fp = os.path.join(folder, name)
    else:
        fp = os.path.join(folder, name+ext)
    
    fig.savefig(fp) # Create an HTML img tag to display the image
    img_tag = (f'<img src="{fp}" alt="plots"'
               'style="display:block; margin-left:auto;'
               'margin-right:auto;width:80%;">') # Display the img tag in the Jupyter Notebook
    display(HTML(img_tag))
