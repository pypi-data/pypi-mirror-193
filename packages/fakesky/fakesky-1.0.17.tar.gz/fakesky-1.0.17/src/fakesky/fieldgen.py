import matplotlib.pyplot as plt
import matplotlib as mpl
import mpl_toolkits.mplot3d.axes3d as axes3d

import numpy as np
import pandas as pd
import scipy

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
from astropy.coordinates import AltAz

from io import StringIO

# The goal of this code is to randomly generate a starfield in the sky, and have it dynamically move over time and given a position!


# the skyField class used to generate the images!
class skyField:
    
    # constructor
    def __init__(self, numStars, seed):
        self.numStars = numStars
        self.seed = seed
        self.generateStars()
        self.getColors()
        
    # This function generates the positions of each star.
    # It should generate stars uniformly, for now.
    def generateStars(self):
        np.random.seed(self.seed)
        
        self.numBackgroundStars = (int)(0.7 * self.numStars)
        self.numDiskStars = self.numStars - self.numBackgroundStars
        
        self.centerRA = np.random.uniform(low = 0.0, high = 24.0, size = 1)
        self.centerDec = scipy.stats.truncnorm.rvs(loc = 0.0, scale = 0.5, a = -4, b = 4, size = 1)
        
        # Let's generate the RAs of our stars.
        # Let's put RA in hours.
        self.RA = np.random.uniform(low = 0.0, high = 24.0, size = self.numBackgroundStars)
        
        # Let's generate Decs. Note that we need to transform them!
        # Let's put RA in degrees.
        Decs = np.random.uniform(low = -1.0, high = 1.0, size = self.numBackgroundStars)
        self.Decs = (180. / np.pi) * np.arcsin(Decs)
        
        # Ah, but we also want to add a "Milky Way"!
        # Let's add a normal distribution of stars to this.
        
        # Let's generate a scale.
        self.scaleRA = np.random.uniform(low = 2.5, high = 4.5, size = 1)
        self.scaleDec = np.random.uniform(low = 0.025, high = 0.125, size = 1)
        
        
        newRAs = (np.random.normal(loc = self.centerRA, scale = self.scaleRA, size = self.numDiskStars)) % 24.0
        self.DiskRA = newRAs
        
        newDecs = scipy.stats.truncnorm.rvs(loc = self.centerDec, scale = self.scaleDec, a = (-1 - self.centerDec) / self.scaleDec, b = (1 - self.centerDec) / self.scaleDec, size = self.numDiskStars)
        newDecs = (180. / np.pi) * np.arcsin(newDecs)
        self.DiskDecs = newDecs
        

    def getColors(self):
        # And now let's get colors!
        
        # .txt files suck, so let's read this as a string literal...
        
        stringLiteral = StringIO("""T_{eff},R,G,B,Hex
2300,1.0,0.409,0.078,#ff6813
2400,1.0,0.432,0.093,#ff6e17
2500,1.0,0.455,0.109,#ff731b
2600,1.0,0.476,0.126,#ff7920
2700,1.0,0.497,0.144,#ff7e24
2800,1.0,0.518,0.163,#ff8429
2900,1.0,0.537,0.182,#ff892e
3000,1.0,0.557,0.202,#ff8d33
3100,1.0,0.575,0.223,#ff9238
3200,1.0,0.593,0.244,#ff973e
3300,1.0,0.611,0.266,#ff9b43
3400,1.0,0.627,0.289,#ff9f49
3500,1.0,0.644,0.311,#ffa44f
3600,1.0,0.66,0.335,#ffa855
3700,1.0,0.675,0.358,#ffac5b
3800,1.0,0.69,0.382,#ffaf61
3900,1.0,0.704,0.405,#ffb367
4000,1.0,0.718,0.429,#ffb76d
4100,1.0,0.732,0.454,#ffba73
4200,1.0,0.745,0.478,#ffbe79
4300,1.0,0.758,0.502,#ffc180
4400,1.0,0.77,0.527,#ffc486
4500,1.0,0.782,0.551,#ffc78c
4600,1.0,0.794,0.575,#ffca92
4700,1.0,0.806,0.599,#ffcd98
4800,1.0,0.817,0.624,#ffd09f
4900,1.0,0.827,0.648,#ffd2a5
5000,1.0,0.838,0.672,#ffd5ab
5100,1.0,0.848,0.696,#ffd8b1
5200,1.0,0.858,0.719,#ffdab7
5300,1.0,0.867,0.743,#ffddbd
5400,1.0,0.877,0.766,#ffdfc3
5500,1.0,0.886,0.789,#ffe1c9
5600,1.0,0.894,0.812,#ffe4cf
5700,1.0,0.903,0.835,#ffe6d4
5800,1.0,0.911,0.858,#ffe8da
5900,1.0,0.919,0.88,#ffeae0
6000,1.0,0.927,0.902,#ffece6
6100,1.0,0.935,0.924,#ffeeeb
6200,1.0,0.942,0.946,#fff0f1
6300,1.0,0.95,0.967,#fff2f6
6400,1.0,0.957,0.989,#fff3fc
6500,0.991,0.955,1.0,#fcf3ff
6600,0.971,0.942,1.0,#f7f0ff
6700,0.952,0.93,1.0,#f2edff
6800,0.934,0.918,1.0,#eeeaff
6900,0.917,0.907,1.0,#e9e7ff
7000,0.901,0.896,1.0,#e5e4ff
7200,0.87,0.876,1.0,#dddfff
7400,0.843,0.858,1.0,#d6daff
7600,0.817,0.841,1.0,#d0d6ff
7800,0.794,0.825,1.0,#cad2ff
8000,0.773,0.81,1.0,#c5ceff
8200,0.753,0.797,1.0,#c0cbff
8400,0.735,0.784,1.0,#bbc7ff
8600,0.718,0.772,1.0,#b7c4ff
8800,0.703,0.761,1.0,#b3c2ff
9000,0.688,0.75,1.0,#afbfff
9200,0.674,0.741,1.0,#abbcff
9400,0.662,0.731,1.0,#a8baff
9600,0.65,0.723,1.0,#a5b8ff
9800,0.639,0.714,1.0,#a2b6ff
10000,0.628,0.706,1.0,#a0b4ff
10200,0.618,0.699,1.0,#9db2ff
10400,0.609,0.692,1.0,#9bb0ff
10600,0.6,0.685,1.0,#99aeff
10800,0.592,0.679,1.0,#96adff
11000,0.584,0.673,1.0,#94abff
11200,0.577,0.667,1.0,#93aaff
11400,0.57,0.662,1.0,#91a8ff
11600,0.563,0.657,1.0,#8fa7ff
11800,0.557,0.652,1.0,#8da6ff
12000,0.55,0.647,1.0,#8ca4ff        
        """)
        
        colorData = pd.read_csv(stringLiteral)
        backgroundColorIndexes = scipy.stats.truncnorm.rvs(loc = 35, scale = 10, a = -3, b = 3.5, size = self.numBackgroundStars).round().astype(int)
        diskColorIndexes = scipy.stats.truncnorm.rvs(loc = 40, scale = 6, a = -5, b = 2.5, size = self.numDiskStars).round().astype(int)
    
        # Let's brighten these colors.
        brightColors = colorData[["R", "G", "B"]].values * 1.1
        for i in brightColors:
            for j in range(3):
                if i[j] > 1:
                    i[j] = 1
    
        self.backgroundColors = brightColors[backgroundColorIndexes]
        self.diskColors = brightColors[diskColorIndexes]
        
        # And sizes?
        # The sizes are just messed around, with whatever values I think look good.
        self.backgroundSizes = 0.005 * (backgroundColorIndexes ** 1.2) * (np.random.poisson(2, size = self.numBackgroundStars) + 0.5)
        self.diskSizes = 0.012 * (diskColorIndexes ** 1.2)
        
        # And brightnesses?
        # We want a LOT of dim stars combined with a select few very bright ones.
        # The disk should be on average, dim, with similar brightnesses.
        self.backgroundBrightnesses = np.power(scipy.stats.truncnorm.rvs(loc = 0., scale = 0.25, a = 0, b = 4, size = self.numBackgroundStars), 2.5)
        self.diskBrightnesses = np.power(scipy.stats.truncnorm.rvs(loc = 0.05, scale = 0.01, a = -5, b = 25, size = self.numDiskStars), 1.2)
        
        # And let's make a small set of stars extra bright.
