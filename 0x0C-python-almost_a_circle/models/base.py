class Base:
        """_summary_
        """
        __nb_objects = 0

        @classmethod
        def __init__(self, id=None):
                """_summary_

                Args:
                    id (_type_, optional): _description_. Defaults to None.
                """
                if id is not None:
                        self.id = id
                else:
                        self.__nb_objects += 1
                        self.id = self.__nb_objects