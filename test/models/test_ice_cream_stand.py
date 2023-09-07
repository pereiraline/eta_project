from src.services.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        #setup
        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")

        #chamada
        resultado = service.flavors_available()
        print(resultado)

    def test_find_flavor_contains_in_list(self):
        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")
        flavor_contains = "Temos no momento Napolitano!"

        #Chamada
        resultado = service.find_flavor("Napolitano")
        print(resultado)

        #Avaliação
        assert resultado == flavor_contains

    def test_find_flavor_not_contains_in_list(self):

        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")
        flavor_contains = "Não temos no momento Uva!"

        # Chamada
        resultado = service.find_flavor("Uva")
        print(resultado)

        # Avaliação
        assert resultado == flavor_contains

    def test_not_stoke_exist(self):
        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")
        not_stoke = "Estamos sem estoque atualmente!"

        resultado = service.add_flavor("Goiaba")
        print(resultado)

        assert resultado == not_stoke


    def test_add_flavor(self):
        #Setup:
        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")
        add_flavor = "Sabor Uva adicionado ao estoque!"

        #Chamada
        resultado = service.add_flavor("Uva")
        print(resultado)

        #Avaliação
        assert resultado == add_flavor
        
    def test_verify_flavor(self):
        #Setup
        service = IceCreamStand(restaurant_name="abc", cuisine_type="Bra")
        verify_flavor = "Sabor Uva já disponível no estoque!"
        service.add_flavor("Uva")

        #Chamada
        resultado = service.add_flavor("Uva")
        print(resultado)

        #Avaliação
        assert resultado == verify_flavor



