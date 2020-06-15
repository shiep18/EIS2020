with open("table.txt","r") as f:
    lines = f.read().split('\n')

with open("table.ics","w",encoding='utf-8') as f:
    f.write('BEGIN:VCALENDAR\nMETHOD:PUBLISH\nPRODID:Microsoft Exchange Server 2010\nVERSION:2.0\nX-WR-CALNAME:日历\nBEGIN:VTIMEZONE\nTZID:China Standard Time\nBEGIN:STANDARD\nDTSTART:16010101T000000\nTZOFFSETFROM:+0800\nTZOFFSETTO:+0800\nEND:STANDARD\nBEGIN:DAYLIGHT\nDTSTART:16010101T000000\nTZOFFSETFROM:+0800\nTZOFFSETTO:+0800\nEND:DAYLIGHT\nEND:VTIMEZONE\n')

    i = 0
    for line in lines:
        i += 1
        if line is not '':
            line = line.split(',')
            f.write('BEGIN:VEVENT\n')
            f.write(f'DESCRIPTION:{line[4]}\\n\n')
            f.write(f'UID:{i}\n')
            f.write(f'SUMMARY:{line[2]}!!-10\n')
            f.write(f'DTSTART;TZID=China Standard Time:{line[0]}\n')
            f.write(f'DTEND;TZID=China Standard Time:{line[1]}\n')
            f.write('CLASS:PUBLIC\n')
            f.write('PRIORITY:5\n')
            f.write('TRANSP:OPAQUE\n')
            f.write('STATUS:CONFIRMED\n')
            f.write('SEQUENCE:0\n')
            f.write(f'LOCATION:{line[3]}\n')
            f.write('END:VEVENT\n')

    f.write('END:VCALENDAR\n')