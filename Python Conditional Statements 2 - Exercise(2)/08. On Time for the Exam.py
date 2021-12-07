exam_time_hours = int(input())
exam_time_minutes = int(input())
arrival_time_hours = int(input())
arrival_time_minutes = int(input())

exam_time_converted_minutes = exam_time_hours * 60 + exam_time_minutes
arrival_time_converted_minutes = arrival_time_hours * 60 + arrival_time_minutes
early = exam_time_converted_minutes - arrival_time_converted_minutes
late = arrival_time_converted_minutes - exam_time_converted_minutes

if exam_time_converted_minutes == arrival_time_converted_minutes or 0 < early <= 30:
    print("On time")
    print(f"{early} minutes before the start")
elif exam_time_converted_minutes > arrival_time_converted_minutes and early > 30:
    print("Early")
    if early >= 60:
        if early % 60 < 10:
            print(f"{(early//60)}:0{(early%60)} hours before the start")
        else:
            print(f"{(early//60)}:{(early%60)} hours before the start")
    elif early < 60:
        print(f"{(early % 60)} minutes before the start")
elif exam_time_converted_minutes < arrival_time_converted_minutes:
    print("Late")
    if late >= 60:
        if late % 60 < 10:
            print(f"{(late//60)}:0{(late%60)} hours after the start")
        else:
            print(f"{(late//60)}:{(late%60)} hours after the start")
    elif late < 60:
        print(f"{(late % 60)} minutes after the start")
