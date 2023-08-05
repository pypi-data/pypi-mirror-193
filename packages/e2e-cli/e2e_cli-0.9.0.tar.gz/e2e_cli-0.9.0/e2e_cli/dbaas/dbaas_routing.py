import subprocess

from e2e_cli.dbaas.dbaas import DBaaSClass


class DBaaSRouting:
    def __init__(self, arguments):
        self.arguments = arguments

    def route(self):
        if self.arguments.dbaas_commands is None:
            subprocess.call(['e2e_cli', 'dbaas', '-h'])

        elif self.arguments.dbaas_commands == 'add':
            if "alias=" in self.arguments.alias:
                alias_name = self.arguments.alias.split("=")[1]
            else:
                alias_name = self.arguments.alias
            dbaas_class_object = DBaaSClass(alias=alias_name)
            try:
              dbaas_class_object.create_dbaas()
            except KeyboardInterrupt:
                print("\n")
                pass

        elif self.arguments.dbaas_commands == 'list' or self.arguments.dbaas_commands == 'ls':
            if "alias=" in self.arguments.alias:
                alias_name = self.arguments.alias.split("=")[1]
            else:
                alias_name = self.arguments.alias
            dbaas_class_object = DBaaSClass(alias=alias_name)
            dbaas_class_object.list_dbaas()

        elif self.arguments.dbaas_commands == 'delete':
            if "alias=" in self.arguments.alias:
                alias_name = self.arguments.alias.split("=")[1]
            else:
                alias_name = self.arguments.alias
            dbaas_class_object = DBaaSClass(alias=alias_name)
            try:
                dbaas_class_object.delete_dbaas_by_name()
            except KeyboardInterrupt:
                print("\n")
                pass
