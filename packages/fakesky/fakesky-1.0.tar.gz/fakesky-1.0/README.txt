----------------------------------------
fakesky: a module for generating dynamic skies
----------------------------------------

This is the README for the fakesky module, which generates fake skies and makes images of them.

The installation requirements are as follows:
   • matplotlib
   • mpl_toolkits
   • numpy
   • pandas
   • scipy
   • astropy

The module has two functions to use:


generateSkyfield(numStars, latitude, longitude, time, filename, seed) does what it says: generates an image of a sky. It generates an image equal to what the sky would look like if you look up at a given location and time!
    • numStars is the number of stars you want to be in the image. (I recommend 100000; it creates good-looking images for me!)
    • latitude and longitude are STRINGS of the decimal values of the latitude and longitude.
    • time is a STRING timestamp of the time you want your image to be taken at.
    • filename is the filename you want your image to be uploaded to.
    • seed is the seed used to generate the random location of the stars, as well as the galactic disk.    
A valid usage, for example, is
   > fakesky.generateSkyfield(100000, "42.28", "-83.74", "2023-02-21 23:00:00", "skyfield.png", 1)
   
   
generateSpherePlot(numStars, seed) creates a field of what the sphere of the sky looks like. The plot should look like a sphere, with different stars plotted onto a sphere.
    • numStars is the number of stars you want to be in the image. (I recommend 100000; it creates good-looking images for me!)
    • filename is the filename you want your image to be uploaded to.
    • seed is the seed used to generate the random location of the stars, as well as the galactic disk. (Note that the same seed will produce the same sky for both of the two functions.)
A valid usage, for example, is
   > fakesky.generateSpherePlot(100000, "sphereplot.png", 1)
   
Thanks to Jan-Vincent Harre and René Heller for figuring otu the colors of these stars. (See Harre et al. (2020) for more details.)