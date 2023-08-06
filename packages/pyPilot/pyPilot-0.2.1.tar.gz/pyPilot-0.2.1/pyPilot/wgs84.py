a           = 6378137.0           # Semi - major Axis [m]
a_sqrd      = a**2                # Semi - major Axis squared [m] 
f           = 1.0 / 298.257223563 # Flattening [unitless]
omega_E     = 7292115.0e-11       # Angular velocity of the Earth [rad / s]
omega_E_GPS = 7292115.1467e-11    # Angular velocity of the Earth [rad / s]
                                  # According to ICD - GPS - 200

GM = 3.986004418e14 # Earth's Gravitational Constant [m^3/s^2]
                    # (mass of earth's atmosphere included)

GM_GPS = 3.9860050e14 # The WGS 84 GM value recommended for GPS receiver usage
                      # by the GPS interface control document(ICD - GPS - 200)
                      # differs from the current refined WGS 84 GM value. [m^3/s^2]

b              = 6356752.3142       # Semi - minor axis [m]
b_sqrd         = b**2               # Semi - minor axis squared [m]
ecc            = 8.1819190842622e-2 # First eccentricity [unitless]
ecc_sqrd       = ecc**2             # First eccentricity squared [unitless]
ecc_prime      = 8.2094437949696e-2 # Second eccentricity [unitless]
ecc_prime_sqrd = ecc_prime**2       # Second eccentricity squared [unitless]
r              = (2*a + b) / 3      # Arithmetic mean radius [m]

c  = 2.99792458e8 # Velocity of light in a vacuum [m / s]
G  = 6.67428e-11  # Universal constant of gravitation [m^3 / kg s^2]
MA = 5.148e18     # Total mean mass of the atmosphere with water vapor [kg]
H  = 3.273795e-3  # Dynamic ellipticity [unitless]

U0  = 6.26368517146e7   # Normal gravity potential on the ellipsoid [m^2 / s^2]
ye  = 9.7803253359      # Normal gravity at the equator on the ellipsoid [m / s^2]
yp  = 9.8321849379      # Normal gravity at the pole on the ellipsoid [m / s^2]
y   = 9.7976432223      # Mean value of normal gravity [m / s^2]
k   = 1.931852652458e-3 # Somigliana's formula - normal gravity formula constant [unitless]
m   = 3.449786506841e-3 # Normal gravity formula constant [unitless]
M   = 5.9721864e24      # Mass of the Earth including atmosphere [kg]
GMp = 3.986000982e14    # Geocentric gravitational constant with Earth's atmosphere excluded [m^3 / s^2]
GMA = 3.4359e8          # Gravitational constant of the Earth's atmosphere [m^3 / s^2]