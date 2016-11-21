To Run, need to start a Python simple server in the folder of the files.
Python -m SimpleHTTPServer
then run the RunME.html

Play 2001 for ambience. 

Mouse buttons to tumble, pan, and zoom.

The data is from a russian astronomical catalogue of nothern stars (WBVR).

Getting the data from a very unwieldy state, (Weird extra characters, zero 
explanation of what columns stood for, astronomical coordinate systems,) 
into a renderable state was a struggle.  The position of the stars had to
be converted from Equitorial Coordinates, into Galactic Coordinates, then
into XYZ.  The distance was needed for these calculations and required a 
set of refernce star magnitudes based on spectral types.  The best data
set for this reference has some holes that needed to be eyeballed and 
patched by hand.  Who ever called astronomy a hard science?  

The stars are rendered with 3js as sprites.  The colors of the stars align
to their actual colors based on their spectral types.  There are seven
colors relating to the seven types present [O,B,A,F,G,K,M].  The base of
the code is taken from a 3js example demostraing sprites rendered on the 
GPU.

The visulization of the data very clearly shows that only a segment of
the sky was mapped.  This makes sense since it was a series of ground
based mesurments from russia.  

I was curious if recognizable constilations could be made out.  I suspect
it is possible but there would need to be a way to properly orient the 
camera to make it easier to do.  

The data also shows the ratio of low magnitude stars such as our sun,
and somewhat obscures the bright B type stars that one can normally spot
in the night sky.  The Gould belt is composed primarily of these stars
so a way to highlight these may serve well to help highlight the belt.

It was nice to see a data set go from massive and unimaginable, to one
that is a fair deal easier to wrap your head around.  But Damn are there 
alot of stars.


PS really wanted to have this play in the background.
https://www.youtube.com/watch?v=923jxZY2NPI
But I'm bad at html, so I couldn't figure out how to make it play and
let you turn it off too.
