def add(a,b):
    sum=a+b
    return sum
    
def sub(a,b):
    sub=a-b
    return sub
def prod(a,b):
    prod=a*b
    return prod
      
def div(a,b):
    div=a/b
    return div

operations={"+":add,"-":sub,"*":prod,"/":div}    
num1=int(input("Enter first number:"))
num2=int(input("Enter second number"))

for symbol in operations:
    print(symbol)
operation_symbol=input("pick up an operation")   

calculation_function=operations[operation_symbol]
answer=calculation_function(num1,num2)

print(f"The result is{num1}{operation_symbol}{num2}:{answer}")