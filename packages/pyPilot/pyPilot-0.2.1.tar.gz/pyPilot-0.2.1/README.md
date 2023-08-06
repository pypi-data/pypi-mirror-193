# pyPilot

Python package for navigation, guidance, path planning, and control. This is also a mirror library of the Arduino/C++ library [navduino.h](https://github.com/PowerBroker2/navduino)

Python library for basic aerial navigation functions used for

* [Euler angles](https://en.wikipedia.org/wiki/Euler_angles)
* [Direction cosine matrices](https://en.wikipedia.org/wiki/Rotation_matrix)
* [Quaternions](https://eater.net/quaternions)
* [Rodrigues Rotation Vectors](https://courses.cs.duke.edu/fall13/compsci527/notes/rodrigues.pdf)
* [Earth radii calculations](https://en.wikipedia.org/wiki/Earth_radius)
* Earth rotation rate calculations
* Frame conversions
  *  [Latitude-Longitude-Altitude (LLA)](https://en.wikipedia.org/wiki/Geographic_coordinate_system)
  *  [North-East-Down (NED)](https://en.wikipedia.org/wiki/Local_tangent_plane_coordinates)
  *  [Earth Centered Earth Fixed (ECEF)](https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system)
  *  [Affine/Pose transforms (conversions between two non-colocated cartesian coordinate frames)](https://en.wikipedia.org/wiki/Affine_transformation)
     *  Native support for transforming points between vehicle, payload, and sensor coordinate frames
* [Distance and bearing calculations between 2 coordinates](http://www.movable-type.co.uk/scripts/latlong.html)
* [Calculating a new coordinate based on a reference coordinate (i.e. given a LLA coordinate, great circle distance, azimuth, and elevation angle, find the resulting LLA coordinate)](http://www.movable-type.co.uk/scripts/latlong.html)

## API

```
pyPilot:
  Constants:
    RADIANS
    DEGREES
    NED_TO_BODY
    BODY_TO_NED
    dRx
    dRy
    dRz
    dtx
    dty
    dtz

  Functions:
    angle2dcm
    dcm2angle
    angle2quat
    quat2angle
    quat2dcm
    dcm2quat
    vec2dcm
    dcm2vec
    vec2quat
    quat2vec
    vec2angle
    angle2vec
    quatMult
    quatInv
    quatRotVec
    interQuat
    quatParts
    earthGeoRad
    earthRad
    earthAzimRad
    earthRate
    llaRate
    navRate
    lla2ecef
    ecef2lla
    ecef2ned_dcm
    ecef2ned
    lla2ned
    ned2ecef
    ned2lla
    poseMat
    pose2dcm
    pose2t
    reversePoseMat
    skew
    poseMatDeriv
    transformPt
    bearingLla
    bearingNed
    distanceLla
    distanceNed
    distanceNedHoriz
    distanceNedVert
    distanceEcef
    elevationLla
    elevationNed
    LDAE2lla
    NDAE2ned

pose:
  Functions:
    payload2vehicle
    vehicle2payload
    sensor2vehicle
    vehicle2sensor
    sensor2payload
    payload2sensor
  
  Classes:
    vehicle_pose
    payload_pose
    sensor_pose

pilotUtils:
  Functions:
    wrapToPi
    constrain
    map

wgs84:
  Constants:
    a
    a_sqrd
    f
    omega_E
    omega_E_GPS
    GM
    GM_GPS
    b
    b_sqrd
    ecc
    ecc_sqrd
    ecc_prime
    ecc_prime_sqrd
    r
```

## Credits

Inspired by several sources including [NavPy](https://github.com/NavPy/NavPy), [bolderflight/navigation](https://github.com/bolderflight/navigation), and [Chris Veness's Geo Scripts](https://www.movable-type.co.uk/scripts/latlong.html)
