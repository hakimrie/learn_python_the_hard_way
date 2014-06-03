name = 'Zed A. Shaw'
age = 35
height = 74 #inch
weight = 180 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % age
print "He's %d pounds heavy." % height
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, height, age + height + weight)

#teeth %r
ulet = "snake"
print "whoa! what is this %r." % ulet

#convert inch to centimeter
print "he's height in centimeters is %f and he's weight in kilo is %f kg " % (height*2.54, weight * 0.453592)