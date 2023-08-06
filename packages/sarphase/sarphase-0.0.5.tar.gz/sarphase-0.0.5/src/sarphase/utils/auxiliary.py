from glob import iglob
import os
import numpy as np
import pandas as pd                  # data analysis and manipulation
import shutil

# Auxiliary functions
# Common operations

def empty_dir(path_dir):
    '''
    Function to empty a dir

    Parameter:
        path_dir    os     Path to the directory to be emptied
    '''
    dir_list = os.listdir(path_dir)
    for file in dir_list:
        print(file)
        #os.remove(os.path.join(path_dir, file))
        shutil.rmtree(os.path.join(path_dir, file))

def check_dir(path_dir):
    '''
    Function to check if the input dir exists in order to create it or not.
    Parameter
        path_dir    os     Path to check
    '''
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    else:  # should to be empty
        empty_dir(path_dir)

def get_file_name_and_extension(path):
    '''
    Function to get the file name and extension from the input path

    Parameter:
        path    os    Path to file
    Returns:
        file_name    str    File name
        file_ext     str    Extension
    '''
    dir_name, file_name = os.path.split(path)
    file_name, file_ext = file_name.split(".")
    return file_name, file_ext

# Get SAR Products as list

def get_s1_product_list_from_dir(path_s1_dir):
    '''
    Function to get the Sentinel-1 products in .zip format from the input dir

    Parameters:
        path_s1_dir     os      S1 product path
    Returns:
        list_s1_data    list    S1 product paths as list
    '''
    list_s1_data = sorted(list(iglob(os.path.join(path_s1_dir, "**", "*S1*.zip"), recursive=True)))
    return list_s1_data

# Get SAR Product attributes from product name or path

def get_properties_from_product_name(product_name):
    '''
    Function to extract the properties of a SAR Product

    Naming Convention
    SAR Product sample name: S1A_IW_GRDH_1SDV_20200418T172508_20200418T172533_032185_03B8C6_28F3
        Mission                 S1A                 Sentinel 1 - A/B
        Mode beam               IW                  S1-6 (SM), IW, EW, WW, SM
        Product type            GRD                 SLC, GRD, OCN
        Resolution class        H                   F (Full), H (High), M (Medium) or _(not applicable). Note: Only for GRD products
        Processing Level        1                   0, 1, 2
        Product class           S                   S (Standard), A (Annotation)
        Polarization            DV                  SH (Single HH), SV (single VV), DH (Dual HH, HV), DV (Dual VV, VH)
        Product start           20200418T172508     YYYYMMDD T (Time) HHMMSS
        Product stop            20200418T172533     YYYYMMDD T (Time) HHMMSS
        Absolute orbit number   032185
        Mission data-take       03B8C6
        Product unique ID       28F3

    Parameters:
        product_name    str    SNAP product name

    Returns:
        sar_info        dict   SNAP product main attributes

    '''
    # using bytes or position...
    product_name = product_name.replace("_", " ") # To0 avoid error for SLC products
    file_data = product_name.split() #whitespace
    mission = file_data[0]  # mission
    satellite_name = "Sentinel" if mission[0] == "S" else "Sentinel"  # Default value
    satellite_number = mission[1]
    satellite_letter = mission[2]
    mission = satellite_name + "-" + satellite_number + satellite_letter
    mode_beam = file_data[1]  # mode_beam
    product_type = file_data[2][0:-1]  # product_type
    resolution = file_data[2][-1]  # resolution Full, High, Medium
    processing_level = file_data[3][0]  # processing_level
    product_class = file_data[3][1]  # product_class
    polarization = file_data[3][2:]  # polarization
    date_init = file_data[4]  # .split("T")[0] ## yyyy mm dd
    date_end = file_data[5]
    pd_date_init = get_date_acquisition(date_init)
    pd_date_end = get_date_acquisition(date_end)
    abs_orbit_number = file_data[6]  # abs_orbit_number
    mission_data_take = file_data[7]  # mission_data_take
    product_unique_id = file_data[8]  # product_unique_ID
    #print(mission, mode_beam, product_type, resolution, processing_level, product_class, polarization, pd_date_init, pd_date_end, abs_orbit_number, mission_data_take, product_unique_id)
    # as dict
    sar_info = {}
    sar_info["Mission"] = mission
    sar_info["SensingMode"] = mode_beam
    sar_info["ProductType"] = product_type
    sar_info["Resolution"] = resolution
    sar_info["ProcessingLevel"] = processing_level
    sar_info["ProductClass"] = product_class
    sar_info["Polarization"] = polarization
    sar_info["Date"] = file_data[4].split("T")[0]
    sar_info["DateAcquisitionInit"] = pd_date_init # date_acquisition
    sar_info["DateAcquisitionEnd"] = pd_date_end
    sar_info["AbsOrbitNumber"] = abs_orbit_number
    sar_info["MissionDataTake"] = mission_data_take
    sar_info["ProductUniqueID"] = product_unique_id
    return sar_info

