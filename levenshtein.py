import nltk, re, math, matplotlib.pyplot as plt, distance
from nltk.metrics.distance import edit_distance
from random import randrange, sample

listOfDocs = []
randomLevenschtein = []
spamLevenschtein = []

t1 = "Why vacation abroad when we have our very own beautiful Manali! Hear all about it from these lovely ladies. #IndiaTripping"
t2 = "HIIT for the Holidays http://bit.ly/2e0N9uX #WeekendGoals #WeekendVibes"
t3 = "Without a future to look towards, the past is the only thing we can look back on. StayWow PositiveReminder remember"
t4 = "There's more to life than training, but training is what puts more in your life ! Check out my latest videos #SidFit #Sidlove"
t5 = "Wondering which #vegetables to start #juicing? Here are some of the best vegetable you can use. Chheck my link here"

spam_list = []

for item in range(6,26):
	tfile = open("/TweetDocs/TweetDoc" + str(item) + ".txt")
	rawdata = tfile.read()
	spam_list.append(rawdata)

print(spam_list)

# 5 lists to carry Levenshtein data
lev_res_t1 = []
lev_res_t2 = []
lev_res_t3 = []
lev_res_t4 = []
lev_res_t5 = []

for item in spam_list:
	print(item)
	ans1 = distance.levenshtein(t1, item)
	ans2 = distance.levenshtein(t2, item)
	ans3 = distance.levenshtein(t3, item)
	ans4 = distance.levenshtein(t4, item)
	ans5 = distance.levenshtein(t5, item)
	lev_res_t1.append(ans1)
	lev_res_t2.append(ans2)
	lev_res_t3.append(ans3)
	lev_res_t4.append(ans4)
	lev_res_t5.append(ans5)

print("Distance of Spam with 1st Random tweet: ")
print(lev_res_t1)
print("Distance of Spam with 2nd Random tweet: ")
print(lev_res_t2)
print("Distance of Spam with 3rd Random tweet: ")
print(lev_res_t3)
print("Distance of Spam with 4th Random tweet: ")
print(lev_res_t4)
print("Distance of Spam with 5th Random tweet: ")
print(lev_res_t5)

Oranges = plt.get_cmap('Oranges')
x = list(range(1,21))
y1 = lev_res_t1
y2 = lev_res_t2
y3 = lev_res_t3
y4 = lev_res_t4
y5 = lev_res_t5
plt.title("Levenschtein edit-distance score graph")
plt.xlabel("Spam Docs")
plt.ylabel("Levenschtein Values")

plot1 = plt.scatter(x,y1,marker="8", s=80, cmap=Oranges, color=['blue'])
plot2 = plt.scatter(x,y2,marker="8", s=80, cmap=Oranges, color=['red'])
plot3 = plt.scatter(x,y3,marker="8", s=80, cmap=Oranges, color=['blue'])
plot4 = plt.scatter(x,y4,marker="8", s=80, cmap=Oranges, color=['blue'])
plot5 = plt.scatter(x,y5,marker="8", s=80, cmap=Oranges, color=['blue'])


plt.legend((plot1,plot2,plot3,plot4,plot5),
           ('Random1 - SpamAll', 'Random2 - SpamAll', 'Random3 - SpamAll', 'Random4 - SpamAll', 'Random5 - SpamAll'),
           scatterpoints=1,
           loc='lower center',
           ncol=3,
           fontsize=10)

plt.show()

