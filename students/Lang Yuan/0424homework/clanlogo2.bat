rem delete any previous 
del queen.binvox

rem use default resolution of 256 and downsample twice, so resolution is 64
rem you will to add your own arguments here - see http://www.patrickmin.com/minecraft/
binvox queen.stl -down -down

rem now display it
viewvox queen.binvox