def get_info_from_sar_path(sar_path):
    '''
    Function to get the SAR product information from path

    Parameter:
        sar_path    os                  os path
    Returns:
        sar_info    dict                SAR product information
        sar_info    pandas.DataFrame    SAR product information
    '''
    file_name, file_ext = get_file_name_and_extension(sar_path)
    sar_info = get_properties_from_product_name(file_name)
    return sar_info

def get_date_acquisition(date_acquisition):
    '''
    Function to get the SAR Product date acquisition as pandas.Timestamp format

    Parameter:
        date_acquisition    str                 Date acquisition information extracted from SAR Product name
    Returns:
        pd_date             pandas.Timestamp    SAR Product date acquisition
    '''
    date = date_acquisition.split("T")[0]
    date_year, date_month, date_day = int(date[0:4]), int(date[4:6]), int(date[6:])
    time = date_acquisition.split("T")[1]
    date_h, date_m, date_s = int(time[0:2]), int(time[2:4]), int(time[4:])
    # as pandas.Timestamp
    pd_date = pd.Timestamp(year=date_year, month=date_month, day=date_day, hour=date_h, minute=date_m, second=date_s)
    return pd_date

def get_date_as_str_from_product_name(product_name, date_format="%d%b%Y"):
    reference_info = get_properties_from_product_name(product_name)
    date_timestamp = reference_info["DateAcquisitionInit"]
    date_str = date_timestamp.strftime(date_format)
    return date_str

def get_polarization_bands_from_sar_product(product):
    product_name = product.getName()
    product_info = get_properties_from_product_name(product_name)
    polarization_mode = product_info["Polarization"]
    polarization_bands = get_polarization_band_names(polarization_mode)
    return polarization_bands

def get_polarization_band_names(polarization_mode):
    polarization_band_dict = {"SH": "HH", "SV": "VV", "DH": ["HH", "HV"], "DV": ["VV", "VH"]}
    polarization_bands = polarization_band_dict[polarization_mode]
    return polarization_bands

def get_subswath_name_from_sar_band_names(product_band_names_list):
    product_subswath_names = []
    for band in product_band_names_list:
        band_data = band.split("_")
        subswath_id = band_data[1]
        if subswath_id not in product_subswath_names:
            product_subswath_names.append(subswath_id)
    return product_subswath_names

def get_band_data_as_numpy_array(product, band_name):
    band = product.getBand(band_name)
    w = band.getRasterWidth()
    h = band.getRasterHeight()

    try: # sometimes fails
        # Option A - using readRasterData
        band_data = band.createCompatibleRasterData()
        band.readRasterData(0, 0, band.getRasterWidth(), band.getRasterHeight(), band_data)
        band_data = np.array(band_data.getElems(), np.float32)
        band_data.shape = h, w
        #print(band_data.shape)
        #print(np.amin(band_data), np.amax(band_data))
    except:
        # Option B - using readPixels
        band_data = np.zeros(w*h, np.float32)
        band.readPixels(0, 0, w, h, band_data)
        band_data.shape = h, w
        #print(band_data.shape)
        #print(np.amin(band_data), np.amax(band_data))

    return band_data

