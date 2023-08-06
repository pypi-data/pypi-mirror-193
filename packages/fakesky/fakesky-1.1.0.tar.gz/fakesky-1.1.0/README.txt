----------------------------------------
fakesky: a module for generating dynamic skies
----------------------------------------

This is the README for the fakesky module, which generates fake skies and makes images of them.

The installation requirements are as follows:
   • matplotlib
   • numpy
   • pandas
   • scipy
   • astropy

To install this module, please enter the following command into your terminal:
   > pip install fakesky
To import this module, please enter the following command:
   > from fakesky import fieldgen



The module has three functions to use:

generateImage(numStars, latitude, longitude, time, filename, seed) does what it says: generates a still image of a sky. It generates an image equal to what the sky would look like if you look up at a given location and time!
    • numStars is the number of stars you want to be in the image. (I recommend 100000; it creates good-looking images for me!)
    • latitude and longitude are STRINGS of the decimal values of the latitude and longitude.
    • time is a STRING timestamp of the time you want your image to be taken at.
    • filename is the filename you want your image to be uploaded to.
    • seed is the seed used to generate the random location of the stars, as well as the galactic disk.    
A valid usage, for example, is
   > fieldgen.generateImage(100000, "42.28", "-83.74", "2023-02-21 23:00:00", "skyfield.png", 1)
   
   
generateSpherePlot(numStars, seed) creates a field of what the sphere of the sky looks like. The plot should look like a sphere, with different stars plotted onto a sphere.
    • numStars is the number of stars you want to be in the image. (I recommend 100000; it creates good-looking images for me!)
    • filename is the filename you want your image to be uploaded to.
    • seed is the seed used to generate the random location of the stars, as well as the galactic disk. (Note that the same seed will produce the same sky for both of the two functions.)
A valid usage, for example, is
   > fieldgen.generateSpherePlot(100000, "sphereplot.png", 1)


generateAnimation(numStars, latitude, longitude, times, filename, seed) creates a .gif of a number of images composed by generateImage()!
    • numStars is the number of stars you want to be in the image. (I recommend 100000; it creates good-looking images for me!)
    • latitude and longitude are STRINGS of the decimal values of the latitude and longitude.
    • times is a LIST of timestamps of the time you want your image to be taken at.
    • filename is the filename you want your image to be uploaded to.
    • seed is the seed used to generate the random location of the stars, as well as the galactic disk.    
A valid usage, for example, is
   > fieldgen.generateAnimation(250000, "47.50", "-122.43", ["2023-02-22 22:00:00", "2023-02-22 23:00:00", "2023-02-23 0:00:00", "2023-02-23 1:00:00", "2023-02-23 2:00:00"], "skyfield.gif", 1)
   


Some notes:
   • The seeds should all generate the same sky for all plotting functions! If you want multiple plots of the same sky, feel free.
   • The image is not necessarily realistic! It samples the star locations from a uniform distributions, with a chunk (25%) coming from a multivariate Gaussian that simulates the galactic bulge. The star colors are (slightly saturated versions of) official star colors, but the distribution of colors, opacities, and sizes is randomly generated based on aesthetics, not scientific accuracy. I'm working on slowly making the sky more realistic, but in the meantime, if you have any recommendations for how I can do this, let me know!
   • For some computers, the images generated will be very coarse. I don't quite know why this is -- I can't replicate it on my own computer.


Thanks to Jan-Vincent Harre and René Heller for figuring out the colors of these stars. (See Harre & Heller (2021) for more details: https://ui.adsabs.harvard.edu/abs/2021AN....342..578H/abstract)