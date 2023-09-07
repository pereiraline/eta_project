from src.services.restaurant import Restaurant


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

        #self.flavors = flavors_list - linha de código removida após declaração de variavel(flavors_list)

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        if self.flavors_list:
            return list(self.flavors_list)

        #Como o objetivo do metodo é imprimir a lista de sabores disponíveis, todo codigo foi subtituido por list

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
        """else:
            return "Estamos sem estoque atualmente!"""
        #Todos os prints substituido por return
        #ultima linha de código removida por já pertencer a outro metodo



    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""

        if self.flavors_list:
            if flavor in self.flavors_list:
                return f"Sabor {flavor} já disponível no estoque!"
            else:
                self.flavors_list.append(flavor)
                return f"Sabor {flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!" #linha de código não coberta por falta de tempo

        # Todos os prints substituido por return


