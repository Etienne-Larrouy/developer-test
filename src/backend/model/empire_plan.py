from src.backend.model.hunter import Hunter

class EmpirePlan():
    def __init__(self, bounty_hunters, countdown):
        """
        Args:
            bounty_hunters (Hunters): Planet of departure
            countdown (integer): Death Star countdown in days
        """
        self.__bounty_hunters = [Hunter(**bh) for bh in bounty_hunters]
        self.__countdown = countdown

    def get_bounty_hunters(self):
        """ Bounty hunters getter

        Returns:
            Array: List of bnounty hunters
        """
        return self.__bounty_hunters

    def get_countdown(self):
        """
        Countdown getter
        Returns:
            Integer: Countdown in days
        """
        return self.__countdown