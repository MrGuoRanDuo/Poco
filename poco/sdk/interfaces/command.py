# coding=utf-8

__author__ = 'lxn3032'


class CommandInterface(object):
    """
    This is one of the main communication interfaces. This interface defines command-level behaviours providing 
    abilities to control remote runtime by sending self-defined command. The command can be various from string type to 
    specific structure of a dict.
    """

    def command(self, cmd, type):
        """
        Emit a command to remote runtime (target device). 

        Args:
            cmd: Any json serializable data.
            type (:obj:`str`): A string value indicated the command type (command tag).

        Returns:
            None (recommended).
        """

        pass