#         brightStarIndexes = self.backgroundBrightnesses > np.percentile(self.backgroundBrightnesses, 0.99)
#         self.backgroundBrightnesses[brightStarIndexes] =  np.sqrt(self.backgroundBrightnesses[brightStarIndexes])
#         self.backgroundBrightnesses[self.backgroundBrightnesses > 1] = 1
        
    # Let's write a function to plot the stars on a 3D mesh, to test.
    def plotStars(self, filename):
        r = 1.001
        theta = (360. / 24.) * (np.pi / 180.) * self.RA
        phi = (np.pi / 180.) * (90. - self.Decs)
        
        self.x = r * np.sin(phi) * np.cos(theta)
        self.y = r * np.sin(phi) * np.sin(theta)
        self.z = r * np.cos(phi)
        
        # And plot the disk
        dtheta = (360. / 24.) * (np.pi / 180.) * self.DiskRA
        dphi = (np.pi / 180.) * (90. - self.DiskDecs)
        
        self.dx = r * np.sin(dphi) * np.cos(dtheta)
        self.dy = r * np.sin(dphi) * np.sin(dtheta)
        self.dz = r * np.cos(dphi)
        
        # And let's make the sphere
        sphi, stheta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
        sx = 1.0 * np.sin(sphi) * np.cos(stheta)
        sy = 1.0 * np.sin(sphi) * np.sin(stheta)
        sz = 1.0 * np.cos(sphi)
        
        fig = plt.figure(figsize = (12, 12), dpi = 600)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(sx, sy, sz, rstride = 1, cstride = 1, color = 'black', alpha = 0.75, linewidth = 0)
        ax.scatter(self.x, self.y, self.z, c = self.backgroundColors, s = self.backgroundSizes, alpha = self.backgroundBrightnesses)
        ax.scatter(self.dx, self.dy, self.dz, c = self.diskColors, s = self.diskSizes, alpha = self.diskBrightnesses)
