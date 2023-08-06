import os
import snappy                        # SNAP Python interface
import subprocess                    # external calls to system
from termcolor import colored        # prints colored text

import auxiliary as aux

# Launches SNAP GPT Help command (Tested)
def print_help_snap_operator(snap_operator):
    '''
    Function to display the help documentation for the input SNAP Operator

    Parameter:
        snap_operator    str    SNAP operator
    '''
    print(subprocess.Popen(["gpt", "-h", snap_operator], stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])

# Basic operations using snappy - Read / Write Product

def read_product(sar_path):
    '''
    Function to read a SAR product using snappy

    Parameter:
        sar_path       os                             os path
    Returns:
        sar_product    snap.core.datamodel.Product    SNAP object
    '''
    sar_product = snappy.ProductIO.readProduct(sar_path)
    return sar_product

def write_snap_product(product, output_path, output_format="BEAM-DIMAP"):
    '''
    Function to write a SAR processing product using snappy

    Parameters:
        product          snap.core.datamodel.Product    SNAP product
        outpath_name     os                             Output path
        output_format    str                            Output SAR product format. Default: "BEAM-DIMAP"
    '''
    # all format options
    #valid_output_format = ["BEAM-DIMAP", "BMP", "CSV", "ENVI", "GDAL-BMP-WRITER", "GDAL-BT-WRITER", "GDAL-COG-WRITER", "GDAL-GS7BG-WRITER",
    #                       "GDAL-GSBG-WRITER", "GDAL-GTX-WRITER", "GDAL-GTiff-WRITER", "GDAL-HFA-WRITER", "GDAL-ILWIS-WRITER", "GDAL-KRO-WRITER",
    #                       "GDAL-MFF-WRITER", "GDAL-NITF-WRITER", "GDAL-PCIDSK-WRITER", "GDAL-PNM-WRITER", "GDAL-RMF-WRITER", "GDAL-RST-WRITER", "GDAL-SAGA-WRITER",
    #                       "GDAL-SGI-WRITER", "GIF", "Gamma", "Gamma for PyRate", "Generic Binary BSQ", "GeoTiff", "GeoTiff+XML", "GeoTiff-BigTIFF", "HDF5",
    #                       "JP2", "JPEG2000", "JPG", "NetCDF4-BEAM", "NetCDF4-CF", "PNG", "PolSARPro", "Snaphu", "ZNAP"]

    # use .extension?
    # output_format_failed =["BMP","CSV",
    #                        "GDAL-BMP-WRITER", "GDAL-BT-WRITER", "GDAL-COG-WRITER", "GDAL-GS7BG-WRITER", "GDAL-GSBG-WRITER", "GDAL-GTX-WRITER", "GDAL-GTiff-WRITER",
    #                        "GDAL-HFA-WRITER", "GDAL-ILWIS-WRITER", "GDAL-KRO-WRITER", "GDAL-MFF-WRITER", "GDAL-NITF-WRITER", "GDAL-PCIDSK-WRITER", "GDAL-PNM-WRITER"
    #                         "GDAL-RMF-WRITER", "GDAL-RST-WRITER", "GDAL-SAGA-WRITER", "GDAL-SGI-WRITER"
    #                         "GIF", "Generic Binary BSQ", "JP2", "JPEG2000", "JPG", "PNG"]
    # GDAL Geotiff writer cannot write a product containing bands with different data types (the data type of band index 2 is 30, different from band index 0).
    # JPEG2000 --> Exception in thread "pool-2-thread-4" java.lang.IllegalArgumentException: operation "BandMerge" requires all source objects to be valid input; a null is supplied.

    # use tested
    valid_output_format = ["BEAM-DIMAP", "ENVI", "Gamma", "Gamma for PyRate", "GeoTiff", "GeoTiff+XML", "GeoTiff-BigTIFF", "HDF5",
                           "NetCDF4-BEAM", "NetCDF4-CF", "PolSARPro", "Snaphu", "ZNAP"] # extension not required, only a dir
    # "Gamma for PyRate" --> coregistered slave/master pair.
    # "HDF5" --> strange bands
    # The NetCDF-BEAM stores some BEAM/SNAP specific stuff, like colour information, expressions etc.
    # The data can be read in other applications too, but some information might be lost.
    # The NetCDF-CF is of more general use. The data is converted in a way that other applications can read it.
    # This is the suggested format when you want to distribute the data. More specifically NetCDF4-CF, because this supports compression.
    # "Snaphu" --> SNAPHU writer requires a wrapped phase band

    if output_format in valid_output_format:
        snappy.ProductIO.writeProduct(product, output_path, output_format)
        print(colored(f"Product successfully saved in: {output_path}", "green"))
    else:
        raise Exception(colored(f"The output format {output_format} is not valid. Please select from the following options: {valid_output_format}", "yellow"))

# Product Stats

def compute_product_band_stats(product, band_name, accurate=True):
    if product.containsBand(band_name):
        band = product.getBand(band_name)
        # compute stats
        stx = band.getStx(accurate=True) if accurate else band.getStx()
        return stx
    else:
        raise Exception(colored(f"The input product band {band_name} is not in the input SAR product", "yellow"))

# SNAP Operators (order list)

# Apply-Orbit-File (Tested)
def compute_orbit_file(product, **kwargs):
    '''
    Function to apply the Orbit correction to a SNAP Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        continueOnFail    bool    Do not fail if new orbit file is not found (True). Default value is 'False'.
        orbitType         str     Value must be one of 'Sentinel Precise (Auto Download)', 'Sentinel Restituted (Auto Download)',
                                  'DORIS Preliminary POR (ENVISAT)', 'DORIS Precise VOR (ENVISAT) (Auto Download)',
                                  'DELFT Precise (ENVISAT, ERS1&2) (Auto Download)', 'PRARE Precise (ERS1&2) (Auto Download)',
                                  'Kompsat5 Precise'.
                                  Default value is 'Sentinel Precise (Auto Download)'.
        polyDegree        int     Default value is '3'.

    Returns:
        apply_orbit    snap.core.datamodel.Product    SNAP Product after orbit correction
    '''
    valid_operator_parameters = ["continueOnFail", "orbitType", "polyDegree"]
    #valid_orbit_type = ['Sentinel Precise', 'Sentinel Restituted', 'DORIS Preliminary POR (ENVISAT)', 'DORIS Precise VOR (ENVISAT)',
    #                    'DELFT Precise (ENVISAT, ERS1&2)', 'PRARE Precise (ERS1&2)', 'Kompsat5 Precise'] # Fails
    valid_orbit_type = ['Sentinel Precise (Auto Download)', 'Sentinel Restituted (Auto Download)',
                        'DORIS Preliminary POR (ENVISAT)', 'DORIS Precise VOR (ENVISAT) (Auto Download)',
                        'DELFT Precise (ENVISAT, ERS1&2) (Auto Download)', 'PRARE Precise (ERS1&2) (Auto Download)',
                        'Kompsat5 Precise'] # (Auto Download) required
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "continueOnFail": # bool
                continue_on_fail = kwargs[key] if isinstance(kwargs[key], bool) else False
                parameters.put(key, continue_on_fail)
                if continue_on_fail != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "orbitType": # str
                orbit_type = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_orbit_type else "Sentinel Precise (Auto Download)" # default
                parameters.put(key, orbit_type)
                if orbit_type != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "polyDegree": # int
                try:
                    poly_degree_value = int(float((kwargs[key]))) # int, float or valid str
                except:
                    poly_degree_value = 3 # default
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, poly_degree_value)
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply orbit file
    apply_orbit = snappy.GPF.createProduct("Apply-Orbit-File", parameters, product)
    print(colored("Orbit File updated successfully", "green"))
    return apply_orbit

