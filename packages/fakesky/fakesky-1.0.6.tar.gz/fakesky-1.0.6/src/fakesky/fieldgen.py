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
        colorData = pd.read_csv("Results_BB.txt")
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


if __name__ == "__main__": 
    generateSkyfield()
    generateSpherePlot()
