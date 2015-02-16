# Calculates tip and splits the total bill

Bill_Amount = float(input("Bill Amount:"))
Tip_Percent = float(input("Tip Percent(%):"))
Tip_Amount = (Bill_Amount * Tip_Percent)/100
print ("Tip Amount:%.2f" % (Tip_Amount))
Total_Amount = Bill_Amount + Tip_Amount
print ("Total Amount:%.2f" % (Total_Amount))
Split_Between = int(input("Number of People:"))
Per_Person_Amount = Total_Amount/Split_Between
print ("Per Person Share:%.2f" %(Per_Person_Amount))