# Back-Geocoding (Tested)
def compute_back_geocoding(reference_product, secondary_product, **kwargs):
    '''
    Function to apply the Back-Geocoding operator to a Reference/Secondary SAR Products.

    This operator co-registers two S-1 SLC split products (master and slave) of the same sub-swath
    using the orbits of the two products and a Digital Elevation Model (DEM)

    Parameters:
        reference_product    snap.core.datamodel.Product    SNAP Reference Product
        secondary_product    snap.core.datamodel.Product    SNAP Secondary Product
        kwargs     dict                           Options

    kwargs Options:
        demName                        str      The digital elevation model. Default value is 'SRTM 3Sec'.
        demResamplingMethod            str      Sets parameter 'demResamplingMethod' to str. Default value is 'BICUBIC_INTERPOLATION'.
        disableReramp                  bool     Sets parameter 'disableReramp' to bool. Default value is 'False'.
        externalDEMFile                os       path to file. Sets parameter 'externalDEMFile' to <file>.
        externalDEMNoDataValue         float    Sets parameter 'externalDEMNoDataValue' to <double>. Default value is '0'.
        maskOutAreaWithoutElevation    bool     Sets parameter 'maskOutAreaWithoutElevation' to <boolean>. Default value is 'True'.
        outputDerampDemodPhase         bool     Sets parameter 'outputDerampDemodPhase' to <boolean>. Default value is 'False'.
        outputRangeAzimuthOffset       bool     Sets parameter 'outputRangeAzimuthOffset' to <boolean>. Default value is 'False'.
        resamplingType                 str      The method to be used when resampling the slave grid onto the master grid.
                                                Default value is 'BISINC_5_POINT_INTERPOLATION'.
    Returns:
        back_geocoding    snap.core.datamodel.Product    SNAP Product after radiometric calibration
    '''
    valid_operator_parameters = ["demName", "demResamplingMethod", "disableReramp", "externalDEMFile", "externalDEMNoDataValue", "maskOutAreaWithoutElevation",
                                 "outputDerampDemodPhase", "outputRangeAzimuthOffset", "resamplingType"]
    # valid_dem_name = ["ACE2_5Min (Auto Download)", "ACE30 (Auto Download)", "ASTER 1 Sec GDEM", "CDEM (Auto Download)", "Copernicus 30m Global DEM (Auto Download)",
    #                  "Copernicus 90m Global DEM (Auto Download)", "GETASSE30 (Auto Download", "SRTM 1Sec Grid", "SRTM 1Sec HGT (Auto Download)",
    #                  "SRTM 3Sec (Auto Download)", "External DEM"] # Fails
    valid_dem_name = ["ACE2_5Min", "ACE30", "ASTER 1 Sec GDEM", "CDEM", "Copernicus 30m Global DEM", "Copernicus 90m Global DEM", "GETASSE30",
                      "SRTM 1Sec Grid", "SRTM 1Sec HGT","SRTM 3Sec", "External DEM"]
    # demResamplingMethod or resamplingType (valid for both)
    valid_resampling_method = ["NEAREST_NEIGHBOUR", "BILINEAR_INTERPOLATION", "CUBIC_CONVOLUTION", "BISINC_5_POINT_INTERPOLATION",
                               "BISINC_11_POINT_INTERPOLATION", "BISINC_21_POINT_INTERPOLATION", "BICUBIC_INTERPOLATION"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "demName": # str
                # validate demName type str
                dem_name = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_dem_name else "SRTM 3Sec" # default
                parameters.put(key, dem_name)
                if dem_name != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "demResamplingMethod": # str
                # validate demResamplingMethod type str
                dem_resampling_method = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_resampling_method else "BICUBIC_INTERPOLATION" # default
                parameters.put(key, dem_resampling_method)
                if dem_resampling_method != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "externalDEMFile": # os path
                if os.path.exists(kwargs[key]):
                    parameters.put(key, kwargs[key])
                else:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} file has been ignored since the file does not exist.", "yellow"))
            elif key == "externalDEMNoDataValue": # float
                try:
                    external_dem_no_data_value = float(kwargs[key]) # float, int or valid str
                except:
                    external_dem_no_data_value = 0. # default value
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, external_dem_no_data_value)
            elif key == "resamplingType":
                # validate demResamplingMethod type str
                resampling_type = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_resampling_method else "BISINC_5_POINT_INTERPOLATION" # default
                parameters.put(key, resampling_type)
                if resampling_type != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "maskOutAreaWithoutElevation": # bool
                mask_out_area_without_elevation = kwargs[key] if isinstance(kwargs[key], bool) else True # default
                parameters.put(key, mask_out_area_without_elevation)
                if mask_out_area_without_elevation != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["disableReramp", "outputDerampDemodPhase", "outputRangeAzimuthOffset"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply Back-Geocoding
    back_geocoding = snappy.GPF.createProduct("Back-Geocoding", parameters, [secondary_product, reference_product]) # tested. change order required
    print(colored("Back-Geocoding successfully applied", "green"))
    return back_geocoding

# BandMaths





# Calibration
# kwargs= {"auxFile": str, "createBetaBand": bool, "createGammaBand": bool, "externalAuxFile": file, "outputBetaBand": bool, "outputGammaBand": bool,
#          "outputImageInComplex": bool, "outputImageScaleInDb": bool, "outputSigmaBand": bool,"selectedPolarisations": str, "sourceBands": str}
def compute_radiometric_calibration(product, **kwargs):
    '''
    Function to apply the Radiometric Calibration to a SNAP Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        auxFile                  str         The auxiliary file. Value must be one of 'Latest Auxiliary File', 'Product Auxiliary File',
                                             'External Auxiliary File'. Default value is 'Latest Auxiliary File'.
        createBetaBand           bool, str    Create beta0 virtual band. Default value is 'False'.
        createGammaBand          bool, str    Create gamma0 virtual band. Default value is 'False'.
        externalAuxFile          file         The antenna elevation pattern gain auxiliary data file.
        outputBetaBand           bool, str    Output beta0 band. Default value is 'False'.
        outputGammaBand          bool, str    Output gamma0 band. Default value is 'False'.
        outputImageInComplex     bool, str    Output image in complex. Default value is 'False'.
        outputImageScaleInDb     bool, str    Output image scale. Default value is 'False'.
        outputSigmaBand          bool, str    Output sigma0 band. Default value is 'True'.
        selectedPolarisations    str         "str,str,str,...". The list of polarisations.
        sourceBands              str         "str,str,str,...". The list of source bands.

    Returns:
        calibrated    snap.core.datamodel.Product    SNAP Product after radiometric calibration
    '''
    valid_operator_parameters = ["auxFile", "createBetaBand", "createGammaBand", "externalAuxFile", "outputBetaBand", "outputGammaBand",
                                 "outputImageInComplex", "outputImageScaleInDb", "outputSigmaBand","selectedPolarisations", "sourceBands"]
    valid_aux_file_options = ["Latest Auxiliary File", "Product Auxiliary File", "External Auxiliary File"]

    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            #print(key, kwargs[key])
            if key == "auxFile":
                # validate Aux File Option
                aux_file = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_aux_file_options else 'Latest Auxiliary File' # default value
                if aux_file != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(aux_file)
                parameters.put(key, aux_file)
            #elif key == "externalAuxFile": # I don't know how to use this option
            elif key == "selectedPolarisations":
                # get product polarization bands
                product_name = product.getName()
                product_info = aux.get_properties_from_product_name(product_name)
                polarization_mode = product_info["Polarization"]
                polarization_bands = aux.get_polarization_band_names(polarization_mode)
                #print("Product polarization bands : ", polarization_bands)
                # validate
                input_polarization_bands = kwargs[key].replace(" ", "").split(",")
                #for char in [" ", "list<", ">"]:
                #    input_polarization_bands_str = input_polarization_bands_str.replace(char, "")
                #input_polarization_bands = input_polarization_bands_str.split(",")
                for band in input_polarization_bands:
                    #print(band)
                    if band not in polarization_bands:
                        raise Exception(colored(f"The input polarization band {band} is not in the input SAR product", "yellow"))
                parameters.put(key, kwargs[key])
            elif key == "sourceBands":
                if isinstance(kwargs[key], str):
                    input_band_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_band_names:
                        if not product.containsBand(band):
                            raise Exception(colored(f"The input product band {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            else:
                parameters.put(key, kwargs[key])
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply radiometric calibration
    calibrated = snappy.GPF.createProduct("Calibration", parameters, product)
    print(colored("Radiometric Calibration successfully applied", "green"))
    return calibrated

# CreateStack






# Enhanced-Spectral-Diversity (Tested)
# Question: Are some of the parameters incompatible with each other?
# kwargs = {} # default options works fine
def compute_enhanced_spectral_diversity(product, **kwargs):
    '''
    Function to compute the Enhanced-Spectral-Diversity to a SNAP Product

    SNAP Help
    This operator follows the S-1 Back Geocoding operator in the TOPS InSAR processing chain. It first estimates a constant range offset for the
    whole sub-swath of the split S-1 SLC image using incoherent cross-correlation. The estimation is done for each burst using a small block of data
    in the center of the burst. The estimates from all bursts are then averaged to get the final constant range offset for the whole sub-swath.

    Note: Use default parameters kwargs={}

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        cohThreshold               float    The coherence threshold for outlier removal. Valid interval is (0, 1]. Default value is '0.3'.
        doNotWriteTargetBands      bool     Do not write target bands. Default value is 'False'.
        esdEstimator               str      ESD estimator used for azimuth shift computation. Value must be one of 'Average', 'Periodogram'.
                                            Default value is 'Periodogram'.
        fineWinAccAzimuth          str      Sets parameter 'fineWinAccAzimuth' to <string>. Value must be one of '2', '4', '8', '16', '32', '64'.
                                            Default value is '16'.
        fineWinAccRange            str      Sets parameter 'fineWinAccRange' to <string>. Value must be one of '2', '4', '8', '16', '32', '64'.
                                            Default value is '16'.
        fineWinHeightStr           str      Sets parameter 'fineWinHeightStr' to <string>. Value must be one of '32', '64', '128', '256', '512', '1024', '2048'.
                                            Default value is '512'.
        fineWinOversampling        str      Sets parameter 'fineWinOversampling' to <string>. Value must be one of '32', '64', '128', '256'.
                                            Default value is '128'.
        fineWinWidthStr            str      Sets parameter 'fineWinWidthStr' to <string>. Value must be one of '32', '64', '128', '256', '512', '1024', '2048'.
                                            Default value is '512'.
        integrationMethod          str      Method used for integrating the shifts network. Value must be one of 'L1', 'L2', 'L1 and L2'.
                                            Default value is 'L1 and L2'.
        maxTemporalBaseline        int      Maximum temporal baseline (in days or number of images depending on the Temporal baseline type) between pairs of images to construct the network.
                                            Any number < 1 will generate a network with all of the possible pairs. Default value is '4'.
        numBlocksPerOverlap        int      The number of windows per overlap for ESD. Valid interval is [1, 20]. Default value is '10'.
        overallAzimuthShift        float    The overall azimuth shift. Default value is '0.0'.
        overallRangeShift          float    The overall range shift. Default value is '0.0'.
        temporalBaselineType       str      Baseline type for building the integration network. Value must be one of 'Number of images', 'Number of days'.
                                            Default value is 'Number of images'.
        useSuppliedAzimuthShift    bool     Use user supplied azimuth shift. Default value is 'False'.
        useSuppliedRangeShift      bool     Use user supplied range shift. Default value is 'False'.
        weightFunc                 str      Weight function of the coherence to use for azimuth shift estimation.
                                            Value must be one of 'None', 'Linear', 'Quadratic', 'Inv Quadratic'.
                                            Default value is 'Inv Quadratic'.
        xCorrThreshold             float    The peak cross-correlation threshold. Valid interval is (0, *).
                                            Default value is '0.1'.
    Returns:
        enhanced_spectral_diversity    snap.core.datamodel.Product    SNAP Product after Enhanced-Spectral-Diversity
    '''
    valid_operator_parameters = ["cohThreshold", "doNotWriteTargetBands", "esdEstimator", "fineWinAccAzimuth", "fineWinAccRange", "fineWinHeightStr", "fineWinOversampling",
                                 "fineWinWidthStr", "integrationMethod", "maxTemporalBaseline", "numBlocksPerOverlap", "overallAzimuthShift", "overallRangeShift",
                                 "temporalBaselineType", "useSuppliedAzimuthShift", "useSuppliedRangeShift", "weightFunc", "xCorrThreshold"]
    valid_esd_estimator = ["Average", "Periodogram"] # Default "Periodogram"
    # "fineWinAccAzimuth" or "fineWinAccRange"
    valid_fine_win_acc = ["2", "4", "8", "16", "32", "64"] # Default value is "16".
    # "fineWinHeightStr" or "fineWinWidthStr"
    valid_fine_win_height_width_str = ["32", "64", "128", "256", "512", "1024", "2048"] # Default "512"
    valid_fine_win_oversampling = ["32", "64", "128", "256"] # Default "128"
    valid_integration_method = ["L1", "L2", "L1 and L2"] # Default "L1 and L2"
    valid_temporal_baseline_type = ["Number of images", "Number of days"] # Default "Number of images"
    valid_weight_func = ["None", "Linear", "Quadratic", "Inv Quadratic"] # Default "Inv Quadratic"
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "cohThreshold": # float in range (0,1]
                try:
                    coh_threshold_checked = float(kwargs[key]) if 0. < float(kwargs[key]) <= 1. else 0.3  # float, int or valid str
                    differs = False if coh_threshold_checked == float(kwargs[key]) else True
                except:
                    coh_threshold_checked = 0.3 # set default value
                    differs = True
                parameters.put(key, coh_threshold_checked)
                if differs:
                    print(colored(f"Warning!. The input cohThreshold {kwargs[key]} is out of range (0,1]. The default value for the cohThreshold parameter has been set.", "yellow"))
            elif key == "esdEstimator": # str
                esd_estimator = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_esd_estimator else "Periodogram" # default
                parameters.put(key, esd_estimator)
                if esd_estimator != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["fineWinAccAzimuth", "fineWinAccRange"]: # str int
                try:
                    fine_win_acc = str(int(float(kwargs[key]))) if str(int(float(kwargs[key]))) in valid_fine_win_acc else "16" # default value. avoid error "16."
                    differs = False if fine_win_acc == str(int(float(kwargs[key]))) else True
                except:
                    differs = True
                    fine_win_acc = "16" # default value
                parameters.put(key, fine_win_acc)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["fineWinHeightStr", "fineWinWidthStr"]: # int, float, valid str
                try:
                    fine_win_acc_h_w = str(int(float(kwargs[key]))) if str(int(float(kwargs[key]))) in valid_fine_win_height_width_str else "512" # default value
                    differs = False if fine_win_acc_h_w == str(int(float(kwargs[key]))) else True
                except:
                    differs = True
                    fine_win_acc_h_w = "512" # default value
                parameters.put(key, fine_win_acc_h_w)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "fineWinOversampling": # int, float, valid str
                try:
                    fine_win_oversampling = str(int(float(kwargs[key]))) if str(int(float(kwargs[key]))) in valid_fine_win_oversampling else "128" # default value
                    differs = False if fine_win_oversampling == str(int(float(kwargs[key]))) else True
                except:
                    differs = True
                    fine_win_oversampling = "128" # default value
                parameters.put(key, fine_win_oversampling)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "integrationMethod": # str
                integration_method = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_integration_method else "L1 and L2"  # default
                parameters.put(key, integration_method)
                if integration_method != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "maxTemporalBaseline": # int, float, valid str
                try:
                    max_temporal_baseline = int(float((kwargs[key]))) # avoid error to cast "10."
                    differs = False if max_temporal_baseline == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    max_temporal_baseline = 4 # default
                parameters.put(key, max_temporal_baseline)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "numBlocksPerOverlap": # int, float or valid str --> in range [1,20]
                try:
                    num_blocks = int(float((kwargs[key]))) if 1 <= int(float((kwargs[key]))) <= 20 else 10 # default value
                    differs = False if num_blocks == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    num_blocks = 10 # default
                parameters.put(key, num_blocks) # default
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["overallAzimuthShift", "overallRangeShift"]: # float
                try:
                    overall_value = float(kwargs[key])
                except:
                    overall_value = 0. # default
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, overall_value)
            elif key == "temporalBaselineType": # str
                temporal_vaseline_value = kwargs[key] if kwargs[key] in valid_temporal_baseline_type else "Number of images" # default value
                if temporal_vaseline_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, temporal_vaseline_value)
            elif key == "weightFunc": # str
                weight_func_value = kwargs[key] if kwargs[key] in valid_weight_func else "Inv Quadratic" # default value
                if weight_func_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, weight_func_value)
            elif key == "xCorrThreshold": # float
                try:
                    x_corr_thershold_checked = float(kwargs[key]) if 0. < float(kwargs[key]) < 1. else 0.1 # default
                    differs = False if x_corr_thershold_checked == float((kwargs[key])) else True
                except:
                    differs = True
                    x_corr_thershold_checked = 0.1 # default
                parameters.put(key, x_corr_thershold_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["doNotWriteTargetBands", "useSuppliedAzimuthShift", "useSuppliedRangeShift"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply Enhanced-Spectral-Diversity
    enhanced_spectral_diversity = snappy.GPF.createProduct("Enhanced-Spectral-Diversity", parameters, product)
    print(colored("Enhanced-Spectral-Diversity successfully applied", "green"))
    return enhanced_spectral_diversity

# GoldsteinPhaseFiltering (Tested)
def compute_goldstein_phase_filtering(product, **kwargs):
    '''
    Funtion to compute the GoldsteinPhaseFiltering to a SNAP Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        alpha                 float    adaptive filter exponent. Valid interval is (0, 1]. Default value is '1.0'.
        coherenceThreshold    float    The coherence threshold. Valid interval is [0, 1]. Default value is '0.2'.
        FFTSizeString         str      Sets parameter 'FFTSizeString' to <string>. Value must be one of '32', '64', '128', '256'.
                                       Default value is '64'.
        useCoherenceMask      bool     Use coherence mask. Default value is 'False'.
        windowSizeString      str      Sets parameter 'windowSizeString' to <string>. Value must be one of '3', '5', '7'.
                                       Default value is '3'.
    Returns:
        goldstein_phase_filtering    snap.core.datamodel.Product    SNAP Product after GoldsteinPhaseFiltering
    '''
    valid_operator_parameters = ["alpha", "coherenceThreshold", "FFTSizeString", "useCoherenceMask", "windowSizeString"]
    valid_fft_size_string = ["32", "64", "128", "256"] # Default "64"
    valid_window_size_string = ["3", "5", "7"] # default "3"
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "alpha": # float in range (0,1]
                try:
                    alpha_value_checked = float(kwargs[key]) if 0 < float(kwargs[key]) <= 1 else 1.0 # default
                    differs = False if alpha_value_checked == float((kwargs[key])) else True
                except:
                    differs = True
                    alpha_value_checked = 1.0
                parameters.put(key, alpha_value_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "coherenceThreshold": # float in range [0,1]
                try:
                    coherence_threshold_value_checked = float(kwargs[key]) if 0 <= float(kwargs[key]) <= 1 else 1.0  # default
                    differs = False if coherence_threshold_value_checked == float((kwargs[key])) else True
                except:
                    differs = True
                    coherence_threshold_value_checked = 0.2
                parameters.put(key, coherence_threshold_value_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "FFTSizeString": # str int
                try:
                    fft_size = str(int(float(kwargs[key]))) if str(int(float(kwargs[key]))) in valid_fft_size_string else "64"  # default value
                    differs = False if fft_size == str(int(float(kwargs[key]))) else True
                except:
                    differs = True
                    fft_size = "64"  # default value
                parameters.put(key, fft_size)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "useCoherenceMask": # boolean
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "windowSizeString": # str int
                try:
                    window_size = str(int(float(kwargs[key]))) if str(int(float(kwargs[key]))) in valid_window_size_string else "3"  # default value
                    differs = False if window_size == str(int(float(kwargs[key]))) else True
                except:
                    differs = True
                    window_size = "3"  # default value
                parameters.put(key, window_size)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply GoldsteinPhaseFiltering
    goldstein_phase_filtering = snappy.GPF.createProduct("GoldsteinPhaseFiltering", parameters, product)
    print(colored("GoldsteinPhaseFiltering successfully applied", "green"))
    return goldstein_phase_filtering

# Interferogram (Tested)
def compute_interferogram(product, **kwargs):
    '''
    Function to obtain the Interferogram from a geocoding SAR Product from a coregistered product

    SNAP Help
    This operator computes (complex) interferogram, with subtraction of the flat-earth (reference) phase (can also be run without).
    The flat-earth phase is the phase present in the interferometric signal due to the curvature of the reference surface (WGS84).

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product - coregistered (e.g. back geocoding)
        kwargs     dict                           Options

    kwargs Options:
        cohWinAz                    int      Size of coherence estimation window in Azimuth direction. Default value is '10'.
        cohWinRg                    int      Size of coherence estimation window in Range direction. Default value is '10'.
        demName                     str      The digital elevation model. Default value is 'SRTM 3Sec'.
        externalDEMApplyEGM         bool     Sets parameter 'externalDEMApplyEGM' to <boolean>. Default value is 'True'.
        externalDEMFile             os       Sets parameter 'externalDEMFile' to <file>.
        externalDEMNoDataValue      float    Sets parameter 'externalDEMNoDataValue' to <double>. Default value is '0'.
        includeCoherence            bool     Sets parameter 'includeCoherence' to <boolean>. Default value is 'True'.
        orbitDegree                 int      Degree of orbit (polynomial) interpolator. Value must be one of '1', '2', '3', '4', '5'. Default value is '3'.
        outputElevation             bool     Sets parameter 'outputElevation' to <boolean>. Default value is 'False'.
        outputLatLon                bool     Sets parameter 'outputLatLon' to <boolean>. Default value is 'False'.
        squarePixel                 bool     Use ground square pixel. Default value is 'True'.
        srpNumberPoints             int      Number of points for the 'flat earth phase' polynomial estimation.
                                             Value must be one of '301', '401', '501', '601', '701', '801', '901', '1001'.
                                             Default value is '501'.
        srpPolynomialDegree         int      Order of 'Flat earth phase' polynomial. Value must be one of '1', '2', '3', '4', '5', '6', '7', '8'.
                                             Default value is '5'.
        subtractFlatEarthPhase      bool     Sets parameter 'subtractFlatEarthPhase' to <boolean>. Default value is 'True'.
        subtractTopographicPhase    bool     Sets parameter 'subtractTopographicPhase' to <boolean>. Default value is 'False'.
        tileExtensionPercent        str      Define extension of tile for DEM simulation (optimization parameter). Default value is '100'.

    Returns:
        interferogram    snap.core.datamodel.Product    Interferogram
    '''
    valid_operator_parameters = ["cohWinAz", "cohWinRg", "demName", "externalDEMApplyEGM", "externalDEMFile", "externalDEMNoDataValue", "includeCoherence",
                                 "orbitDegree", "outputElevation", "outputLatLon", "squarePixel", "srpNumberPoints", "srpPolynomialDegree", "subtractFlatEarthPhase",
                                 "subtractTopographicPhase", "tileExtensionPercent"]
    valid_dem_name = ["ACE2_5Min", "ACE30", "ASTER 1 Sec GDEM", "CDEM", "Copernicus 30m Global DEM", "Copernicus 90m Global DEM", "GETASSE30",
                      "SRTM 1Sec Grid", "SRTM 1Sec HGT","SRTM 3Sec", "External DEM"]
    valid_orbit_degree = [1, 2, 3, 4, 5] # Default value is 3
    valid_srp_number_points = [301, 401, 501, 601, 701, 801, 901, 1001] # Default 501
    valid_srp_polynomial_degree = [1, 2, 3, 4, 5, 6, 7, 8] # Default 5
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key in ["cohWinAz", "cohWinRg"]: # int
                try:
                    coh_win_value = int(float((kwargs[key])))  # avoid error to cast "10."
                except:
                    coh_win_value = 10  # default
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, coh_win_value)
            elif key == "demName": # str
                # validate demName type str
                dem_name = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_dem_name else "SRTM 3Sec" # default value
                if dem_name != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, dem_name)
            elif key in ["externalDEMApplyEGM", "includeCoherence", "squarePixel", "subtractFlatEarthPhase"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else True  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["outputElevation", "outputLatLon", "subtractTopographicPhase"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "externalDEMFile": # path
                if os.path.exists(kwargs[key]):
                    parameters.put(key, kwargs[key])
                else:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} has been ingnored since the path does not exist.", "yellow"))
            elif key == "externalDEMNoDataValue": # float
                try:
                    external_dem_no_data_value = float(kwargs[key])
                except:
                    external_dem_no_data_value = 0. # default value
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, external_dem_no_data_value)
            elif key == "orbitDegree": # int
                try:
                    orbit_degree_checked = int(float(kwargs[key])) if int(float(kwargs[key])) in valid_orbit_degree else 3 # default
                    differs = False if orbit_degree_checked == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    orbit_degree_checked = 3 # default
                parameters.put(key, orbit_degree_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "srpNumberPoints": # int
                try:
                    number_points_checked = int(float(kwargs[key])) if int(float(kwargs[key])) in valid_srp_number_points else 501
                    differs = False if number_points_checked == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    number_points_checked = 501 # default
                parameters.put(key, number_points_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))

            elif key == "srpPolynomialDegree": # int
                try:
                    poly_degree_checked = int(float(kwargs[key])) if int(float(kwargs[key])) in valid_srp_polynomial_degree else 5
                    differs = False if poly_degree_checked == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    poly_degree_checked = 5 # default
                parameters.put(key, poly_degree_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "tileExtensionPercent": # str
                try:
                    tile_extension_percent = str(kwargs[key])
                except:
                    tile_extension_percent = "100"
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, tile_extension_percent)
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # obtain the Interferogram
    interferogram = snappy.GPF.createProduct("Interferogram", parameters, product)
    print(colored("Interferogram successfully obtained", "green"))
    return interferogram

# Multilook (Tested)
def compute_multilook(product, **kwargs):
    '''
    Function to compute the Multilook Operator to a SNAP Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        grSquarePixel      bool, str    Use ground square pixel. Default value is 'True'.
        nAzLooks           int, str     The user defined number of azimuth looks. Valid interval is [1, *). Default value is '1'.
        nRgLooks           int          The user defined number of range looks. Valid interval is [1, *). Default value is '1'.
        outputIntensity    bool, str    For complex product output intensity or i and q. Default value is 'false'.
        sourceBands        str          "str, str,str,...". The list of source bands.
    Returns:
        multilook    snap.core.datamodel.Product    SNAP Product after Multilook
    '''
    valid_operator_parameters = ["grSquarePixel", "nAzLooks", "nRgLooks", "outputIntensity", "sourceBands"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    #update parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "grSquarePixel": # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else True  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["nAzLooks", "nRgLooks"]: # int
                try:
                    n_looks_value = int(float(kwargs[key])) if int(float(kwargs[key]))>=1 else 1
                    differs = False if n_looks_value == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    n_looks_value = 1 # default
                parameters.put(key, n_looks_value)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "outputIntensity": # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "sourceBands":
                if isinstance(kwargs[key], str):
                    input_band_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_band_names:
                        if not product.containsBand(band):
                            raise Exception(colored(f"The input product band {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply Multilook
    multilook = snappy.GPF.createProduct("Multilook", parameters, product)
    print(colored("Multilook successfully applied", "green"))
    return multilook

# PhaseToDisplacement?

# Speckle-Filter
def compute_speckle_filtering(product, **kwargs):
    '''
    Function to apply the Speckle Filtering to a SNAP Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        anSize                 int, str      The Adaptive Neighbourhood size. Valid interval is (1, 200].
                                             Default value is '50'.
        dampingFactor          int, str      The damping factor (Frost filter only). Valid interval is (0, 100].
                                             Default value is '2'.
        enl                    float, str    The number of looks. Valid interval is (0, *).
                                             Default value is '1.0'.
        estimateENL            bool, str     Sets parameter 'estimateENL' to bool.
                                             Default value is 'False'.
        filter                 str           Sets parameter 'filter' to str. Value must be one of 'None', 'Boxcar', 'Median', 'Frost',
                                             'Gamma Map', 'Lee', 'Refined Lee', 'Lee Sigma', 'IDAN'.
                                             Default value is 'Lee Sigma'.
        filterSizeX            int, str      The kernel x dimension. Valid interval is (1, 100].
                                             Default value is '3'.
        filterSizeY            int, str      The kernel y dimension. Valid interval is (1, 100].
                                             Default value is '3'.
        numLooksStr            str, int      Sets parameter 'numLooksStr' to str. Value must be one of '1', '2', '3', '4'.
                                             Default value is '1'.
        sigmaStr               str, float    Sets parameter 'sigmaStr' to str. Value must be one of '0.5', '0.6', '0.7', '0.8', '0.9'.
                                             Default value is '0.9'.
        sourceBands            str           "str,str,str,...". The list of source bands.
        targetWindowSizeStr    str           Sets parameter 'targetWindowSizeStr' to str. Value must be one of '3x3', '5x5'.
                                             Default value is '3x3'.
        windowSize             str           Sets parameter 'windowSize' to str. Value must be one of '5x5', '7x7', '9x9', '11x11', '13x13', '15x15', '17x17'.
                                             Default value is '7x7'.
    Returns:
        speckle    snap.core.datamodel.Product    SNAP Product after speckle filtering
    '''
    valid_operator_parameters = ["anSize", "dampingFactor", "enl", "estimateENL", "filter", "filterSizeX", "filterSizeY", "numLooksStr",
                                "sigmaStr", "sourceBands", "targetWindowSizeStr", "windowSize"]
    valid_filer_option = ["None", "Boxcar", "Median", "Frost", "Gamma Map", "Lee", "Refined Lee", "Lee Sigma", "IDAN"]
    valid_num_look_str = ["1", "2", "3", "4"]
    valid_sigma_str = ["0.5", "0.6", "0.7", "0.8", "0.9"]
    valid_target_window_size_str = ['3x3', '5x5']
    valid_window_size = ['5x5', '7x7', '9x9', '11x11', '13x13', '15x15', '17x17']
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            #print(key, kwargs[key])
            if key == "anSize":
                # validate An Size Option
                an_size_value = int(kwargs[key]) if 1 < int(kwargs[key]) <= 200 else 50 # default value
                if an_size_value != int(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is out of range (1,200]. The default value for the {key} parameter has been set.", "yellow"))
                #print(an_size_value)
                parameters.put(key, an_size_value)
                # raise an Exception
                #if 1 < int(kwargs[key]) <= 200:
                #    parameters.put(key, int(kwargs[key]))
                #else:
                #    raise Exception(colored(f"The input anSize {kwargs[key]} is out of range (1,200]", "yellow"))
            elif key == "dampingFactor":
                # validate An Size Option
                damping_factor_value = int(kwargs[key]) if 0 < int(kwargs[key]) <= 100 else 2 # default value
                if damping_factor_value != int(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is out of range (0,100]. The default value for the {key} parameter has been set.", "yellow"))
                #print(an_size_value)
                parameters.put(key, damping_factor_value)
            elif key == "enl":
                # validate enl Option
                enl_value = float(kwargs[key]) if 0 < float(kwargs[key]) else 1.0 # default value
                if enl_value != float(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is out of range (0,*). The default value for the {key} parameter has been set.", "yellow"))
                #print(enl_value)
                parameters.put(key, enl_value)
            elif key == "filter":
                # validate Aux File Option
                filter_name = kwargs[key] if kwargs[key] in valid_filer_option else "Lee Sigma" # default value
                if filter_name != kwargs[key]:
                    print(colored(f"Warning!. The input {key} name {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(filter_name)
                parameters.put(key, filter_name)
            elif key in ["filterSizeX", "filterSizeY"]:
                # validate filterSize Option
                filter_size_value = int(kwargs[key]) if 1 < int(kwargs[key]) <= 100 else 3 # default value
                if filter_size_value != int(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is out of range (0,100]. The default value for the {key} parameter has been set.", "yellow"))
                #print(filter_size_value)
                parameters.put(key, filter_size_value)
            elif key == "numLooksStr":
                # validate numLooksStr Option
                num_looks_str = str(kwargs[key]) if str(kwargs[key]) in valid_num_look_str else "1" # default value
                if num_looks_str != str(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid {valid_num_look_str}. The default value for the {key} parameter has been set.", "yellow"))
                #print(num_looks_str)
                parameters.put(key, num_looks_str)
            elif key == "sigmaStr":
                # validate sigmaStr Option
                sigma_str = str(kwargs[key]) if str(kwargs[key]) in valid_sigma_str else "0.9" # default value
                if sigma_str != str(kwargs[key]):
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid {valid_sigma_str}. The default value for the {key} parameter has been set.", "yellow"))
                #print(sigma_str)
                parameters.put(key, sigma_str)
            elif key == "sourceBands":
                if isinstance(kwargs[key], str):
                    input_band_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_band_names:
                        if not product.containsBand(band):
                            raise Exception(colored(f"The input product band {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            elif key == "targetWindowSizeStr":
                # validate targetWindowSizeStr Option
                target_window_str = kwargs[key] if kwargs[key] in valid_target_window_size_str else "3x3" # default value
                if target_window_str != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid {valid_target_window_size_str}. The default value for the {key} parameter has been set.", "yellow"))
                #print(target_window_str)
                parameters.put(key, target_window_str)
            elif key == "windowSize":
                # validate targetWindowSizeStr Option
                window_str = kwargs[key] if kwargs[key] in valid_window_size else "7x7" # default value
                if window_str != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid {valid_window_size}. The default value for the {key} parameter has been set.", "yellow"))
                #print(window_str)
                parameters.put(key, window_str)
            else:
                parameters.put(key, kwargs[key])
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply speckle filter
    speckle = snappy.GPF.createProduct("Speckle-Filter", parameters, product)
    print(colored("Speckle Filtering successfully applied", "green"))
    return speckle

# StampsExport (Fails)
def export_snap_product_to_stamps(coregistered_stack, interferogram_stack, **kwargs):
    '''
    Funtion to export a SNAP Product to StaMPS

    Parameters:
        coregistered_ref_sec_product    snap.core.datamodel.Product    Coregistered SLC stack with a reference image and at least 4 secondary images
        interferogram                   snap.core.datamodel.Product    Interferogram for reference/secondary pairs and an elevation band
        kwargs                          dict                           Options

    kwargs Options:
        psiFormat       bool    Format for PSI or SBAS. Default value is 'True'. (False, SBAS, but not supported yet)
        targetFolder    os      <file>. The output folder to which the data product is written.

    '''
    valid_operator_parameters = ["psiFormat", "targetFolder"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})

    if "targetFolder" not in kwargs.keys():
        raise Exception(colored(f"Please add a target folder.", "yellow")) # targetFolder parameter is mandatory

    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "psiFormat": # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else True  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "targetFolder": # path
                if os.path.exists(kwargs[key]):
                    target_folder = kwargs[key]
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} {kwargs[key]} path does not exist.", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # StampsExport
    snappy.GPF.createProduct("StampsExport", parameters, [interferogram_stack, coregistered_stack]) # list change order
    print(colored(f"SNAP Product successfully exported to StaMPS to folder --> {target_folder}", "green"))

# Subset (Tested)
def create_subset_from_sar_product(product, **kwargs):
    '''
    Function to create a spatial and/or spectral subset of a given SAR product

    Parameters:
        product    snap.core.datamodel.Product    SNAP product
        kwargs     dict                           Options

    kwargs Options:
        copyMetadata    bool    Whether to copy the metadata of the source product.
                                Default value is 'False'.
        fullSwath       bool    Forces the operator to extend the subset region to the full swath.
                                Default value is 'False'.
        geoRegion       str     The subset region in geographical coordinates using WKT-format,
                                e.g. POLYGON((<lon1> <lat1>, <lon2> <lat2>, ..., <lon1> <lat1>))
                                (make sure to quote the option due to spaces in <geometry>).
                                If not given, the entire scene is used.
        referenceBand   str     The band used to indicate the pixel coordinates.
        region          str     The subset region in pixel coordinates. Use the following format: <x>,<y>,<width>,<height>
                                If not given, the entire scene is used. The 'geoRegion' parameter has precedence over this parameter.
        sourceBands     str     "str,str,str,...". The list of source bands.
        subSamplingX    int     The pixel sub-sampling step in X (horizontal image direction)
                                Default value is '1'.
        subSamplingY    int     The pixel sub-sampling step in Y (vertical image direction)
                                Default value is '1'.
        tiePointGrids   str     "str,str,str,...". The list of tie-point grid names.

    Returns:
        subset    snap.core.datamodel.Product    SNAP Product after applying the subset
    '''
    valid_operator_parameters = ["copyMetadata", "fullSwath", "geoRegion", "referenceBand", "region", "sourceBands", "subSamplingX", "subSamplingY", "tiePointGrids"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key in ["copyMetadata", "fullSwath"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["geoRegion", "region"]: # str
                if isinstance(kwargs[key], str):
                    parameters.put(key, kwargs[key]) # "geoRegion", "region" parameters are validated directly by snappy
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            elif key == "referenceBand": # str
                if isinstance(kwargs[key], str):
                    if not product.containsBand(kwargs[key]):
                        raise Exception(colored(f"The input product reference band {kwargs[key]} is not in the input SAR product", "yellow"))
                    else:
                        parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            elif key == "sourceBands": # list as str
                if isinstance(kwargs[key], str):
                    input_band_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_band_names:
                        print(band)
                        if not product.containsBand(band):
                            raise Exception(colored(f"The input product band {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            elif key in ["subSamplingX",  "subSamplingY"]: # int, float, valid str
                try:
                    sub_sampling_value = int(float((kwargs[key]))) # avoid error to cast "10."
                    differs = False if sub_sampling_value == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    sub_sampling_value = 1 # default
                parameters.put(key, sub_sampling_value)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "tiePointGrids": # str
                if isinstance(kwargs[key], str):
                    input_tie_point_grid_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_tie_point_grid_names:
                        if not product.containsTiePointGrid(band):
                            raise Exception(colored(f"The input product tie-point grid {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply subset
    subset = snappy.GPF.createProduct("Subset", parameters, product)
    print(colored("Subset successfully applied", "green"))
    return subset

# Terrain-Correction
def compute_terrain_correction(product, **kwargs):
    '''
    Function to apply the Terrain Correction to a SNAP product

    Parameters:
        product    snap.core.datamodel.Product    SNAP product
        kwargs     dict                           Options

    kwargs Options:
        alignToStandardGrid                 bool, str     Force the image grid to be aligned with a specific point.
                                                          Default value is 'False'.
        applyRadiometricNormalization       bool, str     Sets parameter 'applyRadiometricNormalization' to bool.
                                                          Default value is 'False'.
        auxFile                             str           The auxiliary file. Value must be one of 'Latest Auxiliary File', 'Product Auxiliary File',
                                                          'External Auxiliary File'.
                                                          Default value is 'Latest Auxiliary File'.
        demName                             str           The digital elevation model.
                                                          Default value is 'SRTM 3Sec'.
        demResamplingMethod                 str           Sets parameter 'demResamplingMethod' to str.
                                                          Value must be one of 'NEAREST_NEIGHBOUR', 'BILINEAR_INTERPOLATION', 'CUBIC_CONVOLUTION',
                                                          'BISINC_5_POINT_INTERPOLATION', 'BISINC_11_POINT_INTERPOLATION', 'BISINC_21_POINT_INTERPOLATION',
                                                          'BICUBIC_INTERPOLATION', 'DELAUNAY_INTERPOLATION'.
                                                          Default value is 'BILINEAR_INTERPOLATION'.
        externalAuxFile                     file          The antenne elevation pattern gain auxiliary data file.
        externalDEMApplyEGM                 bool, str     Sets parameter 'externalDEMApplyEGM' to bool.
                                                          Default value is 'True'.
        externalDEMFile                     file          Sets parameter 'externalDEMFile' to file.
        externalDEMNoDataValue              float, str    Sets parameter 'externalDEMNoDataValue' to double.
                                                          Default value is '0'.
        imgResamplingMethod                 str           Sets parameter 'imgResamplingMethod' to str. Value must be one of 'NEAREST_NEIGHBOUR',
                                                          'BILINEAR_INTERPOLATION', 'CUBIC_CONVOLUTION', 'BISINC_5_POINT_INTERPOLATION',
                                                          'BISINC_11_POINT_INTERPOLATION', 'BISINC_21_POINT_INTERPOLATION', 'BICUBIC_INTERPOLATION'.
                                                          Default value is 'BILINEAR_INTERPOLATION'.
        incidenceAngleForGamma0             str           Sets parameter 'incidenceAngleForGamma0' to str. Value must be one of
                                                          'Use incidence angle from Ellipsoid', 'Use local incidence angle from DEM',
                                                          'Use projected local incidence angle from DEM'.
                                                          Default value is 'Use projected local incidence angle from DEM'.
        incidenceAngleForSigma0             str           Sets parameter 'incidenceAngleForSigma0' to str. Value must be one of
                                                          'Use incidence angle from Ellipsoid', 'Use local incidence angle from DEM',
                                                          'Use projected local incidence angle from DEM'.
                                                          Default value is 'Use projected local incidence angle from DEM'.
        mapProjection                       str           The coordinate reference system in well known text format.
                                                          Default value is 'WGS84(DD)'.
        nodataValueAtSea                    bool, str     Mask the sea with no data value (faster).
                                                          Default value is 'true'.
        outputComplex                       bool, str     Sets parameter 'outputComplex' to bool.
                                                          Default value is 'False'.
        pixelSpacingInDegree                float, str    The pixel spacing in degrees.
                                                          Default value is '0'.
        pixelSpacingInMeter                 float, str    The pixel spacing in meters.
                                                          Default value is '0'.
        saveBetaNought                      bool, str     Sets parameter 'saveBetaNought' to bool.
                                                          Default value is 'False'.
        saveDEM                             bool, str     Sets parameter 'saveDEM' to bool.
                                                          Default value is 'False'.
        saveGammaNought                     bool, str     Sets parameter 'saveGammaNought' to bool.
                                                          Default value is 'False'.
        saveIncidenceAngleFromEllipsoid     bool, str     Sets parameter 'saveIncidenceAngleFromEllipsoid' to bool.
                                                          Default value is 'False'.
        saveLatLon                          bool, str     Sets parameter 'saveLatLon' to bool.
                                                          Default value is 'False'.
        saveLayoverShadowMask               bool, str     Sets parameter 'saveLayoverShadowMask' to bool.
                                                          Default value is 'False'.
        saveLocalIncidenceAngle             bool, str     Sets parameter 'saveLocalIncidenceAngle' to bool.
                                                          Default value is 'False'.
        saveProjectedLocalIncidenceAngle    bool, str     Sets parameter 'saveProjectedLocalIncidenceAngle' to bool.
                                                          Default value is 'False'.
        saveSelectedSourceBand              bool          Sets parameter 'saveSelectedSourceBand' to bool.
                                                          Default value is 'True'.
        saveSigmaNought                     bool          Sets parameter 'saveSigmaNought' to bool.
                                                          Default value is 'False'.
        sourceBands                         str           "str,str,str,...". The list of source bands.
        standardGridOriginX                 float, str    x-coordinate of the standard grid's origin point
                                                          Default value is '0'.
        standardGridOriginY                 float, str    y-coordinate of the standard grid's origin point
                                                          Default value is '0'.

    Returns:
        terrain_correction    snap.core.datamodel.Product    SNAP Product after terrain correction
    '''
    valid_operator_parameters = ["alignToStandardGrid", "applyRadiometricNormalization", "auxFile", "demName", "demResamplingMethod",
                                "externalAuxFile", "externalDEMApplyEGM", "externalDEMFile", "externalDEMNoDataValue", "imgResamplingMethod",
                                "incidenceAngleForGamma0", "incidenceAngleForSigma0", "mapProjection", "nodataValueAtSea", "outputComplex",
                                "pixelSpacingInDegree", "pixelSpacingInMeter", "saveBetaNought", "saveDEM", "saveGammaNought",
                                "saveIncidenceAngleFromEllipsoid", "saveLatLon", "saveLayoverShadowMask", "saveLocalIncidenceAngle",
                                "saveProjectedLocalIncidenceAngle", "saveSelectedSourceBand", "saveSigmaNought", "sourceBands",
                                "standardGridOriginX", "standardGridOriginY"]
    valid_aux_file_options = ["Latest Auxiliary File", "Product Auxiliary File", "External Auxiliary File"]
    valid_dem_name = ["ACE2_5Min", "ACE30", "ASTER 1 Sec GDEM", "CDEM", "Copernicus 30m Global DEM", "Copernicus 90m Global DEM", "GETASSE30",
                      "SRTM 1Sec Grid", "SRTM 1Sec HGT","SRTM 3Sec", "External DEM"]
    valid_dem_resampling_method = ["NEAREST_NEIGHBOUR", "BILINEAR_INTERPOLATION", "CUBIC_CONVOLUTION", "BISINC_5_POINT_INTERPOLATION",
                                   "BISINC_11_POINT_INTERPOLATION", "BISINC_21_POINT_INTERPOLATION", "BICUBIC_INTERPOLATION", "DELAUNAY_INTERPOLATION"]
    valid_img_resampling_method = ["NEAREST_NEIGHBOUR", "BILINEAR_INTERPOLATION", "CUBIC_CONVOLUTION", "BISINC_5_POINT_INTERPOLATION",
                                   "BISINC_11_POINT_INTERPOLATION", "BISINC_21_POINT_INTERPOLATION", "BICUBIC_INTERPOLATION"]
    valid_incidence_angle_for_gamma0 = ["Use incidence angle from Ellipsoid', 'Use local incidence angle from DEM", "Use projected local incidence angle from DEM"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            print(key, kwargs[key])
            if key == "auxFile":
                # validate Aux File Option
                aux_file = kwargs[key] if kwargs[key] in valid_aux_file_options else 'Latest Auxiliary File' # default value
                if aux_file != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(aux_file)
                parameters.put(key, aux_file)
            elif key == "demName":
                # validate demName type str
                dem_name = kwargs[key] if kwargs[key] in valid_dem_name else "SRTM 3Sec" # default value
                if dem_name != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, dem_name)
            elif key =="demResamplingMethod":
                dem_resamplign_method = kwargs[key] if kwargs[key] in valid_dem_resampling_method else "BILINEAR_INTERPOLATION" # default value
                if dem_resamplign_method != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(dem_resamplign_method)
                parameters.put(key, dem_resamplign_method)
            elif key =="imgResamplingMethod":
                img_resamplign_method = kwargs[key] if kwargs[key] in valid_img_resampling_method else "BILINEAR_INTERPOLATION" # default value
                if img_resamplign_method != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(img_resamplign_method)
                parameters.put(key, img_resamplign_method)
            elif key in ["incidenceAngleForGamma0", "incidenceAngleForSigma0"]:
                incidence_angle_for_gamma0 = kwargs[key] if kwargs[key] in valid_incidence_angle_for_gamma0 else "Use projected local incidence angle from DEM" # default value
                if incidence_angle_for_gamma0 != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                #print(incidence_angle_for_gamma0)
                parameters.put(key, incidence_angle_for_gamma0)
            elif key == "sourceBands":
                if isinstance(kwargs[key], str):
                    input_band_names = kwargs[key].replace(" ", "").split(",")
                    for band in input_band_names:
                        if not product.containsBand(band):
                            raise Exception(colored(f"The input product band {band} is not in the input SAR product", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            else:
                parameters.put(key, kwargs[key])
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    terrain_correction = snappy.GPF.createProduct("Terrain-Correction", parameters, product)
    print(colored("Terrain-Correction successfully applied", "green"))
    return terrain_correction

# ThermalNoiseRemoval
# kwargs= {"outputNoise": bool, "reIntroduceThermalNoise": bool, "removeThermalNoise": bool, "selectedPolarisations": "<str,str,str,...>"}
def compute_thermal_noise_removal(product, **kwargs):
    '''
    Function to apply the Thermal Noise Removal to a SNAP product

    Parameters:
        product    snap.core.datamodel.Product    SNAP product
        kwargs     dict                           Options

    kwargs Options:
        outputNoise                bool, str    Default value is 'False'.
        reIntroduceThermalNoise    bool, str    Default value is 'False'.
        removeThermalNoise         bool, str    Default value is 'True'.
        selectedPolarisations      str          "str,str,str,...". The list of polarisations (as str).

    Returns:
        thermal_noise    snap.core.datamodel.Product    SNAP Product after thermal noise reduction
    '''
    valid_operator_parameters = ["outputNoise", "reIntroduceThermalNoise", "removeThermalNoise", "selectedPolarisations"]
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            #print(key, kwargs[key])
            if key == "selectedPolarisations":
                # get product polarization bands
                product_name = product.getName()
                product_info = aux.get_properties_from_product_name(product_name)
                polarization_mode = product_info["Polarization"]
                polarization_bands = aux.get_polarization_band_names(polarization_mode)
                #print("Product polarization bands : ", polarization_bands)
                # validate
                input_polarization_bands = kwargs[key].replace(" ", "").split(",")
                #for char in [" ", "list<", ">"]:
                #    input_polarization_bands_str = input_polarization_bands_str.replace(char, "")
                #input_polarization_bands = input_polarization_bands_str.split(",")
                for band in input_polarization_bands:
                    #print(band)
                    if band not in polarization_bands:
                        raise Exception(colored(f"The input polarization band {band} is not in the input SAR product", "yellow"))
                parameters.put(key, kwargs[key])
            else:
                parameters.put(key, kwargs[key])
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply thermal noise removal
    thermal_noise = snappy.GPF.createProduct("ThermalNoiseRemoval", parameters, product)
    print(colored("Thermal Noise Removal successfully applied", "green"))
    return thermal_noise

# TopoPhaseRemoval (Tested)
def compute_topo_phase_removal(product, **kwargs):
    '''
    Function to compute the TopoPhaseRemoval operator to a SAR Product

    SNAP Help
    This operator estimates and subtracts topographic phase from the interferogram. More specifically, this operator first "radarcodes" the
    Digital Elevation Model (DEM) of the area of interferogram, and then subtracts it from the complex interferogram.
    This operator must be performed after the interferogram generation. It also requires an input DEM, SRTM can be used, or any other supported
    DEM. The DEM handling for most of elevation models, selection and download from internet of tiles covering the area of interest, interpolation,
    accounting for geoid undulation, etc, is performed automatically by the operator itself.

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        demName                   str      The digital elevation model. Default value is 'SRTM 3Sec'.
        externalDEMFile           os       Sets parameter 'externalDEMFile' to <file>.
        externalDEMNoDataValue    float    Sets parameter 'externalDEMNoDataValue' to <double>. Default value is '0'.
        orbitDegree               int      Degree of orbit interpolation polynomial. Valid interval is (1, 10].
                                           Default value is '3'.
        outputElevationBand       bool     Output elevation band. Default value is 'False'.
        outputLatLonBands         bool     Output lat/lon bands. Default value is 'False'.
        outputTopoPhaseBand       bool     Output topographic phase band. Default value is 'False'.
        tileExtensionPercent      str      Define extension of tile for DEM simulation (optimization parameter).
                                           Default value is '100'.
    Returns:
        topo_phase_removal    snap.core.datamodel.Product    SNAP Product after TopoPhaseRemoval operator
    '''
    valid_operator_parameters = ["demName", "externalDEMFile", "externalDEMNoDataValue", "orbitDegree", "outputElevationBand",
                                 "outputLatLonBands", "outputTopoPhaseBand", "tileExtensionPercent"]
    valid_dem_name = ["ACE2_5Min", "ACE30", "ASTER 1 Sec GDEM", "CDEM", "Copernicus 30m Global DEM", "Copernicus 90m Global DEM", "GETASSE30",
                      "SRTM 1Sec Grid", "SRTM 1Sec HGT","SRTM 3Sec", "External DEM"]
    # create java dict
    parameters = snappy.HashMap()  # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "demName":
                # validate demName type str
                dem_name = kwargs[key] if isinstance(kwargs[key], str) and kwargs[key] in valid_dem_name else "SRTM 3Sec" # default value
                parameters.put(key, dem_name)
                if dem_name != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "externalDEMFile": # os path
                if os.path.exists(kwargs[key]):
                    parameters.put(key, kwargs[key])
                else:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} file has been ignored since the file does not exist.", "yellow"))
            elif key == "externalDEMNoDataValue":
                try:
                    external_dem_no_data_value = float(kwargs[key])
                except:
                    external_dem_no_data_value = 0. # default value
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, external_dem_no_data_value)
            elif key == "orbitDegree": # int in range (1, 10]
                try:
                    orbit_degree_checked = int(float(kwargs[key])) if 1 < int(float(kwargs[key])) <= 10 else 3 # default
                    differs = False if orbit_degree_checked == int(float((kwargs[key]))) else True
                except:
                    differs = True
                    orbit_degree_checked = 3 # default
                parameters.put(key, orbit_degree_checked)
                if differs:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
            elif key in ["outputElevationBand", "outputLatLonBands", "outputTopoPhaseBand"]: # bool
                bool_value = kwargs[key] if isinstance(kwargs[key], bool) else False  # default
                parameters.put(key, bool_value)
                if bool_value != kwargs[key]:
                    print(colored(f"Warning!. The input {key} {kwargs[key]} value is not a valid bool type. The default value for the {key} parameter has been set.", "yellow"))
            elif key == "tileExtensionPercent": # str
                try:
                    tile_extension_percent = str(kwargs[key])
                except:
                    tile_extension_percent = "100"
                    print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid. The default value for the {key} parameter has been set.", "yellow"))
                parameters.put(key, tile_extension_percent)
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply TopoPhaseRemoval
    topo_phase_removal = snappy.GPF.createProduct("TopoPhaseRemoval", parameters, product)
    print(colored("TopoPhaseRemoval successfully applied", "green"))
    return topo_phase_removal

# TOPSAR-Deburst (Tested)
def compute_topsar_deburst(product, **kwargs):
    '''
    Function to compute the TOPSAR-Deburst operator to a SAR Product

    SNAP Help
    This processor merges the bursts to a continuous image based on their zero Doppler time and removes the demarcation pixels.

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        selectedPolarisations    "str, str, str,..."    The list of polarisations

    Returns:
        topsar_deburst    snap.core.datamodel.Product    SNAP Product after TOPSAR-Deburst operator
    '''
    valid_operator_parameters = ["selectedPolarisations"]
    # create java dict
    parameters = snappy.HashMap()  # empty dict (the snap operator will use the default options if kwargs={})
    # update the parameters
    for key in kwargs.keys():
        if key in valid_operator_parameters:
            if key == "selectedPolarisations":
                if isinstance(kwargs[key], str):
                    # get product polarization bands
                    polarization_bands = aux.get_polarization_bands_from_sar_product(product)
                    # validate
                    input_polarization_bands = kwargs[key].replace(" ", "").split(",")
                    for band in input_polarization_bands:
                        if band not in polarization_bands:
                            raise Exception(colored(f"The input polarization band {band} is not in the input SAR product {polarization_bands}", "yellow"))
                    parameters.put(key, kwargs[key])
                else:
                    raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
        else:
            raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # apply TOPSAR-Deburst
    topsar_deburst = snappy.GPF.createProduct("TOPSAR-Deburst", parameters, product)
    print(colored("TOPSAR-Deburst successfully applied", "green"))
    return topsar_deburst

# TOPSAR-Split (Tested)
def compute_topsar_split(product, **kwargs):
    '''
    Function to compute the TOPSAR-split operator to a SAR Product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        firstBurstIndex          int    The first burst index. Valid interval is [1, *). Default value is '1'
        lastBurstIndex           int    The last burst index. Valid interval is [1, *). Default value is '9999'
        selectedPolarisations    str    "str,str,str,...". The list of polarisations
        subswath                 str    Source band.
        wktAoi                   str    WKT polygon to be used for selecting bursts

    Returns:
        topsar_split    snap.core.datamodel.Product    SNAP Product after TOPSAR-split operator
    '''
    valid_operator_parameters = ["firstBurstIndex", "lastBurstIndex", "selectedPolarisations", "subswath", "wktAoi"]
    if kwargs=={}: # TOPSAR-Split operator fails if the kwargs is an empty dict
        raise Exception(colored(f"The input kwargs cannot be an empty dict", "yellow"))
    else:
        # create java dict
        parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
        # update the parameters
        for key in kwargs.keys():
            if key in valid_operator_parameters:
                if key == "firstBurstIndex": # int
                    try:
                        first_burst_index = int(float((kwargs[key]))) if int(float((kwargs[key]))) >= 1 else 1 # int, float or valid str
                        differs = False if first_burst_index == int(float((kwargs[key]))) else True
                    except:
                        first_burst_index = 1 # default
                        differs = True
                    parameters.put(key, first_burst_index)
                    if differs:
                        print(colored(f"Warning!. The input {key} {kwargs[key]} is not valid or is out of range [1, *). The default value for the {key} parameter has been set.", "yellow"))
                elif key == "lastBurstIndex": # int
                    try:
                        # how to get the max number of bursts of a SAR Product?
                        last_burst_index = int(float((kwargs[key]))) if int(float((kwargs[key]))) >= 1 else 9999 # default fails
                        differs = False if last_burst_index == int(float((kwargs[key]))) else True
                    except:
                        last_burst_index = 9999
                        differs = True
                    parameters.put(key, last_burst_index)
                    if differs:
                        print(colored( f"Warning!. The input {key} {kwargs[key]} is not valid or is out of range [1, *). The default value for the {key} parameter has been set.", "yellow"))
                elif key == "selectedPolarisations": # list as str
                    if isinstance(kwargs[key], str):
                        # get product polarization bands
                        polarization_bands = aux.get_polarization_bands_from_sar_product(product)
                        # validate
                        input_polarization_bands = kwargs[key].replace(" ", "").split(",")
                        for band in input_polarization_bands:
                            if band not in polarization_bands:
                                raise Exception(colored(f"The input polarization band {band} is not in the input SAR product {polarization_bands}", "yellow"))
                        parameters.put(key, kwargs[key])
                    else:
                        raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
                elif key == "subswath": # str (only one allowed)
                    if isinstance(kwargs[key], str):
                        product_band_names = [b for b in product.getBandNames()]
                        product_subswath = aux.get_subswath_name_from_sar_band_names(product_band_names)
                        if kwargs[key] not in product_subswath:
                            raise Exception(colored(f"The input {key} {kwargs[key]} is not in the input SAR product {product_subswath}", "yellow"))
                        parameters.put(key, kwargs[key])
                elif key == "wktAoi":
                    if isinstance(kwargs[key], str):
                        parameters.put(key, kwargs[key])
                    else:
                        raise Exception(colored(f"The input {key} parameter is not a valid str", "yellow"))
            else:
                raise Exception(colored(f"The input {key} option is not a valid operator parameter {valid_operator_parameters}", "yellow"))
    # Apply TOPSAR-split
    topsar_split = snappy.GPF.createProduct("TOPSAR-Split", parameters, product)
    print(colored("TOPSAR-Split successfully applied", "green"))
    return topsar_split

# Fails (but this function is not required, since we can use the sar_processing.write_snap_product() function
def write_product(product, **kwargs):
    '''
    Function to write a SAR product

    Parameters:
        product    snap.core.datamodel.Product    SNAP Product
        kwargs     dict                           Options

    kwargs Options:
        clearCacheAfterRowWrite    bool, str    If true, the internal tile cache is cleared after a tile row has been written.
                                                Ignored if writeEntireTileRows=false. Default value is 'False'.
        deleteOutputOnFailure      bool, str    If true, all output files are deleted after a failed write operation.
                                                Default value is 'True'.
        file                       os            <file>. The output file to which the data product is written.
        formatName                 str          The name of the output file format. Default value is 'BEAM-DIMAP'.
        writeEntireTileRows        bool, str    If true, the write operation waits until an entire tile row is computed.
                                                Default value is 'False'.
    '''
    # create java dict
    parameters = snappy.HashMap() # empty dict (the snap operator will use the default options if kwargs={})
    # write product
    snappy.GPF.createProduct("Write", parameters, product)