#1 #60 #3600 #86400
request = int(input('write amount of seconds: '))
days, seconds1 = divmod(request, 86400)
hours, seconds2 = divmod(seconds1, 3600)
minutes, seconds3 = divmod(seconds2, 60)
seconds = seconds3
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)
if request <=0 or request >= 8640000:
    print('error, your number is too small or it\'s bigger then 100 days')
else:
    print('days:', days, end='  ')
    print(hours, minutes, seconds, sep=':')
