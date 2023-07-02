def say_my_name(first_name, last_name=""):
    """
    Prints a message with given first and last name

    Args:
        first_name (str): The first name to include in a message
        last_name (str): The last name to include in the message. Optional

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
