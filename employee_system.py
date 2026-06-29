"""
Autor: Julio Cesar Lopez Sanchez
"""

class Address:
    """define una clase que representa una dirección con atributos de calle, ciudad y código postal.
    """

    def __init__(self, street: str, city: str, postal_code: str) -> None:
        """Inicializa una nueva instancia de la clase Address.
        Args:
            street (str): La calle de la dirección.
            city (str): La ciudad de la dirección.
            postal_code (str): El código postal de la dirección.
        """
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def __repr__(self) -> str:
        """Devuelve una representación en cadena de la dirección.
        Returns:
            str: Una cadena que representa la dirección.
        """
        return f"Address(street={self.street!r}, city={self.city!r}, postal_code={self.postal_code!r})"

class Employee:
    """define una clase para representar a un empleado con atributos de nombre, salario y dirección.
    """

    def __init__(self, name: str, salary: float, address: Address) -> None:
        """Inicializa una nueva instancia de la clase Employee.
        Args:
            name (str): El nombre del empleado.
            salary (float): El salario del empleado.
            address (Address): La dirección del empleado.
        Raises:
            ValueError: Si el salario es negativo.
        """
        if salary < 0:
            raise ValueError("El salario no puede ser negativo")

        self.name = name
        self.salary = salary
        self.address = address 

    def give_raise(self, amount: float) -> None:
        """Aumenta el salario del empleado.
        Args:
            amount (float): La cantidad por la que aumentar el salario.
        Raises:
            ValueError: Si la cantidad es negativa o cero.
        """
        if amount <= 0:
            raise ValueError("El aumento de salario no puede ser negativo o 0")

        self.salary += amount

    def __str__(self) -> str:
        """Devuelve una representación en cadena del empleado.
        Returns:
            str: Una cadena que representa al empleado.
        """

        return f"Empleado: {self.name} - Salario: ${self.salary}"

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del empleado.
        Returns:
            str: Una cadena que representa al empleado.
        """

        return f"Employee(name={self.name!r}, salary={self.salary!r}, address={self.address!r})"

    def __eq__(self, other: object) -> bool:
        """Compara si dos empleados son iguales.
        Args:
            other (object): Otro objeto para comparar.
        Returns:
            bool: True si los empleados son iguales, False en caso contrario.
        """

        if not isinstance(other, Employee):
            return NotImplemented
        return self.name == other.name and self.salary == other.salary

class Manager(Employee):
    """define una clase para representar a un gerente con atributos de nombre, salario y tamaño del equipo.
    """

    def __init__(self, name: str, salary: float, address: Address, team_size: int) -> None:
        """Inicializa una nueva instancia de la clase Manager.
        Args:
            name (str): El nombre del gerente.
            salary (float): El salario del gerente.
            address (Address): La dirección del gerente.
            team_size (int): El tamaño del equipo del gerente.
        """
        super().__init__(name, salary, address)
        self.team_size = team_size

    def add_team_member(self) -> None:
        """Añade un miembro al equipo del gerente.
        """
        self.team_size += 1

def main() -> None:
    """Función principal.
    Crea instancias de Employee y Manager, realiza operaciones y muestra resultados.
    """
    address1 = Address("Calle 123", "Ciudad A", "12345")
    address2 = Address("Avenida 456", "Ciudad B", "67890")
    employee1 = Employee("Julio Cesar", 99.99, address1)
    employee2 = Employee("Juan", 49.99, address2)
    employee3 = Employee("Juan", 49.99, address1)
    manager1 = Manager("Adolfo", 149.99, address2, 4)
    manager2 = Manager("Pedro", 149.99, address1, 6)
    manager3 = Manager("Pedro", 149.99, address2, 5)

    print(employee1)
    print(manager1)

    print(employee1 == employee2)
    print(employee2 == manager1)

    employee1.give_raise(10)
    manager1.give_raise(20)

    print(employee1)
    print(manager1)

    print(employee3 == employee2)
    print(employee1 == employee2)
    print(employee2 == manager1)
    print(manager1 == manager2)
    print(manager3 == manager2)


    manager1.add_team_member()


if __name__ == "__main__":
    main()
