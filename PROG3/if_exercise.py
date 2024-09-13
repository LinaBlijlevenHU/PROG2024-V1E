#a) If age is greater than 62 then print 'You can get Social Security benefits’
age = 64

if age > 62:
    print("You can get Social Security benefits")

#b) If string 'large bonuses' appears in string report then print 'Vacation time!’
report = "We had a very good fiscal year and everyone is getting large bonuses."

if 'large bonuses' in report:
    print("Vacation time!")

#c) If hits is greater than 10 and shield is 0 then print "You're dead..."
hits = 15
hp = 15
shield = 0

if hits > 10 and shield == 0 and (hp - hits) <= 0:
    print("You're dead...")
