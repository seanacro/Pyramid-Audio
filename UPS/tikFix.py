import csv

def main():
  with open("track.csv", "r", newline='') as track:
    tik=csv.reader(track, delimiter=',')
    for i in tik:
      if len(i[0]) != 6:
        i[0]='999999'
      with open('track.txt', 'w') as fixed:
        write=csv.writer(fixed,delimiter=',')
        for i in tik:
          write.writerow(i)

main()