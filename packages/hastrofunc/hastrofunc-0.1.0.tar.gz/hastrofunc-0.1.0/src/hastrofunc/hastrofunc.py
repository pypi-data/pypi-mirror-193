import numpy as np
import matplotlib as mpl
import matplotlib.colors as colors
from PyAstronomy.pyasl.asl.astroTimeLegacy import precess
from astropy.io import fits
from astropy import constants as const
import gc

######
### XXXXXXXXX BROKEN, DO NOT USE!!!!!!!!!!!!!!
### Calculates v_LSR given RA and Dec (in degrees)
######
def lsr_vel(RA_deg, Dec_deg, equinox=2000):
    ## Precess the given RA, Dec to 1900
    ra1900_deg, dec1900 = precess(RA_deg, Dec_deg, equinox, 1900)
    ra1900 = ra1900_deg/15.
    
    ## Convert RA, Dec to radians
    ra = np.deg2rad(ra1900_deg)
    dec = np.deg2rad(dec1900)
    
    ## Get the X,Y,Z vector of the source at equinox 1900...
    xx = np.empty(3)
    xx[0] = np.cos(dec) * np.cos(ra)
    xx[1] = np.cos(dec) * np.sin(ra)
    xx[2] = np.sin(dec)
    
    ## Get the conventional LSR solar motion.
    ##	LSR MOVES WITH 20.000 KM/S TOWARDS ra1900, dec1900 = 18.000, 30.000
    ralsr = np.pi * 18./12.
    declsr = np.pi * 30./180.
    
    xxlsr = np.empty(3)
    xxlsr[0] = np.cos(declsr) * np.cos(ralsr)
    xxlsr[1] = np.cos(declsr) * np.sin(ralsr)
    xxlsr[2] = np.sin(declsr)
    
    vvlsr = xxlsr * 20.
    vvlsrsrc = np.sum(np.multiply(xx,vvlsr))
    delvlsr = -vvlsrsrc
    
    return delvlsr

######
### Calculates v_GSR given v_LSR, Galactic latitude, and Galactic longitude
######
def convert_lsr2gsr(v_LSR, Glat, Glon, MW_rot=220.):
    # v_LSR = LSR velocity (km/s)
    # Glat, Glon = Galactic latitude and longitude (degrees)
    # MW_rot = Assumed rotation velocity for the Milky Way (km/s)
    return v_LSR + (MW_rot*np.sin(np.deg2rad(Glon))*np.cos(np.deg2rad(Glat)))


