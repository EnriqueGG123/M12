import calendar
import math

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador("7.1")

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    
    return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
            
separador("7.2")

def days_in_month(year, month):
	_, number_of_days = calendar.monthrange(year, month)
	return number_of_days

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
		
separador("7.3")

separador("7.4")

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")

separador("7.5")

def liters_100km_to_miles_gallon(liters):
    mpg = (liters * 100) / 2.352
    return mpg

def miles_gallon_to_liters_100km(miles):
    km = 282.481053 / miles
    return km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

separador("7.6")

precio_factura = int(input("Cuanto es la factura?: "))
iva = 21

def factura(precio):
    return precio * (iva / 100 + 1)

print("La factura total sera: ", factura(precio_factura))

separador("7.7")

def calc_area(r):
    area = math.pi * (r ** 2)
    return area

print(calc_area(1))

def calc_volumen_cyl(h, r):
    v = calc_area(r) * h
    return v

print(calc_volumen_cyl(2, 1))

separador("7.8")

def dec_a_bin(numero):
      return format(numero ,"b")

def bin_a_dec(numero):
      return int(numero, 2)

print(dec_a_bin(5))
print(bin_a_dec("101"))