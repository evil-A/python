from datetime import datetime

kata = (2019, 9, 25, 3, 30)

print(datetime(*kata).strftime("%m/%d/%Y %H:%M"))
