
n = int(input())
arr = []
arr = list(map(int,input().strip().split()))[:n]


TENS = {30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
ZERO_TO_TWENTY = (
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
)

def number_to_english(n):
    if any(not x.isdigit() for x in str(n)):
        return ''

    if n <= 20:
        return ZERO_TO_TWENTY[n]
    elif n < 100 and n % 10 == 0:
        return TENS[n]
    elif n < 100:
        return number_to_english(n - (n % 10)) + ' ' + number_to_english(n % 10)
    elif n < 1000 and n % 100 == 0:
        return number_to_english(n / 100) + ' hundred'
    elif n < 1000:
        return number_to_english(n / 100) + ' hundred ' + number_to_english(n % 100)
    elif n < 1000000:
        return number_to_english(n / 1000) + ' thousand ' + number_to_english(n % 1000)

    return ''

b = []

for i in range(n):
    b.append(number_to_english((arr[i])))

count = 0

for test in b:
    count = count + (len(list(filter(lambda x: x in 'aeiou', test))))
    
count = int(count)

def getPairsCount(arr, n, sum): 
      
    count = 0 
  
    
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
      
    return count

ans = getPairsCount(arr,n,count)
print(number_to_english(ans))