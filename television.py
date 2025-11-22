class Television:
    """
    Basic Television class that can change channels, volume, mute and trun tv on and off.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self)-> None:
        """
        Set up the TV with default values.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the TV on or off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self)-> None:
        """
        Mute or unmute the TV, only if it is on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self)-> None:
        """
        Move the channel up.
        """
        if self.__status:
            self.__muted = False

            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self)-> None:
        """
        Move the channel down.
        """
        if self.__status:
            self.__muted = False
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
        else:
            self.__channel = Television.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        Increase the volume by one step.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self)-> None:
        """
        Decrease the volume by one step.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:
        """
        Retrun a simple string showing the TV's status.
        """
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume

        if self.__status:
            power_str = "True"
        else:
            power_str = "False"
            
        return f"Power = {power_str}, Channel = {self.__channel}, Volume = {volume}"
