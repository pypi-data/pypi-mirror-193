import cv2
import matplotlib
import matplotlib.colors as colors   # create visualizations
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from termcolor import colored        # prints colored text
from zipfile import ZipFile          # zip file manipulation

import auxiliary as aux

#matplotlib.use('TkAgg')

# Improve: How to select the proper values for min_value_VV, max_value_VV, min_value_VH, max_value_VH?
def single_band_output_view(product, band_name, min_value, max_value, method="matplotlib"): # "matplotlib", "OpenCV"
    '''
    Function to create and display the visualization of SAR Data using matplotlib

    Parameters:
        product      snap.core.datamodel.Product    SNAP object
        band_name    str                            product's band to be visualized
        min_value    int, float                     min value for color strech
        max_value    int, float                     max value for color strech
    '''
    valid_diaplay_method = ["matplotlib", "OpenCV"]
    band_data = aux.get_band_data_as_numpy_array(product, band_name)
    print(band_data.shape) # band dim
    # basic stats
    print(np.amin(band_data), np.amax(band_data))

    # plot histo --> high processing time
    #plt.hist(band_data, bins=30)
    #plt.show()
    #plt.close()

    if method in valid_diaplay_method:
        if method=="matplotlib":
            # display band
            fig, ax = plt.subplots(1, 1, figsize=(16, 16))
            # using cmap
            #valid_cmap = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
            ax.imshow(band_data, cmap="Greys", vmin=min_value, vmax=max_value)
            # usign custom style
            #plt.style.use("classic")
            #ax.imshow(band_data, vmin=min_value, vmax=max_value)
            ax.set_title(band_name)
            ax.label_outer()
            plt.show()
            plt.close()
        else:
            band_data = band_data.astype(np.uint8) # to 8 bits
            # OpenCV Notation: CV_<bit-depth>{U|S|F}C(<number_of_channels>)
            # Type CV_8UC1(gray - scale) or CV_8UC3(rgb) required
            band_data_jet = cv2.applyColorMap(band_data, cv2.COLORMAP_JET)  # Fails.
            band_data_resize = cv2.resize(band_data_jet, (960, 540)) # get new shape
            # imshow fails
            while True:
                cv2.imshow(band_name, band_data_resize)
                cv2.waitKey(0) # Display image until key pressed. Fails if we close the window clicking X
                print(cv2.getWindowProperty(band_name, cv2.WND_PROP_VISIBLE))
                if cv2.getWindowProperty(band_name, cv2.WND_PROP_VISIBLE) < 1:
                    cv2.destroyAllWindows()
                    break
                    #print(cv2.getWindowProperty(band_name, cv2.WND_PROP_VISIBLE)) # -1 is closed
            cv2.destroyAllWindows()
            cv2.waitKey(1)
    else:
        raise Exception(colored(f"The display method {method} is not implemented {valid_diaplay_method}", "yellow"))

def display_interferogram(product, band_name, colormap_style="classic"):
    '''
    Function to create and display the visualization of a Interferogram

    Parameters:
        product           nap.core.datamodel.Product    SNAP object
        band_name         str                           product's band to be visualized
        colormap_style    strint                        Matplotlib style. Default "classic"
    '''
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    valid_colormap_style = ["classic", "Solarize_Light2", "bmh", "dark_background", "fast", "fivethistyeight", "ggplot", "grayscale", "tableau-colorblind10"]
    # check colormap
    colormap_style_used = colormap_style if colormap_style in valid_colormap_style else "classic" # default

    band_data = aux.get_band_data_as_numpy_array(product, band_name)
    print(band_data.shape) # band size

    # display band
    #fig, ax = plt.subplots(1, 1, figsize=(16, 16))
    #ax.imshow(band_data, cmap="gray", vmin=0, vmax=np.pi)
    #ax.set_title(band_name)
    #ax.label_outer()
    #plt.style.use(colormap_style_used)
    #plt.show()
    #plt.close()

    #using imshow
    #plt.imshow(band_data)
    #plt.style.use(colormap_style_used)
    #plt.show()
    #plt.close()

    #using openCV

    # using OpenCV
    band_data = band_data.astype(np.uint8) # to 8 bits
    band_data_jet = cv2.applyColorMap(band_data, cv2.COLORMAP_JET)  # Fails. Type CV_8UC1 or CV_8UC3 required
    band_data_resize = cv2.resize(band_data_jet, (960, 540)) # get new shape
    cv2.imshow(f"Interferogram {band_name}", band_data_resize) # -pi, pi
    cv2.waitKey(0) # # waits until a key is pressed
    cv2.destroyAllWindows() # # destroys the window showing image

