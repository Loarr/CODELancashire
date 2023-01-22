def spherical_prism(power, decentration, direction="horizontal"):
    """Calculates prism in simple spherical lenses when given power in dioptres and decentration in cm, defaults to calculating horizontal prism but can take an optional argument for vertical. Returns a list where [0] is magnitude and [1] is base direction"""
    prism = power * decentration
    if direction == "vertical":
        if prism > 0:
            base = "Down"
        else:
            base = "Up"
    else:
        if prism > 0:
            base = "In"
        else:
            base = "Out"
    prism=format(abs(prism), '.2f')
    return prism, base


def calculate_simple_blanksize(a, dbl, ed, pd, power = 0, wastage = 2):
    """Calculates a simple blank size taking A, DBL, ED and PD. Measurements in mm. Does not take in to account vertical decentration or lens shape, if passes a +ve power will round blank up to nearest 5, checks ed > a and if not sets ed to a. Returns an integer"""
    if ed < a:
        ed = a
    blank = a+dbl+ed-pd+wastage
    if power > 0:
        blank += 5-blank%5
    
    return blank

def calculate_sag(power, blank, n=1.498):
    """Takes a surface power in dioptres and a blank size in mm and calculates sag, optional arg for index defaults to CR39. Returns sag in mm"""
    y = (blank/2)/1000
    r = (n-1)/abs(power)
    sag = r - ((r**2)-(y**2))**0.5
    return sag*1000

def lens_thickness(front_power, blank, back_power = 0, n = 1.498, min_thick = 1):
    """Calculate the thickess of a meniscus lens, min_thick takes edge substance for +ve power and min centre thickness for -ve"""
    front_sag = calculate_sag(front_power, blank, n)
    if back_power != 0:
        back_sag = calculate_sag(back_power, blank, n)
    else:
        back_sag = 0
    max_thickness = front_sag - back_sag + min_thick
    return max_thickness

def effective_power(power, test_bvd, fit_bvd, cyl = 0):
    """Calculates effective power of a lens when moved from testing distance, power in dioptres, bvd in mm, returns new power in D"""
    diff = (fit_bvd - test_bvd)/1000
    eff_power = power/(1-(diff*power))
    if cyl != 0:  
        power2 = power + cyl  
        eff_power2 = power2/(1-(diff*power2))
        eff_cyl = eff_power - eff_power2
        return eff_power, eff_cyl
    else:
        return eff_power

def compensated_power(power, test_bvd, fit_bvd, cyl = 0):
    """Calculates compensated power required when a lens moved from testing distance, power in dioptres, bvd in mm, returns new power in D"""
    diff = (test_bvd - fit_bvd)/1000
    comp_power = power/(1-(diff*power))
    if cyl != 0:
        power2 = power + cyl  
        comp_power2 = power2/(1-(diff*power2))
        comp_cyl = round(comp_power - comp_power2, 2)
        comp_power = round(comp_power, 2)    
        return comp_power, comp_cyl
    else:
        return comp_power

def thick_lens_power(power, base_curve, center_thick):
    """Given a target lens power in D, base curve in D, and a centre thickness in mm accurately calculate the required back surface power in D"""
    base_focal = 1/base_curve
    power_at_s2 = 1/(base_focal - center_thick)
    back_surface = power - power_at_s2
    return back_surface
