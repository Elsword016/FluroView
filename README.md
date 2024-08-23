# Fluroview
A Python package for visualization of biological data. It is built on top of matplotlib, allowing it to use all its functions. Fluroview is a simple way to generate beautiful and publication figures, especially for multi-channel images representing them as composite images similar to what can be 
achieved using an Image processing software like Fiji. Alongside generating figures, it also completes the figures with appropriate scalebars, titles and colormaps. 

## Installation:
You can install this package directly from pip:

```bash
pip install FluroView
```

This will install the latest `0.2.0` version.


## Main modules:

+ `bioviz_multichannel.py`: `MultiChannelImage` is designed to handle multi-channel image data, allowing for easy manipulation and visualization of individual channels or composite images.
    - ### Key features:
      +  Support for single or multiple image channels
      +  Flexible colormap assignment, including custom and built-in colormaps
      +  Internally intensity rescaling options so that the colors are more visually clear.

### Basic Usage:

To create an `MultiChannelImage` object:

Here we are creating a figure of a 4 channel Rat Hippocampal neuron image (Taken from ImageJ sample library):
```python
eximg = imread('Rat_Hippocampal_Neuron.tif')
exim = MultiChannelImage(
    channels=[eximg[0], eximg[1], eximg[2], eximg[3]],
    channel_names=['Bungarotoxin','ACh','CFP','Hoeschst'],
    colormaps=['pure_red','pure_green','pure_magenta','pure_cyan']
)
#Lots of customization, use or can use panel to plot the figure as well
fig, ax = MultiChannelImage.create_multichannel_figure(
        exim, 
        pixel_size=0.16,
        units='um',
        panel_label='A',  
        rescale=True, 
        label_position='top-right',
        label_color='black',
        channel_label_show=True,
        scalebar_color='white',
        scalebar_font_size=12,
        panel_label_color='white',
        panel_label_font_size=16,
        channel_label_font_size=10,
        scalebar_position='lower right',
        panel_label_position='upper left',
        figsize=(15,5)
    )
```
### Output:

![image](https://github.com/user-attachments/assets/9f1dca9a-0937-4e00-9269-ea50f37d6b67)

+ `bioviz_imagepanel.py`: The `ImagePanel` class facilitates the creation of figure panels containing multiple `MultiChannelImage` objects, ideal for creating publication-ready figures.
    - ### Key features:
        + Arrange multiple images in a grid layout.
        + Figure layout is done automatically so no need to fidget around with scaling options.
        + Add scale bars, panel labels, and titles.
        + Customize frame visibility and title colors
        + Easy saving of high-resolution figures.


### Basic Usage:
Create `MultiChannelImage` objects for all the images to put together:
```python
exim1 = MultiChannelImage(
    channels=[eximg[0]],
    channel_names=['Bungarotoxin'],
    colormaps=['pure_red'])

exim2 = MultiChannelImage(
    channels=[eximg[1]],
    channel_names=['ACh'],
    colormaps=['pure_green'])

exim3 = MultiChannelImage(
    channels=[eximg[2]],
    channel_names=['CFP'],
    colormaps=['pure_magenta'])

exim4 = MultiChannelImage(
    channels=[eximg[3]],
    channel_names=['Hoeschst'],
    colormaps=['pure_cyan'])
```

Now use the `ImagePanel` Class:

```python
panel = ImagePanel(1,5,figsize=(15,5))
panel.add_multichannel_image(0, 0, exim1, title='Bungarotoxin', panel_label='A')
panel.add_multichannel_image(0, 1, exim2, title='ACh', panel_label='B')
panel.add_multichannel_image(0, 2, exim3, title='CFP', panel_label='C')
panel.add_multichannel_image(0, 3, exim4, title='Hoeschst', panel_label='D')
panel.add_multichannel_image(0, 4, exim, title='Overlay', panel_label='E',scalebar=True, pixel_size=0.16,units='um',set_title_color_default=True)
panel.adjust_layout()
panel.show();
```
### Output

![image](https://github.com/user-attachments/assets/c2cc2164-22ea-442a-9ac3-131fc787df7d)

The call `panel.adjust_layout()` automatically does all the necessary scaling and spacing for the given figsize and the panel grid.
## Advanced Features

### Custom Colormaps

You can use custom colormaps, including hex color codes:

```python
image = MultiChannelImage(
    channels=[channel_data],
    channel_names=['Custom'],
    colormaps=['#FF5733']  # Using a hex color code
)
```

### Grayscale images

The library handles grayscale images and allows applying colormaps for visualization:

```python
grayscale_image = np.random.rand(100, 100)
image = MultiChannelImage(
    channels=[grayscale_image],
    channel_names=['Grayscale'],
    colormaps=['viridis']
)
```

### Panel Customization

You can customize various aspects of the image panel:

```python
panel.add_multichannel_image(
    0, 0, image,
    title='Custom Image',
    panel_label='A', #change label of each panel
    show_frame=False,
    set_title_color_default=True, #set the color of the titles if not it defaults to colormaps of the current image
    scalebar=True, #turn scale bar on/off
    pixel_size=0.05,
    units='μm'
)
```

## To Do

- [x] Release `MultiChannelImage`
- [x] Release `ImagePanel`
- [x] Release notebook tutorial
- [x] Add to PyPI
- [ ] Release interactive elements with ipympl, scrolling along z-axis, intensity sliders.
- [ ] Release simple interactive segmentation using Segment Anything and matplotlib ipympl backend
- [ ] More future: add more customization as per needs.

## Contributing
Contributions to the FluroView library are much welcomed. Feel free to send pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


