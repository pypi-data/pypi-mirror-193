import asf_search as asf
import os
from termcolor import colored        # prints colored text

#kwargs = {"platform": asf.PLATFORM.SENTINEL1A, "processingLevel": asf.PRODUCT_TYPE.SLC, "flightDirection": asf.FLIGHT_DIRECTION.DESCENDING,
#              "intersectsWith": wkt, "asfFrame": 526, "start": date(2019, 11, 1), "end": date(2020, 11, 1)}

def search_sar_products_using_asf_api(**kwargs):
    '''
    Funtion to Search SAR Products using ASF Data Search API (using asf_search.search() method)

    ASF API documentation:
        https://docs.asf.alaska.edu/asf_search/searching/ # ASF Searh API documentation

    Parameters:
        kwargs    dict    ASF search parameters

    kwargs Options:
        platform              asf_search.PLATFORM.                      SENTINEL1A, SENINEL1B, SIRC, ALOS, ERS, ERS1, ERS2, JERS, RADARSAT, AIRSAR, SEASAT, SMAP, UAVSAR
        instrument            asf_search.INSTRUMENT.                    C_SAR, PALSAR, AVNIR_2
        absoluteOrbit         int, tuple or list (range of values)
        asfFrame              int, tuple or list (range of values)      This is primarily an ASF / JAXA frame reference. However, some platforms use other conventions.
                                                                        You may specify a single value, range of values, or a list of values.
                                                                        Values:    ERS, JERS, RADARSAT: ASF frames 0 to 900
                                                                                   ALOS PALSAR: JAXA frames 0 to 7200
                                                                                   SEASAT: ESA-like frames 208 to 3458
                                                                                   Sentinel-1: In-house values 0 to 1184
        beamMode              asf_search.BEAMMODE.                      IW, EW, S1, S2, S3, S4, S5, S6, WV, DSN, FBS, FBD, PLR, WB1, WB2, OBS, SIRC11, SIRC13, SIRC16,
                                                                        SIRC20, SLC, STD, POL, RPI, EH3, EH4, EH6, EL1, FN1, FN2, FN3, FN4, FN5, SNA, SNB, ST1, ST2,
                                                                        ST3, ST4, ST5, ST6, ST7, SWA, SWB, WD1, WD2, WD3
        beamSwath             str, list (str)                           Sample: "IW", ["IW","EW"]
        campaign              asf_search.PLATFORM.                      For a list of available campaigns, use the asf_search.campaigns() function.
                                                                        You must provide the desired platform.
        maxDoppler            float                                     Doppler provides an indication of how much the look direction deviates from the ideal perpendicular
                                                                        flight direction acquisition.
        minDoppler            float                                     Doppler provides an indication of how much the look direction deviates from the ideal perpendicular
                                                                        flight direction acquisition.
        maxFaradayRotation    float (int ?)                             Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed.
                                                                        One-way rotations exceeding 5° are likely to significantly reduce the accuracy of geophysical parameter
                                                                        recovery, such as forest biomass.
        minFaradayRotation    int (float ?)                             Rotation of the polarization plane of the radar signal impacts imagery. HH and HV signals become mixed.
                                                                        One-way rotations exceeding 5° are likely to significantly reduce the accuracy of geophysical parameter
                                                                        recovery, such as forest biomass.
        flightDirection       asf_search.FLIGHT_DIRECTION.              ASCENDING, DESCENDING
        flightLine            str
        frame                 int, tuple or list (range of values)      ESA-referenced frames are offered to give users a universal framing convention. Each ESA
                                                                        frame has a corresponding ASF frame assigned. You may specify a single value, range of values,
                                                                        or a list of values (Any number from 0 to 7200).
        groupID               str, list (str)                           List of specific group IDs. For some datasets, the group ID is the same as the scene name. For others,
                                                                        such as Sentinel-1, the group ID is unique for a group of scenes.
        lookDirection         str                                       R, RIGHT, L, LEFT
        offNadirAngle         float, tuple or list (range of values)    Off-nadir angles for ALOS PALSAR.
        polarization          asf_search.POLARIZATION.                  HH, VV, VV_VH, HH_HV, DUAL_HH, DUAL_VV, DUAL_HV, DUAL_VH, HH_3SCAN, HH_4SCAN, HH_5SCAN, QUAD,
                                                                        HH_VV, HH_HV_VH_VV, FULL, UNKNOWN
        processingLevel       asf_search.PRODUCT_TYPE.                  Level to which the data has been processed, also type of product.
                                                                        https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PRODUCT_TYPE.py
                                                                        Sentinel-1: GRD_HD, GRD_MD, GRD_MS, GRD_HS, GRD_FD, SLC, OCN, RAW, METADATA_GRD_HD,
                                                                        METADATA_GRD_MD, METADATA_GRD_MS, METADATA_GRD_HS, METADATA_SLC, METADATA_OCN, METADATA_RAW
        relativeOrbit         int, tuple or list (range of values)      Path or track of satellite during data acquisition.
                                                                        Values: ALOS: 1-671; ERS-1: 0-2410; ERS-2: 0-500; JERS-1: 0-658; RADARSAT-1: 0-342; SEASAT: 1-243;
                                                                        UAVSAR: various
        intersectsWith        str                                       Search by polygon, a line segment (“linestring”), or a point defined in 2-D Well-Known Text (WKT).
        processingDate        str                                       Sample: '2017-01-01T00:00:00UTC'
        start                 str, date                                 Date of data acquisition. Can be used in combination with 'end'. You may enter natural language dates,
                                                                        or a date and/or time stamp. All times are in UTC.
        end                   str, date                                 Date of data acquisition. Can be used in combination with 'end'. You may enter natural language dates,
                                                                        or a date and/or time stamp. All times are in UTC.
        season                list                                      Start and end day of year for desired seasonal range.
        stack_from_id         str                                       Input the scene name for which you wish to see baseline results.
        maxResults            int                                       Maximum number of data records to return.

    Returns
        asf_search_results    ASFSearchResults class                    SAR Products
    '''
    valid_operator_parameters = ["platform", "instrument", "absoluteOrbit", "asfFrame", "beamMode", "beamSwath", "campaign", "maxDoppler", "minDoppler",
                                 "maxFaradayRotation", "minFaradayRotation", "flightDirection", "flightLine", "frame", "groupID", "lookDirection",
                                 "offNadirAngle", "polarization", "processingLevel", "relativeOrbit", "intersectsWith", "processingDate", "start",
                                 "end", "season", "stack_from_id", "maxResults"]
    kwargs_keys = kwargs.keys()
    for key in kwargs_keys:
        if key not in valid_operator_parameters:
            raise Exception(colored(f"The input parameter {key} is not valid: {valid_operator_parameters}", "yellow"))

    asf_search_results = asf.search(**kwargs)
    print(colored(f"Total SAR Products found: {len(asf_search_results)}", "green"))
    return asf_search_results

