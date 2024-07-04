from nada_dsl import *

def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")

    # Define two secret integer inputs from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform the computation: multiply the two secret integers
    product_int = my_int1 * my_int2

    # Return the output of the computation
    return [Output(product_int, "my_product_output", party1)]
