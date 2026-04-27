import logging
from datetime import datetime, timedelta

logging.basicConfig(filename="hb_test.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    encoding="utf-8")

errors = []

with open('hblog.txt', 'r') as f:
    for line in f.readlines():
        if 'Key TSTFEED0300|7E3E|0400' in line:
            errors.append(line)

def time_log(lines:list):

    for i in range(len(lines)-1):
        str1, str2 = lines[i].split(), lines[i+1].split()
        t1, t2 = str1[str1.index("Timestamp") + 1], str2[str2.index("Timestamp") + 1]
        time1, time2 = datetime.strptime(t1, "%H:%M:%S"), datetime.strptime(t2, "%H:%M:%S")

        time_res = abs(time2 - time1)
        if timedelta(seconds=31) < time_res < timedelta(seconds=33):
            logging.warning(f"\nЧас помилки: {time1.time()}\n"
                            f"Час серцебиття: {time_res}\n"
                            f"Рядок: {lines[i]}")
        elif time_res >= timedelta(seconds=33):
            logging.error(f"\nЧас помилки: {time1.time()}\n"
                            f"Час серцебиття: {time_res}\n"
                            f"Рядок: {lines[i]}")


    return "hb_test.log"

time_log(errors)
