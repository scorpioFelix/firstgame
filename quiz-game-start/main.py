print("welcome to norm game show ✨ 🎇 🎈 🎡 ")
player = input("wanna play a game? ").lower()
if player != "yes":
    quit()
print("Let's go 🕹 🎮 📢 ")
score = 0

answer = input(" first man? ")
if answer == ("black man"):
    print("correct! 👍📌 ")
    score += 1
else:
    print("👎👎👎")

answer = input(" best rapper? ")
if answer == ("Rakim,Pac,Nas,Biggie or Kanye"):
    print("correct! 👍📌 ")
    score += 1
else:
    print("👎👎👎")

answer = input("best cure? ")
if answer == ("love"):
    print("correct! 👍📌 ")
    score += 1
else:
    print("👎👎👎")

answer = input("best game? ")
if answer == ("fun"):
    print("correct! 👍📌 ")
    score += 1
else:
    print("👎👎👎")

print("umepata " + str(score))
print("umepata " + str(score/4 * 100) + "%")