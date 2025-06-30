# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება წამების რაოდენობას და გამოიტანეთ საათების,
# წუთების და წამების რაოდენობას (მაგ. 20000 წამი არის  5 საათი, 33 წუთი, 20 წამი)

seconds = int(input("gtxovs seiyvanot wamebis raodenoba:  "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60

print(f'{seconds} wami aris {hours} saati, {minutes} tsuti da {sec} wami')