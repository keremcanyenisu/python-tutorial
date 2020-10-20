
# Çalıştırmak için : py cron_interpreter.py 19:00  config.txt    ---- Windows

import sys

def cron_interpret_func(task):
    # hour_schedule ve minute_schedule dosyadan gelen taskın zaman değerleri: Örneğin hour_schedule : 19, minute_schedule : *
    minute_schedule = task.split(" ")[0]
    hour_schedule = task.split(" ")[1]
    task_definition = task.split(" ")[2] # taskın açıklaması : örn : /bin/run_me_daily

    scheduled_current_hour = scheduled_current_time.split(":")[0] # kullanıcı tarafından verilen saat
    scheduled_current_minute = scheduled_current_time.split(":")[1] # kullanıcı tarafından verilen dakika

    result_list = [] #sonuçların toplandığı liste
    if hour_schedule == "*" :
        if minute_schedule == "*" :
            result_list.append(scheduled_current_time + " today - " + task_definition)
        else :
            if minute_schedule >= scheduled_current_minute :
                result_list.append(scheduled_current_hour + ":" + minute_schedule + " today - " + task_definition)
            else :
                result_list.append((scheduled_current_hour + 1) + ":" + minute_schedule + " today - " + task_definition)
    else :
        if minute_schedule == "*":
            if scheduled_current_hour == hour_schedule :
                result_list.append(scheduled_current_time + " today - " + task_definition)
            elif hour_schedule > scheduled_current_hour : 
                result_list.append(hour_schedule + ":00" + " today - " + task_definition)
            else :
                result_list.append(hour_schedule + ":00" + " tomorrow - " + task_definition)
        else : 
            if scheduled_current_hour == hour_schedule :
                if scheduled_current_minute == minute_schedule :
                    result_list.append(scheduled_current_time + " today - " + task_definition)
                elif minute_schedule > scheduled_current_minute : 
                    result_list.append(hour_schedule + ":" + minute_schedule + " today - " + task_definition)
                else : 
                    result_list.append(hour_schedule + ":" + minute_schedule + " tomorrow - " + task_definition)
            elif hour_schedule > scheduled_current_hour :
                    result_list.append(hour_schedule + ":" + minute_schedule + " today - " + task_definition)
            else :
                    result_list.append(hour_schedule + ":" + minute_schedule + " tomorrow - " + task_definition)

    for result in result_list:
        print(result)



# PROGRAM GİRİŞİ BURASI
file_name = sys.argv[2] # system argümanların sonuncusu dosya adı : py cron_interpreter.py HH:mm file_name
cron_schedule_file = open(file_name,"r")
cron_task_list = cron_schedule_file.read().splitlines() ##dosyadan okunan task schedule ve açıklamaları
scheduled_current_time = sys.argv[1]

# her bir taskı (her bir line) for ile dönüp interpret functiona veriyoruz
for cron_task in cron_task_list:
    cron_interpret_func(cron_task)



