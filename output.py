from agents import Drone


class output:
    def __init__(self, file_name, drones):
        with open(file_name, "w") as out_file:
            for d in drones:
                name = d.kind[0].upper()
                out = name + "|"
                for i in d.index_history:
                    out += str(i) + ","
                out = out[0:-1] + "\n"
                out_file.write(out)
        print("Output written to:", file_name)