def output_view(product, output_band, min_value_VV, max_value_VV, min_value_VH, max_value_VH):
    '''
    Function to create and display the visualization of SAR Data using matplotlib

    Parameters:
        product              snap.core.datamodel.Product    SNAP object
        band                 list                           product's band to be visualized
        min_value_VV         int, float                     min value for color strech in VV band
        max_value_VV         int, float                     max value for color strech in VV band
        min_value_VH         int, float                     min value for color strech in VH band
        max_value_VH         int, float                     max value for color strech in VH band
    '''

    band_data_list = []

    for band_label in output_band:
        band = product.getBand(band_label)
        w = band.getRasterWidth()
        h = band.getRasterHeight()
        band_data = np.zeros(w*h, np.float32)
        band.readPixels(0, 0, w, h, band_data)
        band_data.shape = h, w
        band_data_list.append(band_data)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 16))
    ax1.imshow(band_data_list[0], cmap="gray", vmin=min_value_VV, vmax=max_value_VV)
    ax1.set_title(output_band[0])
    ax2.imshow(band_data_list[1], cmap="gray", vmin=min_value_VH, vmax=max_value_VH)
    ax2.set_title(output_band[1])

    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()
    plt.close()

def create_quiclook_visualization(path):
    '''
    Function to create and display the quicklook image of a SAR product using matplotlib

    Parameter:
        path    os    os path to the SAR product
    '''
    product_path, _ = os.path.split(path)
    # print(product_path)
    file_name, file_ext = aux.get_file_name_and_extension(path)
    # print(file_ext)
    if file_ext in ["zip", "ZIP"]:
        with ZipFile(path, "r") as qck_look:
            file_png = file_name + ".SAFE/preview/quick-look.png"
            qck_look.extract(file_png, product_path)  # extract first
            png_path = os.path.join(product_path, file_png)
            # print(png_path)
            img = mpimg.imread(png_path)  # load image
            # create the figure
            plt.figure(figsize=(15, 15))
            plt.title("Quicklook visualization - " + file_name + "\n")
            plt.axis("off")
            plt.imshow(img)
            plt.show()  # not required for display on Jypiter Notebooks
            plt.close()
            # remove extracted folder
            path_to_remove = os.path.join(product_path, (file_name + ".SAFE"))
            shutil.rmtree(path_to_remove)  # better than use os.rmdir(), as it should to be an empty dir
        
def plot_3D_delaunay_triangulation(delaunay_triangulation, labels, title="3D Delaunay triangulation"):
    fig = plt.figure()
    plt.suptitle(title)
    ax = plt.axes(projection='3d')
    for triangle in delaunay_triangulation.simplices:
        point = delaunay_triangulation.points[triangle, :]
        # sample [0,1,2,3]
        # join 0 with 1,2,3 \ 1 with 2 and 3 \ 2 with 3
        ax.plot3D(point[[0,1],0], point[[0,1],1], point[[0,1],2], color='g', lw='0.1')
        ax.plot3D(point[[0,2],0], point[[0,2],1], point[[0,2],2], color='g', lw='0.1')
        ax.plot3D(point[[0,3],0], point[[0,3],1], point[[0,3],2], color='g', lw='0.1')
        ax.plot3D(point[[1,2],0], point[[1,2],1], point[[1,2],2], color='g', lw='0.1')
        ax.plot3D(point[[1,3],0], point[[1,3],1], point[[1,3],2], color='g', lw='0.1')
        ax.plot3D(point[[2,3],0], point[[2,3],1], point[[2,3],2], color='g', lw='0.1')

    ax.set_xlabel('$B$', linespacing=4)
    ax.set_ylabel('$T$', linespacing=4)
    ax.set_zlabel('$\Delta{fdc}$', linespacing=4)

    ax.scatter(delaunay_triangulation.points[1:,0], delaunay_triangulation.points[1:,1], delaunay_triangulation.points[1:,2], color='b')
    ax.scatter(0, 0 , 0, color='r')  # origin point

    for i, coordinate in enumerate(delaunay_triangulation.points):
        point_label = labels[i]
        ax.text(coordinate[0], coordinate[1], coordinate[2], point_label, color='blue', fontsize=6)

    plt.show()

def plot_3D_baselines(points_as_array, labels, baseline_index_list, title):
    fig = plt.figure()
    plt.suptitle(title)
    ax = plt.axes(projection='3d')
    ax.scatter(0, 0, 0, color='r')  # origin point
    ax.scatter(points_as_array[1:, 0], points_as_array[1:, 1], points_as_array[1:, 2], color='b')
    ax.set_xlabel('$B$', linespacing=4)
    ax.set_ylabel('$T$', linespacing=4)
    ax.set_zlabel('$\Delta{fdc}$', linespacing=4)
    # add labels
    for i, coordinate in enumerate(points_as_array):
        point_label = labels[i]
        ax.text(coordinate[0], coordinate[1], coordinate[2], point_label, color='blue', fontsize=6)
    # baselines
    for line in baseline_index_list:
        ax.plot3D(points_as_array[[line[0], line[1]], 0], points_as_array[[line[0], line[1]], 1], points_as_array[[line[0], line[1]], 2], color='g', lw='0.3')
    plt.show()