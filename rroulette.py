import os
import random
import time

bullet = random.randint(1, 6)

print("Spin the the cylinder")
time.sleep(1)
print("Pull the trigger")
time.sleep(1)
if bullet == 6:
    os.system("shutdown /s /t 0")

else:
    print("Next round! ;)")