def get_metadata_as_geojson_from_asf_search_results(asf_search_results):
    '''
    Function to get the metadata from the ASF search results

    Parameter:
        asf_search_results      ASFSearchResults class    SAR Products

    Returns:
        asf_results_metadata    dict                      Metadata as dict
    '''
    asf_results_metadata = asf_search_results.geojson()
    return asf_results_metadata

def get_url_list_from_asf_results_metadata(asf_results_metadata):
    '''
    Function to get the urls from a ASF Search Result (as metadata dict)

    Parameter:
        metadata_dict    dict    ASF Search Result class as dict (geojson)
    Returns:
        url_list         list    SAR Product urls
    '''
    url_list = [product["properties"]["url"] for product in asf_results_metadata["features"]]
    return url_list

def create_asf_session(username, password):
    '''
    Function to create a ASFSession class to download products (using asf.ASFSession().auth_with_creds() method)

    Session Authentication Options:
        https://docs.asf.alaska.edu/asf_search/downloading/

    Parameters:
        username    str
        password    str
    Returns:
        session    ASFSession class
    '''
    session = asf.ASFSession().auth_with_creds(username, password)
    return session

def download_sar_products(asf_search_results, output_path, user_session):
    '''
    Funtion to download all the products from a ASF Search Results object

    Parameters:
        asf_search_results    ASF Search Result    SAR Products
        output_path           os                   Output path
        user_session          ASFSession object    Authentication
    '''
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    print(colored("Downloading all the products found", "cyan"))
    try:
        asf_search_results.download(path=output_path, session=user_session) #, processes=simult_downl # Fails
        print(colored("SAR Products successfully downloaded", "green"))
    except:
        print(colored("SAR Products download failure. Please try again.", "green"))

def download_sar_products_from_url(url_list, output_path, user_session):
    '''
    Function to download list of SAR products from its url

    Parameter:
        url_list           list    SAR Product url
    Returns:
        url_failed_list    list    Failed downloading SAR Products
    '''
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    url_failed_list = []
    total_url = len(url_list)
    for i, url_link in enumerate(url_list):
        print(f"Downloading product ({(i+1)}/{total_url}): Url --> {url_link} ")
        try:
            asf.download_url(url=url_link, path=output_path, session=user_session)
            print(colored("Product successfully downloaded", "green"))
        except:
            url_failed_list.append(url_link)
            print(colored("Product not downloaded", "yellow"))
    if url_failed_list != []:
        print(f"Total failed urls {len(url_failed_list)}: {url_failed_list}")
    return url_failed_list