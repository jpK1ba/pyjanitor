import os
import matplotlib.pyplot as plt
from IPython.display import HTML

def center_fig(name, width=80, dpi='figure'):
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
    
    if os.path.exists(fp):
        os.remove(fp)
        
    # Create an HTML img tag to display the image
    plt.savefig(fp, dpi=dpi) 
    img_tag = (f'<img src="{fp}" alt="plots"'
               'style="display:block; margin-left:auto;'
               f'margin-right:auto;width:{width}%;">') 
    
    # Display the img tag in the Jupyter Notebook
    display(HTML(img_tag))
    plt.close()
