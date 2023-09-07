class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served #Substitui valor por argumento
        self.open = False

        #Novo argumento inserido (number_serverd)

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        return f"Esse restaurante chama {self.restaurant_name}, serve comida {self.cuisine_type} e está servindo {self.number_served} consumidores desde que está aberto."
        #Return no lugar do print
        #Removi os parenteses
        #Foi feita a concatenação em uma unica string, chamando novo argumento para imprimir a descrição

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if self.open:
            #Remoção do not para entrar em restaurante aberto
            #self.open = False não precisa ser usado
            #self.number_served = -2 não precisa ser usado
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está fechado!"
        #Return no lugar dos prints

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return self.number_served
        #Return adicionado
        else:
            return f"{self.restaurant_name} está fechado!"
        #Return no lugar do print
        #Remoção dos parenteses

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers
            #Adicionei sinal de + para implementar o incremento
            return self.number_served
            #Adiciionei o return para ler o resultado
        else:
            return f"{self.restaurant_name} está fechado!"
            #Substitui o print pelo return e removi os parenteses