#         ax.scatter(self.dx, self.dy, self.dz, c = "blue", s = self.diskSizes, alpha = self.diskBrightnesses)
        
        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_zlim([-1,1])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_aspect("equal")
        plt.tight_layout()
        fig.savefig(filename)
        
    # This should store the altitude and azimuth of each star, given a latitude, longitude, and location (and possibly a height)!
    def altAz(self, latitude, longitude, time, location_height = 0):
        LOCATION = EarthLocation(lat = latitude, lon = longitude, height = location_height *u.m)
        OBSTIME  = Time(time) 
        OBSERVER = AltAz(location= LOCATION, obstime = OBSTIME)
        
        backgroundStarCoords = SkyCoord(1.0 * self.RA, self.Decs, unit = (u.hourangle, u.deg))
        backgroundAltAz = backgroundStarCoords.transform_to(OBSERVER)
        diskStarCoords = SkyCoord(1.0 * self.DiskRA, self.DiskDecs, unit = (u.hourangle, u.deg))
        diskAltAz = diskStarCoords.transform_to(OBSERVER)
        
        self.backgroundAlt = backgroundAltAz.alt.deg
        self.backgroundAz = backgroundAltAz.az.deg
        self.diskAlt = diskAltAz.alt.deg
        self.diskAz = diskAltAz.az.deg
        
#         diskCenterCoords = SkyCoord(15.0 * self.centerRA, self.centerDecs, unit = u.deg)
#         diskCenterAltAz = diskCenterCoords.transform_to(OBSERVER)
#         self.diskCenterAlt = diskCenterAltAz.alt.deg
#         self.diskCenterAz = diskCenterAltAz.az.deg

    # This should plot the sky as a circle!
    def plotSky(self, latitude, longitude, time, filename):
        self.altAz(latitude, longitude, time, 0)

        # Let's figure out which stars are UP!
        self.backgroundUpIndexes = self.backgroundAlt > 0.
        self.diskUpIndexes = self.diskAlt > 0.
        
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize = (12, 12), dpi = 600)
        ax.tick_params(grid_alpha = 0.175)
        ax.set_rlim(0,90)

        bkg = plt.Circle((0, 0), 90., transform = ax.transData._b, color = 'black')
        ax.add_patch(bkg)
        
        ax.scatter((np.pi / 180.) * self.backgroundAz[self.backgroundUpIndexes], 90. - self.backgroundAlt[self.backgroundUpIndexes],
                    c = self.backgroundColors[self.backgroundUpIndexes],
                    s = self.backgroundSizes[self.backgroundUpIndexes],
                    alpha = self.backgroundBrightnesses[self.backgroundUpIndexes])
        
        # Don't plot if the disk is not up
        if (np.sum(self.diskUpIndexes) != 0):
            ax.scatter((np.pi / 180.) * self.diskAz[self.diskUpIndexes], 90. - self.diskAlt[self.diskUpIndexes],
                        c = self.diskColors[self.diskUpIndexes],
                        s = self.diskSizes[self.diskUpIndexes],
                        alpha = self.diskBrightnesses[self.diskUpIndexes])

#             ax.scatter((np.pi / 180.) * self.diskAz[self.diskUpIndexes], 90. - self.diskAlt[self.diskUpIndexes],
#                         c = "green",
#                         s = self.diskSizes[self.diskUpIndexes],
#                         alpha = 1)
        fig.savefig(filename)
#         plt.show()
        
    
def generateSkyfield(numStars, latitude, longitude, time, filename, seed):
    skyField(numStars, seed).plotSky(latitude, longitude, time, filename)
    
def generateSpherePlot(numStars, filename, seed):
    skyField(numStars, seed).plotStars(filename)
