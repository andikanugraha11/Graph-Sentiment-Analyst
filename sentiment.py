import nltk 
import string
import xlsxwriter
import matplotlib.pyplot as plt

messages = [line.rstrip() for line in open("comments.txt",encoding="utf8")]
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

summary = {"positive":0,"neutral":0,"negative":0}

data_and_result = []

for x in messages: 
    ss = sid.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary["neutral"] +=1
        data_x_result = [x,'neutral']
    elif ss["compound"] > 0.0:
        summary["positive"] +=1
        data_x_result = [x,'positive']
    else:
        summary["negative"] +=1
        data_x_result = [x,'negative']
    data_and_result.append(data_x_result)
print(summary)

# plot
labels = 'Positive', 'Neutral', 'Negative'
sizes = [summary["positive"], summary["neutral"], summary["negative"]]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
         startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

workbook = xlsxwriter.Workbook('Analisa.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for data, result in (data_and_result):
    worksheet.write(row, col,     data)
    worksheet.write(row, col + 1, result)
    row += 1

workbook.close()