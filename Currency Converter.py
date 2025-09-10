rates = {
    "USD": 1.00,
    "GBP": 0.90,
    "EUR": 0.95,
    "AUD": 1.80,
}
print(rates["GBP"])



while True:
 from_curr = input("Which currency would you like to convert from: USD, GBP, EUR, AUD or Exit?: ")
 if from_curr.lower() == "exit":
    break
 
 if from_curr.upper() not in rates and from_curr.lower() != "exit":
    print("Invalid currency, please choose from either USD, GBP, EUR or AUD\n")
    continue
 
 while True:
  try:
   amount = float(input("Enter amount you would like to convert?: "))
   break
  except ValueError:
    print("❌ That wasn't a valid number.")
    continue
  
 while True:
  to_curr = input("And which currency would you like to convert into: USD, GBP, EUR or AUD or Exit?: ")
  if to_curr.lower() == "exit":
    break
  
  if to_curr.upper() not in rates and to_curr.lower() != "exit":
    print("Invalid currency, please choose from either USD, GBP, EUR or AUD\n")
    continue
  break

 if to_curr.lower() == "exit":
  break
 
 print(f"Converting {amount}{from_curr} to {to_curr}")
 if from_curr == 'USD':
      currency_returned = amount * (float(rates[to_curr]))
      print(f"\n You will receive {currency_returned}{to_curr}")
 elif to_curr == 'USD':
       currency_returned = amount / (float(rates[from_curr]))
       print(f"\n You will receive {currency_returned}{to_curr}")
 else:
       currency_returned = amount / (float(rates[from_curr])) * (float(rates[to_curr]))
       print(f"\n You will receive {currency_returned}{to_curr}")
print("Thank you for using our Currency Convertion website.")

    