######
### Create a gradient between two colors and return a color on that gradient determined by the mix parameter (a value between 0 and 1)
######
# c1, c2: any color name recognized by matplotlib
def mix_colors(c1, c2, mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
    
    ### Example:
    #c1='red'
    #c2='white'
    #n=10
    #fig, ax = plt.subplots(figsize=(8, 5))
    #for x in range(n+1):
    #    ax.axvline(x, color=colorFader(c1,c2,x/n), linewidth=4) 
    #ax.scatter(0,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=0.))
    #ax.scatter(5,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=0.5))
    #ax.scatter(10,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=1.))
    #plt.show()
    


######
### Return a truncated version of an existing colormap
######
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

    ### Example:
    # new_cmap = truncate_colormap(plt.get_cmap('viridis'), 0., 0.98)
    
    
######
### Stack QuaStar spectra from table
######  
def stack_quastar_spectra(input_table, objtype='',line='', stacktype='median'): # 'line' parameter is integer wavelength in Angstroms
    ### Check for valid input parameters
    if objtype == 'BHB':
        vel_key = 'BHB_vels_'+line+'A'
        flux_key = 'BHB_normflux'
    elif objtype == 'QSO':
        vel_key = 'QSO_binned_vels_'+line+'A'
        flux_key = 'QSO_binned_normflux'
    else:
        raise ValueError("Must specify objtype: 'BHB' or 'QSO'")
    if not any(line == validline for validline in ['1548','1550','1393','1402','1526','1608','1611','1670']):
    #if line == !('1548' or '1550' or '1393' or '1402' or '1526' or '1608' or '1611' or '1670'):
        raise ValueError("Must specify line parameter (integer wavelength in Angstroms) \n" + \
                        "Available ions: \n" + \
                         "C IV (1548, 1550) \n" + \
                         "Si IV (1393, 1402) \n" + \
                         "Si II (1526) \n" + \
                         "Fe II (1608, 1611) \n" + \
                         "Al II (1670)")
    ### Combine velocity arrays so they are the same for both lines, then use interpolation get the flux values and stack them
    # Create array that contains velocity values for all rows of the input table
    combined_vels = np.unique(np.concatenate([row[vel_key] for row in input_table]))
    # Initialize array for summing fluxes
    interpflux_sum = np.zeros(len(combined_vels))
    for row in input_table:
            # Interpolate so the line has corresponding flux values at every velocity
            interpflux_obj = np.interp(combined_vels, row[vel_key], row[flux_key], left=0, right=0) # Perform interpolation on this object using combined velocity array
            # Add the interpolated flux values to running sum
            interpflux_sum = np.vstack([interpflux_sum, interpflux_obj])
    if stacktype == 'mean':
        flux_stack = np.mean(interpflux_sum[1:],axis=0)
    elif stacktype == 'median':
        flux_stack = np.median(interpflux_sum[1:],axis=0)
    return combined_vels, flux_stack


######
### Get continuum-fit spectrum from FITS file
######
def get_spectrum(filename):
    """
    flux_line = fits.getdata(filename, ext=0)
    flux_error = fits.getdata(filename, ext=1)
    lambda_data = fits.getdata(filename, ext=2)
    flux_cont = fits.getdata(filename, ext=3)
    #"""
    with fits.open(filename, memmap=False) as hdul:
        flux_line = hdul[0].data
        flux_error = hdul[1].data
        lambda_data = hdul[2].data
        flux_cont = hdul[3].data
        for hdu in hdul:
#             del hdu_data
            del hdu.data
#         print(hdu.closed)
        gc.collect()
    return lambda_data, flux_line, flux_error, flux_cont

######
### Convert wavelength to velocity for a specific line
######
def convert_wave2vel(obs_wave, rest_wave, LSR_vel=0.):
    # Define constants
    c = const.c.to('km/s').value
    return (((obs_wave - rest_wave)/rest_wave) * c) - LSR_vel

    #obs_wave = ((vel + LSR_vel) * rest_wave / c) + rest_wave
    #(vel + LSR_vel)*(rest_wave/c) = (obs_wave-rest_wave)
    #(vel + LSR_vel)/c = (obs_wave-rest_wave)/rest_wave
    #vel + LSR_vel = ((obs_wave-rest_wave)/rest_wave)*c
    #return vel = (((obs_wave-rest_wave)/rest_wave)*c) - LSR_vel

######
### Convert velocity to wavelength for a specific line
######
def convert_vel2wave(vel, rest_wave, LSR_vel=0.):
    # Define constants
    c = const.c.to('km/s').value
    return ((vel + LSR_vel) * rest_wave / c) + rest_wave

######
### Convert velocity to redshift (approximation)
######
def convert_vel2z(vel):
    return vel/c

######
### Convert redshift to velocity (approximation)
######
def convert_z2vel(z):
    return z*c

######
### Convert rest wavelength to observed wavelength
######
def convert_restwave2obswave(rest_wave, z):
    return (z*rest_wave) + rest_wave

######
### Convert column density to equivalent width for a specific line
######    
def convert_N2EW(N, lambda_0, f):
    # N: column density [cm^-2; not the log value!]
    # lambda_0: rest wavelength of the line being measured [Angstroms]
    # f: oscillator strength of the line [dimensionless; 0<f<1]
    #
    # This is for the optically thin case only!
    return N * lambda_0**2 * f / 1.13e20

###### !!!!!!BROKEN?
### Propogate errors for addition or subtraction
######
def propogate_error_addsub(err_array):
    # err_array: numpy array of integer values being added (you cannot give the function an array of error arrays)
    #if np.any([type(el) != float for el in err_array]):
    #    raise ValueError('The input error array must contain floats!')
    err_array = np.array(err_array)
    # dQ = sqrt((da)^2 + (db)^2 + ... + (dy)^2 + (dz)^2)
    errs_squared = err_array**2
    dQ = np.sqrt(np.sum(errs_squared))
    return dQ

######
### Propogate errors for multiplication or division
######
def propogate_error_multdiv(err_array, val_array, final_val):
    # val_array: numpy array of values being multiplied
    # err_array: numpy array of errors on those values (must be the same length as val_array)
    # final_val: the result of the multiplication/division, to which the fractional error will be applied (float)
    val_array = np.array(val_array)
    err_array = np.array(err_array)
    # dQ/Q = sqrt((da/a)^2 + (db/b)^2 + ... + (dy/y)^2 + (dz/z)^2)
    err_fracs = err_array/val_array
    errs_squared = err_fracs**2
    dQ = np.sqrt(np.sum(errs_squared)) * abs(final_val)
    return dQ

######
### Propogate errors for exponentials
######
def propogate_error_exp(power, base, base_err, final_val): # all integers
    # power: power of the exponential (float)
    # base: value in the base of the exponent (float)
    # base_err: error of the value in the base of the exponent (float)
    # final_val: the result of the exponential operation, to which the fractional error will be applied (float)
    # dQ/Q = abs(n) * dx/abs(x) where Q=x^n
    err_frac = abs(power) * (base_err / abs(base))
    dQ = err_frac * abs(final_val)
    return dQ

######
### Propogate errors for log10
######
def propogate_error_log10(arg, arg_err): # all integers
    # arg: value in the logarithm (float)
    # arg_err: error of the value in the logarithm (float)
    # dQ = 0.434 * dx/x where Q=log10(x)
    dQ = 0.434 * (arg_err/arg)
    return dQ

######
### Calculate column density for a specific line
######
# This was adapted from IDL code passed on by Jess, and last used in Python 2 - may need updating
# Used this to measure logN on absorption-free region near NaI, CaII lines (which will then give an upper limit on column density sensitivity)
def calc_N(wave, spec, error, vrange, w0, f0,limit=2):
    # wave: wavelength array
    # spec: flux array
    # error: flux error array
    # vrange: 2-element list or array with lower, upper limits of velocity range
    # w0: central wavelength for measurement
    # f0: oscillator strength
    # limit: ???
    # Returns logN and error
    vv = (wave-w0) / w0 * 2.9979e5
    iv = (vv[1:] >= vrange[0]) & (vv[1:]<= vrange[1])
    #
    tau = -1. *np.log(spec)
    nv = tau / 2.654e-15 / f0 / w0 # in units cm^-2 / (km s^-2) column density per unit velocity
    n = nv[1:] * np.diff(vv) # column density per bin obtained by multiplying differential Nv by bin width
    col = np.sum(n[iv])
    #
    tauerr = error/spec
    nerr = tauerr[1:] / 2.654e-15 / f0 / w0 * np.diff(vv)
    colerr = np.sum((nerr[iv])**2)**0.5
    #
    print('Limit N = (',   '%e'%col, ') +/- ', '%e' %(colerr))
    print('Limit N = (',   np.log10(abs(col)), ') +/- ', np.log10(colerr))
    #
    return col, colerr

######
### Round to the nearest multiple of a given number
######
# Source: https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python
def roundtomultiple(x, base):
    # x: number you are rounding
    # base: number the output should be a multiple of (must be an integer)
    if round_direction == 'neutral':
        return base * round(x/base)
    elif round_direction == 'down':
        return base * int(x/base)
    elif round_direction == 'up':
        return base * (int(x/base)+1)
        
######
### Convert absolute and apparent magnitude to distance
######
def convert_mags2dist(M, m):
    return 10**((m - M + 5)/5)

######
### Convert Galactic coordinates to cylindrical coordinates
######
## Adapted from Enrico's code
def convert_galactic2cylindrical(l,b,D):
    # l, b are in radians here, D in kpc
    z  = D*np.sin(b)
    dp = D*np.cos(b)
    x  = RSun - dp*np.cos(l)
    y  = dp*np.sin(l)
    R  = np.sqrt(x**2+y**2)
    th = np.arctan2(y,x)
    return (R,th,z)

######
### Convert Galactic coordinates to Cartesian coordinates
######
## Adapted from Enrico's code
def convert_galactic2cartesian(l,b,D, angle='degrees'):
    if angle == 'degrees':
        l = np.deg2rad(l)
        b = np.deg2rad(b)
    # l, b are in radians here, D in kpc
    x  = D*np.cos(l)*np.cos(b)
    y  = D*np.sin(l)*np.cos(b)
    z  = D*np.sin(b)
    return (x,y,z)


# ## From Yong
# #############
# def vhelio2vlsr_Westmeier(vel_init, l_deg, b_deg, reverse=False, do_print=False):
#     '''
#     - from http://www.atnf.csiro.au/people/Tobias.Westmeier/tools_hihelpers.php
#     - l_deg:  should be in degree
#     - b_deg: should be in degree
#     - vel_init: velocity that need to be transformed
#     -          vel_init = vhelio if reverse = False
#     -          vel_init = vlsr   if reverse = True
#     - Favor this one than the other one from Rosolowsky
#     History:
#     YZ. created a while ago, use to have ra, dec conversion as well
#     03/16/2020, now only take l_deg, b_deg to avoid confusion
#     How to use:
#     vhelio2vlsr_Westmeier(vlsr, l_deg, b_deg, reverse=True)
#     vhelio2vlsr_Westmeier(vhelio, l_deg, b_deg, reverse=False)
#     '''
#     import numpy as np

#     l = np.radians(l_deg)
#     b = np.radians(b_deg)
#     # vlsr 00> vhelio
#     if reverse == True:
#         delv = -(9*np.cos(l)*np.cos(b)+12*np.sin(l)*np.cos(b)+7*np.sin(b))
#         v_final = vel_init+delv
#         if do_print == True:
#             print("Input: vlsr=%.2f km/s, l_deg=%.4f, b_deg=%.4f"%(vel_init, l_deg, b_deg))
#             print("Output: vhelio=%.2f km/s"%(v_final))
#     else:
#         delv = +9*np.cos(l)*np.cos(b)+12*np.sin(l)*np.cos(b)+7*np.sin(b)
#         v_final = vel_init+delv
#         if do_print == True:
#             print("Input: vhelio=%.2f km/s, l_deg=%.4f, b_deg=%.4f"%(vel_init, l_deg, b_deg))
#             print("Output: vlsr=%.2f km/s"%(v_final))

#     # print 'Velocity correction at this (RA, DEC) is (km/s): ', delv
#     return v_final

# ##########################

# Created using snippet from function above
# def get_LSR(l_deg, b_deg):
#     l = np.radians(l_deg)
#     b = np.radians(b_deg)
#     return -(9*np.cos(l)*np.cos(b)+12*np.sin(l)*np.cos(b)+7*np.sin(b))



# def hex_to_rgb(hex_string):
#     rgb = colors.hex2color(hex_string)
#     return tuple([int(255*x) for x in rgb])

# def rgb_to_hex(rgb_tuple):
#     return colors.rgb2hex([1.0*x/255 for x in rgb_tuple])

# def lighter(color, percent):
#     '''assumes color is rgb between (0, 0, 0) and (255, 255, 255)'''
#     color = np.array(color)
#     white = np.array([255, 255, 255])
#     vector = white-color
#     return color + vector * percent

# def darker(color, percent):
#     '''assumes color is rgb between (0, 0, 0) and (255, 255, 255)'''
#     color = np.array(color)
#     black = np.array([0,0,0])
#     vector = color-black
#     return color - vector * percent

# def prepend_line(file_name, line, col_line_char=''):
#     """ Insert given string as a new line at the beginning of a file """
#     # define name of temporary dummy file
#     dummy_file = file_name + '.bak'
#     # open original file in read mode and dummy file in write mode
#     with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
#         # Write given line to the dummy file
#         write_obj.write(line + '\n' + col_line_char)
#         # Read lines from original file one by one and append them to the dummy file
#         for index, line in enumerate(read_obj):
#             if (index == 0):
#                 line = line[len(col_line_char):] # This replaces the beginning of the first line in the file with some string (usually a comment character, since AstroPy Tables doesn't comment column lines in fixed width)
#             write_obj.write(line)
#     # remove original file
#     os.remove(file_name)
#     # Rename dummy file as the original file
#     os.rename(dummy_file, file_name)


# Submit issue request
# Function to find the array entry with the minimum absolute value
# *** add to hastrofunc ***

def minabsval(x):
    print(np.min(x[x > 0.]))
    if len(x) <= 1:
        return x
    else:
        if  np.min(x[x > 0.]) < np.min(np.abs(x[x < 0.])):
            return np.min(x[x > 0.])
        else:
            return np.max(x[x < 0.])

# To adapt from Yong's code:
# def gal2radec(l_deg, b_deg, do_print):
#     from astropy.coordinates import SkyCoord
#     import numpy as np
#     import astropy.units as u

#     gal_coord = SkyCoord(l=l_deg, b=b_deg, frame='galactic', unit=(u.deg, u.deg))
#     ra_deg = gal_coord.icrs.ra.deg
#     dec_deg = gal_coord.icrs.dec.deg

#     ra_hms = gal_coord.icrs.ra.to_string(u.hour)
#     dec_dms = gal_coord.icrs.dec.to_string(u.deg)

#     if do_print == True:
#         print(">> l, b =%.4f  %.4f"%(l_deg, b_deg))
#         print(">> ra, dec = %.4f  %.4f "%(ra_deg, dec_deg))
#         print(">> ra, dec = %s  %s"%(ra_hms, dec_dms))

#     return l_deg, b_deg, ra_deg, dec_deg, ra_hms, dec_dms

# def radec2gal(ra_deg, dec_deg, do_print=False):
#     """
#     input:
#     $ python radec2gal.py 30 50
#     or:
#     from yztools.radec2gal import radec2gal
#     radec2gal(ra_deg, dec_deg)
#     will return:
#     l_deg, b_deg, ra_deg, dec_deg, ra_hms, dec_dms, ms_l, ms_b
#     """
#     from astropy.coordinates import SkyCoord
#     import numpy as np
#     import astropy.units as u

#     gal_coord = SkyCoord(ra=ra_deg, dec=dec_deg,
#                          frame='icrs', unit=(u.deg, u.deg))
#     l_deg = gal_coord.galactic.l.deg
#     b_deg = gal_coord.galactic.b.deg

#     ra_deg = gal_coord.icrs.ra.deg
#     dec_deg = gal_coord.icrs.dec.deg

#     ra_hms = gal_coord.icrs.ra.to_string(u.hour)
#     dec_dms = gal_coord.icrs.dec.to_string(u.deg)

#     if do_print == True:
#         print(">> ra, dec = %.4f  %.4f "%(ra_deg, dec_deg))
#         print(">> ra, dec = %s  %s"%(ra_hms, dec_dms))
#         print(">> l, b =%.4f  %.4f"%(l_deg, b_deg))

#     ## bonus, also do ms transformation ##
#     from yztools.gal2mscoord import gal2mscoord
#     ms_l, ms_b = gal2mscoord(l_deg, b_deg)

#     res = {'l_deg': l_deg, 'b_deg': b_deg,
#            'ra_deg': ra_deg, 'dec_deg': dec_deg,
#            'ra_hms': ra_hms, 'dec_dms': dec_dms,
#            'ms_l': ms_l, 'ms_b': ms_b}

#     # return l_deg, b_deg, ra_deg, dec_deg, ra_hms, dec_dms, ms_l, ms_b
#     return res

# from astropy import constants as const
# import astropy.units as u
# from astropy.table import Table
# def lt_Voigt_profile(line, wave, logN, b, z):
#     """
#     line: e.g., 'SiIV 1393'
#     wave_AA: wavelength array values in unit of AA
#     """

#     import astropy.units as u
#     from linetools.spectralline import AbsLine
#     line_comp = AbsLine(trans=line)

#     line_comp.attrib['N'] = 10**logN*u.cm**(-2)
#     line_comp.attrib['b'] = b*u.km/u.s
#     line_comp.setz(z)

#     line_comp_voigt = line_comp.generate_voigt(wave=wave)

#     return line_comp_voigt


## From Enrico
# def convert_galactic2cylindrical(l,b,D):
#     # l, b are in radians here, D in kpc
#     z  = D*np.sin(b)
#     dp = D*np.cos(b)
#     x  = RSun - dp*np.cos(l)
#     y  = dp*np.sin(l)
#     R  = np.sqrt(x**2+y**2)
#     th = np.arctan2(y,x)
#     return (R,th,z)

# def convert_galactic2cartesian(l,b,D, angle='degrees'):
#     if angle == 'degrees':
#         l = np.deg2rad(l)
#         b = np.deg2rad(b)
#     # l, b are in radians here, D in kpc
#     x  = D*np.cos(l)*np.cos(b)
#     y  = D*np.sin(l)*np.cos(b)
#     z  = D*np.sin(b)
#     return (x,y,z)

## From Yong
# def extract_HI_from_cube(tar_ra, tar_dec, header, cube_data, radius_deg):
#     '''
#     tar_ra/tar_dec: the ra/dec for the sightline, in degree
#     radius_deg: the radius of the extraction area, in unit of degree
#           Note that, HI4PI's beamsize is 16 arcmin
#           and GALFA-HI's beamsize is 4 arcmin. 
#     '''
    
#     # get sky coordinate for the target
#     tar_coord = SkyCoord(ra=tar_ra*u.deg, dec=tar_dec*u.deg, frame='icrs')
#     print('Sightline: RA=%.2f, DEC=%.2f, l=%.2f, b=%.2f (degree)'%(tar_ra, tar_dec, 
#                                                                    tar_coord.galactic.l.degree, 
#                                                                    tar_coord.galactic.b.degree))
#     print('Extracted within radius: %.2f arcmin (%.2f deg)'%(radius_deg*60, radius_deg))
    
#     # parse the cube header information to get RA/DEC coordinators 
#     cube_ra, cube_dec, cube_vel = get_cubeinfo(header)
#     cube_coord = SkyCoord(ra=cube_ra*u.deg, dec=cube_dec*u.deg, frame='icrs')
#     print('Cube RA range: [%.2f, %.2f], DEC range: [%.2f, %.2f]'%(cube_ra[0, -1], 
#                                                                   cube_ra[0, 0], 
#                                                                   cube_dec[0, 0], 
#                                                                   cube_dec[-1, 0]))
    
#     # calculate the distance between the sightline and the whole cube
#     dist_coord = tar_coord.separation(cube_coord)
#     dist_deg = dist_coord.degree # distance in degree 
    
#     # this create a 2d mask of [Dec, RA]
#     within_r_2d = dist_deg<=radius_deg/2. # beam should be in unit of degree. 
#     print('2D MASK data shape: ', within_r_2d.shape)
    
#     # this creates a 3 mask of (Vhel, Dec, RA) so that we can use it to take out the spec within the search area 
#     within_r_3d = np.asarray([within_r_2d]*cube_vel.size)
#     print('3D MASK data shape: ', within_r_3d.shape)
    
#     # 3D mask shape should be the same as the data cube shape 
#     print('cube data shape: ', cube_data.shape)

#     # now mask the data 
#     data = cube_data.copy()
#     data[np.logical_not(within_r_3d)] = np.nan

#     # take the mean value along the Dec (axis=2) and the RA (axis=1) directions 
#     mean_spec = np.nanmean(np.nanmean(data, axis=2), axis=1)
    
#     return cube_vel, mean_spec
