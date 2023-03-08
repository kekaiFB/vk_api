import datetime


#birthday in ISO format 
def get_birthdays(bdate):
        #not bdate
        if len(bdate) < 2:
            return datetime.datetime \
                .strptime(f"{'01'}/{'01'}/{'0001'}", "%d/%m/%Y") \
                .isoformat()
        #dd.mm
        elif len(bdate) == 2:
            return datetime.datetime \
                .strptime(f"{bdate[0]}/{bdate[1]}/{'0001'}", "%d/%m/%Y") \
                .isoformat()
        #dd.mm.yyyy.
        elif len(bdate) == 3:
            return datetime.datetime \
                .strptime(f"{bdate[0]}/{bdate[1]}/{bdate[2]}", "%d/%m/%Y") \
                .isoformat()