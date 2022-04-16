import sqlite3


class AccountingPassengers:
    def __init__(self, table_name):
        connector = sqlite3.connect(table_name)
        self.cursor = connector.cursor()

    def trip(self, date, name):
        command = f"""
                    SELECT * FROM accounting AS file
                     WHERE file.date='{date}'
                     AND file.ship_id in 
                     (SELECT file_s.id FROM ships AS file_s WHERE file_s.name IN ('{name}'))
                """
        out, people = self.cursor.execute(command), []
        for elem in out:
            people += [elem]
        people = sorted(people, key=lambda x: (x[2], x[3]))
        command = f"""
                    SELECT * FROM tickets
                """
        tickets = {}
        for ticket in self.cursor.execute(command):
            tickets[ticket[0]] = ticket[2]
        out = []
        for man in people:
            out += [f'{" ".join(man[2:4])}, {tickets[man[5]] * man[6]}']
        return out

    def date_list(self, date):
        command = f"""
                    SELECT file.ship_id, file.tickets FROM accounting AS file
                     WHERE file.date='{date}'
                """
        out, people = self.cursor.execute(command), []
        for elem in out:
            people += [elem]
        command = f"""
                    SELECT * FROM ships
                    """
        ships = {}
        for ship in self.cursor.execute(command):
            ships[ship[0]] = [ship[1], 0]
        for elem in people:
            ships[elem[0]][1] += elem[1]
        out = []
        for ship in ships.values():
            if ship[1]:
                out += [tuple(ship)]
        return sorted(out, key=lambda x: x[0])[::-1]