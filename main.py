# Program to find interest of Hatemalo Bachet tatha rin sahakari sanstha...
# -----------------Imports Modules--------------------------------
from Interest import monthly_interest


#------------------ Monthly saving Input Program --------------------
def interest():
    while True:

        try:
            january = int(input("Enter the saving of January: "))
            febrary = int(input("Enter the saving of Febrary: "))
            march = int(input("Enter the saving of March: "))
            april = int(input("Enter the saving of April: "))
            may = int(input("Enter the saving of May: "))
            june = int(input("Enter the saving of June: "))
            july = int(input("Enter the saving of July: "))
            august = int(input("Enter the saving of August: "))
            september = int(input("Enter the saving of September: "))
            october = int(input("Enter the saving of October: "))
            november = int(input("Enter the saving of November: "))
            december = int(input("Enter the saving of December: "))
        
        #-----------------Program for monthly interest-----------

            jan_int = monthly_interest(january,30)
            
            feb_int = monthly_interest(febrary,60)
            
            mar_int = monthly_interest(march,90)
            
            apr_int = monthly_interest(april,120)
            
            may_int = monthly_interest(may,150)
            
            june_int = monthly_interest(june,180)
            
            july_int = monthly_interest(july,210)
            
            aug_int = monthly_interest(august,240)
            
            sep_int = monthly_interest(september,270)
            
            oct_int = monthly_interest(october,300)
            
            nov_int = monthly_interest(november,330)
            
            dec_int = monthly_interest(december,360)
            

            total_int = int(jan_int+feb_int+mar_int+apr_int+mar_int+june_int+july_int+aug_int+sep_int+oct_int+nov_int+dec_int)
            saving = january + febrary+ march+april+ may +june+ july+ august+ september+ october+ november+ december
        except Exception as e:
            print("Please enter valid number.")
            
        
        
    #------------MAIN BALANCE ACCOUNT------------------
        else:
            while True:
            
                    input_1 = input("Is Balance Return (Y/N): ")
        #-----------------APPENDING LIST--------------------------   
                    balance_list=[]
                    balance_int_list=[]
                    

        #------------------INPUT FOR MAIN BALANCE ACCOUNT-----------

                    if input_1.upper() == 'Y':
                        try:
                            n= int(input("Enter the number of time of return: "))
                        except:
                            print("Please input valid number")
                        r=1
                        try:
                            while r <= n:
                                try:
                                    b1=int(input("Enter balance:"))
                                    t1=int(input("Enter time:"))
                                except:
                                    print("Please input valid number")
                                balance_list.append(b1)
                                balance_int= ((b1*t1*8)/1200)
                                balance_int_list.append(balance_int)

                                r=r+1
                            a=0
                            for x in balance_int_list:
                                
                                a=x+a
                        
                            max = len(balance_list)
                            b = balance_list[max - 1]

                        
                                
                                
                            

                        
                            balance_int=a
                            balance1= b
                        except:
                            print("")


                    elif input_1.upper() == "N":
                        try:
                            balance=int(input("Enter the balance: "))
                            rate=int(input("Enter the rate: "))
                        except:
                            print("Please input valid number")

                        balance_int2=((balance*rate*1)/100)
                        balance_int=balance_int2
                        balance1=balance

                    else:
                        print("Please type 'Y' or 'N' \n Thank you..")
            
                    try:
                        total_interest= balance_int + total_int
                
                        tax = (5/100)*total_interest
                        exact_interest = total_interest - tax
                        total_balance= saving + balance1+ exact_interest
                    

                #---------------------OUTPUT SECTION--------------------
                        return (f" Saving in a year {saving} \n total interest is {total_interest} \n Tax : {tax} \n Exact Interest: {exact_interest} \n Total saving: {total_balance}  ")
                        
                    except:
                        print('')

print("hello world")
print("hello world")

