# Primer programa
def main():
  while True:
    try:

      print(
        "Lista de programas"
        "\n1. calcular edad"
        "\n2. calcular comida favorita"
        "\n3. calcular si frio o caliente"
        "\n4. salir"  
      )
      value = int(input("Ingresa una opcion: "))

      if value == 1:
          age = int(input("Enter your age: "))
          calculate_age(age)
      elif value == 2:
          food = input("Enter your favorite food: ")
          favorite_food(food)
      elif value == 3:
          isTrue = input("Te gusta el frio o el calor? (si o no): ")
          print(frioOCaliente(isTrue))
      elif value == 4:
          print("Exiting the program. Goodbye!")
          return
      else:
          print("Invalid option. Please try again.")
    except ValueError:
      print("Please enter a valid number for your age.")

def calculate_age(age):
  if age == 0:
    print("Exiting the program. Goodbye!")
    return

  if age < 1 or age >= 110:
    print("Please enter a valid age")
  elif age < 18:
    print("You are a minor")
  elif age >= 18 and age <= 65:
    print("You are an adult")
  else:
    print("You are a senior citizen")

def favorite_food(food):
  print(f"Mi comida favorita es {food}")

def frioOCaliente(paylaod):
  if paylaod == "si":
    print("Me gusta el frio")
  else:
    print("Me gusta el caliente")

main() # Llamando a la función principal para iniciar el programa.

# Juan David Cardona Bageth 