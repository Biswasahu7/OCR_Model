# Importing required libraries...
import datetime
import logging
# import pandas as pd
from logging.handlers import TimedRotatingFileHandler
# import time
l2 = datetime.datetime.now()
import easyocr

# DEFINING EASY_OCR with language English...
reader = easyocr.Reader(['en'])

# LOGGER INFO FOR CODE REFERENCE... (Debug checking)
l1 = datetime.datetime.now()
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Cam_1_INFO/OCR_Result/OCR_Logs/logeer_{}.log".format(l1),when="m", interval=60)
logger.addHandler(handler)


code = 0

# global code

def Easy_OCR(image):

    # global code

    # Reading image from model
    result = reader.readtext(image)
    with open("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Crop_Images/OCR_Result {}.txt".format(l2), "a") as f:
        f.write("\n")
        f.write(str(result))
        f.write("\n")
    logger.info("Image has been rade from opencv model")

    # # Checking Result...
    if result:
        # print(result)
        # print(len(result))
    # print(result)
    # Assign empty list to append final result...
        codelist = []
        code6 = []
        code5 = []

        # Running for loop into OCR result to check special character...

        if result == "":
            print("Blank OCR Result")
            logger.info("Blank OCR Result came for EasyOCR")

        else:

            if len(result) >= 2:

                for z in result:
                    # print(z[1])
                            code6.append(z)
                            code5.append(z)

                # Take the proper number index from the list...
                A = str(code6[0][1])+str(code5[1][1])

                # Replace the special character to 1...
                a = A.replace('|', '1')
                b = a.replace('/', '1')
                c = b.replace('!', '1')
                d = c.replace('(', '1')
                e = d.replace(')', '1')
                f = e.replace('S', '5')
                g = f.replace('&', 'x')
                h = g.replace('%', 'x')
                i = h.replace('^', '1')
                j = i.replace('p', 'B')
                k = j.replace('$', '9')
                l = k.replace('[', '1')
                m = l.replace('@', '2')
                n = m.replace('I', '1')
                o = n.replace('i', '1')
                p = o.replace('g', '9')
                q = p.replace('e', '2')
                r = q.replace('}', '1')
                s = r.replace(']', '1')
                t = s.replace('l', '1')
                u = t.replace('o', '0')
                v = u.replace('G', '6')
                result1 = v.replace('?', '1')

                # print("result1-{}".format(result1+result1))

                finalcode = result1
                logger.info("All special character has been removed")

                # # Appending final code result to codelist variable...
                codelist.append(finalcode)
                # # print(codelist)

                # Converting list to string for mapping with IR data...
                code = ''.join(codelist)
                logger.info("Final Code has been taken after replaced special character-{}".format(code))
                # print(type(code))
                # print("code-{}".format(code))
                return (codelist)

            else:

                for z in result:

                         # Take the proper number index from the list...
                        A = str(z[1])
                        # print(A)

                        # Replace the special character to 1...
                        a = A.replace('|', '1')
                        b = a.replace('/', '1')
                        c = b.replace('!', '1')
                        d = c.replace('(', '1')
                        e = d.replace(')', '1')
                        f = e.replace('S', '5')
                        g = f.replace('&', 'x')
                        h = g.replace('%', 'x')
                        i = h.replace('^', '1')
                        j = i.replace('p', 'B')
                        k = j.replace('$', '9')
                        l = k.replace('[', '1')
                        m = l.replace('@', '2')
                        n = m.replace('I', '1')
                        o = n.replace('i', '1')
                        p = o.replace('g', '9')
                        q = p.replace('e', '2')
                        r = q.replace('}', '1')
                        s = r.replace(']', '1')
                        t = s.replace('l', '1')
                        u = t.replace('o', '0')
                        result = u.replace('?', '1')

                        finalcode =  result
                        logger.info("All special character has been removed")

                        # Appending final code result to codelist variable...
                        codelist.append(finalcode)
                        # print(codelist)

                        # Converting list to string for mapping with IR data...
                        code = ''.join(codelist)
                        logger.info("Final Code has been taken after replaced special character-{}".format(code))

                        # with open("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Cam_1_INFO/OCR_Result/OCR_Result {}.txt".format(l2), "a") as f:
                        #     # f.write("extract code from wagon -{}".format(Wagon_number))
                        #     # f.write("; ")
                        #     f.write(code)
                        #     f.write("; ")
                        #     # f.write("*" * 20)
                        #     print("code written")

                        return (codelist)

