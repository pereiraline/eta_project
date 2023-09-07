from src.services.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        describe = "Esse restaurante chama LaCuisine, serve comida italiana e está servindo 40 consumidores desde que está aberto."

        #Chamada
        resultado = service.describe_restaurant()

        #Avaliação
        assert resultado == describe

    def test_open_restaurant(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        restaurant_is_open = "LaCuisine agora está aberto!"
        service.open = True

        #Chamada
        resultado = service.open_restaurant()
        print(resultado)

        #Avaliação
        assert resultado == restaurant_is_open

    def test_close_restaurant(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        restaurant_is_close = "LaCuisine já está fechado!"
        service.open = False

        #Chamada
        resultado = service.open_restaurant()
        print(resultado)

        #Avaliação
        assert resultado == restaurant_is_close

    def test_set_number_served(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        total_pessoas = 40
        service.open = True

        #Chamada
        resultado = service.set_number_served(40)
        print(resultado)

        #Avaliação
        assert resultado == total_pessoas

    def test_set_number_serverd_close(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        closed = "LaCuisine está fechado!"
        service.open = False

        #Chamada
        resultado = service.set_number_served(40)
        print(resultado)

        #Avaliação
        assert resultado == closed

    def test_increment_number(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        service.open = True
        service.set_number_served(2)
        increment = 42

        #Chamada
        resultado = service.increment_number_served(40)
        print(resultado)

        #Avaliação
        assert resultado == increment

    def test_increment_number_serve(self):
        #Setup
        service = Restaurant(restaurant_name="LaCuisine", cuisine_type="italiana", number_served=40)
        service.open = False
        closed = "LaCuisine está fechado!"

        #Chamada
        resultado = service.increment_number_served(40)
        print(resultado)

        #Avaliação
        assert resultado == closed
