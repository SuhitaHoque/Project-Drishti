
from modules import currency_detection, medicine_detection, object_detection, text_detection

# Taking input for mode of operation
print("\n\n1. Object Detection | 2. Currency Detection | 3. Medicine Detection | 4. Text Detection");
mode = int(input("Please Enter mode of operation: "));

# Object Detection
if mode==1:
    object_detection.detect_object();

# Currency Detection
elif mode==2:
    currency_detection.detect_currency();
    
# Medicine Detection
elif mode==3:
    medicine_detection.detect_medicine();

# Text Detection
elif mode==4:
    text_detection.detect_text();
    
# Terminating conditions
else:
    print("\nModule not found");