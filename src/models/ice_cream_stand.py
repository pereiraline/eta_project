from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""
    flavors_list = ["Goiaba", "Abacate", "Napolitano"]

    #Adição da variável para guardar os sabores

    def __init__(self, restaurant_name, cuisine_type):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type, number_served=None)



    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        if self.flavors_list:

            return list(self.flavors_list)

        #Como o objetivo do metodo é imprimir a lista de sabores disponível
        #Todo o codigo foi reformulado, a fim de atender o que foi proposto

        """if self.flavors:
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")
        else:
            print("Estamos sem estoque atualmente!")"""


    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors_list:
            if flavor in self.flavors_list:
                return f"Temos no momento {flavor}!"
            else:
                return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"


    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""

        if self.flavors_list:
            if flavor in self.flavors_list:
                return "Sabor já disponivel!"
            else:
                self.flavors_list.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"
