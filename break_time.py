import webbrowser
import time

total_breaks = input("how many breaks you need")
break_count = 0

print("this program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(1*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=OrQNzqB35O4")
    break_count += 1
